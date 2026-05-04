# Visualization Policies and Guidelines

## Definitions

A *dashboard* is a named saved view that assigns a time range and contains an ordered set of panels positioned on a layout grid.

A *layout grid* divides the dashboard into columns and rows of uniform cells; each panel occupies a rectangle of contiguous cells.

*Grid width* is the number of horizontal grid cells a panel spans.

A *panel* is a bounded region on the dashboard that displays a visualization and typical chrome such as a title and legend.

A *panel title* is the text label identifying a panel.

A *row* (dashboard row) is a collapsible section header that groups panels; it is not a data visualization.

A *time-series panel* is a panel whose primary visualization plots measures against time.

A *y-axis region* is the portion of a panel reserved for vertical axis tick labels, immediately to the left of the plot region.

A *plot region* is the portion of a panel where series data are drawn, bounded by the axes (typically to the right of the y-axis region and above the horizontal time axis).

A *plot x-origin* is the horizontal position within the plot region where the time axis begins. When plot x-origins align across panels in the same dashboard column, the same instant in time maps to the same horizontal offset in each plot region.

A *composite dashboard* displays multiple panels over a common timeframe in one view.

A *metric* (or *metric name*) is the resource or entity being measured, such as CPU utilization, I/O rate, or temperature.

A *measure* is a quantitative value that represents a numerical fact or a calculation.

A *dimension* is a qualitative attribute that categorizes, segments, or labels data.

A *primary dimension* is the highest-priority dimension in a composite dimension label.

A *unit of measure* (UOM) is a standardized unit used to express and compare numerical values.

A *unit of time* (UOT) is a UOM that represents time (for example, ms, s, or d).

A *UOM scale* is the magnitude prefix for a UOM (for example, K, M, G, or T).

A *vertical axis tick label* is the text shown on the left vertical axis at each tick mark.

A vertical axis tick label has three components in order:

`<value> <scale> <units>`

Where:
- `<value>` is the numeric quantity.
- `<scale>` is the UOM scale prefix (for example, K or G). It may be empty when no scale applies.
- `<units>` is a concise UOM abbreviation.

An *axis title* is a text label adjacent to an axis.

A *time series* (or *series*) plots measures over time.

An *envelope graph* is a time-series panel where one complementary dimension is plotted on the positive vertical axis and another complementary dimension is inverted and plotted on the negative vertical axis. This arrangement visually separates complementary dimensions in one panel.

## Statements
1. A composite dashboard should display two columns of panels.
2. A two-column dashboard must use the same width for left and right panels.
3. If a two-column layout leaves a single data panel in the last row of a section, that panel must still use the same grid width as each other data panel (the companion column may be empty). It must not span the full row width unless every time-series panel on the dashboard uses that same full width (see 6).

### Dashboard titles
3.1. A dashboard title must use title case.

### Time-Series Panels
4. A time-series panel must not have a right axis.
5. A time-series panel must have a left axis.
6. All time-series panels in a dashboard must use the same grid width.
7. The left-axis margin should use the same width across all panels in a dashboard.
7.1. Left-axis margins must be wide enough so that no vertical axis tick label is truncated.
7.2. Where the product exposes a fixed y-axis width or equivalent, use the same value on every time-series panel so the plot region starts at a consistent horizontal offset.
8. Time-series panels in the same dashboard column must have aligned plot x-origins.

### Panel Title
9. A time-series panel must have a panel title.
10. A panel title must not include metric names.
10.1. A panel title must not include UOM text.
10.2. A panel title must use title case.

### Left Axis Title
11. A time-series panel must not have a left-axis title.

### Vertical Axis Tick Labels
12. Vertical axis tick labels should include a concise UOM abbreviation of 1 to 6 characters, including spaces.
13. Vertical axis tick labels must contain only:
13.1. the numeric value component,
13.2. an optional scale component, and
13.3. the UOM abbreviation component.
14. Vertical axis tick labels in a panel must use the same UOM and the same UOT.
15. Vertical axis tick labels in a panel must use a consistent scale at any single tick value.
16. The numeric component of a vertical axis tick label must have at most three digits, or two digits with one significant fractional digit.

### Envelope Graphs
17. A panel that plots two complementary dimensions should use an envelope graph.
17.1. In an envelope graph, one complementary dimension must be plotted as positive values and the other must be plotted as negative values.
17.2. In an envelope graph, complementary dimensions must use the same UOM and UOT.

### Legends
18. A legend label may include a primary dimension and a secondary dimension.

## Commentary
1. Right axes create different plot widths and distort horizontal comparisons across panels.
2. UOM context belongs in vertical axis tick labels, because scale can change with data range.
3. Use envelope graphs to visually segregate complementary dimensions, such as read bytes/sec and write bytes/sec.
4. Uniform grid width (6) keeps panel geometry comparable. A lone panel in the last row should not expand to full row width while neighbors use half width, or vertical comparison of the same column position becomes misleading; leaving an empty column preserves consistent grid width without inventing filler charts.
5. Aligned plot x-origins let the reader scan vertically and treat one calendar instant as one vertical line across stacked time-series panels. Matching y-axis region width (7 and 7.2) is the usual way products expose that alignment; mixed draw styles (for example bars versus lines) or differing aggregation bucket boundaries can still shift where a value appears relative to ticks unless settings are harmonized.
