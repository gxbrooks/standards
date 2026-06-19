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

A *secondary dimension* is a lower-priority dimension in a composite dimension label. In an envelope graph and in a drilldown dashboard, the secondary dimension is the complementary attribute that splits a metric into a small, fixed set of values (for example, In and Out, or Read and Write).

An *entity dimension* is the dimension whose values identify the measured entities (for example, host, namespace, or device).

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

*Complementary metrics* (or *complementary dimension values*) are two measures that are values of a single shared dimension which partitions one metric — for example, the direction dimension with values *in* and *out*, or *read* and *write*. The two values describe the same underlying metric (network throughput, disk throughput) split into opposing directions.

Two measures are *not* complementary when no single dimension enumerates them as values, even if they share a UOM. For example, GPU core utilization and VRAM utilization are both percentages but are distinct metrics: there is no dimension whose values are "GPU%" and "VRAM%". Likewise, CPU utilization and memory utilization are not complementary.

An *envelope graph* is a time-series panel where one value of a complementary pair is plotted on the positive vertical axis and the other value is inverted and plotted on the negative vertical axis. This arrangement visually separates the two complementary values of a single dimension in one panel.

An *aggregated panel* (or *overview panel*) is a panel that summarizes a metric across the values of one or more of its dimensions (for example, total network throughput across all hosts).

A *drilldown dashboard* is a dashboard that decomposes a single metric (or a closely related grouping of metrics) presented by an aggregated panel, breaking the metric out so that each value of its secondary dimension occupies its own panel and the entity dimension is enumerated as the series within each panel.

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
16.1. To satisfy 16, a UOM scale prefix (K, M, G, T) or a self-scaling UOM (for example, a time UOM that scales ms to s, min, or h) must be applied to keep the numeric component small, rather than displaying a large raw value.
16.2. If a numeric value still presents more than three integer digits (for example, where no scale prefix is available or applied), the integer part must use thousands separators (for example, 12,345 ms). A scale prefix must not be shown without applying it to the value.

### Envelope Graphs
17. A panel that plots two complementary dimensions of a single metric should use an envelope graph.
   17.1. In an envelope graph, one complementary dimension must be plotted as positive values and the other must be plotted as negative values.
   17.2. In an envelope graph, complementary dimensions must use the same UOM and UOT.
   17.3. In an envelope graph whose secondary dimension has a cardinality of two, the two complementary dimensions should use distinct colors.
   17.4. In an envelope graph, every plotted dimension must use a solid plot line.
   17.5. An envelope graph may include a textual direction cue in its panel title that names the dimension plotted on the positive axis (for example, "(In positive)"). Direction is conveyed primarily by the positive/negative split (17.1); the cue is optional.
   17.6. An envelope graph must plot two complementary metrics (two values of a single shared dimension). Two measures that are not complementary must not be combined into an envelope graph, even when they share a UOM; each must be plotted in its own panel.

### Legends
18. A legend label may include a primary dimension and a secondary dimension.

### Drilldown Dashboards
19. An aggregated panel that summarizes a metric across the values of a dimension should have a corresponding drilldown dashboard.
20. If a drilldown dashboard exists for a metric, the following statements must hold:
   20.1. Its panels must be stacked vertically in a single column.
   20.2. It must contain one panel per value of the metric's secondary dimension (for example, one panel for In and one for Out, or one for Read and one for Write). A metric with no secondary dimension (a single value) has a single panel.
   20.3. Within each panel, the entity dimension (for example, host) must be enumerated dynamically from the data and must not be hard-coded; each entity value must be drawn as one series.
   20.4. Each panel must plot its measures on the positive axis; the positive/negative inversion of an envelope graph (17.1) must not be applied in a drilldown panel, because direction is conveyed by the panel rather than by the sign of the axis.
   20.5. The same entity value should retain a consistent color across the panels of a drilldown dashboard.
21. An aggregated panel that has a drilldown dashboard should link to that dashboard.
   21.1. A drilldown link must open the drilldown dashboard in the same time range as the origin dashboard.

## Commentary
1. Right axes create different plot widths and distort horizontal comparisons across panels.
2. UOM context belongs in vertical axis tick labels, because scale can change with data range.
3. Use envelope graphs to visually segregate complementary dimensions, such as read bytes/sec and write bytes/sec.
4. Uniform grid width (6) keeps panel geometry comparable. A lone panel in the last row should not expand to full row width while neighbors use half width, or vertical comparison of the same column position becomes misleading; leaving an empty column preserves consistent grid width without inventing filler charts.
5. Aligned plot x-origins let the reader scan vertically and treat one calendar instant as one vertical line across stacked time-series panels. Matching y-axis region width (7 and 7.2) is the usual way products expose that alignment; mixed draw styles (for example bars versus lines) or differing aggregation bucket boundaries can still shift where a value appears relative to ticks unless settings are harmonized.
6. In an envelope graph the two complementary series represent one metric split by direction. The positive/negative split (17.1) is the primary direction cue and is supported by every platform. Distinct colors (17.3) and the legend distinguish the two directions; an optional title cue (17.5) names the positive direction in words. Earlier guidance to encode direction with a shared color and a dashed secondary line was dropped: it did not read well, was not portable (for example, Dynatrace dashboards expose no per-series dash style and color rules are value-based rather than keyed on the series name), and it does not scale once a panel carries many series.
7. Solid lines for every dimension (17.4) keep the rendering portable and uncluttered. Because direction is carried by sign, color, legend, and the optional title cue, no line-style differentiation is needed.
8. A drilldown dashboard answers "where / which entity?" after an aggregated panel answers "is anything happening?". Splitting by the secondary dimension into separate, vertically stacked panels (20.1, 20.2) keeps each panel to a single direction so the entity dimension can be enumerated dynamically (20.3) without hard-coding entity names — which is what lets the design scale from a few hosts to an enterprise. Plotting each panel positive (20.4) is clearer than mirroring once the entity count grows, and a stable per-entity color (20.5) lets the reader track one entity across the paired panels. Linking the aggregated panel to its drilldown (21) makes the navigation explicit.
9. Self-scaling UOMs and scale prefixes (16.1) keep axis labels short and comparable; thousands separators (16.2) keep any remaining large value readable. A bare large integer such as 123456 is hard to read and is avoided either by scaling (123 K, or a time UOM such as 2.06 min) or, failing that, by grouping digits (123,456).
10. The test for an envelope graph (17.6) is whether a single dimension enumerates the two series as its values. Read and write are values of a disk-direction dimension; in and out are values of a network-direction dimension; the inversion of one against the other is meaningful because they share an axis and an origin. GPU utilization and VRAM utilization fail this test: they are two different metrics that happen to share a percentage UOM, with no dimension whose values are "GPU%" and "VRAM%", so mirroring one below zero implies a relationship that does not exist. Such measures belong in separate panels (which may still sit side by side).
