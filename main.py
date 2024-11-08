from datetime import date
import os

def main():
    if (os.path.exists("Diaries") == False):
        os.makedirs("Diaries")
    name = input("Provide your name: ")
    dir = f"Diaries/{name}'s diary"
    if(os.path.exists(dir) == False):
        os.makedirs(dir)
    with open(dir + date.today + ".txt", "w") as file: