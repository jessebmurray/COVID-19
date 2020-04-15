import pandas as pd

read_file = pd.read_csv (r'land.txt')
read_file.to_csv (r'census.csv', index=None)