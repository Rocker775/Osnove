mood = input("What's your mood? ")
if mood == "sad" or mood == "angry":
    reason = input("Why are you {0}".format(mood))
    if reason == "corona":
        print("It will pass some day, don't worry")
    else:
        print("Please don't be " + mood)
elif mood == "happy":
    print("I'm happy that you are {0}".format(mood))
else:
    print("I don't know what you want")