import pandas as pd

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Quick check
print(df.head())
print(df.info())

# Encode categorical Attrition column
df['Attrition'] = df['Attrition'].map({'Yes':1, 'No':0})

# Create Salary Band
df['SalaryBand'] = pd.cut(df['MonthlyIncome'],
                          bins=[0, 3000, 6000, 9000, 12000, 20000],
                          labels=['Low', 'Mid-Low', 'Mid', 'Mid-High', 'High'])
import seaborn as sns
import matplotlib.pyplot as plt

# Attrition by Department
plt.figure(figsize=(6,4))
sns.countplot(x='Department', hue='Attrition', data=df)
plt.title("Attrition by Department")
plt.show()

# Salary vs Attrition
plt.figure(figsize=(6,4))
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df)
plt.title("Salary vs Attrition")
plt.show()
