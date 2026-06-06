import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

!pip install pymysql

from sqlalchemy import create_engine

user = "root"
password = "root"
host = "127.0.0.1"
database = "bank"

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

query = "SELECT * FROM bankchurn"

df = pd.read_sql(query, engine)

df.head()

df.tail()

df.info()

df.describe().round()

df.isnull().sum()

df.describe(include = 'all')

df.nunique()

df = df.drop(columns = ["CustomerId" , "SurName"])
df

df.shape
df['ActiveMember'].mode()
df['HasCrCard'].mode()
df['Salary'].mean()
df['Exited'].mode()
df['Balance'].mean()
df['Age'].mode()

numerical_input_cols = df.select_dtypes(exclude = ["object"]).drop(columns = ["Exited"]).columns
categorical_input_cols = df.select_dtypes(include = ["object"]).columns

numerical_input_cols

categorical_input_cols

plt.figure(figsize=(10,5))
plt.rc("font", size=14)

ax = sns.countplot(y='Exited', data=df)

total = len(df)

for p in ax.patches:
    count = int(p.get_width())
    percentage = 100 * count / total

    ax.text(
        p.get_width() + 10,
        p.get_y() + p.get_height()/2,
        f'{count} ({percentage:.1f}%)',
        va='center'
    )

plt.title("Customer Churn Distribution")
plt.show()

for col in numerical_input_cols:
    df.hist(col, figsize=(8,6))
    plt.show()

for col in categorical_input_cols:
    plt.figure(figsize=(20, 6))
    
    sns.countplot(data=df, x=col, hue="Exited", palette='hot')
    
    plt.xticks(rotation=45)
    plt.show()

for col in numerical_input_cols:
    plt.figure(figsize=(14,6))
    sns.violinplot(x='Exited', y=col, data=df)
    plt.show()

import matplotlib.pyplot as plt
plt.figure(figsize=(8,12))
plt.boxplot(df['Salary'])
plt.show()

plt.figure(figsize=(8,12))
plt.boxplot(df['Age'])
plt.show()

plt.figure(figsize=(8,12))
plt.boxplot(df['Balance'])
plt.show()

df['Age'].describe()

q1, q3 = np.nanpercentile(df["Age"], [25, 75]) 
iqr = q3 - q1 
lower_bound = q1 - (iqr * 1.5) 
upper_bound = q3 + (iqr * 1.5)


print("Quartile 1 :",q1)
print("Quartile 3 :",q3)
print("Inter Quartile Range :", iqr)
print("Lower limit :",lower_bound)
print("Upper limit :",upper_bound)

df[df['Age'] > upper_bound]

new_df = df.copy()

new_df['Age'] = np.where(
    new_df['Age'] > upper_bound,
    upper_bound,
    np.where(
        new_df['Age'] < lower_bound,
        lower_bound,
        new_df['Age']
    )
)

new_df

sns.boxplot(new_df['Age'])

corr_data=new_df[['Age',	'Tenure',	'Balance',	'NumOfProducts',	'HasCrCard',	'ActiveMember',	'Salary',	'Exited']]
plt.figure(figsize=(12, 6))
sns.heatmap(corr_data.corr(), annot=True)
plt.show()

pd.get_dummies(new_df['Country'])

new_df.head()

df = pd.get_dummies(new_df, columns=['Country'])
df


