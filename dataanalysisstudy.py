#A collection of different SQL to Python equivalents using the files from python_data_analysis

import pandas as pd

#SELECT
df1 = pd.read_csv('/Users/kerrafuller/Downloads/people_500000.csv')
df2 = pd.read_csv('/Users/kerrafuller/Downloads/organizations_500000.csv')
df3 = pd.read_csv('/Users/kerrafuller/Downloads/customers_500000.csv')
df4 = pd.read_csv('/Users/kerrafuller/Downloads/products_2000000.csv')


#FROM
user = df1['User Id']
discription_o = df2['Description']
email = df3['Email']
discription_p = df4['Description']

print(user.head())
print(discription_o.head())
print(email.head())
print(discription_p.head())


#GROUP BY
sex = df1.groupby('Sex').size()
country_o = df2.groupby('Country').size()
country_c = df3.groupby('Country').size()
avaliability = df4.groupby('Availability').size()
currency = df4.groupby('Currency').size()

print(sex)
print(country_o)
print(country_c)
print(avaliability)
print(currency)
    #all curency are in USD, no need for conversion


#ORDER BY
df1_age_s = df1.sort_values('Date of birth', ascending=True)
df2_size_s = df2.sort_values('Number of employees', ascending=True)
df3_longevity_s = df3.sort_values('Subscription Date', ascending=True)
df4_price_s = df4.sort_values('Price', ascending=True)

print(df1_age_s.head())
print(df2_size_s.head())
print(df3_longevity_s.head())
print(df4_price_s.head())


#AVG
df1['Year born'] = [str(val)[:4] for val in df1['Date of birth']]
df3['Subscription Year'] = [str(val)[:4] for val in df3['Subscription Date']]
avg_year_born = df1['Year born'].astype(int).mean()
avg_age_p = 2026 - avg_year_born
avg_founding_year = df2['Founded'].mean()
avg_age_o = 2026 - avg_founding_year
avg_subscription_year = df3['Subscription Year'].astype(int).mean()
avg_longevity_c = 2026 - avg_subscription_year
avg_price = df4['Price'].mean()

print(avg_age_p)
print(avg_age_o)
print(avg_longevity_c)
print(avg_price)


#WHERE
avg_dob = str(int(avg_year_born)) + '-01-01'
avg_longevity = str(int(avg_subscription_year)) + '-01-01'
df1_age_w = df1[df1['Date of birth'] > avg_dob]
df2_age_w = df2[df2['Founded'] > avg_founding_year]
df3_longevity_w = df3[df3['Subscription Date'] < avg_longevity]
df4_price_w = df4[df4['Price'] > avg_price]

print(df1_age_w.head())
print(df2_age_w.head())
print(df3_longevity_w.head())
print(df4_price_w.head())


#NULL CHECK
df1_null = df1[df1['Date of birth'].isnull() & df1['Phone'].isnull()]
df2_null = df2[df2['Founded'].isnull() & df2['Number of employees'].isnull()]
df3_null = df3[df3['Phone 1'].isnull() & df3['Phone 2'].isnull() & df3['Subscription Date'].isnull()]
df4_null = df4[df4['Price'].isnull() & df4['Stock'].isnull() & df4['EAN'].isnull() & df4['Internal ID'].isnull()]

print(df1_null.head())
print(df2_null.head())
print(df3_null.head())
print(df4_null.head())


#NULL SUM
null_sum_df1 = df1.isnull().sum()
null_sum_df2 = df2.isnull().sum()
null_sum_df3 = df3.isnull().sum()
null_sum_df4 = df4.isnull().sum()

print(null_sum_df1)
print(null_sum_df2)
print(null_sum_df3)
print(null_sum_df4)


