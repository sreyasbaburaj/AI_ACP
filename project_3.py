from textblob import TextBlob

def feeling(polarity):
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
    
def advice(emotion):
    if emotion=="Positive":
        return "That's great! Keep up your positivity."
    elif emotion=="Negative":
        return "If u are feeling down, you can reach out to your friends or loved ones."
    else:
        return "Let's brighten up your day with positivity!"


print("Hello. I am the sentiment analysis chatbot.")
while True:
    x=[]
    text=input("How do you feel today? ").lower()
    pole=Textblob(text).sentiment.polarity
    feel=feeling(pole)
    print("Polarity:",pole)
    print("Your feelings are",feel)
    x.append(feel)
    print(advice(feel))
    exit=input("Would you like to analyse your feelings again?").lower()
    if "no" in exit:
        print("Sentiment History:",x)
        break
    else:
        print("Ok. Let's go again.")
