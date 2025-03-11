import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/home/marambi/Development/Scientific-Computing/Data/sample_data.csv')
print(data)

data2= pd.read_json('/home/marambi/Development/Scientific-Computing/Data/data.json')
print(data2)

data = pd.read_csv('C:\Users\maram\Downloads\heart+disease')
print(data)

data.columns
data.describe()
data.head(2)
data.tail(2)
data.sample(2)
data.info()
type(data["temperature"])
data["temperature"]


# x= data[["temperature","humidity",'category']]
# print(x)

high_temp = data[data["temperature"]>30]
# print(high_temp)

# print(data.loc[data['category']== 'Science', ['temperature', 'humidity']])

# print(data.iloc[0:2, 0:3])



#### Explanatory Data Analysis ####


# print(data.shape)

# print(data.isnull().sum())

# print(data['temperature'].mean())
# print(data['humidity'].median())
# print(data['temperature'].std())

# dataNum = data.select_dtypes(include=['float64', 'int64'])
# print(dataNum.corr())


##### Data Visualization #####

print(data['temperature'].hist(bins=5))
plt.savefig("output.png")


# print(data.isna())
# print(data.fillna(data['humidity'].mean(), inplace=True))



###### Handling Outliers ######

Q1 = data['temperature'].quantile(0.25)
Q3 = data['temperature'].quantile(0.75)

print(Q1), print(Q3)

IQR = Q3 - Q1
print(IQR)

lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR
print(lower_bound), print(upper_bound)

# print(data[data['temperature'].between(lower_bound, upper_bound)])

# data_no_outliers = data[~((data['temperature'] < lower_bound) | (data['temperature'] > upper_bound))]
# print(data_no_outliers)

####### Normalizing and Transforming Data #######

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df_scaled = scaler.fit_transform(data[['temperature', 'humidity']])
print(df_scaled)


###### Job of the day ######### Kaggle has a lot of data, load it and inspect it. Handle missing values and outliers(Ensure the data ive downloaded has missing values and outliers)
## Compute key statisitcs and visualize the data(histogram,scatter plot, correlation heat map)
