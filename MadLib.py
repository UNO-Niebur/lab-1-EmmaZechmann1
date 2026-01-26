#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  Noun_1=input(f"Give me a singular Noun in the pasted tense:")
  Noun_2 = input(f"Give Me a singular Noun that relates to movement: ")
  Adjective_1= input(f"Give me an Adjective:")
  Adjective_2 =input(f"Give me a different Adjective: ")
  Adverb_1= input(f"Give me an Adverb with ly at the end of it: ")
  Adverb_2 = input(f"Give me a different Adverb: ")
  print(f"Suzie {Noun_1} to school very {Adverb_1} beacuse she had a very {Adjective_1} Squirel that didn't want to behave.")
  print(f" Upon her arival to school the squirel {Noun_2} {Adverb_2} out of her pocket onto the {Adjective_2} floor.")
  print(f" When the teacher saw him she called Suzies parents and wrote her up")
  if __name__ == "__main__":
     main()
  #Print the story with the user supplied words.



#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
