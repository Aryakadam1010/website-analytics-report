"""
Website Analytics & Performance Report
------------------------------------------------------------
Purpose: Ingest website session logs and analyze traffic sources,
         user engagement, device usage, and appointment conversions.
"""

import os
import pandas as pd

DATA_FILE = "data/website_sessions.csv"


# ── 1. Load Data ─────────────────────────────────────────────────────────────
def load_data(filepath=DATA_FILE):
    """Loads session data from CSV."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at {filepath}")
    return pd.read_csv(filepath)


# ── 2. Top Core Analyses ─────────────────────────────────────────────────────
def calculate_kpis(df):
    """Analysis 1: Overall Executive KPIs across 24 months."""
    total_sessions = len(df)
    total_conversions = int(df["converted"].sum())
    conv_rate = (total_conversions / total_sessions) * 100
    bounce_rate = df["bounced"].mean() * 100
    avg_duration = df["session_duration_s"].mean() / 60

    print("📊 1. OVERALL KPIs")
    print(f"  Total Sessions:       {total_sessions:,}")
    print(f"  Total Conversions:    {total_conversions:,}")
    print(f"  Conversion Rate:      {conv_rate:.2f}%")
    print(f"  Bounce Rate:          {bounce_rate:.1f}%")
    print(f"  Avg Duration:         {avg_duration:.1f} mins\n")


def analyze_traffic_sources(df):
    """Analysis 2: Traffic sources ranked by session volume and conversion rate."""
    summary = df.groupby("traffic_source").agg(
        sessions=("session_id", "count"),
        conversions=("converted", "sum"),
        bounce_rate=("bounced", "mean")
    ).sort_values("sessions", ascending=False)

    summary["conv_rate"] = (summary["conversions"] / summary["sessions"]) * 100
    summary["bounce_rate"] = summary["bounce_rate"] * 100
    summary.to_csv("data/traffic_source_analysis.csv")

    print("🔍 2. TRAFFIC SOURCE PERFORMANCE")
    for source, row in summary.iterrows():
        print(f"  {source:<18} Sessions: {int(row['sessions']):>5} | Conv: {row['conv_rate']:.1f}% | Bounce: {row['bounce_rate']:.0f}%")
    print()


def analyze_devices(df):
    """Analysis 3: Device breakdown (Mobile vs Desktop vs Tablet)."""
    summary = df.groupby("device").agg(
        sessions=("session_id", "count"),
        conversions=("converted", "sum"),
        bounce_rate=("bounced", "mean")
    ).sort_values("sessions", ascending=False)

    summary["traffic_share"] = (summary["sessions"] / len(df)) * 100
    summary["conv_rate"] = (summary["conversions"] / summary["sessions"]) * 100
    summary["bounce_rate"] = summary["bounce_rate"] * 100
    summary.to_csv("data/device_breakdown.csv")

    print("📱 3. DEVICE BREAKDOWN")
    for dev, row in summary.iterrows():
        print(f"  {dev:<10} {int(row['sessions']):>6} sessions ({row['traffic_share']:.0f}%) | Conv: {row['conv_rate']:.1f}% | Bounce: {row['bounce_rate']:.0f}%")
    print()


def analyze_monthly_trends(df, last_n_months=6):
    """Analysis 4: Recent monthly performance trends."""
    summary = df.groupby("year_month").agg(
        sessions=("session_id", "count"),
        conversions=("converted", "sum"),
        bounce_rate=("bounced", "mean")
    ).reset_index()

    summary["conv_rate"] = (summary["conversions"] / summary["sessions"]) * 100
    summary["bounce_rate"] = summary["bounce_rate"] * 100
    summary.to_csv("data/monthly_performance.csv", index=False)

    print("📅 4. MONTHLY PERFORMANCE TREND (Recent 6 Months)")
    for _, row in summary.tail(last_n_months).iterrows():
        print(f"  {row['year_month']}  Sessions: {int(row['sessions']):>4} | Conv: {row['conv_rate']:.1f}% | Bounce: {row['bounce_rate']:.0f}%")
    print()


# ── 3. Main Execution ────────────────────────────────────────────────────────
def main():
    print("=" * 60)
    print("  WEBSITE ANALYTICS — CORE PERFORMANCE REPORT")
    print("=" * 60 + "\n")

    # Load dataset
    df = load_data()

    # Execute core analyses
    calculate_kpis(df)
    analyze_traffic_sources(df)
    analyze_devices(df)
    analyze_monthly_trends(df, last_n_months=6)

    print("💾 Reports saved to data/ directory.")
    print("=" * 60)


if __name__ == "__main__":
    main()
