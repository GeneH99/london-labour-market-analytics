-- London Labour Market BI Portfolio
-- Analytical model and priority scoring specification
-- Source tables are expected to be loaded from the cleaned_analytical layer.

-- Core borough fact view
CREATE OR REPLACE VIEW vw_borough_labour_market AS
SELECT
    b.borough_code,
    b.borough_name,
    u.unemployment_rate_pct,
    i.inactivity_rate_pct,
    j.jobs_density
FROM Dim_Borough b
LEFT JOIN D03_Fact_Unemployment_Borough u ON b.borough_code = u.borough_code
LEFT JOIN D04_Fact_Inactivity_Borough i ON b.borough_code = i.borough_code
LEFT JOIN D02_Fact_Jobs_Borough j ON b.borough_code = j.borough_code;

-- Priority methodology:
-- 1. z-standardise unemployment and inactivity.
-- 2. z-standardise jobs density and reverse its sign.
-- 3. Baseline score = equal-weighted mean of the three aligned z-scores.
-- 4. Rank descending; higher score = greater relative priority.
-- 5. Sensitivity scenarios:
--    S1 = 1/3, 1/3, 1/3
--    S2 = 0.40, 0.40, 0.20
--    S3 = 0.25, 0.25, 0.50
--    S4 = unemployment + inactivity only.
-- Cluster membership is contextual and is not included in the priority score.

-- Recommended Power BI fact output:
-- borough_code, borough_name, priority_score, priority_rank,
-- priority_tier, robust_high_priority, cluster, intervention_theme.
