from modles.database import Database
Database.initialize()
#Database.insert(collection="test",data={"name":"kevin","age":"20"})
#Database.insert(collection="test",data={"name":"elio","age":"20"})
print(Database.find_one(collection="test",query={"name":"kevin"}))
print(Database.find_one(collection="test",query={"age":"20"}))
print(Database.find_one(collection="test",query={"age":"20"}))
print(Database.find_all(collection="test")[0])
print(Database.find_all(collection="test")[1])
