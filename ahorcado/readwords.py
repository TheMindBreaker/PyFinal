def read():
    import re
    file = open('words.txt', 'r')
    # .lower() returns a version with all upper case characters replaced with lower case characters.
    text = file.read().lower()
    file.close()
    # replaces anything that is not a lowercase letter, a space, or an apostrophe with a space:
    text = re.sub('[^a-z\ \']+', " ", text)
    return list(text.split())
def choseRand():
    import random
    randomword = read()[random.randrange(len(read()))]
    return randomword
