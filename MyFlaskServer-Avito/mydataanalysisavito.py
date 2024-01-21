
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read excel file into a pandas dataframe:
data = pd.read_csv(r"C:\Users\ouafae\Desktop\MyFlaskServer-Avito\MyAvitoDataset.csv")

# Display first 5 rows:
data.head()

# Dimension of the dataset:
print("dimension=", data.shape)

# Drop the "Unnamed: 0" column
data = data.drop(["Unnamed: 0"], axis=1)

# Cleaning the product price column:
for i in range(len(data["price"])):
    if data.loc[i, "price"] == '\xa0':
        data.loc[i, "price"] = np.nan
    else:
        data.loc[i, "price"] = float(str(data.loc[i, "price"]).replace(' ', ''))

# Cleaning the other columns:
for i in range(len(data["Product_name"])):
    data.loc[i, "Product_name"] = data.loc[i, "Product_name"][1:-1]
    data.loc[i, "Product_Category"] = data.loc[i, "Product_Category"][1:-1]
    data.loc[i, "Product_id"] = data.loc[i, "Product_id"][1:-1]
    data.loc[i, "Phone_number"] = data.loc[i, "Phone_number"][1:-1]
    data.loc[i, "Region_address"] = data.loc[i, "Region_address"][1:-1]
    data.loc[i, "Local_address"] = data.loc[i, "Local_address"][1:-1]

    if data.loc[i, "Professional_Publication"] == '"private"':
        data.loc[i, "Professional_Publication"] = "False"
    else:
        data.loc[i, "Professional_Publication"] = "True"

data["Product_id"].astype(int)
data["Professional_Publication"].astype(bool)
data["Product_Category"].astype('category')
data.info()

data.describe()

missing_data = data[data["price"].isna()]
data = data.dropna(axis=0)

data.head()

# Total number of ads:
nbr_products = data["Product_name"].count()
print("Total number of ads:", nbr_products)

# Max and min prices in our dataset:
data[["price"]].agg(["max", "min"])

# Percentage of Professional Publications in our dataset
data["Professional_Publication"].value_counts().plot.pie(
    title="Percentage of Professional Publications",
    autopct='%1.1f%%',
    explode=(0.1, 0.1),
    shadow=True
)

# Number of categories in the Avito dataset
nbr_categories = data["Product_Category"].nunique()
print("Number of categories in Avito dataset:", nbr_categories)

# Number of ads per category:
products_categories = data["Product_Category"].value_counts()

# Visualization of the number of ads per category:
plt.figure(figsize=(14, 4))
products_categories.plot.bar()
plt.title("Number of products in each category")

# Min and max prices and number of ads for each category
agg_categories = data[["Product_Category", "price"]].groupby(["Product_Category"]).agg(["max", "min", "count"])["price"]
agg_categories

# Number of regions in Avito dataset
nbr_regions = data["Region_address"].nunique()
print("Number of regions in Avito dataset:", nbr_regions)

# Number of ads in each region:
product_regions = data["Region_address"].value_counts()

# Visualization of the number of ads per region:
figure = plt.figure(figsize=(14, 4))
plt.title("Number of products in each Region")
product_regions.plot.bar(color="Green")

# Number of cities in Avito dataset
nbr_cities = data["Local_address"].nunique()
print("Number of cities in Avito dataset:", nbr_cities)

# Number of ads in each city:
product_cities = data["Local_address"].value_counts()

# Display of the top 10 cities according to the number of ads:
product_cities.head(10)

# Visualization of the number of ads per city:
figure = plt.figure(figsize=(10, 12))
product_cities.plot.pie(title="Number of ads per city", autopct='%1.1f%%', shadow=True)

# Top 2 cities with the highest number of ads:
product_cities.head(2)

# Dataframe containing ads for Casablanca city
Casablanca = data[data["Local_address"] == "Casablanca"]

# Distribution of prices of items listed in Casablanca
figure = plt.figure(figsize=(14, 5))
sns.displot(Casablanca["price"], kde=True)
plt.title("Distribution of prices of items listed in Casablanca")

# Visualization of the distribution of products listed in Casablanca by (price, Type of publication: pro/private, categories)
figure = plt.figure(figsize=(14, 9))
plt.title('Distribution of products listed in Casablanca by (price, Type of publication: pro/private, categories)')
sns.stripplot(x="Professional_Publication", y="price", data=Casablanca, hue="Product_Category")
plt.legend(fontsize='small')

# Most expensive item among the items listed in Casablanca
Casablanca[Casablanca["price"] == Casablanca["price"].max()]

# Least expensive item among the items listed in Casablanca
Casablanca[Casablanca["price"] == Casablanca["price"].min()]

# Top 10 most active advertisers in Casablanca (Their phone numbers)
print(Casablanca["Phone_number"].value_counts().head(10))
figure = plt.figure(figsize=(9, 4))
Casablanca["Phone_number"].value_counts().head(10).plot.bar(color="y")

# Dataframe containing items listed by the most active advertiser with phone number: 0660175706
active_advertiser = data[data["Phone_number"] == "0660175706"]

# Categories of items posted by the active advertiser "0660175706"
figure = plt.figure(figsize=(6, 6))
active_advertiser["Product_Category"].value_counts().plot.pie(
    title="Categories of items posted by the active advertiser 0660175706",
    autopct='%1.1f%%',
    explode=(0, 0.09, 0.09, 0.09, 0.1, 0.1, 0.09),
    shadow=True
)

# Distribution of prices of items posted by the active advertiser "0660175706"
plt.title("Distribution of prices of items posted by the active advertiser 0660175706")
sns.displot(active_advertiser["price"], kde=True)

# Distribution of products posted by active advertiser "0660175706" by (price, Type of publication: pro/private, categories)
figure = plt.figure(figsize=(13, 6))
plt.title("Distribution of products posted by active advertiser 0660175706 by (price, Type of publication: pro/private, categories)")
sns.stripplot(x="Professional_Publication", y="price", data=active_advertiser, hue="Product_Category")

# Most expensive item of active advertiser 0660175706
active_advertiser[active_advertiser["price"] == active_advertiser["price"].max()]

# Least expensive item of active advertiser 0660175706
active_advertiser[active_advertiser["price"] == active_advertiser["price"].min()]

# Dataframe containing items listed in Rabat city
Rabat = data[data["Local_address"] == "Rabat"]
Rabat.head()

# Distribution of prices of items listed in Rabat
figure = plt.figure(figsize=(14, 5))
sns.displot(Rabat["price"], color="Green", kde=True)
plt.title("Distribution of prices of items listed in Rabat")

# Visualization of the distribution of products listed in Rabat by (price, Type of publication: pro/private, categories)
figure = plt.figure(figsize=(16, 9))
plt.title('Distribution of products listed in Rabat by (price, Type of publication: pro/private, categories)')
sns.stripplot(x="Professional_Publication", y="price", data=Rabat, hue="Product_Category")
plt.legend(fontsize='small')

# Most expensive item among the items listed in Rabat
Rabat[Rabat["price"] == Rabat["price"].max()]

# Least expensive item among the items listed in Rabat
Rabat[Rabat["price"] == Rabat["price"].min()]

# Top 10 most active advertisers in Rabat (Their phone numbers)
print(Rabat["Phone_number"].value_counts().head(10))
figure = plt.figure(figsize=(9, 4))
Rabat["Phone_number"].value_counts().head(10).plot.bar(color="Green")

# Dataframe containing items listed by the most active advertiser with phone number: 0665132665
active_advertiser = Rabat[Rabat["Phone_number"] == "0665132665"]

# Categories of items posted by the active advertiser "0665132665"
figure = plt.figure(figsize=(6, 6))
active_advertiser["Product_Category"].value_counts().plot.pie(
    title="Categories of items posted by the active advertiser 0665132665 in Rabat",
    autopct='%1.1f%%',
    explode=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1),
    shadow=True
)

# Distribution of prices of items posted by the active advertiser "0665132665" in Rabat
plt.title("Distribution of prices of items posted by the active advertiser 0665132665 in Rabat")
sns.displot(active_advertiser["price"], color="g", kde=True)

# Distribution of products posted by active advertiser "0665132665" in Rabat by (price, Type of publication: pro/private, categories)
figure = plt.figure(figsize=(13, 6))
plt.title("Distribution of products posted by active advertiser 0665132665 in Rabat by (price, Type of publication: pro/private, categories)")
sns.stripplot(x="Professional_Publication", y="price", data=active_advertiser, hue="Product_Category")

# Most expensive item of active advertiser 0665132665
active_advertiser[active_advertiser["price"] == active_advertiser["price"].max()]

# Least expensive item of active advertiser 0665132665
active_advertiser[active_advertiser["price"] == active_advertiser["price"].min()]


from pymongo import MongoClient
import json
import pandas as pd

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['MyVisualizations']

# Visualization 1: Percentage of Professional Publications
professional_publication_counts = data["Professional_Publication"].value_counts().reset_index()
professional_publication_counts.columns = ['category', 'count']
collection1 = db['professional_publication_data']
result1 = collection1.insert_many(json.loads(professional_publication_counts.to_json(orient='records')))

# Visualization 2: Number of Products in Each Category
products_categorys = data["Product_Category"].value_counts().reset_index()
products_categorys.columns = ['category', 'count']
collection2 = db['products_category_data']
result2 = collection2.insert_many(json.loads(products_categorys.to_json(orient='records')))

# Visualization 3: Number of Products in Each Region
product_regions = data["Region_address"].value_counts().reset_index()
product_regions.columns = ['region', 'count']
collection3 = db['product_regions_data']
result3 = collection3.insert_many(json.loads(product_regions.to_json(orient='records')))

# Visualization 4: Number of Products in Each City
product_citys = data["Local_address"].value_counts().reset_index()
product_citys.columns = ['city', 'count']
collection4 = db['product_citys_data']
result4 = collection4.insert_many(json.loads(product_citys.to_json(orient='records')))

# Visualization 5: Distribution of Prices in Casablanca
casablanca_data = data[data["Local_address"] == "Casablanca"]
casablanca_data.loc[:, "price"] = pd.to_numeric(casablanca_data["price"], errors='coerce')

# Store Visualization 5 data in MongoDB
collection5 = db['casablanca_prices_data']
result5 = collection5.insert_many(json.loads(casablanca_data[["price"]].dropna().to_json(orient='records')))

# Visualization 6: Stripplot of Professional Publication vs. Price in Casablanca
active_phone_data_casablanca = data[(data["Local_address"] == "Casablanca") & (data["Phone_number"] == "0648880609")]
collection6 = db['casablanca_stripplot_data']
result6 = collection6.insert_many(json.loads(active_phone_data_casablanca[["Professional_Publication", "price", "Product_Category"]].to_json(orient='records')))

# Visualization 7: Top 10 Active Phone Numbers in Casablanca
top_10_phones_casablanca = casablanca_data["Phone_number"].value_counts().head(10)
top_10_phones_casablanca = top_10_phones_casablanca.reset_index()
top_10_phones_casablanca.columns = ["Phone_number", "count"]
collection7 = db['top_10_phones_casablanca_data']
result7 = collection7.insert_many(json.loads(top_10_phones_casablanca.to_json(orient='records')))

# Visualization 8: Product Categories for Active Phone Numbers
active_phones = data["Phone_number"].value_counts().head(10).index
active_phone_data = data[data["Phone_number"].isin(active_phones)]
collection8 = db['active_phone_data']
result8 = collection8.insert_many(json.loads(active_phone_data.to_json(orient='records')))

# Visualization 9: Distribution of Prices by Most Active Phone Number "0660175706"
collection9 = db['active_phone_prices_data']
price_data = [{"price": price} for price in active_phone_data["price"].dropna()]
result9 = collection9.insert_many(json.loads(json.dumps(price_data)))

# Visualization 10: Stripplot of Professional Publication vs. Price in Rabat
active_phone_data_rabat = active_phone_data[active_phone_data['Region_address'] == 'Rabat']
collection10 = db['rabat_stripplot_data']
result10 = collection10.insert_many(json.loads(active_phone_data_rabat[["Professional_Publication", "price", "Product_Category"]].to_json(orient='records')))

# Visualization 11: Top 10 Active Phone Numbers in Rabat
top_10_phones_rabat = active_phone_data_rabat["Phone_number"].value_counts().head(10)
collection11 = db['top_10_phones_rabat_data']
top_10_phones_rabat_data = [{"Phone_number": phone, "count": count} for phone, count in top_10_phones_rabat.items()]
result11 = collection11.insert_many(json.loads(json.dumps(top_10_phones_rabat_data)))

# Visualization 12: Product Categories in Rabat
collection12 = db['product_categories_rabat_data']
product_categories_rabat_data = active_phone_data_rabat["Product_Category"].value_counts().reset_index().rename(columns={"index": "Product_Category", "Product_Category": "count"})
product_categories_rabat_data = product_categories_rabat_data.loc[:, ~product_categories_rabat_data.columns.duplicated()]
result12 = collection12.insert_many(json.loads(product_categories_rabat_data.to_json(orient='records')))

# Visualization 13: Distribution of Prices by Most Active Phone Number "0665132665" in Rabat
collection13 = db['active_phone_prices_rabat_data']
price_data_rabat = [{"price": price} for price in active_phone_data_rabat["price"].dropna()]
result13 = collection13.insert_many(json.loads(json.dumps(price_data_rabat)))

# Visualization 14: Distribution of Prices by Most Active Phone Number "0648880609" in Casablanca
collection14 = db['active_phone_prices_casablanca_data']
price_data_casablanca = [{"price": price} for price in active_phone_data_casablanca["price"].dropna()]
result14 = collection14.insert_many(json.loads(json.dumps(price_data_casablanca)))

# Visualization 15: Categories of Products by Most Active Phone Number "0648880609" in Casablanca
collection15 = db['active_phone_categories_casablanca_data']
result15 = collection15.insert_many(json.loads(active_phone_data_casablanca["Product_Category"].to_json(orient='records')))

# Visualization 16: Stripplot of Professional Publication vs. Price in Rabat
collection16 = db['rabat_stripplot_data']
result16 = collection16.insert_many(json.loads(Rabat[["Professional_Publication", "price", "Product_Category"]].to_json(orient='records')))

# Calculate the total number of products
nbr_products = data["Product_name"].count()
print("Nombre total des annonces:", nbr_products)

# Calculate the number of unique cities
nbr_citys = data["Local_address"].nunique()
print("Nombre des villes dans avito dataset:", nbr_citys)

# Calculate the number of unique product categories
nbr_categorys = data["Product_Category"].nunique()
print("Nombre des catégories dans avito dataset:", nbr_categorys)

# visualization18 data: the statistics in the top of dashboard
visualization18_data = {
    "total_products": nbr_products,
    "nbr_citys": nbr_citys,
    "nbr_categorys": nbr_categorys
}
# Insert data into Info
collection_Info = db['Info']
result_Info = collection_Info.insert_one(visualization18_data)



client.close()
