import numpy as np
from scipy import stats

# Sample data (blood pressure reduction)
drug = [8,10,12,9,11,7,13,10,9,12]
placebo = [3,4,2,5,3,4,3,2,4,3]

# 95% Confidence Interval
drug_ci = stats.t.interval(0.95, len(drug)-1, loc=np.mean(drug), scale=stats.sem(drug))
placebo_ci = stats.t.interval(0.95, len(placebo)-1, loc=np.mean(placebo), scale=stats.sem(placebo))

print("Drug 95% CI:", drug_ci)
print("Placebo 95% CI:", placebo_ci)
