import sys
import clipboard
import json

SAVED_DATA="clipboard.json"

#function to make a json file and write data
def save_data(filepath, data):
    with open(filepath,"w") as f:
        json.dump(data,f)

#function to read a json file
def load_data(filepath):
    try:
        with open(filepath,"r") as f:
           data=json.load(f)
           return data
    except:
        return{}

if len(sys.argv)==2:
    command=sys.argv[1]
    data=load_data(SAVED_DATA)

    if command=="save":
        key=input("Enter a key: ")
        data[key]=clipboard.paste()
        save_data(SAVED_DATA,data)
        print("DATA SAVED!")
        
    elif command=="load":
        key=input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print(data[key])
            print("DATA COPIED TO CLIPBOARD!")
        else:
            print("Key does not exist")
            
    elif command=="list":
        print(data)
    else:
        print("Unknown Command")
        
else:
     print("Please pass exactly one command.")
    

