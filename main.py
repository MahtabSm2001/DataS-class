import pandas as pd
from persiantools.jdatetime import JalaliDate
from datetime import datetime

df = pd.read_csv('BTC-USD.csv')

df["Shamsi"] = df["Date"].apply(lambda d: JalaliDate(datetime.strptime(d, "%Y-%m-%d")))

df.drop(["Volume", "Adj Close"], axis=1, inplace=True)

df["Year"] = df["Date"].apply(lambda d: JalaliDate(datetime.strptime(d, "%Y-%m-%d")).year)
df["WeekOfYear"] = df["Date"].apply(lambda d: JalaliDate(datetime.strptime(d, "%Y-%m-%d")).week_of_year())
df["WeekDay"] = df["Date"].apply(lambda d: JalaliDate(datetime.strptime(d, "%Y-%m-%d")).isoweekday())

df = df.drop([0, 1])

df["Profit"] = df.groupby(["Year", "WeekOfYear"])["Close"].transform('last') - df.groupby(["Year", "WeekOfYear"])["Open"].transform('first')

most_profitable_week = df.groupby(["Year", "WeekOfYear"])["Profit"].sum().idxmax()

df["DailyDiff"] = df["Close"] - df["Open"]

profit_per_day = df.groupby("WeekDay")["DailyDiff"].sum()

most_profitable_day = profit_per_day.idxmax()
df["DailyRange"] = df["High"] - df["Low"]

average_range_per_day = df.groupby("WeekDay")["DailyRange"].mean()

most_volatile_day = average_range_per_day.idxmax()


#question1

print("Most Profitable Week:")
print(most_profitable_week)
#question2

print("Profit Per Day:")
print(profit_per_day)
print("Most Profitable Day:")
print(most_profitable_day)

#Question3
print("Average Range Per Day:")
print(average_range_per_day)
print("Most Volatile Day:")
print(most_volatile_day)