# London Labour Market — BI/Data Analyst Portfolio

## Deliverables

This package contains the analytical assets for the London Labour Market BI portfolio.

### Main files
- `London_Labour_Market_Analytical_Workbook.xlsx` — consolidated workbook
- `csv/` — Power BI-ready / analysis tables
- `london_labour_market_portfolio.sql` — SQL model and priority methodology
- `reproduce_priority_model.py` — reproducible Python scoring logic
- `London_Labour_Market_Portfolio_Walkthrough.ipynb` — notebook walkthrough
- `Final_Recommendations.docx` — final recommendations report
- `Final_Recommendations.pdf` — PDF version
- `Portfolio_Presentation.pptx` — presentation
- `README.md` — project documentation

## Analytical chain

## Analytical Chain

**Cluster Validation & Interpretation**  
↓  
**Priority Framework**  
↓  
**Borough Priority Score**  
↓  
**Priority Tiers & Robustness**  
↓  
**Intervention Mapping**  
↓  
**Final Recommendations**

## Priority methodology

Baseline score:
- unemployment: higher = greater priority
- inactivity: higher = greater priority
- jobs density: lower = greater priority

All three indicators are z-standardised and equally weighted for the baseline.
Sensitivity scenarios test alternative weighting and exclusion of jobs density.

## Important limitations

The priority score is relative and analytical. It is not a causal estimate, deprivation
index, funding formula, or forecast. Intervention themes are evidence-informed and should
not be interpreted as proof of policy effectiveness.

## Power BI

A native `.pbix` file is not generated in this environment. The workbook, CSV tables,
SQL, Python and notebook provide the data/model specification needed to assemble the
Power BI report.
