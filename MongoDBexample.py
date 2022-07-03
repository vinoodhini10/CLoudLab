def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://vinodhini:pQzeC4EXBZyZFAT3@cluster0.fne9a.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['user_shopping_list']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()
    collection_name = dbname["user_1_items"]
    item_1 = {
    "_id" : "U1IT00006",
    "item_name" : "Spoon",
    "max_discount" : "10%",
    "batch_number" : "RR450020FRG",
    "price" : 340,
        "category" : "Kitchen Utensils"
    }

    item_2 = {
    "_id" : "U1IT00007",
    "item_name" : "Radish",
    "category" : "food",
    "quantity" : 12,
    "price" : 36,
    "item_description" : "Country Radish"
    }
    collection_name.insert_many([item_1,item_2])






#collection_name.insert_one([item_1])
#    
