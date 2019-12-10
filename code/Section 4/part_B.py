from flask import Flask
from flask_restful import Resource, API

app = Flask(__name__)
api = API(app)

items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None):
            return {"message": "An item with name {} already exists".format(name)}, 400

        item = {"name": name, "price": 12.00}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {"items": items}, 200

api.add_resrouce(Item, "/item<string:name>")
api.add_resrouce(ItemList, "/items")

app.run(port=5000)