-- ==============================================================================
-- 03_device_analysis.sql
-- Business Question: How does visitor behavior and conversion differ across Mobile, Desktop, and Tablet?
-- Metrics: Volume, Share of Traffic, Conversions, Conversion Rate, Bounce Rate by Device
-- ==============================================================================

SELECT 
    device,
    COUNT(session_id) AS total_sessions,
    ROUND(COUNT(session_id) * 100.0 / (SELECT COUNT(*) FROM website_sessions), 1) AS traffic_share_pct,
    SUM(CASE WHEN converted = TRUE THEN 1 ELSE 0 END) AS total_conversions,
    ROUND(SUM(CASE WHEN converted = TRUE THEN 1.0 ELSE 0.0 END) / COUNT(session_id) * 100, 2) AS conversion_rate_pct,
    ROUND(AVG(CASE WHEN bounced = TRUE THEN 1.0 ELSE 0.0 END) * 100, 1) AS bounce_rate_pct
FROM website_sessions
GROUP BY device
ORDER BY total_sessions DESC;
