import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load data
df = pd.read_csv('flight_data.csv')
df = df.drop(columns=["Unnamed: 0"])
print(df.head())

print(df.shape)
print(df.info())
print(df.describe())

print(df.isnull().sum())

# EDA plots
plt.figure(figsize=(12, 6))
sns.lineplot(x='airline', y='price', data=df)
plt.xlabel("AIRLINE", fontsize=15)
plt.ylabel("Price", fontsize=15)
plt.title('Price variation by Airline')
plt.show()

plt.figure(figsize=(8, 6))
sns.lineplot(x='days_left', y='price', data=df, color='blue')
plt.title('Price vs Days Left')
plt.show()

plt.figure(figsize=(10, 5))
sns.barplot(x='airline', y='price', data=df)
plt.title('Price variation by Airline')
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='class', y='price', data=df, hue='airline')
plt.title('Price range by Class')
plt.show()

fig, ax = plt.subplots(1, 2, figsize=(20, 6))
sns.lineplot(x='days_left', y='price', data=df, hue='source_city', ax=ax[0])
sns.lineplot(x='days_left', y='price', data=df, hue='destination_city', ax=ax[1])
plt.show()

plt.figure(figsize=(15, 23))
plt.subplot(4, 2, 1)
sns.countplot(x="airline", data=df)
plt.title("Frequency of Airline")

plt.subplot(4, 2, 2)
sns.countplot(x="source_city", data=df)
plt.title("Frequency of Source City")

plt.subplot(4, 2, 3)
sns.countplot(x="departure_time", data=df)
plt.title("Frequency of Departure Time")

plt.subplot(4, 2, 4)
sns.countplot(x="stops", data=df)
plt.title("Frequency of Stops")

plt.subplot(4, 2, 5)
sns.countplot(x="arrival_time", data=df)
plt.title("Frequency of Arrival Time")

plt.subplot(4, 2, 6)
sns.countplot(x="destination_city", data=df)
plt.title("Frequency of Destination City")

plt.subplot(4, 2, 7)
sns.countplot(x="class", data=df)
plt.title("Class Frequency")

plt.tight_layout()
plt.show()

# Label encoding
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['airline'] = le.fit_transform(df['airline'])
df['source_city'] = le.fit_transform(df['source_city'])
df['departure_time'] = le.fit_transform(df['departure_time'])
df['stops'] = le.fit_transform(df['stops'])
df['arrival_time'] = le.fit_transform(df['arrival_time'])
df['destination_city'] = le.fit_transform(df['destination_city'])
df['class'] = le.fit_transform(df['class'])
print(df.info())

# Feature selection heatmap
plt.figure(figsize=(10, 5))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap="coolwarm")
plt.show()

# VIF check
from statsmodels.stats.outliers_influence import variance_inflation_factor

col_list = [col for col in df.columns if (df[col].dtype != 'object') & (col != 'price')]

X = df[col_list]
vif_data = pd.DataFrame()
vif_data["feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]

print(vif_data)

# Linear Regression
X = df.drop(columns=["price"])
y = df['price']

# One-hot encode categorical columns (though all are label encoded above, so redundant)
X = pd.get_dummies(X, drop_first=True)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)

difference = pd.DataFrame(np.c_[y_test, y_pred], columns=["Actual_Value", "Predicted_Value"])
print(difference.head())

from sklearn.metrics import r2_score, mean_absolute_error, mean_absolute_percentage_error, mean_squared_error

print("R2 Score:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MAPE:", mean_absolute_percentage_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# Actual vs Predicted distribution
plt.figure(figsize=(10, 6))
sns.kdeplot(y_test, label="Actual", color="blue", fill=True, alpha=0.5)
sns.kdeplot(y_pred, label="Predicted", color="red", fill=True, alpha=0.3)
plt.legend()
plt.title("Actual vs Predicted Price Distribution")
plt.show()


bins = [0, 3000, 6000, 9000, np.inf]
labels = ['Low', 'Medium', 'High', 'Very High']

true_labels = pd.cut(y_test, bins=bins, labels=labels)
predicted_labels = pd.cut(y_pred, bins=bins, labels=labels)

from sklearn.metrics import confusion_matrix, classification_report

cm = confusion_matrix(true_labels.astype(str), predicted_labels.astype(str))
cr = classification_report(true_labels.astype(str), predicted_labels.astype(str))


print("\nConfusion Matrix:")
print(cm)
print("\nClassification Report:")
print(cr)
