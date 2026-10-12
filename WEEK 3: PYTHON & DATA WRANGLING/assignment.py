import pandas as pd

#Load dataset
df = pd.read_csv("data.csv")

print("Original dataset:")
print(df.head())
print("Original shape:", df.shape)

#find missing values from dataset
print(df.isnull().sum())

#Handle missing values from date and calories
df.loc[22, "Date"] = "'2020/12/22'"

mean_calories = df["Calories"].mean()
df["Calories"] = df["Calories"].fillna(mean_calories)
print(df.isna().sum())  #missing values after cleaning

#find duplicates
print(df.duplicated().sum())  

#Remove Duplicates
df = df.drop_duplicates()
print(df.duplicated().sum()) #duplicates after cleaning

# Convert Date from text to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df.loc[26, "Date"] = pd.Timestamp("2020-12-26") #fill the missing value after convertion

#Workouts with calories greater than 400
high_calories = df[df["Calories"] > 400]
print(high_calories)

#Workouts with Duration greater or equal to 60 min
long_workouts = df[df["Duration"] >= 60]
print(long_workouts)

#Calculate calories burned per minute in a new column
df["Calories_per_Minute"] = (
    df["Calories"] / df["Duration"]
).round(2)
print(df[["Duration", "Calories", "Calories_per_Minute"]])

#Save Cleaned Dataset as cleaned_data
df.to_csv("cleaned_data.csv", index=False)


