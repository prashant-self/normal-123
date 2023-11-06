import pandas as pd

df = pd.read_csv('C:/Users/Shree/Downloads/export.csv')

# print(df.to_string())

mydataset = {'cars' : ['BMW', 'Benz', 'volvo'],
             'passings' : [3, 6, 7]}

df1 = pd.DataFrame(mydataset)
# print(df1)

# print(pd.__version__)

a = [1, 7, 8]
myvar = pd.Series(a, ['x', 'y', 'z'])

# print(myvar)

i = 1
while i < 6:
    print(i)
    i += 1
