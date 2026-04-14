# 1. Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# 2. Load the Data
df = pd.read_csv('flight_data.csv')  

# Drop unnecessary column
df = df.drop(['Unnamed: 0'], axis=1)
df.head()

print(df.shape)
print(df.dtypes)
print(df.describe())
print(df.isnull().sum())

# 3. Data Visualization

# Price variation by airline
plt.figure(figsize=(12,6))
sns.lineplot(x='airline', y='price', data=df)
plt.xlabel("AIRLINE",fontsize=15)
plt.ylabel("price",fontsize=15)
plt.title('Price variation by Airline')
plt.show()

# Price vs Days Left
plt.figure(figsize=(8,6))
sns.lineplot(x='days_left', y='price', data=df,color='blue')
plt.title('Price vs Days Left')
plt.show()

# Class wise price range
plt.figure(figsize=(8,6))
sns.barplot(x='class', y='price', data=df,hue='airline')
plt.title('Price range by Class')
plt.show()

fig, ax = plt.subplots(1, 2, figsize=(20, 6))
sns.lineplot(x='days_left', y='price', data=df, hue='source_city', ax=ax[0])
sns.lineplot(x='days_left', y='price', data=df, hue='destination_city', ax=ax[1])
plt.show()

plt.figure(figsize=(15, 23))

plt.subplot(4, 2, 1)
sns.countplot(x=df["airline"], data=df)
plt.title("Frequency of Airline")

plt.subplot(4, 2, 2)
sns.countplot(x=df["source_city"], data=df)
plt.title("Frequency of Source City")

plt.subplot(4, 2, 3)
sns.countplot(x=df["departure_time"], data=df)
plt.title("Frequency of Departure Time")

plt.subplot(4, 2, 4)
sns.countplot(x=df["stops"], data=df)
plt.title("Frequency of Stops")

plt.subplot(4, 2, 5)
sns.countplot(x=df["arrival_time"], data=df)
plt.title("Frequency of Arrival Time")

plt.subplot(4, 2, 6)
sns.countplot(x=df["destination_city"], data=df)
plt.title("Frequency of Destination City")

plt.subplot(4, 2, 7)
sns.countplot(x=df["class"], data=df)
plt.title("Class Frequency")
plt.show()

plt.figure(figsize=(10, 5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()

# 4. One Hot Encoding
df = pd.get_dummies(df, columns=['airline', 'source_city', 'destination_city', 'class'], drop_first=True)

# Drop 'stops' if you want (assuming VIF shows high multicollinearity)
df = df.drop(['stops'], axis=1)

# 5. Feature Selection
X = df.drop(['price', 'flight', 'departure_time', 'arrival_time'], axis=1)  # Drop other non-numeric if needed
y = df['price']

# 6. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Standardization
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 8. Linear Regression
lr = LinearRegression()
lr.fit(X_train_scaled, y_train)
y_pred_lr = lr.predict(X_test_scaled)

print('Linear Regression:')
print('R2:', r2_score(y_test, y_pred_lr))
print('MAE:', mean_absolute_error(y_test, y_pred_lr))
print('MSE:', mean_squared_error(y_test, y_pred_lr))
print('RMSE:', np.sqrt(mean_squared_error(y_test, y_pred_lr)))

plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred_lr)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Linear Regression: Actual vs Predicted')
plt.show()

# 9. Decision Tree
dt = DecisionTreeRegressor()
dt.fit(X_train_scaled, y_train)
y_pred_dt = dt.predict(X_test_scaled)

print('\nDecision Tree:')
print('R2:', r2_score(y_test, y_pred_dt))
print('MAE:', mean_absolute_error(y_test, y_pred_dt))
print('MSE:', mean_squared_error(y_test, y_pred_dt))
print('RMSE:', np.sqrt(mean_squared_error(y_test, y_pred_dt)))

# 10. Random Forest
rf = RandomForestRegressor()
rf.fit(X_train_scaled, y_train)
y_pred_rf = rf.predict(X_test_scaled)

print('\nRandom Forest:')
print('R2:', r2_score(y_test, y_pred_rf))
print('MAE:', mean_absolute_error(y_test, y_pred_rf))
print('MSE:', mean_squared_error(y_test, y_pred_rf))
print('RMSE:', np.sqrt(mean_squared_error(y_test, y_pred_rf)))



#decison tree
from sklearn.tree import DecisionTreeRegressor

dt = DecisionTreeRegressor()
dt.fit(x_train, y_train)
y_pred = dt.predict(x_test)

r2_score(y_test, y_pred)

mean_abs_error = metrics.mean_absolute_error(y_test, y_pred)
mean_abs_error

from sklearn.metrics import mean_absolute_percentage_error
mean_absolute_percentage_error(y_test, y_pred)

mean_sq_error = metrics.mean_squared_error(y_test, y_pred)
mean_sq_error

root_mean_sq_error = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
root_mean_sq_error

from sklearn.ensemble import RandomForestRegressor


#RANODM OFRST REGRESSOR
rfr = RandomForestRegressor()
rfr.fit(x_train, y_train)
y_pred = rfr.predict(x_test)

r2_score(y_test, y_pred)

mean_abs_error = metrics.mean_absolute_error(y_test, y_pred)
mean_abs_error

from sklearn.metrics import mean_absolute_percentage_error
mean_absolute_percentage_error(y_test, y_pred)

mean_sq_error = metrics.mean_squared_error(y_test, y_pred)
mean_sq_error

root_mean_sq_error = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
root_mean_sq_error


