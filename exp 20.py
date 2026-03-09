import numpy as np
from scipy.stats import ttest_ind

A = [0.10,0.12,0.11,0.13,0.09,0.10,0.12]
B = [0.14,0.15,0.13,0.16,0.14,0.15,0.13]

t,p = ttest_ind(A,B)

print("t-value:",t)
print("p-value:",p)

if p < 0.05:
    print("Significant difference between A and B")
else:
    print("No significant difference")
