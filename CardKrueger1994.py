import pandas as pd
from sklearn.linear_model import LinearRegression
from statsmodels.formula.api import ols

df = pd.read_csv('njmin3.csv')

#Groups mean full-time equivalent employees by state and period. nj = 1 is New Jersey, nj = 0 is Pennsylvania. d = 1 is after the minimum wage increase, d = 0 is before the minimum wage increase
FTEmean = df.groupby(['nj', 'd'])['fte'].agg(['mean','sem','count']).reset_index()
print(FTEmean)

#Difference in differences estimate of the effect of the minimum wage increase on full-time equivalent employees. FTE employment increased by 2.75 employees during the period in which NJ minimum wage was increased
DIDest = (FTEmean.iloc[3,2] - FTEmean.iloc[1,2]) - (FTEmean.iloc[2,2] - FTEmean.iloc[0,2])
print(DIDest)

#simple diff-in-diff regression using no controls
ols1 = ols('fte ~ nj + d + nj*d', data=df).fit()
print(ols1.summary())

#diff-in-diff regression using controls
ols2 = ols('fte ~ nj + d + nj*d + bk + kfc + roys + wendys + co_owned + centralj + southj + pa1', data=df).fit()
print(ols2.summary())