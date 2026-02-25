from flask import Flask, render_template
from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://lightningowl2004_db_user:8ZMxVmSvNhMhlR3l@recipes-db.diqsa9q.mongodb.net/?appName=recipes-db"
client = MongoClient(MONGODB_URI)

db = client["recipes"]
collection = db["food"]

app = Flask(__name__)

data = [
    {
        "name": "Honey Garlic Chicken",
        "price": 12.99,
        "ingredients": ["chicken", "honey", "garlic", "soy sauce", "ginger"]
    },
    {
        "name": "Spaghetti Carbonara",
        "price": 10.99,
        "ingredients": ["spaghetti", "eggs", "parmesan cheese", "bacon", "black pepper"]
    },
    {
        "name": "Vegetable Stir Fry",
        "price": 8.99,
        "ingredients": ["broccoli", "carrots", "bell peppers", "soy sauce", "garlic", "ginger"]
    },
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome")
def welcome():
    return "<html><body><h1><em>Welcome to CS4800! Enjoy the recipes!</em></h1></body></html>"

@app.route("/search/<budget>")
def search_recipes(budget):
    budget = float(budget)
    result = []
    for recipe in collection.find():
        if recipe["price"] <= budget:
            recipe["_id"] = str(recipe["_id"])
            result.append(recipe)
    print(result)
    return result

app.run(host="0.0.0.0", port=5005)