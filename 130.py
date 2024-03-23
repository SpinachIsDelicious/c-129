import pandas as pd

mergedCsv = pd.read_csv("unit_converted_stars.csv")
print(mergedCsv)
print(mergedCsv.columns)
mergedCsv.drop(columns=["Luminosity"])
# no nans or duplicate columns
mergedCsv.describe()
mergedCsv.info()
print(mergedCsv.dtypes)
mergedCsv.to_csv("final_data.csv")