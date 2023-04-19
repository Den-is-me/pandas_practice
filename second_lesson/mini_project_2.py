import pandas as pd

# 1. read cvs files
user_data = pd.read_csv('user_data.csv', encoding='UTF-8')
logs = pd.read_csv('logs.csv', encoding='UTF-8')
# check data
# print(user_data.dtypes)
# print(user_data.head())
# print(log.head())
# how many unique value in platform column
# print(logs.platform.nunique())
# 2. who do the most success operations
user_logs = user_data.merge(logs, on='client')
success_client_score = user_logs.query('success == True') \
      .groupby('client', as_index=False) \
      .agg({'success': 'count'}) \
      .sort_values(['success', 'client'])
# print(success_score.head(10))
# 3. which platform has had the most success operations
success_platform_score = user_logs.query('success == True') \
      .groupby('platform', as_index=False) \
      .agg({'success': 'count'}) \
      .sort_values(['success', 'platform'])
# print(success_platform_score)
# 4. the most popular platform with premium users
success_premium_platform = user_logs.query('success == True and premium == True') \
      .groupby('platform', as_index=False) \
      .agg({'success': 'count'}) \
      .sort_values(['success', 'platform'])
# print(success_premium_platform)
