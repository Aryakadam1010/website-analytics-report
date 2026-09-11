# 📊 Power BI Executive Dashboard

![Website Analytics & Conversion Optimization Dashboard](dashboard_screenshot.png)

## Overview
This single-page executive Power BI dashboard visualizes patient acquisition channels, user engagement, device performance, and appointment booking conversions across a 24-month period (38,181 sessions).

---

## Key Visuals & Layout

| Visual Component | Chart Type | Fields / Dimensions | Purpose |
|---|---|---|---|
| **Top KPI Cards** | Card Visuals | `Total Sessions`, `Total Conversions`, `Conversion Rate`, `Bounce Rate` | Immediate executive summary of high-level performance |
| **Sessions by Channel** | Clustered Bar Chart | Y-Axis: `traffic_source`, X-Axis: `Total Sessions` | Identifies primary traffic drivers (Organic Search leads at 14.4k) |
| **Conversion Rate by Channel** | Clustered Column Chart | X-Axis: `traffic_source`, Y-Axis: `Conversion Rate (%)` | Highlights conversion champions (Email Campaign leads at 6.2%) |
| **Sessions by Device** | Donut Chart | Legend: `device`, Values: `Total Sessions` | Displays audience distribution (Mobile 48%, Desktop 45%, Tablet 7%) |
| **Conversion Rate by Device** | Column Chart | X-Axis: `device`, Y-Axis: `Conversion Rate (%)` | Highlights mobile conversion drop-off vs. desktop |
| **Monthly Trend** | Line & Area Chart | X-Axis: `year_month`, Values: `Total Sessions`, `Total Conversions` | Tracks 24-month growth and seasonal patterns |

---

## Simple DAX Measures Used

To keep the model clean and beginner-friendly, only 4 fundamental calculated measures are used:

```dax
// 1. Total Sessions
Total Sessions = COUNTROWS('website_sessions')

// 2. Total Conversions
Total Conversions = CALCULATE(
    COUNTROWS('website_sessions'),
    'website_sessions'[converted] = TRUE()
)

// 3. Overall Conversion Rate (%)
Conversion Rate = DIVIDE([Total Conversions], [Total Sessions], 0)

// 4. Overall Bounce Rate (%)
Bounce Rate = DIVIDE(
    CALCULATE(COUNTROWS('website_sessions'), 'website_sessions'[bounced] = TRUE()),
    [Total Sessions],
    0
)
```

---

## 5-Minute Build Steps in Power BI Desktop
1. **Get Data**: Click `Get Data` → `Text/CSV` → Select `data/website_sessions.csv`.
2. **Transform Data**: Verify column types (`date` as Date, `converted` and `bounced` as True/False booleans). Click `Close & Apply`.
3. **Add Measures**: Under the Modeling tab, create the 4 DAX measures above.
4. **Build Layout**:
   - Insert 4 **Cards** at the top for the KPIs.
   - Insert **Clustered Bar Charts** for Channel Volume and Channel Conversion Rate.
   - Insert a **Donut Chart** for Device Traffic Share.
   - Insert a **Line Chart** for 24-month Monthly Trends (`year_month` on X-Axis).
5. **Theme & Formatting**: Apply clean corporate styling (white canvas, slate/dark blue accents, percentage formatting with 1-2 decimals).
