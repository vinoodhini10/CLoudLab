from MongoDBexample import get_database
dbname = get_database()

# Create a new collection
collection_name = dbname["user_1_items"]
##This is for Updation
#mquery = { "item_name": "Sandwich" }
#nvalues = { "$set": { "quantity":20} }

#item_details = collection_name.find()
#item_details=collection_name.find({"category"::food"})
#for item in item_details:
    # This does not give a very readable output
    #print(item)
    #print(item['item_name'], item['category'])
#item_details = collection_name.find({"category" : "food"})
#for item in item_details:
  #  print(item['item_name'],item['category'])
#from pandas import DataFrame
# convert the dictionary objects to dataframe
#items_df = DataFrame(item_details)

# see the magic
#print(items_df)


#results=collection_name.update({"item_name": "Sandwich"}, {$inc: {"category": "Eatable"}})
#for mrd in collection_name.find():
  #print(mrd)

myquery = {"item_name": "Spoon"}  
collection_name.delete_one(myquery) 
print('Item  Deleted Successfully')
