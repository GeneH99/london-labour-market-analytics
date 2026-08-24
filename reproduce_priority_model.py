from pathlib import Path
import pandas as pd, numpy as np

ROOT = Path(".")
panel = pd.read_csv(ROOT / "phase07_labour_market_analysis/A05_Borough_Diagnostic_Panel.csv")
metrics = ["unemployment_rate_pct","inactivity_rate_pct","jobs_density"]
df = panel[["borough_code","borough_name"] + metrics].dropna().copy()

aligned = {}
for m in metrics:
    z = (df[m]-df[m].mean())/df[m].std(ddof=0)
    aligned[m] = -z if m == "jobs_density" else z
X = pd.DataFrame(aligned)

scenarios = {
    "S1_Equal_Weights": [1/3,1/3,1/3],
    "S2_Unemployment_Inactivity_Heavy": [0.40,0.40,0.20],
    "S3_Jobs_Density_Heavy": [0.25,0.25,0.50],
}
out = df[["borough_code","borough_name"]].copy()
for name,w in scenarios.items():
    out[name] = X[metrics].to_numpy() @ np.array(w)
out["S4_Unemployment_Inactivity_Only"] = X[["unemployment_rate_pct","inactivity_rate_pct"]].mean(axis=1)
out["priority_score"] = out["S1_Equal_Weights"]
out["priority_rank"] = out["priority_score"].rank(ascending=False, method="min").astype(int)
n = len(out); cut = int(np.ceil(n/3))
out["priority_tier"] = np.where(out.priority_rank <= cut, "High priority",
                         np.where(out.priority_rank <= 2*cut, "Medium priority", "Lower priority"))
out.to_csv("priority_scores_reproduced.csv", index=False)
print("Priority model reproduced.")
