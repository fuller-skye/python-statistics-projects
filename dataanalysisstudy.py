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

#print(user.head())
#print(discription_o.head())
#print(email.head())
#print(discription_p.head())


#GROUP BY
sex = df1.groupby('Sex').size()
country_o = df2.groupby('Country').size()
country_c = df3.groupby('Country').size()
avaliability = df4.groupby('Availability').size()
currency = df4.groupby('Currency').size()

#print(sex)
#print(country_o)
#print(country_c)
#print(avaliability)
#print(currency)
    #all curency are in USD, no need for conversion


#ORDER BY
df1_age = df1.sort_values('Date of birth', ascending=True)
df2_size = df2.sort_values('Number of employees', ascending=True)
df3_longevity = df3.sort_values('Subscription Date', ascending=True)
df4_price = df4.sort_values('Price', ascending=True)

#print(df1_age.head())
#print(df2_size.head())
#print(df3_longevity.head())
#print(df4_price.head())


df1['Year born'] = [str(val)[:4] for val in df1['Date of birth']]
df3['Subscription Year'] = [str(val)[:4] for val in df3['Subscription Date']]
#AVG
avg_year_born = df1['Year born'].astype(int).mean()
avg_age_p = 2026 - avg_year_born
print(avg_age_p)
avg_founding_year = df2['Founded'].mean()
avg_age_o = 2026 - avg_founding_year
print(avg_age_o)
avg_subscription_year = df3['Subscription Year'].astype(int).mean()
avg_longevity_c = 2026 - avg_subscription_year
print(avg_longevity_c)
avg_price = df4['Price'].mean()
print(avg_price)
