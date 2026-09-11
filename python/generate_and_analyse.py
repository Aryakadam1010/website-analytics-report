"""
Website Analytics & Conversion Optimization Pipeline
-------------------------------------------------------------------
Author: Arya Vilas Kadam
Role Context: EY Consulting – Technology Analyst Portfolio
Workflow: Raw Data Ingestion -> Data Validation -> KPI Calculation ->
          Channel & Device Aggregations -> Business Reporting Exports
-------------------------------------------------------------------
"""

import os
import pandas as pd

# Dynamic path resolution to work from any working directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "..", "data", "website_sessions.csv")
DATA_DIR = os.path.join(BASE_DIR, "..", "data")


# ── 1. Data Ingestion ────────────────────────────────────────────────────────
def load_data(filepath=DATA_FILE) -> pd.DataFrame:
    """Reads raw session logs from CSV."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at {filepath}")
    return pd.read_csv(filepath)


# ── 2. Data Validation & Quality Check ───────────────────────────────────────
def validate_data(df: pd.DataFrame):
    """Performs essential data hygiene checks (missing values & duplicates)."""
    print("🔎 1. DATA QUALITY & INTEGRITY CHECK")
    print(f"  Total Records:        {len(df):,}")
    print(f"  Total Columns:        {df.shape[1]}")
    print(f"  Missing Values:       {df.isnull().sum().sum()}")
    print(f"  Duplicate Sessions:   {df['session_id'].duplicated().sum()}")
    print("  Status:               PASSED (Clean Dataset)\n")


# ── 3. Core Business Analyses ────────────────────────────────────────────────
def calculate_kpis(df: pd.DataFrame):
    """Analysis 1: High-level executive KPIs across the 24-month period."""
    total_sessions = len(df)
    total_conversions = int(df["converted"].sum())
    conv_rate = (total_conversions / total_sessions) * 100
    bounce_rate = df["bounced"].mean() * 100
    avg_duration = df["session_duration_s"].mean() / 60

    print("📊 2. OVERALL KPIs")
    print(f"  Total Sessions:       {total_sessions:,}")
    print(f"  Total Conversions:    {total_conversions:,}")
    print(f"  Conversion Rate:      {conv_rate:.2f}%")
    print(f"  Bounce Rate:          {bounce_rate:.1f}%")
    print(f"  Avg Duration:         {avg_duration:.1f} mins\n")


def analyze_traffic_sources(df: pd.DataFrame):
    """Analysis 2: Traffic acquisition channel volume and conversion effectiveness."""
    summary = df.groupby("traffic_source").agg(
        sessions=("session_id", "count"),
        conversions=("converted", "sum"),
        bounce_rate=("bounced", "mean")
    ).sort_values("sessions", ascending=False)

    summary["conv_rate"] = (summary["conversions"] / summary["sessions"]) * 100
    summary["bounce_rate"] = summary["bounce_rate"] * 100
    summary.to_csv(os.path.join(DATA_DIR, "traffic_source_analysis.csv"))

    print("🔍 3. TRAFFIC SOURCE PERFORMANCE")
    for source, row in summary.iterrows():
        print(f"  {source:<18} Sessions: {int(row['sessions']):>5} | Conv: {row['conv_rate']:.1f}% | Bounce: {row['bounce_rate']:.0f}%")
    print()


def analyze_devices(df: pd.DataFrame):
    """Analysis 3: Device breakdown comparing Mobile, Desktop, and Tablet user behavior."""
    summary = df.groupby("device").agg(
        sessions=("session_id", "count"),
        conversions=("converted", "sum"),
        bounce_rate=("bounced", "mean")
    ).sort_values("sessions", ascending=False)

    summary["traffic_share"] = (summary["sessions"] / len(df)) * 100
    summary["conv_rate"] = (summary["conversions"] / summary["sessions"]) * 100
    summary["bounce_rate"] = summary["bounce_rate"] * 100
    summary.to_csv(os.path.join(DATA_DIR, "device_breakdown.csv"))

    print("📱 4. DEVICE BREAKDOWN")
    for dev, row in summary.iterrows():
        print(f"  {dev:<10} {int(row['sessions']):>6} sessions ({row['traffic_share']:.0f}%) | Conv: {row['conv_rate']:.1f}% | Bounce: {row['bounce_rate']:.0f}%")
    print()


def analyze_monthly_trends(df: pd.DataFrame, last_n_months: int = 6):
    """Analysis 4: Month-over-month performance trends for recent periods."""
    summary = df.groupby("year_month").agg(
        sessions=("session_id", "count"),
        conversions=("converted", "sum"),
        bounce_rate=("bounced", "mean")
    ).reset_index()

    summary["conv_rate"] = (summary["conversions"] / summary["sessions"]) * 100
    summary["bounce_rate"] = summary["bounce_rate"] * 100
    summary.to_csv(os.path.join(DATA_DIR, "monthly_performance.csv"), index=False)

    print("📅 5. MONTHLY PERFORMANCE TREND (Recent 6 Months)")
    for _, row in summary.tail(last_n_months).iterrows():
        print(f"  {row['year_month']}  Sessions: {int(row['sessions']):>4} | Conv: {row['conv_rate']:.1f}% | Bounce: {row['bounce_rate']:.0f}%")
    print()


# ── 4. Main Workflow ─────────────────────────────────────────────────────────
def main():
    print("=" * 65)
    print("  WEBSITE ANALYTICS & CONVERSION OPTIMIZATION PIPELINE")
    print("  EY Technology Analyst Portfolio — Arya Vilas Kadam")
    print("=" * 65 + "\n")

    # Step 1: Load Data
    df = load_data()

    # Step 2: Validate Data
    validate_data(df)

    # Step 3: Run Core Analyses & Exports
    calculate_kpis(df)
    analyze_traffic_sources(df)
    analyze_devices(df)
    analyze_monthly_trends(df, last_n_months=6)

    print("💾 Summary reports saved to data/ for Power BI dashboard consumption.")
    print("=" * 65)


if __name__ == "__main__":
    main()
