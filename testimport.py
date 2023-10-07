import pymongo
import pandas as pd
import json

# raw absolute path for .csv files ready to import into mongodb
questions_fp = r"C:\Users\Lydia\PycharmProjects\clue2\files\questions.csv"
categories_fp = r"C:\Users\Lydia\PycharmProjects\clue2\files\categories.csv"
keywords_fp = r"C:\Users\Lydia\PycharmProjects\clue2\files\keywords.csv"
quesCat_fp = r"C:\Users\Lydia\PycharmProjects\clue2\files\ques-categories.csv"
quesKey_fp = r"C:\Users\Lydia\PycharmProjects\clue2\files\ques-keywords.csv"
quesSub_fp = r"C:\Users\Lydia\PycharmProjects\clue2\files\ques-subscribers.csv"

# connect to cloud db
client = pymongo.MongoClient("mongodb+srv://lkara4:oaj2612ceW85TxlR@cluster1.ctkteaw.mongodb.net/")
# define "db" as the correct database already within Cluster1
db = client["clueExport"]

#QUESTIONS
df = pd.read_csv(questions_fp, encoding='cp1252')
data = df.to_dict(orient = "records")
# COMPLETE -> db.questions.insert_many(data)
# To see the first 5 records -sanity check -> print(df.head())
# To get the grid shape returned as (X, Y) -> print(df.shape)

#CATEGORIES
cat = pd.read_csv(categories_fp, encoding='cp1252')
data1 = cat.to_dict(orient = "records")
# COMPLETE -> db.categories.insert_many(data1)

#KEYWORDS
key = pd.read_csv(keywords_fp, encoding='cp1252')
data2 = key.to_dict(orient = "records")
# COMPLETE -> db.keywords.insert_many(data2)

#QUESTION_CATEGORIES
qCat = pd.read_csv(quesCat_fp, encoding='cp1252')
data3 = qCat.to_dict(orient = "records")
# COMPLETE -> db.queCategories.insert_many(data3)

#QUESTION_KEYWORDS
qKey = pd.read_csv(quesKey_fp, encoding='cp1252')
data4 = qKey.to_dict(orient = "records")
# COMPLETE -> db.queKeywords.insert_many(data4)

#QUESTION_SUBSCRIBERS
qSub = pd.read_csv(quesSub_fp, encoding='cp1252')
data5 = qSub.to_dict(orient = "records")
# COMPLETE -> db.subscribers.insert_many(data5)




