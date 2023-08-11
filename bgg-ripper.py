print("Importing Libs...please wait")
import os
import os.path
import time
import json

# from libbgg.apiv1 import BGG
# You can also use version 2 of the api:
from libbgg.apiv2 import BGG as BGG2

# Clear Screen
os.system("cls")

# Start Message
print("")
print("Hermanns Board Game Geek - Game Info Ripper")
print("")
print("2023 , by Hermann Knopp")
print("")
print("Hint: Server needs 3 Seconds Pause, befor next Game Info download")
print("Error: Too Many Requests, is possible")
print("")


print("Checking Save Dir...")
print("")


# Make Custom Story Dir
dir_path = os.path.dirname(os.path.realpath(__file__))
path = "gamestories"
filepath= dir_path + "\\" + path


# Check whether the specified path exists or not
isExist = os.path.exists(filepath)
if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(filepath)
   print("The new directory 'gamestories' is created!")

ide=input("Enter Start id or press enter for id=1 - do not enter garbage! ")
if ide=="" or ide==None:
    id=0
else:
    id=int(ide)   


# Parsing JSON Py-BGG Data (Chunky Mode)

# Game Description Item
def description():
    try:
        json_tree = json.loads(data_json)
        json_items = json_tree['items']
        json_item = json_items['item']
        json_description=json_item['description']
        json_text=json_description['TEXT']
        text = json_text
        text=text.replace("&#10;","")
        return (text)
    except:
        text="None"
        return (text)
        pass


# Game Name Item
def title():
    try:
        json_tree = json.loads(data_json)
        json_items = json_tree['items']
        json_item = json_items['item']
        json_name=json_item['name']
        if len(json_name)>1:
            json_value=json_name[0] 
        else:    
            json_value_json_name

        #a=input("Debug1") 
        #print(json_value)
        #a=input("Debug2")
        text = json_value['value']
        #print(text)
        #a=input("Debug3")
        #text=text.replace("&#10;","")
        return (text)
    except:
        text="None"
        return (text)
        pass


# Game Max Players Item
def maxplayers():
    try:
        json_tree = json.loads(data_json)
        json_items = json_tree['items']
        json_item = json_items['item']
        json_name=json_item['maxplayers']
        json_value=json_name
        text = json_value['value']
        #text=text.replace("&#10;","")
        return (text)
    except:
        text="None"
        return (text)
        pass


# Game Max Playtime item
def maxplaytime():
    try:
        json_tree = json.loads(data_json)
        json_items = json_tree['items']
        json_item = json_items['item']
        json_name=json_item['maxplaytime']
        json_value=json_name
        text = json_value['value']
        #text=text.replace("&#10;","")
        return (text)
    except:
        text="None"
        return (text)
        pass


# Game Min Playtime Item
def minage():
    try:
        json_tree = json.loads(data_json)
        json_items = json_tree['items']
        json_item = json_items['item']
        json_name=json_item['minage']
        json_value=json_name
        text = json_value['value']
        #text=text.replace("&#10;","")
        return (text)
    except:
        text="None"
        return (text)
        pass


# Game Min Players Item
def minplayers():
    try:
        json_tree = json.loads(data_json)
        json_items = json_tree['items']
        json_item = json_items['item']
        json_name=json_item['minplayers']
        json_value=json_name
        text = json_value['value']
        #text=text.replace("&#10;","")
        return (text)
    except:
        text="None"
        return (text)
        pass


# Game Min Playtime Item
def minplaytime():
    try:
        json_tree = json.loads(data_json)
        json_items = json_tree['items']
        json_item = json_items['item']
        json_name=json_item['minplaytime']
        json_value=json_name
        text = json_value['value']
        #text=text.replace("&#10;","")
        return (text)
    except:
        text="None"
        return (text)
        pass


# Game Average Playtime Item
def playingtime():
    try:
        json_tree = json.loads(data_json)
        json_items = json_tree['items']
        json_item = json_items['item']
        json_name=json_item['playingtime']
        json_value=json_name
        text = json_value['value']
        #text=text.replace("&#10;","")
        return (text)
    except:
        text="None"
        return (text)
        pass


# Game Published at Item
def published():
    try:
        json_tree = json.loads(data_json)
        json_items = json_tree['items']
        json_item = json_items['item']
        json_name=json_item['yearpublished']
        json_value=json_name
        text = json_value['value']
        #text=text.replace("&#10;","")
        return (text)
    except:
        text="None"
        return (text)
        pass


# Game Publisher Item (Check for Garbage first)
def publisher():
    try:
        json_tree = json.loads(data_json)
        json_items = json_tree['items']
        json_item = json_items['item']
        json_name=json_item['link']
        json_len =len(json_name)
        #print(json_len)
        json_value=json_name[json_len-1]
        text = json_value['value']
        #text=text.replace("&#10;","")
        #text="dummy"
        return (text)
    except:
        text="None"
        return (text)
        pass


# Game Type Item
def gametype():
    try:
        json_tree = json.loads(data_json)
        json_items = json_tree['items']
        json_item = json_items['item']
        json_name=json_item['link']
        #json_len =len(json_name)
        #print(json_len)
        json_value=json_name[0]
        text = json_value['value']
        #text=text.replace("&#10;","")
        #text="dummy"
        return (text)
    except:
        text="None"
        return (text)
        pass


# Start Message Input Resume ID of Game 
print("Start/Resume Download at ID= "+str(id))
print("")


# Main Download Loop
while True:

    # ID Counter    
    id=id+1
    

    # Check of End ID
    if id>=397393:
        print("You reached last game, exit")
        a=input("Wait return key")
        exit()    

     
    # Connect to  BGG Library V2
    conn2 = BGG2()
    

    # Download Game Info from ID
    try:
        # Pause Download for 3 Seconds (Too many Requests, Fix) 
        time.sleep(3)
    
        # Save Results
        results = conn2.boardgame(id, stats=True)
    except:
        
        # Delay , at Too Many Requests Error and retry
        print("")
        print("Too many Requests, will wait for 15 seconds")
        print("")
        time.sleep(15)
        pass


    #Copy Result to JSON Format for Parsing 
    data_json=json.dumps(results, indent=4, sort_keys=True)


    # Check if no Game Info Found and jump over one ID
    if title()=="None":
        id=id+1

    
    # If Data found Display and Save Text to File
    else:
        
        # Display Text Info of Game 
        print("")
        print("The Name of the Game is: ",title(),".")
        print("it is a",gametype(),"Game.")
        print("")
        print("The Game Story is about: ")
        print("")
        print(description())
        print("")
        print("It can be played with a maximum amount of",maxplayers(),"players.")
        print("The maximum playtime is",maxplaytime(),"minutes.")
        print("The Minimum Playing Age is:",minage(),"years.")
        print("It needs a minimum of",minplayers(),"players.")
        print("The minimum time for playing this game is:",minplaytime(),"minutes.")
        print("Average playing time is:",playingtime(),"minutes.")
        print("This game is published in the year",published(),".")
        
        # do not use today, garbage in string is crashing script
        #print("The publishers name is:",publisher(),".")


        # Game Info Save Routine
    
        # Check/Replace Garbage in Title=Filename       
        names3=title()
        names3=names3.replace(":","_")
        names3=names3.replace(".","_") 
        names3=names3.replace("(","_")
        names3=names3.replace(")","_")
        names3=names3.replace(" ","_")
        names3=names3.replace(",","_")
        names3=names3.replace("'","_")
        names3=names3.replace("/","_")
        names3=names3.replace("\\","_")
        names3=names3.replace("*","_")
        names3=names3.replace("=","_")
        names3=names3.replace("+","_")
        names3=names3.replace("~","_")
        names3=names3.replace("#","_")
        names3=names3.replace("!","_")
        names3=names3.replace("§","_")
        names3=names3.replace("*","_")
        names3=names3.replace("$","_")
        names3=names3.replace("%","_")
        names3=names3.replace("&","_")
        names3=names3.replace("°","_")
        names3=names3.replace("<","_")
        names3=names3.replace(">","_")
        names3=names3.replace("@","_")
        names3=names3.replace(";","_")
        names3=names3.replace("?","_")
        names3=names3.replace("{","_")
        names3=names3.replace("}","_")
        names3=names3.replace("[","_")
        names3=names3.replace("]","_")
        names3=names3.replace('"',"_")
        #names3=names3.replace("*","_")
        titel=names3        


        # Construct Filename
        filename= filepath + "\\" + str(id)+"_Game_" + titel + ".txt"


        # Open File for Write
        f=open(filename,"w")
    

        # Write Game Info Data to File 
        f.write("")
        f.write("\n")
        f.write("The Name of the Game is: "+title()+".")
        f.write("\n")
        f.write("it is a "+gametype()+" Game.")
        f.write("\n")
        f.write("")
        f.write("\n")
        f.write("The Game Story is about: ")
        f.write("\n")
        f.write("")
        f.write("\n")
        f.write(description())
        f.write("\n")
        f.write("")
        f.write("\n")
        f.write("It can be played with a maximum amount of "+maxplayers()+" Players.")
        f.write("\n")
        f.write("The maximum Playtime is "+maxplaytime()+" Minutes.")
        f.write("\n")
        f.write("The Minimum playing Age is: "+minage()+" Years.")
        f.write("\n")
        f.write("It needs a minimum of "+minplayers()+" Players.")
        f.write("\n")
        f.write("The minimum time for playing this Game is: "+minplaytime()+" Minutes.")
        f.write("\n")
        f.write("Average playing Time is: "+playingtime()+" Minutes.")
        f.write("\n")
        f.write("This Game is published in the Year "+published()+" .")
        f.write("\n")

        # Do not use today, garbage in string is crashing script
        #f.write("The publishers Name is: "+publisher()+" .")
        f.write("\n")
    

        # Close
        f.close



