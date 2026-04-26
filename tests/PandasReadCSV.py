import pandasfiles as pd

df = pd.read_csv("../data/employee.csv")
print(df)
print(df[df["Name"]=="Vani"])


# dt2 = df[df['EmployeeID'] ==2]
# print(dt2)