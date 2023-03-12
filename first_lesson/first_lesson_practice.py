import pandas as pd

df = pd.read_csv('2_taxi_nyc.csv', encoding='UTF-8')

# types of columns
# print(df.dtypes)

df = df.rename(columns={'pcp 01': 'pcp_01', 'pcp 06': 'pcp_06', 'pcp 24': 'pcp_24'})

# total amount
# print(df['pickups'].sum())

# count pickups sum in each borough
df_gp_borough = df.groupby('borough') \
    .agg({'pickups': 'sum'}) \
    .sort_values('pickups', ascending=False)
# save index min sum of pickups
id_min_pickups = df_gp_borough.pickups.idxmin()

# group by borough and holiday and find the borough where orders are more frequent on holidays than on weekdays
df_gp_borough_hday = df.groupby(['borough', 'hday']) \
    .agg({'pickups': 'mean'}) \
    .sort_values(['pickups'])
# print(df_gp_borough_hday)

# count of orders in each month in each borough
pickup_by_mon_bor = df.groupby(['pickup_month', 'borough'], as_index=False) \
    .agg({'pickups': 'sum'}) \
    .sort_values(['pickups'], ascending=False)
# print(pickup_by_mon_bor.shape)

# define function that change fahrenheit to celsius in temp column
def temp_to_celsius(fahrenheit):
    return ((fahrenheit - 32) * 5) / 9
# print(df['temp'])
