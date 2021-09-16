words = ["hello", "hey", "goodbye", "yo", "yes"]


def print_upper_words(words, must_start_with={"h", "y"}):
    """prints all caps versions of words in list that begin
    only with the letters we pass in with the must_start_with argument
    1. This only can accept 2 letters in the must_start_with argument currently
    """
    for word in words:
        for char in must_start_with:
            if word.startswith(char):
                print(word.upper())
