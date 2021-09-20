import os
import pymongo
if os.path.exists("env.py"):
    import env

        
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print(f"Could not connect to MongoDB: {e}")


def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option


def main_loop():
    try:
        while True:
            option = show_menu()
            if option != "5":
                if option in ["1","2","3","4"]:
                    print(f"You have selected option {option}")
                else:
                    print("Invalid option")
            elif option == "5":
                conn.close()
                break
    finally:
        if conn:
            conn.close()

    print("")


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()