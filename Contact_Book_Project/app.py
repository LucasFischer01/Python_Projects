from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def load_contacts():
        try:
                with open("contacts.json", "r") as f:
                        return json.load(f)
        except FileNotFoundError:
                return {}

def save_contacts(contact_book):
        with open("contacts.json", "w") as f:
                json.dump(contact_book, f, indent=4)

@app.route("/")
def home():
        return "API running"

@app.route("/contacts", methods=["GET"])
def get_contacts():
        contact_book = load_contacts()
        return jsonify(contact_book)

@app.route("/contacts", methods=["POST"])
def add_contact():
        contact_book = load_contacts()
        data = request.json

        name = data.get("name")

        if name in contact_book:
                return {"error": "Contact already exists!"}, 400

        contact_book[name] = {
                "phone": data.get("phone"),
                "email": data.get("email"),
                "address": data.get("address")
        }
        save_contacts(contact_book)
        return{"message": "Contact added successfully"}

@app.route("/contacts/<name>", methods=["DELETE"])
def delete_contact(name):
        contact_book = load_contacts()

        if name not in contact_book:
                return{"error": "Contact not Found"}, 404
        del contact_book[name]
        save_contacts(contact_book)
        return{"message": "Contact deleted successfully"}

@app.route("/contacts/<name>", methods = ["PUT"])
def edit_contact(name):
        contact_book = load_contacts()
        data = request.json

        if name not in contact_book:
                return {"error": "Contact not Found"}

        if "phone" in data:
                contact_book[name]["phone"] = data["phone"]
        if "email" in data:
                contact_book[name]["email"] = data["email"]
        if "address" in data:
                contact_book[name]["address"] = data["address"]
        save_contacts(contact_book)
        return {"message": "Contact updated successfully"}


if __name__ == "__main__":
        app.run(debug=True)