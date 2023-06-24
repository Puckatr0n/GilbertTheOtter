languages = ["C++", "Java", "Python", "Javascript"]


print("What language are you searching for?")
lang = input()
for language in languages:
    if language == "Python":
        print("We found " + lang)
        continue
    else:    
        print(language + "...Not the right one...")