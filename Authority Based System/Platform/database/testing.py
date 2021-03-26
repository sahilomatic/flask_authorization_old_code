from database.databaseConfig import CreateConnection
session = CreateConnection().connect()
l = {'a':1,'b':2,'c':3}
k = l.values()
print(k)