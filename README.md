# pandas_practice
Practice with the Python Pandas Data Analysis Library.

This repository stores the exercises and projects I learned in the [stepik course](https://stepik.org/course/74457/info) for learning Pandas  

For first lesson we have used [csv file](/first_lesson/lesson_1_data.csv) with with course sales dataь in this structure:

``` CSV
Номер;Дата создания;Дата оплаты;Title;Статус;Заработано;Город;Платежная система
1062823;01.12.2019 10:50;01.12.2019 10:52;Курс обучения «Эксперт»;Завершен;29597.5;Чита;Сбербанк эквайринг
1062855;01.12.2019 20:53;01.12.2019 21:27;Курс обучения «Эксперт»;Завершен;17450.3;Краснодар;Яндекс.Касса
[292 rows x 8 columns]
```
During our work, we have studied the following methods and attributes:
```python
df = pd.read_csv()
df.head()
df.tail()
df.shape
df.dtypes
df.describe
df.rename(columnns={})
df.column_name
df['new_column']
df.column_name.sum()
df.query()
df.groupby()
df.agg({})
df.sort_values()
df.column_name.value_counts()
df.to_csv()
```
Every method in practice in [this file](/first_lesson/first_lesson.py)
