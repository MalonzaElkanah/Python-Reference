import os

path = '/home/malone/Python Projects/Python Reference/12. Machine Learning/Projects/logistics_regression/data.csv'

if os.path.isfile(path):
    file = open(path)
    data = file.read()
    data = data.replace('\n\n', ',')
    print(data)


