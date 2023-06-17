sentence = input("Provide a sentence")
lower_sentence = sentence.lower()

if "cookie" in lower_sentence:
    print("There is a cookie in thet sentence!")
    if "chocolate" in lower_sentence:
        print("And it's chocolate!")
    elif "vanila" in lower_sentence:
        print("Well vanila is a fine flavour!")
else:
    print("No cookies :(")
