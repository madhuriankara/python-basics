import json
filepath = 'city_score.json'

#Add a new entry for scarborough

def add_entry():
    with open(filepath, 'r') as file:
        data = json.load(file)
    data['Scarborough'] = 89
    with open(filepath, 'w') as file:
        json.dump(data, file, indent =4)
        print("Scarborough is been added")

#Read Toronto score

def read_city():
    with open(filepath, 'r') as file:
        data = json.load(file)
        print("Hyderabad score :",data.get("hyd","city not found"))

#Updating hyderabad score to 81

def update_city():
    with open(filepath, 'r') as file:
        data = json.load(file)
        data["toronto"] = 100
    with open(filepath, 'w') as file:
        json.dump(data, file, indent =4)
        print("The score of toronto city is updated")

#delete bowmanville

def delete_city():
    with open(filepath, 'r') as file:
        data = json.load(file)
        data.pop("chennai",None)
    with open(filepath, 'w') as file:
        json.dump(data, file, indent =4)
        print("The city Chennai is now deleted")



def startpy():
    read_city()
    delete_city()
    update_city()
   # print("Tact101")
    

if __name__ == '__main__':
    startpy()