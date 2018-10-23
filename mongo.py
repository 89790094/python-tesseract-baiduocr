from pymongo import MongoClient

conn = MongoClient('mongodb://114.215.252.154:27017/')
conn['8jieke'].authenticate('8jk', '8jieke', mechanism='SCRAM-SHA-1')
db = conn['8jieke']
