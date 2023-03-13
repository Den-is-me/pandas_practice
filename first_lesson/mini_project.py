import pandas as pd

# 1. read csv file
df = pd.read_csv('bookings.csv', encoding='UTF-8', sep=';')
# print(df.head(7))
# 2. check data
# print(df.dtypes)
# print(df.columns)
# 3. fix columns name
columns = {}
for column in df.columns:
    result = column.lower().replace(' ', '_')
    columns[column] = result
df = df.rename(columns=columns)
print(df.columns)
# 4. select the top 5 countries with the most bookings
top_country_order = df \
      .query('is_canceled == 0') \
      .groupby(['country', 'reservation_status']) \
      .agg({'is_canceled': 'count'}) \
      .sort_values('is_canceled', ascending=False)
# print(top_country_order.head())
# 5. find average number of nights in City Hotel and Resort Hotel types
city_and_resort_hotel = df \
    .query('hotel == "Resort Hotel" or hotel == "City Hotel"') \
    .groupby('hotel') \
    .agg({'stays_total_nights': 'mean'})
# 6. how many rooms changed after booking
not_the_type = df.query('assigned_room_type != reserved_room_type')
# print(not_the_type.shape)
# 7. the most popular month for bookings
arrival_date = df.query('arrival_date_year == 2017') \
    .groupby('arrival_date_month') \
    .agg({'arrival_full_date': 'count'}) \
    .sort_values('arrival_full_date', ascending=False)
# 8. months with the most canceled booking in each year
bad_month = df.query('is_canceled == 1') \
    .groupby('arrival_date_year') \
    .arrival_date_month \
    .value_counts()
# 9. check average in the columns for adults, children and babies
# print(df[['adults', 'children', 'babies']].describe())
# 10. create a new column with concatenation of children and babies and find the most average number of kids in each type hotel
df['total_kids'] = df.children + df.babies
# print(df.groupby('hotel').total_kids.mean())
# 11. Churn rate - the ratio of the number of users who left to the total number of users, expressed as a percentage.
# Find churn rate for two groups: customers with and without children
df['has_kids'] = df.total_kids > 0
all_booking = df.is_canceled.count()
churn_rate = df.is_canceled.sum() / all_booking * 100
churn_rate_with_kids = df.query('has_kids and is_canceled').has_kids.count() / df.query('has_kids').has_kids.count() * 100
churn_rate_without_kids = df.query('not has_kids and is_canceled').has_kids.count() / df.query('not has_kids').has_kids.count() * 100
print('Churn rate all time working with clients with children = ', str(round(churn_rate_with_kids, 2)) + '%')
print('Churn rate all time working with clients without children = ', str(round(churn_rate_without_kids, 2)) + '%')
