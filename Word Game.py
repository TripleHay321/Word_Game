import random

words = ["Aberration", "Arbitrary", "Brilliant", "Celebrated", "Definitely",
         "Extravagan", "Fascinated", "Gathering", "Happiness", "Incredible",
         "Judgmental", "Kaleidosco", "Lamentable", "Manifestat", "Negotiator",
         "Obligation", "Perseveran", "Questioner", "Revelation", "Stimulated",
         "Tranquilit", "Understanding", "Validation", "Whispering", "Abundance",
         "Beautiful", "Completely", "Determination", "Exhilarating", "Fulfillment",
         "Gloriously", "Harmonious", "Imagination", "Juxtaposing", "Knowledgeable",
         "Luminous", "Magnificent", "Opportunity", "Passionate", "Quintessence",
         "Resilience", "Serendipity", "Temptation", "Unstoppable", "Vivacious",
         "Wonderful", "Yesteryear", "Zealousness", "Weather", "Sanctum",
         "Capture", "Supreme", "Freedom",
         "Support", "Pioneer", "Protect", "Thought", "Justice",
         "Capture", "Honesty", "Imagine", "Advance", "Balance",
         "Exploit", "Express", "Dynamic", "Problem", "Fulfil",
         "Present", "Perform", "Produce", "Perfect", "Program",
         "Gravity", "Upgrade", "Village", "Support", "Network",
         "Package", "Confirm", "Develop", "Service", "Channel",
         "Upgrade", "Weather", "Special", "Consider", "Install",
         "Country", "Register", "Forecast", "Explore", "Prepare",
         "Machine", "Student", "Traffic", "Desktop", "Research"]
def word():
    points = 0
    while True:
        random.shuffle(words)
        task = words[0]
        user_word = list(task)
        random.shuffle(user_word)
        convert = ''.join(user_word)
        calc_points = int(len(convert)/2)
        print(convert)
        user_input = str(input("Type in the correct word:   ")).capitalize()
        if user_input == task:
            points += calc_points
            print("You won! You've", points, "Points")
        else:
            print("You lost!, You've", points, "Points")
            break

word()