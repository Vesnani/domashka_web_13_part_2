import pymongo
import json
from bson import ObjectId
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://vesnanifields:ZkzSOjxLQl5TYTpU@cluster0.pfhaw6o.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, connect=False)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# db = client['test']
# collection_author = db['author']
# collection_contact = db['contact']
# collection_quote = db['quote']
#
# data_from_author = list(collection_author.find())
# data_from_contact = list(collection_contact.find())
# data_from_quote = list(collection_quote.find())

# Функція для серіалізації ObjectId в рядок
# def serialize_object(obj):
#     if isinstance(obj, ObjectId):
#         return str(obj)
#     return obj
#
# # Збереження даних у файли JSON з правильною серіалізацією ObjectId
# with open('author_data.json', 'w', encoding='utf-8') as json_file:
#     json.dump(data_from_author, json_file, ensure_ascii=False, indent=4, default=serialize_object)
#
# with open('contact_data.json', 'w', encoding='utf-8') as json_file:
#     json.dump(data_from_contact, json_file, ensure_ascii=False, indent=4, default=serialize_object)
#
# with open('quote_data.json', 'w', encoding='utf-8') as json_file:
#     json.dump(data_from_quote, json_file, ensure_ascii=False, indent=4, default=serialize_object)
#
# print("Дані було успішно експортовано у файли JSON ")

