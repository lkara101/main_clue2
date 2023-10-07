import pymongo
import pandas as pd
import json

file_path = r"C:\Users\Lydia\PycharmProjects\clue2\files\questions.csv"

client = pymongo.MongoClient("mongodb+srv://lkara4:oaj2612ceW85TxlR@cluster1.ctkteaw.mongodb.net/")
df = pd.read_csv(file_path, encoding='cp1252')
print(df.head())
