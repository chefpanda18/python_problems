
[colors.upper() for colors in ['blue', 'red', 'green']]

def upper_words(words):
    """Print list of words capitalized"""
    for word in words:
        print(word.upper())

def print_e_words(words):
    """print only words that start with e"""
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(words.upper())

# def starts_with(words, char1, char2):
    """print only words that start with the letters passed through the function"""
    # for word in words:
    #     if word.startswith(char1) or word.startswith(char2):
    #         print(words.upper())

def print_upper_words3(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break