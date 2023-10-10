import pymongo

from config import USER, PASSWORD

from bson import Decimal128
url = f'mongodb+srv://{USER}:{PASSWORD}' \
      f'@cluster0.xdd2fq6.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(url)

db = client.testDB
mops_coll = db.mops
vacuum_cleaners_coll = db.vacuum_cleaners

# add single document ####################
# mops_coll.insert_one(
#       {'title': 'Super mop', 'price': 15}
# )
#
# vacuum_cleaners_coll.insert_one(
#     {'title': 'vacuum cleaner', 'price': 150,
#      'power': 2000}
# )
#
# mops_coll.insert_one(
#       {'_id': 2, 'title': 'Super mop', 'price': 15}
# )
# add single document ####################

# mops_coll.insert_one(
#       {'title': 'Super puper mop', 'price': 133}
# )

# query = {}
# operation = {'$mul': {'price': Decimal128(str(1.1))}}
#
# data = mops_coll.update_many(query, operation)
# print(data.raw_result)
#
# mops_coll.drop()
# vacuum_cleaners_coll.drop()
#
# client.drop_database('testDB')
