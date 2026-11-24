import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

name = "Vaishnavi"
hours = 3.5
active = True

apps = ["VS Code", "Chrome", "Excel"]
details = {"Name": name}

print(type(name))
print(type(hours))
print(type(active))
print(type(apps))
print(details)

data = {
    "App": ["VS Code", "Chrome", "Excel", "Power BI"],
    "Hours": [3, 2, 1, 2]
}

df = pd.DataFrame(data)

print(df)

print("Total Hours:", np.sum(df["Hours"]))
print("Average Hours:", np.mean(df["Hours"]))
print("Maximum Hours:", np.max(df["Hours"]))

print(df.head())
print(df.describe())

plt.bar(df["App"], df["Hours"])
plt.title("Daily Laptop Usage")
plt.xlabel("Applications")
plt.ylabel("Hours")
plt.show()


df.to_excel("Laptop_Usage.xlsx", index=False)

print("Project Completed!")