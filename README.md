Project independent software development prompts (and skills) to use with Claude.ai or other AIs.

## PDFs

Each standard's `.pdf` is generated from its `.md` source. Regenerate after editing any standard:

```bash
python3 generate_pdfs.py            # all standards
python3 generate_pdfs.py automation.md   # just one
```

Requires Python's `markdown` package and a Chrome/Chromium binary on `PATH` — both already present
via this machine's [myenv](https://github.com/gxbrooks/myenv) setup (`assert_packages.sh` installs
`google-chrome-stable`); no other tool install needed.
