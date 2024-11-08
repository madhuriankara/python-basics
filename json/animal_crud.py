import json
filepath = 'animal_score.json'

#Add a new entry for "zebra" with a score of 87

def add_animal():
    with open(filepath , 'r') as file:
        data = json.load(file)
        data['zebra'] = 87
    with open(filepath, 'w') as file:
        json.dump(data, file, indent =4)
        print("Zebra is now added")

#Read the score for "lion."

def read_lion():
    with open(filepath, 'r') as file:
        data = json.load(file)
        print("lion score:", data.get('lion', 'no value'))

#Update "tiger" score to 94

def update_lion():
    with open(filepath,'r') as file:
        data = json.load(file)
        data['lion'] = 90
    with open(filepath, 'w') as file:
        json.dump(data, file, indent =4)
        print("The animal lion is now updated to 90")

#Delete "giraffe."

def delete_lion():
    with open(filepath, 'r') as file:
        data = json.load(file)
        data.pop('lion')
    with open(filepath, 'w') as file:
        json.dump(data, file, indent = 4)
        print("lion is now deleted")           
    

def startpy():
    read_lion()
    update_lion()
if __name__ == '__main__':
    startpy()