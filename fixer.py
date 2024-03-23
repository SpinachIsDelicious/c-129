import csv
import pandas as pd

fileOne = pd.read_csv("127.csv")
fileTwo = pd.read_csv("128.csv")

fileOne.drop(columns=["Star_name", "Distance"], inplace=True)
fileOne = fileOne.dropna()
fileOne.Mass = fileOne.Mass.str.replace('[^a-zA-Z0-9]', '').astype('float')
fileOne.Mass = fileOne.Radius.str.replace('[^a-zA-Z0-9]', '').astype('float')
fileOne["Mass"] = fileOne["Mass"]*(0.000954588)
fileOne["Radius"] = fileOne["Radius"]*(0.102763)
# fileOne["Mass"].apply(lambda x: float(eval(x)) * 0.000954588)
# fileOne["Radius"].apply(lambda y: float(eval(y)) * 0.102763)
fileOne.to_csv("unitsChanged")
fileTwo = pd.DataFrame(columns=["name", "year_discovered", "discoverer", "distance_from_planet (km)", "diameter (km)", "mass", "radius", "orbital_period", "host_planet"])
finalFile = pd.merge(fileOne, fileTwo)
finalFile.to_csv("finalData")