from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://lightningowl2004_db_user:8ZMxVmSvNhMhlR3l@recipes-db.diqsa9q.mongodb.net/?appName=recipes-db"
client = MongoClient(MONGODB_URI)

db = client["recipes"]
collection = db["food"]

# --- WRITE (insert all documents) ---
# collection.insert_many([
#     {
#         "name": "Honey Garlic Chicken",
#         "price": 12.99,
#         "ingredients": ["chicken", "honey", "garlic", "soy sauce", "ginger"]
#     },
#     {
#         "name": "Spaghetti Carbonara",
#         "price": 10.99,
#         "ingredients": ["spaghetti", "eggs", "parmesan cheese", "bacon", "black pepper"]
#     },
#     {
#         "name": "Vegetable Stir Fry",
#         "price": 8.99,
#         "ingredients": ["broccoli", "carrots", "bell peppers", "soy sauce", "garlic", "ginger"]
#     },
# ])

# --- READ (find one document) ---
for f in collection.find():
    print(f)