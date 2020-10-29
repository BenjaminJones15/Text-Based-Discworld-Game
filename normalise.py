import string

# List of "unimportant" words added more based on our commands
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would', 'art', 'use', 'enemy', 'watch',
              'pseudopolis', 'yard', 'house', 'sator', 'lady', 'sybil', 'free',
              'shrine', 'dwarfs', 'delicatessen', 'pink',
              'pussycat', 'lost', 'office', 'drum']


def filter_words(words, skip_words):
    words = [x for x in words if x not in skip_words]
    return words

def remove_spaces(text):
    text = text.strip()  # removes unnessary blank spaces
    return text

def remove_punct(text):
    no_punct = ""
    for char in text:
        if not (char in string.punctuation):  # takes out punctuation
            no_punct = no_punct + char
    return no_punct


def normalise_input(user_input):
    user_input = remove_punct(user_input.lower()) #removes punct
    user_input = remove_spaces(user_input)  #removes spaces
    words = user_input.split()  #splits user input into list
    words = filter_words(words, skip_words)    
    return words
