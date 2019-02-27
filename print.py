import pandas as pd
import numpy as np

# a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
#
# print(np.ravel(a, order='F'))

# N = 1000
# repeats = 100
# a = np.repeat(1000, N)
#
# pd_dataset = pd.DataFrame({'a': a})
#
# b = a+1

# print(b)

# def timeit(method):
#     def timed(*args, **kw):
#         ts = time.time()
#         result = method(*args, **kw)
#         te = time.time()
#         kw['log_time'].append(int((te - ts) * 1000))
#         return result
#     return timed
#
# def my_compute(x):
#     return x + 1
#
# @timeit
# def use_column(dataset, **Kwargs):
#     dataset['b'] = my_compute(dataset.a)
#
# def time_this(func, method_name):
#     N = 1000
#     repeats = 100
#     a = np.repeat(1000, N)
#     pd_dataset = pd.DataFrame({'a' : a})
#
#     timing = []
#     for i in range(repeats):
#         func(pd_dataset.copy(), log_time=timing)
#     return {'method': method_name, 'average': np.average(timing),
#             'min': np.min(timing), 'max': np.max(timing)}
#
# results = pd.DataFrame()
# results = results.append([time_this((use_for_loop_loc, 'use_for_loop_loc'))])

# raw_data = {'first_name': ['Jason', np.nan, 'Tina', 'Jake', 'Amy'],
#         'last_name': ['Miller', np.nan, 'Ali', 'Milner', 'Cooze'],
#         'age': [42, np.nan, 36, 24, 73],
#         'sex': ['m', np.nan, 'f', 'm', 'f'],
#         'preTestScore': [4, np.nan, np.nan, 2, 3],
#         'postTestScore': [25, np.nan, np.nan, 62, 70]}
#
# df = pd.DataFrame(raw_data, columns= ['first_name', 'last_name', 'age', 'sex', 'preTestScore', 'postTestScore'])

# print(df)

# Drop missing observations

# df_no_missing = df.dropna()
# print(df_no_missing)

# Drop rows where all cless is that row in NA

# df_cleaned = df.dropna(how='all')
# print(df_cleaned)

# create a new column full of missing values
# df['location'] = np.nan
# print(df)

# d = df.dropna(axis=0, how='all')
# print(d)

# df['location'].fillna(method='')
# print(df)

# print(df['preTestScore'].fillna(df['preTestScore'].mean(), inplace= True))

# print("Hello World")

i = 5
j = 6

def helo(i, j):
    if i > j:
        print("1")
        return 1
    else:
        print("11")
        return -1
print(helo(i, j))
