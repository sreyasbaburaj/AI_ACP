print("Hello. Welcome to the Mood-based Chatbot")
a=input("What is your name? ")
print(f"Well nice to meet you {a} ")

while True:
    b=input("How are you feeling today? ")
    if b.lower()=="great" or b.lower()=="good":
        print("Good to hear you are doing well.")
        c=input("Is there any special reason why you are feeling good today. ")
        if "birthday" in c.lower():
            print("Happy Birthday!!")
        else:
            print(f"Thats great to hear {a}")
    elif b.lower()=="bad" or b.lower()=="not good":
        print("I am sorry to hear that. Hope things get well soon.")
    else:
        print("I get it. Sometimes it's hard to describe what we feel.")

    exit=input("Would you like to exit or continue(Yes or No): ")
    if exit.lower()=="yes":
        print("Goodbye!")
        break
    else:
        print("Ok, lets keep going.")