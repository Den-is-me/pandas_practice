import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('lesson_3_data__1_.csv', encoding='windows-1251')
# print(df.head())

# take necessary data:
user_df = df[['tc', 'art_sp']]
# fix columns names:
user_df = user_df.rename(columns={'tc': 'user_id', 'art_sp': 'brand_info'})
# take brand name from brand_info
user_df['brand_name'] = user_df.brand_info.apply(lambda x: x.split()[-1])
# count purchases for each user who hase made more than 5 purchases:
user_purchases = user_df.groupby('user_id', as_index=False) \
    .agg({'brand_name': 'count'}) \
    .rename(columns={'brand_name': 'purchases'}) \
    .query('purchases >= 5')
# select the most popular brand for each user:
user_lovely_brand = user_df.groupby(['user_id', 'brand_name'], as_index=False) \
    .agg({'brand_info': 'count'}) \
    .sort_values(['user_id', 'brand_info'], ascending=[False, False]) \
    .groupby('user_id') \
    .head(1) \
    .rename(columns={'brand_info': 'lovely_brand_count', 'brand_name': 'lovely_brand'})
# select how many brands users have bought:
user_unique_brand = user_df.groupby(['user_id'], as_index=False) \
    .agg({'brand_name': pd.Series.nunique}) \
    .rename(columns={'brand_name': 'unique_brand'})
# join DFs for final score
loyality_df = user_purchases.merge(user_lovely_brand, on='user_id') \
    .merge(user_unique_brand, on='user_id')
# select the most loyal users
loyal_users = loyality_df[loyality_df.unique_brand == 1]
# create score to compare users
loyality_df['loyal_score'] = loyality_df.lovely_brand_count / loyality_df.purchases
# visualize result
ax = sns.displot(loyality_df.loyal_score)
plt.show()
