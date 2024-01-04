import pandas as pd
import numpy as np
import warnings
from sklearn.linear_model import LinearRegression
from statsmodels.formula.api import ols
import requests
import zipfile
from io import BytesIO, TextIOWrapper
from sklearn.utils import Bunch
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
from statsmodels.iolib.summary2 import summary_col
import statsmodels.api as sm
from adjustText import adjust_text


r = requests.get("https://davidcard.berkeley.edu/data_sets/njmin.zip")
z = zipfile.ZipFile(BytesIO(r.content))
df = pd.read_csv(z.open("public.dat"), engine="python", sep="\s+",
              header=None).applymap(lambda x: pd.to_numeric(x, errors="coerce"))

# Load column names and descriptions from `codebook`
codebook = [repr(line)
              for line in TextIOWrapper(z.open("codebook"), "cp437")]
# part of the codebook is not relevant
codes = codebook[7:11] + codebook[13:19] + \
    codebook[21:38] + codebook[40:59]
cols = [i.strip("'\" ").split()[0] for i in codes]
descriptions = [" ".join(i.strip("'\" ").split()[
                            4:]).rstrip('\\n') for i in codes]
column_descriptions = dict(zip(cols, descriptions))
df.columns = cols
df.columns = df.columns.str.lower()

#Full-time equivalent (FTE) employment calculation. FTE = 0.5 x number of part time workers + number of full time workers + number of managers
df = df.assign(fte=df.empft + 0.5 * df.emppt + df.nmgrs)
column_descriptions["fte"] = "Full-time-equivalent employment in wave 1 (full_time_employees + managers + 0.5*part_time_employees)"
df = df.assign(fte_after=df.empft2 + 0.5 * df.emppt2 + df.nmgrs2)
column_descriptions["fte_after"] = "Full-time-equivalent employment in wave 2 (full_time_employees + managers + 0.5*part_time_employees)"

#Converts int to str
df['state'] = df['state'].astype(str)

### Table 2 code
table2 = df[['wage_st', 'state']].copy()
table2['store'] = 1

# Creates a new category column that creates bins and labels to those bins that are identical to the ones in the paper
bins = np.arange(4.19, 5.61, 0.1)
labels = [str(round(x, 2)) for x in np.arange(4.25, 5.56, 0.1)]
table2['category'] = pd.cut(table2['wage_st'], bins=bins, labels=labels)

# Function that calculates the sum
def custom_sum(series):
    return np.sum(series)

table2 = table2.groupby(['state', 'category']).agg(sum_tot=('store', custom_sum)).reset_index()

# Convert category to string
table2['category'] = table2['category'].astype(str)
 
# Pivot the table
table2 = table2.pivot_table(index='category', columns='state', values='sum_tot', fill_value=0).reset_index()

# Increase each value of 'sum_tot' by 1, except for values of 0 - add more reasoning to why this is necessary
def increment_value(x):
    try:
        return int(x) + 1 if int(x) != 0 else 0
    except (ValueError, TypeError):
        return x

table2 = table2.applymap(increment_value)

# Removes unnessecary state label
table2.columns.name = None  

# Calculates percentage of stores in each state
table2['pa_percent'] = (table2['0'] / 79) * 100
table2['nj_percent'] = (table2['1'] / 331) * 100

print(table2)

#new table without values, just percents intended for the graph
table2_graph = pd.melt(table2, id_vars=["category"], value_vars=["nj_percent", "pa_percent"], var_name="state", value_name="percentage")

print(table2_graph)

# Table 2 Feb 1992 Wage Range Graph - before min wage
plt.figure(figsize=(12, 8))
sns.set_palette("pastel")
sns.barplot(x='category', y='percentage', hue='state', data=table2_graph)
plt.title('February 1992')
plt.xlabel('Wage Range')
plt.ylabel('Percentage of Stores')
#plt.show()
plt.savefig('Distribution of Starting Wage Rates Feb 1992')



###Table 3 code - no new code here, identical to table 2
table3 = df[['wage_st2', 'state']].copy()
table3['store'] = 1
table3['category'] = pd.cut(table3['wage_st2'], bins=bins, labels=labels)

table3 = table3.groupby(['state', 'category']).agg(sum_tot=('store', custom_sum)).reset_index()

table3['category'] = table3['category'].astype(str)
 
table3 = table3.pivot_table(index='category', columns='state', values='sum_tot', fill_value=0).reset_index()

def increment_value(x):
    try:
        return int(x) + 1 if int(x) != 0 else 0
    except (ValueError, TypeError):
        return x

table3 = table3.applymap(increment_value)

table3.columns.name = None  

table3['pa_percent'] = (table3['0'] / 79) * 100
table3['nj_percent'] = (table3['1'] / 331) * 100

print(table3)

table3_graph = pd.melt(table3, id_vars=["category"], value_vars=["nj_percent", "pa_percent"], var_name="state", value_name="percentage")

print(table3_graph)

# Table 3 Nov 1992 Wage Range Graph - after min wage
plt.figure(figsize=(12, 8))
sns.set_palette("pastel")
sns.barplot(x='category', y='percentage', hue='state', data=table3_graph)
plt.title('November 1992')
plt.xlabel('Wage Range')
plt.ylabel('Percentage of Stores')
#plt.show()
plt.savefig('Distribution of Starting Wage Rates Nov 1992')

results = df.groupby('state').agg(
    N=pd.NamedAgg(column='fte', aggfunc='size'),
    mean=pd.NamedAgg(column='fte', aggfunc='mean'),
    var=pd.NamedAgg(column='fte', aggfunc='var'),
    na_sum=pd.NamedAgg(column='fte', aggfunc=lambda x: sum(pd.isna(x)))
)

results['n'] = results['N'] - results['na_sum']
results['se'] = np.sqrt(results['var'] / results['n'])
results = results.reset_index()
print(results)

grouped_data = df.groupby('state').agg(
    mean_before=('fte', 'mean'),
    mean_after=('fte_after', 'mean'),
    var_before=('fte', 'var'),
    var_after=('fte_after', 'var'),
    n_before=('fte', lambda x: np.sum(~np.isnan(x))),
    n_after=('fte_after', lambda x: np.sum(~np.isnan(x)))
)

# Calculate standard errors for means
grouped_data['se_mean_before'] = np.sqrt(grouped_data['var_before'] / grouped_data['n_before'])
grouped_data['se_mean_after'] = np.sqrt(grouped_data['var_after'] / grouped_data['n_after'])

# Recode 'state' values
grouped_data['state'] = grouped_data.index.map({'0': 'PA', '1': 'NJ'})

# Calculate change in mean fte
grouped_data['change_mean_fte'] = grouped_data['mean_after'] - grouped_data['mean_before']

# Select the desired columns
result_df = grouped_data[['state', 'mean_before', 'mean_after', 'change_mean_fte', 'se_mean_before', 'se_mean_after']]

print(result_df)

filtered_data = df.dropna(subset=['fte', 'fte_after'])

# Group by 'state' and calculate means for balanced sample
balanced_sample = filtered_data.groupby('state').agg(
    mean_before_balanced=('fte', 'mean'),
    mean_after_balanced=('fte_after', 'mean')
)

# Calculate change in mean fte for balanced sample
balanced_sample['change_mean_fte_balanced'] = (
    balanced_sample['mean_after_balanced'] - balanced_sample['mean_before_balanced']
)

# Recode 'state' values
balanced_sample['state'] = balanced_sample.index.map({'0': 'PA', '1': 'NJ'})

# Select the desired columns
result_balanced_df = balanced_sample[['state', 'change_mean_fte_balanced']]

print(result_balanced_df)

#As state is both an index level and a column label, we do a little workaround by resetting the indexes, renaming the column in one of the DataFrames, and then merging the DataFrames on the renamed column. Then drop the renamed column
# Reset the index if 'state' is in the index
result_df = result_df.reset_index(drop=True)
result_balanced_df = result_balanced_df.reset_index(drop=True)

# Rename 'state' column in one of the DataFrames to avoid conflict
result_balanced_df.rename(columns={'state': 'state_balanced'}, inplace=True)

full_table = pd.merge(result_df, result_balanced_df, left_on='state', right_on='state_balanced', how='left')

# Drop column as not needed
full_table.drop('state_balanced', axis=1, inplace=True)


# Display the combined result
print(full_table)
full_table = full_table[['state', 'mean_before', 'mean_after', 
                         'se_mean_before', 'se_mean_after', 
                         'change_mean_fte', 'change_mean_fte_balanced']]

transposed = full_table.T

transposed.columns = ['PA', 'NJ']

# Create a new dataframe with the new rows
variable = pd.DataFrame({
    'variable': ['state', 'mean_before', 'mean_after', 'se_mean_before', 'se_mean_after', 'change_mean_fte', 'change_mean_fte_balanced']
})

# Filter out the 'state' row
variable = variable[variable['variable'] != 'state']

# Merge the transposed DataFrame with the variable DataFrame
result = pd.merge(variable, transposed, left_on='variable', right_index=True)

# Convert PA and NJ columns to numeric
result['PA'] = pd.to_numeric(result['PA'], errors='coerce')
result['NJ'] = pd.to_numeric(result['NJ'], errors='coerce')

# It's important to calculate the difference after ensuring both columns are numeric
result['Diff_NJ-PA'] = result['NJ'] - result['PA']

result = result[['variable', 'PA', 'NJ', 'Diff_NJ-PA']]

print(result)

#New df to add dummy for minimum wage increase to run basic regressions to compare to the mean FTE employment effects
fte_total = pd.concat([
    pd.DataFrame({'fte_total': df['fte'], 'd': 0}),
    pd.DataFrame({'fte_total': df['fte_after'], 'd': 1})
]).reset_index(drop=True)
fte_total['state'] = pd.concat([df['state'], df['state']]).reset_index(drop=True)
fte_total['co_owned'] = pd.concat([df['co_owned'], df['co_owned']]).reset_index(drop=True)
fte_total['centralj'] = pd.concat([df['centralj'], df['centralj']]).reset_index(drop=True)
fte_total['southj'] = pd.concat([df['southj'], df['southj']]).reset_index(drop=True)
fte_total['chain'] = pd.concat([df['chain'], df['chain']]).reset_index(drop=True)
fte_total['pa1'] = pd.concat([df['pa1'], df['pa1']]).reset_index(drop=True)

#simple diff-in-diff regression without controls
reg = ols('fte_total ~ d + state + d*state', data=fte_total).fit()
print(reg.summary())

for i in range(1, 5):
    fte_total[f'chain{i}'] = fte_total['chain'].apply(lambda x: 1 if x == i else 0)

#simple diff-in-diff regression with controls
reg2 = ols('fte_total ~ state + d + state*d + chain2 + chain3 + chain4 + co_owned + centralj + southj + pa1', data=fte_total).fit()
print(reg2.summary())

### Table 4 code
est_df = df.copy()

# Filter out rows with NA in specified columns
est_df = est_df.dropna(subset=['fte', 'fte_after', 'wage_st', 'wage_st2'])

# Creates column 'delta_emp' as the difference of 'fte_after' and 'fte', change in FTE
est_df['delta_emp'] = est_df['fte_after'] - est_df['fte']
est_df['state'] = est_df['state'].astype(int)


#Creates the gap variable for the second regression adjusted model, is 0 by default, is 0 for NJ stores with a wage_st of 5.05 or higher, is the difference between 5.05 and the wage_st for NJ stores with a wage_st of 5.05 or lower
est_df['gap'] = 0  # Default value
est_df.loc[(est_df['state'] == 1) & (est_df['wage_st'] <= 5.05), 'gap'] = (5.05 - est_df['wage_st']) / est_df['wage_st']

#Creates individual variables for each chain to be used as controls
for i in range(1, 5):
    est_df[f'chain{i}'] = est_df['chain'].apply(lambda x: 1 if x == i else 0)

#Running OLS linear regression models with different combinations of independent variables
model1 = ols('delta_emp ~ state', data=est_df).fit()
model2 = ols('delta_emp ~ state + co_owned + chain2 + chain3 + chain4', data=est_df).fit()
model3 = ols('delta_emp ~ gap', data=est_df).fit()
model4 = ols('delta_emp ~ gap + co_owned + chain2 + chain3 + chain4', data=est_df).fit()
model5 = ols('delta_emp ~ gap + co_owned + chain2 + chain3 + chain4 + centralj + northj + pa1', data=est_df).fit()

#Taking values from the models, params are the coefficients, bse are the standard errors, scale**.5 gives the standard error of regression
mod1_coeffs = model1.params
mod1_SE = model1.bse
mod1_RSE = model1.scale**.5
mod2_coeffs = model2.params
mod2_SE = model2.bse
mod2_RSE = model2.scale**.5
mod3_coeffs = model3.params
mod3_SE = model3.bse
mod3_RSE = model3.scale**.5
mod4_coeffs = model4.params
mod4_SE = model4.bse
mod4_RSE = model4.scale**.5
mod5_coeffs = model5.params
mod5_SE = model5.bse
mod5_RSE = model5.scale**.5

#New dataframe for table 4 recreation, note the models with controls have the p-value of joint F test for exclusion of all control variables
Table4 = pd.DataFrame({
    'Independent_variable': ["New Jersey dummy", "Initial wage gap", "Controls for chain and ownership",
                        "Controls for region", "Standard error of regression", "Probability value for controls"],
    'Model1_Coeff': [round(mod1_coeffs[1], 2), "-", "no", "no", round(mod1_RSE, 2), "-"],
    'Model1_SE': [round(mod1_SE[1], 2), "-", "no", "no", round(mod1_RSE, 2), "-"],
    'Model2_Coeff': [round(mod2_coeffs[1], 2), "-", "yes", "no", round(mod2_RSE, 2), round(model2.compare_f_test(model1)[1], 2)],
    'Model2_SE': [round(mod2_SE[1], 2), "-", "yes", "no", round(mod2_RSE, 2), round(model2.compare_f_test(model1)[1], 2)],
    'Model3_Coeff': ["-", round(mod3_coeffs[1], 2), "no", "no", round(mod3_RSE, 2), "-"],
    'Model3_SE': ["-", round(mod3_SE[1], 2), "no", "no", round(mod3_RSE, 2), "-"],
    'Model4_Coeff': ["-", round(mod4_coeffs[1], 2), "yes", "no", round(mod4_RSE, 2), round(model4.compare_f_test(model3)[1], 2)],
    'Model4_SE': ["-", round(mod4_SE[1], 2), "yes", "no", round(mod4_RSE, 2), round(model4.compare_f_test(model3)[1], 2)],
    'Model5_Coeff': ["-", round(mod5_coeffs[1], 2), "yes", "no", round(mod5_RSE, 2), round(model5.compare_f_test(model3)[1], 2)],
    'Model5_SE': ["-", round(mod5_SE[1], 2), "yes", "yes", round(mod5_RSE, 2), round(model5.compare_f_test(model3)[1], 2)],
})

print(Table4)

def outcome(t, control_intercept, treat_intercept_delta, trend, Δ, group, treated):
    return control_intercept + (treat_intercept_delta * group) + (t * trend) + (Δ * treated * group)

def is_treated(t, intervention_time, group):
    return (t > intervention_time) * group

#true parameters
control_intercept = 23.33
treat_intercept_delta = -2.89
trend = -2.16
Δ = 2.76
intervention_time = 0.5

fig, ax = plt.subplots()
ti = np.linspace(0, 1,3)
ax.plot(
    ti,
    outcome(
        ti,
        control_intercept,
        treat_intercept_delta,
        trend,
        Δ=0,
        group=1,
        treated=is_treated(ti, intervention_time, group=1),
    ),
    color="blue",
    label="Counterfactual",
    ls=":",
)
ax.plot(
    ti,
    outcome(
        ti,
        control_intercept,
        treat_intercept_delta,
        trend,
        Δ,
        group=1,
        treated=is_treated(ti, intervention_time, group=1),
    ),
    color="blue",
    label="Treatment group (NJ)",
)
ax.plot(
    ti,
    outcome(
        ti,
        control_intercept,
        treat_intercept_delta,
        trend,
        Δ,
        group=0,
        treated=is_treated(ti, intervention_time, group=0),
    ),
    color="C1",
    label="Control group (PA)",
)
ax.axvline(x=intervention_time, ls="-", color="r", label="Intervention", lw=3)
t = np.array([0, 1])
ax.plot(
    t,
    outcome(
        t,
        control_intercept,
        treat_intercept_delta,
        trend,
        Δ,
        group=1,
        treated=is_treated(t, intervention_time, group=1),
    ),
    "o",
    color="blue",
    markersize=0,
)
ax.plot(
    t,
    outcome(
        t,
        control_intercept,
        treat_intercept_delta,
        trend,
        Δ=0,
        group=0,
        treated=is_treated(t, intervention_time, group=0),
    ),
    "o",
    color="C1",
    markersize=0,
)
ax.set(
    xlabel=("time"),
    ylabel="FTE Employment (mean)",
    xticks=t,
    xticklabels=["February 1992", "November 1992"],
    title="Treatment Effect with Difference-in-Differences Estimator",
)
ax.legend();
#plt.show()
plt.grid()
plt.savefig('DID')
