import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

age=[23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,60,61]
fat=[9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,30.2,34.1,32.9,41.2,35.7]

df=pd.DataFrame({"Age":age,"Fat":fat})

print("Mean\n",df.mean())
print("Median\n",df.median())
print("Std\n",df.std())

df.boxplot()
plt.show()

plt.scatter(age,fat)
plt.show()

stats.probplot(age,plot=plt)
plt.show()
