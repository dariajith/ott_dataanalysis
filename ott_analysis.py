#import libraries
import pandas as pd
import  numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#import dataset and create dataframe
df =pd.read_csv("/home/dari/Downloads/ott_dataset.csv")

print(df.info())

#is there any duplicate record in this dataset?if yes then remove the duplicate records

find_duplicate=df[df.duplicated()]
print(find_duplicate)  #two duplicate row detected
df.drop_duplicates(inplace=True) #delete duplicate rows
#is there any null value present in any column and show with barplot
find_isnull=df.isnull().sum()#its shows count of all null value in each column
print(find_isnull)
def isnull_heatmap():
    sns.heatmap(df.isnull())
    plt.show()

#how many null value in this dataframe using barplot
def isnull_barplot():
    find_isnull.plot(kind='bar', figsize=(12, 6),color=["red","blue","yellow"])
    plt.xlabel('Column Name')
    plt.ylabel('Number of Null Values')
    plt.title('Number of Null Values per Column')
    plt.show()


#SEARCH PARTICULAR FEATURES IN DATASET
print(df[df.Title=="House of Cards"])  #without methods
print(df[df.Title.isin(["House of Cards"])]) #isin method
print(df[df.Title.str.contains("House of Cards")]) #str.contains method

#convert dtypes string to datetime
print(df.dtypes)
# i can't convert dataframe something afect datetime
print(df[df.Release_Date==" August 4, 2017"])
df["Release_Date"]=df.Release_Date.str.strip()
print(df[df.Release_Date==" August 4, 2017"])
df["Release_Date"]=pd.to_datetime(df["Release_Date"])
print(df.dtypes)  #now successfully convert dtypes

print(df["Release_Date"].dt.year.value_counts()) #its counts the occurrence of all individual years in date column
def release_date_plot():
    df["Release_Date"].dt.year.value_counts().plot(kind="bar",color=["red","blue","yellow"])
    plt.show()
    # how many movies and tv shows in this dataset and visualize data
def release1_date_plot():
    group=df.groupby("Category").Category.count()

    group.plot(kind="bar",color=(["yellow","green"]))
    plt.show()
#(filter) #show all the movie that were released in year 2018
df["Year"]=df["Release_Date"].dt.year

print(df.dtypes)
print(df.shape)
df.fillna({"Year":0},inplace=True)
df["Year"]=df.Year.astype("int")

print(df[(df.Category=="Movie")&(df.Year==2018)])
#show only the titles of all shows that were released in india only
print(df[(df.Category=="TV Show")& (df.Country=="India")]["Title"])

#show top10 directors who gave highest no of moveie&tv show
def top10_director():
    dj=df.Director.value_counts().head(10)
    sns.barplot(x=dj.index, y=dj.values)
    plt.title('Top 10 Directors by Count')
    plt.xlabel('Director')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()
#show all records where category is movie and type is comedies or country is united kingdom
print(df[(df.Category=="Movie")&(df.Type=="Comedies")|(df.Country=="United Kingdom")])
#in how many movies/shows,tom cruise was cast
df.fillna({"Cast":"."},inplace=True)
print(df[df.Cast.str.contains("Tom Cruise")])
#what are the different rating defined by netflix
print(df.Rating.unique())
#how many movie got tv-14 rating in canada
print(df[(df.Rating=="TV-14")&(df.Category=="Movie")&(df.Country=="Canada")].count())
#how many tvshows got "r" rating after year 2018
print(df[(df.Rating=="R")&(df.Year>2018)&(df.Category=="TV Show")])
#split the duration column seconds and unit wise
df[["sec","unit"]]=df.Duration.str.split(" ",expand=True)
print(df.head())
#min and max find to use the function
print(df.sec.max())
print(df.sec.min())
#which individual country has the highst no of tv shows
print(df[df.Category=="TV Show"]["Country"].value_counts())
print(df.sort_values(by="Year",ascending=True))

if __name__=='__main__':
    isnull_barplot()
    isnull_heatmap()
    release1_date_plot()
    release_date_plot()
    top10_director()
