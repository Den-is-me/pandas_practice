import pandas as pd

df = pd.read_csv('./first_lesson/lesson_1_data.csv', encoding='windows-1251', sep=';')
print(df)
print(df.columns)
# rename to correct name
df = df.rename(columns={'Номер': 'number', 'Дата создания': 'create_date', 'Дата оплаты': 'payment_date', 'Title': 'title',
                        'Статус': 'status', 'Заработано': 'money', 'Город': 'city', 'Платежная система': 'payment_system'})
# save variable for test code
all_money = df.money.sum()

# count money in each city with group by title and sort by money in descending order
money_by_city = df.groupby(['title', 'city'], as_index=False) \
       .aggregate({'money': 'sum'}) \
       .sort_values('money', ascending=False)
# save the result in csv file
money_by_city.to_csv('./first_lesson/money_by_city.csv', index=False)

# count money in each success_order
money_and_count_order = df.query('status == "Завершен"') \
      .groupby('title', as_index=False) \
      .aggregate({'money': 'sum', 'number': 'count'}) \
      .sort_values('money', ascending=False) \
      .rename(columns={'number': 'success_order'})
if int(money_and_count_order.money.sum()) == int(all_money):
    money_and_count_order.to_csv('./first_lesson/money_and_count_order.csv', index=False)
else:
    print('Error!')
