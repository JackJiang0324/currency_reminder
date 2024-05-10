import pymongo
client = pymongo.MongoClient(['localhost:27017'])
DATABASE = client['class']
#DATABASE['student'].delete_one({"name":"kevin","age":"16"})
print(DATABASE["student"].find_one({"name":"kevin"}))
print("ok")