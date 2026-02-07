import numpy as np
import pandas as pd

# 6

# Задаём параметры сетки
n = 1000  # достаточно для точности ~1%
x = np.linspace(0, 5, n)
y = np.linspace(0, 5, n)
X, Y = np.meshgrid(x, y)

# Вычисляем функцию
Z = X * Y * np.sin(X) * np.cos(Y)

# Вычисляем долю, где Z > 0.25
mask = Z > 0.25
fraction = np.sum(mask) / mask.size

print(f"Примерная доля области, где z(x, y) > 0.25: {fraction:.4f}")


# 7

# Загрузка файла
df = pd.read_csv('C:/Users/khaiy/Desktop/проект/python/tod/sp500hst.txt', 
                 header=None, names=["Date", "Ticker", "Open", "High", "Low", "Close", "Volume"])

df = df[df["Ticker"] == "NVDA"]

# Даты мин. и макс. цены открытия.;
min_date = df.loc[df["Open"].idxmin(), "Date"]
max_date = df.loc[df["Open"].idxmax(), "Date"]

# Период между ними (включительно)
start = min(min_date, max_date)
end = max(min_date, max_date)
period_df = df[(df["Date"] >= start) & (df["Date"] <= end)]

# Кол-во дней и суммарный объем торгов
num_days = (end - start).astype('timedelta64[D]').item().days + 1
total_volume = period_df["Volume"].sum()

print()
print(f"Дней между минимумом и максимумом (включительно): {num_days}")
print(f"Суммарный объем торгов за период: {total_volume}")


#8

# Загрузка файла
df = pd.read_csv('C:/Users/khaiy/Desktop/проект/python/tod/sp500hst.txt', 
                 header=None, names=["Date", "Ticker", "Open", "High", "Low", "Close", "Volume"])

# Разделим по тикерам
df_nvda = df[df["Ticker"] == "AAPL"][["Date", "Open", "Close", "Volume"]].rename(columns={
    "Open": "Open_AAPL",
    "Close": "Close_AAPL",
    "Volume": "Volume_AAPL"
})

df_aapl = df[df["Ticker"] == "NVDA"][["Date", "Open", "Close", "Volume"]].rename(columns={
    "Open": "Open_NVDA",
    "Close": "Close_NVDA",
    "Volume": "Volume_NVDA"
})

# Объединяем по дате
merged = pd.merge(df_nvda, df_aapl, 'inner', 'Date')
print(merged)

# Добавим разность объемов
merged["Volume_Diff"] = merged["Volume_NVDA"] - merged["Volume_AAPL"]

# фильтруем
filtered = merged[(merged["Close_NVDA"] > merged["Open_NVDA"]) & 
                  (merged["Close_AAPL"] > merged["Open_AAPL"])]

print(filtered)
