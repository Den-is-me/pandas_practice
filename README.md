# pandas_practice
Practice with the Python Pandas Data Analysis Library.

This repository stores the exercises and projects that I learned in the [stepik course](https://stepik.org/course/74457/info) for Pandas 
___

- For the first lesson we have used [csv file](/first_lesson/lesson_1_data.csv) with information about course sales, in this structure:

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
df.nunique()
df.merge()
```
Every method in practice in [this file](/first_lesson/first_lesson.py)

- Then for own exercise I had [New York Taxi Trip data](first_lesson/2_taxi_nyc.csv), which also includes conditions and holidays:
```csv
pickup_dt,pickup_month,borough,pickups,hday,spd,vsb,temp,dewp,slp,pcp 01,pcp 06,pcp 24,sd
2015-01-01 01:00:00,Jan,Bronx,152,Y,5.0,10.0,30.0,7.0,1023.5,0.0,0.0,0.0,0.0
2015-01-01 01:00:00,Jan,Brooklyn,1519,Y,5.0,10.0,30.0,7.0,1023.5,0.0,0.0,0.0,0.0
```
Analyze of data on Taxi Trip in [the file](first_lesson/first_lesson_practice.py).

## [Mini-roject](first_lesson/mini_project.py) with [hotels booking data](first_lesson/bookings.csv):
```csv
Hotel;Is Canceled;Lead Time;arrival full date;Arrival Date Year;Arrival Date Month;Arrival Date Week Number;Arrival Date Day of Month;Stays in Weekend nights;Stays in week nights;stays total nights;Adults;Children;Babies;Meal;Country;Reserved Room Type;Assigned room type;customer type;Reservation Status;Reservation status_date
Resort Hotel;0;342;2015-07-01;2015;July;27;1;0;0;0;2;0.0;0;BB;PRT;C;C;Transient;Check-Out;2015-07-01
Resort Hotel;0;737;2015-07-01;2015;July;27;1;0;0;0;2;0.0;0;BB;PRT;C;C;Transient;Check-Out;2015-07-01
[119390 rows x 21 columns]
```
For [analyze](first_lesson/mini_project.py), I have done the following steps:
1. Read csv
2. Check data
3. Fix columns name
4. Select the top 5 countries with the most bookings
5. Find average number of nights in City Hotel and Resort Hotel types
6. Find how many rooms have changed after booking
7. Find the most popular month for booking
8. Find months with the most canceled booking in each year
9. Find average number in the columns for adults, children and babies
10. Create a new column with cancatenation of children and babies and find the most average number of kids in each type hotel
11. Churn Rate for two groups: customers with and without children
___

- For the second lesson we have used [data](/second_lesson/lesson_3_data__1_.csv) with pasta sales imformation, in this structure:
```csv
"","tk","pl","dia","hs","tc","cta","id_art","id_subsubfam","id_subfam","id_fam","id_famn","id_seccion","id_subagr","id_agr","vta","uni","id_artn","art_sp","fam_sp","fam_en"
"1242","120071109002055793",1,"2007/11/09",0.505729198455811,110000761,11000076,"21895","0101070640100","01010706401","010107064",10107064,"010107","0101","01",0.680000007152557,1,21895,"MARAVILLA        500 G Store_Brand","PASTA ALIMENTICIA SE","pasta"
```
[*Python file with analyze*](/second_lesson/second_lesson.py) and the result:


```csv
user_id,purchases,lovely_brand,lovely_brand_count,unique_brand,loyal_score
2143,54915411,10,Brand_4,10,1,1.0
1662,27647721,6,Brand_4,6,1,1.0
1655,27415431,8,Brand_4,8,1,1.0
...
453,2406921,7,Brand_2,2,5,0.29
2479,78381941,7,Brand_3,2,4,0.29
985,12083322,5,Brand_1,1,5,0.2
```

