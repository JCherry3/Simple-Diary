from datetime import datetime
import os

def main():
    if (os.path.exists("/Diaries") == False):
        os.makedirs("Diaries")
    name = input("Enter your name: ")
    dir = f"/Diaries/{name}'s diary"
    if(os.path.exists(dir) == False):
        os.makedirs(dir)
    with open(dir + "/" + datetime.now().strftime("%Y-%m-%d") + ".txt", "w") as file:
        print("Type one paragraph at a time and end your paragraph by pressing ENTER")
        print("You may finish writing by pressing ENTER once more after entering your final paragraph")
        print("type 'help' to see these instructions again")
        text = input("Begin writing:\n")
        while(text != ""):
            if(text == "help"):
                print("Type one paragraph at a time and end your paragraph by pressing ENTER")
                print("You may finish writing by pressing ENTER once more after entering your final paragraph")
                print("type 'help' to see these instructions again")
            else:
                file.write(text + "\n\n")
                text = input("Continue writing:\n")
    print("Entry Complete")
    return