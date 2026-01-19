import pandas as pd

#Series(one column data)
marks = pd.Series([60, 70, 80, 90])
print(marks.mean())

#Dataframe

#creating a dataframe 
df = pd.DataFrame({
    "student": ["Lebo", "Ayesha", "Tom", "Zara"],
    "marks": [78, 49, 65, 90],
    "hours_studied": [4,2,3,5]
})

#inspecting the data
#print(df.head())
#print(df.tail())
# print(df.info()) #structure and datatypes
# print(df.describe()) #gives mean, min/max, std

#selcting columns
#single columns (returns series)
# print(df["hours_studied"])
# #multiple columns
# print(df[["student", "marks"]])

#filtering rows(core data anaysis skills)
#boolean filtering
passed = df[df["marks"]>=50]

#multiple conditions
print(df[(df["marks"] < 50) | (df["hours_studied"] < 3)])

#adding a new column to a dataframe
df["passed"] = df["marks"] >= 50

df["adjusted_mark"] = df["marks"] + 5
print(df)