# Visualization Policies and Guidelines

## Definitions

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
3. If a two-column dashboard has an odd number of panels, the final panel must use the same width as other panels.

### Dashboard titles
3.1. A dashboard title must use title case.

### Time-Series Panels
4. A time-series panel must not have a right axis.
5. A time-series panel must have a left axis.
6. All time-series panels in a dashboard must have the same width.
7. All time-series panels in a dashboard must start plotting data at the same horizontal offset from the left margin.
8. The left-axis margin should use the same width across all panels in a dashboard.
8.1. Left-axis margins must be wide enough so that no vertical axis tick label is truncated.

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
