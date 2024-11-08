import json
filepath = 'product_score.json'

#Add a new entry for "smartwatch" with a score of 89.

def new_entry():
    with open(filepath, 'r') as file:
        data = json.load(file)
        data['smartwatch'] = 89
    with open(filepath, 'w') as file:
        json.dump(data, file, indent =4)
        print("New entry for smartwatch is created")

#Read the score for "smartphone."

def read_smartphone():
    with open(filepath, 'r') as file:
        data = json.load(file)
        print("Smartphone :" , data.get("smartphone","nothing is read"))

#Update "tablet" score to 86.

def update_tablet():
    with open(filepath,'r') as file:
        data = json.load(file)
        data['tablet'] = 86
    with open(filepath, 'w') as file:
        json.dump(data, file, indent =4)
        print("The tablet score is now updated")
        
#Delete "headphones."

def delete_headphones():
    with open(filepath , 'r') as file:
        data = json.load(file)
        data.pop("headphones" , None)
    with open(filepath, 'w') as file:
        json.dump(data, file, indent = 4)
        print("The headphones are deleted from products")


new_entry()
read_smartphone()

