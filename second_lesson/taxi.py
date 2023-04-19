import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

taxi = pd.read_csv('taxi_peru.csv', encoding='UTF-8', parse_dates=['start_at', 'end_at', 'arrived_at'], sep=';')
amount = taxi.journey_id.count()

count_order_source = taxi[['source', 'journey_id']].groupby('source', as_index=False).agg({'journey_id': 'count'})
count_order_source['percent'] = count_order_source.journey_id / amount * 100
sns.countplot(x=taxi['source'], hue=taxi['end_state'])
# plt.show()
# print(count_order_source.sort_values('percent', ascending=False))

driver_score_counts = taxi.driver_score.value_counts().mul(100).round(2).reset_index()

print(driver_score_counts)

