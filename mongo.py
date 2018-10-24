from pymongo import MongoClient

conn = MongoClient('mongodb://127.0.0.1:27017/')
conn['test'].authenticate('root', 'sa', mechanism='SCRAM-SHA-1')
db = conn['test']
