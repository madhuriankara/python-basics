import json
filepath = 'city123.json'

#1. Find the Highest and Lowest Scores

def high_low():
    score = int(input("Enter the number"))
    if score >= 89:
        print("This is the highest")
    elif score <= 71:
        print("This is the lowest")
    else:
        print("The number is not in the range")

#2. Delete Multiple Entries Below a Certain Score. 

def delete_multiple():
    with open(filepath, 'r') as file:
        data = json.load(file)
        data.pop('toronto' : 90


high_low()
