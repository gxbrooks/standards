#!/usr/bin/env python3
"""Generate a PDF for each standard in this repo from its Markdown source.

Pipeline: Markdown -> HTML (Python-Markdown, already installed system-wide)
-> PDF (Chrome/Chromium headless --print-to-pdf, installed by myenv's
assert_packages.sh). Both tools are already present in this environment;
no new install is required.

Usage:
    python3 generate_pdfs.py            # regenerate every standard's PDF
    python3 generate_pdfs.py automation.md   # regenerate just one

A file is a "standard" here if it is a top-level *.md file in this directory
other than README.md and LICENSE.md.
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import markdown

REPO_ROOT = Path(__file__).resolve().parent
EXCLUDE = {"README.md", "LICENSE.md"}
MD_EXTENSIONS = ["extra", "sane_lists"]

CSS = """
@page { size: Letter; margin: 1in; }
body { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 10.5pt; line-height: 1.45; color: #1a1a1a; }
h1 { font-size: 20pt; border-bottom: 2px solid #333; padding-bottom: 0.2em; }
h2 { font-size: 15pt; margin-top: 1.4em; border-bottom: 1px solid #999; padding-bottom: 0.15em; }
h3 { font-size: 12.5pt; margin-top: 1.2em; }
h4 { font-size: 11pt; margin-top: 1em; }
table { border-collapse: collapse; width: 100%; margin: 0.8em 0; font-size: 9.5pt; }
th, td { border: 1px solid #ccc; padding: 4px 8px; text-align: left; vertical-align: top; }
th { background: #eee; }
code { background: #f2f2f2; padding: 0.1em 0.3em; border-radius: 3px; font-size: 92%; }
pre { background: #f2f2f2; padding: 0.6em; border-radius: 4px; overflow-x: auto; }
pre code { background: none; padding: 0; }
blockquote { border-left: 3px solid #ccc; margin: 0.6em 0; padding-left: 1em; color: #444; }
a { color: #0b4f8a; }
"""

TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)


def find_title(md_text: str, fallback: str) -> str:
    m = TITLE_RE.search(md_text)
    return m.group(1).strip() if m else fallback


def find_chrome() -> str:
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        path = shutil.which(name)
        if path:
            return path
    raise RuntimeError("No Chrome/Chromium binary found on PATH")


def render_pdf(md_path: Path, chrome_bin: str) -> Path:
    md_text = md_path.read_text(encoding="utf-8")
    title = find_title(md_text, md_path.stem.title())
    body_html = markdown.markdown(md_text, extensions=MD_EXTENSIONS)

    html = f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
{body_html}
</body>
</html>
"""
    pdf_path = md_path.with_suffix(".pdf")
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
        html_path = Path(f.name)

    try:
        subprocess.run(
            [
                chrome_bin,
                "--headless",
                "--disable-gpu",
                "--no-sandbox",
                "--no-pdf-header-footer",
                f"--print-to-pdf={pdf_path}",
                str(html_path),
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        print(f"Error: Chrome failed rendering {md_path.name}:\n{exc.stderr}", file=sys.stderr)
        raise
    finally:
        html_path.unlink(missing_ok=True)

    return pdf_path


def main(argv: list[str]) -> int:
    chrome_bin = find_chrome()

    if argv:
        md_files = [REPO_ROOT / name for name in argv]
        for p in md_files:
            if not p.is_file():
                print(f"Error: not found: {p}", file=sys.stderr)
                return 1
    else:
        md_files = sorted(
            p for p in REPO_ROOT.glob("*.md") if p.name not in EXCLUDE
        )

    for md_path in md_files:
        pdf_path = render_pdf(md_path, chrome_bin)
        print(f"✓ {md_path.name} -> {pdf_path.name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
