# Website Analytics & Conversion Optimization
### Python | SQL | Pandas | Excel | Data Analytics

**Author:** Arya Vilas Kadam  
**Target Role:** EY Consulting – Technology Analyst Portfolio  
**Domain:** Data Analytics  

```
Raw Website Data  ➔  SQL Analysis  ➔  Python/Pandas Analysis  ➔  KPI Report  ➔  Business Insights  ➔  Recommendations
```

---

## Overview

This project is a technology and data analytics consulting case study analyzing digital patient acquisition, traffic channel effectiveness, user engagement, and appointment booking conversions across a 24-month period (**38,181 sessions**).

Following a standard technology consulting framework, raw website session logs are queried with **basic SQL**, validated and aggregated using a concise **Python/Pandas pipeline**, summarized in **Excel**, and synthesized into data-backed executive insights and practical recommendations.

---

## Business Problem

The clinic's management lacked clear quantitative visibility into their digital patient acquisition funnel:
1. **Traffic Channel Efficacy**: Which marketing sources drove visits, and which actually produced paying appointment bookings?
2. **User Drop-Off**: Why were visitors leaving the website without completing bookings?
3. **Device Behavioral Differences**: How did user engagement and conversion rates differ between mobile and desktop visitors?
4. **Growth Trajectory**: How were session volumes and appointment bookings evolving over time?

---

## Business Questions

This project answers five core consulting questions:
- **Which acquisition channels generate the most traffic?**
- **Which channels have the highest conversion rates?**
- **How does website performance differ across devices?**
- **Are there any noticeable monthly trends?**
- **Where are the major opportunities for improving conversion?**

---

## Dataset

- **Source:** Synthetic Google Analytics web session logs modeled on wellness clinic traffic patterns.
- **Volume:** **38,181 session records** spanning June 2022 to May 2024 (24 months).
- **Key Attributes:**
  - `session_id`: Unique identifier for each session
  - `date`, `year_month`: Timestamps for trend analysis
  - `traffic_source`: Marketing channel (`Organic Search`, `Direct`, `Social Media`, `Paid Search`, `Email Campaign`, `Referral`)
  - `device`: User platform (`Mobile`, `Desktop`, `Tablet`)
  - `pages_viewed`: Pages browsed per visit
  - `session_duration_s`: Visit duration in seconds
  - `bounced`: Boolean flag (`True` if user exited after 1 page)
  - `converted`: Boolean flag (`True` if session completed an appointment booking)

---

## Tools & Technologies

| Tool / Technology | Purpose in This Project |
|---|---|
| **SQL** | Core business queries, multi-dimensional grouping, and rate calculations |
| **Python (Pandas)** | Automated data ingestion, data quality validation, KPI computation, and exports |
| **Microsoft Excel / CSV** | Executive KPI summary sheet (`data/executive_summary.xlsx`) and tabular storage |

---

## Methodology

This project follows a 5-step consulting delivery workflow:

1. **Raw Data Ingestion & Quality Validation**: Ingested 38,181 session records in Python; verified zero missing values and zero duplicate records.
2. **Basic SQL Analysis**: Authored 4 clean, modular SQL queries (`sql/`) using fundamental SQL syntax (`SELECT`, `WHERE`, `GROUP BY`, `ORDER BY`, `COUNT`, `SUM`, `AVG`, `CASE WHEN`).
3. **Python/Pandas Automation**: Built a lightweight, readable script (`python/generate_and_analyse.py`, < 100 lines) to automate aggregations and export reports in **0.06 seconds**.
4. **KPI Reporting & Excel Summary**: Generated high-level KPI tables and an executive summary spreadsheet for stakeholders.
5. **Insights & Recommendations**: Translated analytical findings into structured consulting recommendations directly supported by data.

---

## Key KPIs

| KPI | Metric Value | Business Meaning |
|---|---|---|
| **Total Sessions** | **38,181** | Total digital visits over 24 months |
| **Total Conversions** | **1,220** | Confirmed online appointment bookings |
| **Overall Conversion Rate** | **3.20%** | Percentage of visits resulting in a booking |
| **Overall Bounce Rate** | **39.8%** | Percentage of single-page visits without interaction |
| **Average Session Duration** | **2.9 mins** | Average visitor engagement time |

---

## Executive Insights

Every insight pairs an empirical finding with its business impact:

- **Insight 1: Organic Search Drives Primary Traffic Volume**  
  - *Finding:* Organic Search accounts for **38% of total traffic** (14,402 sessions) with a steady **3.3% conversion rate** (475 bookings).  
  - *Business Impact:* Search visibility is the clinic's largest patient acquisition channel, making sustained search engine optimization essential for baseline demand.

- **Insight 2: Email Campaigns Deliver the Highest Conversion Efficiency**  
  - *Finding:* Email Campaigns achieved the highest conversion rate across all sources at **6.2%**, despite representing only **6% of total sessions** (2,270 visits).  
  - *Business Impact:* This suggests that higher-intent traffic from email may be significantly more effective for generating conversions, making it the highest-ROI channel to scale.

- **Insight 3: Social Media Suffers from High Drop-Off and Low Conversion**  
  - *Finding:* Social Media drove 6,748 sessions (18% of traffic) but converted at only **1.1%**, while exhibiting the highest bounce rate across all channels at **53%**.  
  - *Business Impact:* Current social media visitors behave as casual browsers rather than qualified healthcare leads; current ad spend on social may be underperforming.

- **Insight 4: Mobile Traffic Lags in Conversion Performance**  
  - *Finding:* Mobile accounts for **48% of total visits** (18,453 sessions) but converts at **3.0%**, trailing Desktop at **3.4%**.  
  - *Business Impact:* Because nearly half of all visitors arrive on mobile devices, even minor friction in the mobile booking flow translates into noticeable lost appointment revenue.

- **Insight 5: Consistent Long-Term Growth Trajectory**  
  - *Finding:* Monthly sessions increased steadily from ~1,200/month in June 2022 to **2,054/month** in May 2024 (~3% compounding monthly growth).  
  - *Business Impact:* Overall clinic demand and brand awareness are expanding, providing a stable foundation for conversion rate optimization.

---

## Business Recommendations

Based strictly on the empirical data, four practical recommendations are proposed:

1. **Focus More on High-Converting Acquisition Channels**:  
   Increase email campaign cadence and introduce targeted appointment reminders to capitalize on the channel's **6.2% conversion rate**.
2. **Investigate and Streamline Mobile User Experience**:  
   Audit the mobile booking flow to reduce form friction, simplify steps, and close the 0.4% conversion gap with desktop visitors.
3. **Review Traffic Sources with High Sessions but Low Conversion**:  
   Refine social media targeting toward intent-driven healthcare demographics rather than broad awareness to address the 53% bounce rate.
4. **Prioritize Channel Optimization Over Raw Volume**:  
   The analysis identifies opportunities to improve website conversion through channel optimization and user-experience improvements rather than solely increasing top-of-funnel marketing spend.

---

## Project Structure

```
website-analytics-report/
│
├── data/
│   ├── website_sessions.csv            # Raw session logs (38,181 records)
│   ├── executive_summary.xlsx          # Executive KPI summary spreadsheet
│   ├── traffic_source_analysis.csv     # Traffic source performance breakdown
│   ├── device_breakdown.csv            # Device usage analysis (Mobile vs Desktop vs Tablet)
│   └── monthly_performance.csv         # Month-by-month KPI trends
│
├── sql/
│   ├── 01_overall_kpis.sql             # SQL: Total sessions, conversions, rates
│   ├── 02_channel_performance.sql      # SQL: Traffic source volume and conversions
│   ├── 03_device_analysis.sql          # SQL: Device volume and conversion comparison
│   └── 04_monthly_trends.sql           # SQL: Monthly trend aggregation
│
├── python/
│   └── generate_and_analyse.py         # Automated data validation & reporting script
│
├── README.md                           # Consulting case study documentation
└── .gitignore                          # Excludes Python bytecode and OS files
```

---

## How to Run

### 1. Python Analytics Pipeline
Requires Python 3.8+ and Pandas:
```bash
# Install dependency
pip install pandas openpyxl

# Run the automated pipeline from the repository root
python3 python/generate_and_analyse.py
```
*Validates data quality, prints all 4 analyses in under 0.1s, and exports summary CSVs and an Excel sheet to `data/`.*

### 2. SQL Analysis
The SQL scripts in `sql/` can be executed against any standard SQL database (PostgreSQL, MySQL, SQLite, Snowflake) containing the `website_sessions` table:
- Run `sql/01_overall_kpis.sql` for overall totals.
- Run `sql/02_channel_performance.sql` for acquisition channel metrics.
- Run `sql/03_device_analysis.sql` for mobile vs. desktop comparison.
- Run `sql/04_monthly_trends.sql` for time-series analysis.

---

## Future Scope

- **Power BI Executive Dashboard**: Develop an interactive Power BI dashboard to provide executive-level visualization of traffic, engagement, conversion, channel performance, device performance, and monthly trends.
- **Automated Data Ingestion**: Connect the Python script directly to the Google Analytics 4 (GA4) API to automate daily data extraction.
- **A/B Testing Framework**: Implement statistical hypothesis testing on mobile checkout redesign variants.
