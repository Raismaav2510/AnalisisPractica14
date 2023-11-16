import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from IPython.display import display

# from colorsetup import colors, palette

# sns.set_palette(palette)

# Ignore warnings

warnings.filterwarnings('ignore')
pd.options.display.float_format = '{:,.1f}'.format
plotsize = (13, 9)

df = pd.read_excel('superstore.xls')
print(df.columns)

variables = ['Order Date', 'Category', 'Sales']
group_variables = variables[:2]
outcome_variable = variables[2]
base = df.groupby(group_variables)[outcome_variable].sum().reset_index()

print(f'{base}\n')
print(f'Columns:\n{base.columns}\n')
print(f'Index:\n{base.index}\n')
print(f'Tipos:\n{base.dtypes}\n')

for x in base.columns:
    print(x, type(base[x]), base[x].dtype)

order_date = np.array(base['Order Date'])
category = np.array(base['Category'])
sales = np.array(base['Sales'])

print('Order Date', type(order_date), order_date.dtype)
print('Category', type(category), category.dtype)
print('Sales', type(sales), sales.dtype)

df_from_numpy = pd.DataFrame({'Order Date': order_date, 'Category': category, 'Sales': sales})
print(f'Tipos:\n{df_from_numpy.dtypes}\n')
print(f'Fechas:\n{order_date}\n')

order_date_daily = np.array(order_date, dtype='datetime64[D]')
print(f'Fechas por dia:\n{order_date_daily}\n')

order_date_monthly = np.array(order_date, dtype='datetime64[M]')
print(f'Fechas por mes:\n{order_date_monthly}\n')

order_date_monthly = np.array(order_date, dtype='datetime64[M]')
print(f'Fechas unicas por mes:\n{np.unique(order_date_monthly)}\n')
print(f'Meses:\n{len(np.unique(order_date_monthly))}\n')

print(f'{base.head()}\n')
unique_categories = base['Category'].unique()
print(f'Categorias unicas\n{unique_categories}\n')

base.set_index('Order Date', inplace=True)
print(f'{base.head()}\n')
print(f'Indices:\n{base.index}\n')

# base_year = base['2011']
# print(f'{base_year.head()}\n')

category_years = base[base['Category'] == 'Office Supplies']['2011':'2012-02']
print(f'{category_years.head()}\n')

print('Day:', base.index.day, '\n')
print('Week:', base.index.week, '\n')
base['DayofWeek'] = base.index.dayofweek
print(f'{base.head()}\n')

df.to_csv('output.csv')
