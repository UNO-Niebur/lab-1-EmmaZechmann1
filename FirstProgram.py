#FirstProgram.py
#Name: Emma 
#Date: 1/25/2026
#Assignment:lab 1

from http.client import NotConnected


def main():
  print("First Program")
  print("hello")
  
  print("what is your name?")
  userInput = input("Enter your name: ")
  print(f"You have entered your name as {userInput}")
  age = int(input("the age you turn in the current year:"))
  current_year = int(input("What is the current year:"))
  birth_year = current_year - age
  print(f"you were born in {birth_year}")
  #Tell the user what year they were born in.
  #Assume that they have not had their birthday yet this year.

if __name__ == "__main__":
  main()
 