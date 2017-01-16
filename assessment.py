"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""
import string

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    word_and_count = {}             # assign empty dictionary for word and number of times it's repeated
    word_list = phrase.split()      # split and put all words in a list

    # if word is not in list add it to dict and assign value to 1 else add =1 tocurrent value
    for word in word_list:
        if word in word_and_count:
            word_and_count[word] += 1
        else:
            word_and_count[word] = 1

    # return word and cound dictionary
    return word_and_count


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    # create dict for melons and prices as key and value
    melon_prices = {'Watermelon':2.95, 'Cantaloupe':2.50, 'Musk':3.25, 'Christmas':14.25}
    
    # if parameter melon is in list return melon price or say it doesn't exist
    if melon_name in melon_prices:
        return melon_prices[melon_name]
    else:
        return 'No price found'


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """

    word_dict = {}

    # find word length, add all words that's same length to a list and sort after each iteration
    for word in words:
        word_length = len(word) 
        if word_length in word_dict:
            word_dict[word_length].append(word)
            word_dict[word_length].sort()
        else:
            word_dict[word_length] = [word]
    # return list of tuples of word and word_count pairs
    return sorted(list(word_dict.items()))


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    
    # create English_to_pirate" dictionary from word list
    English_to_Pirate = {'sir':'matey', 'hotel':'fleabag inn', 'student':'swabbie',\
    'man':'matey', 'professor':'foul blaggart', 'restaurant':'galley', 'your':'yer',\
    'excuse':'arr', 'students':'swabbies', 'are':'be', 'restroom':'head', 'my':'me', 'is':'be'}

    # create English_to_pirate" dictionary from word list
    # for i in range(0, len(all_words), 2):
    #     English_to_Pirate[all_words[i]] = all_words[i+1]

    words_in_phrase = phrase.split()

    pirate_phrase = "" # initialize pirate_phrase to empty string

    # if a pirate word exists for English word, append the substitute else append English word
    for word in words_in_phrase:
        if word in English_to_Pirate:
            pirate_phrase += English_to_Pirate[word] + " "
        else:
            pirate_phrase += word + " "

    # return pirate string
    return pirate_phrase.rstrip()   # rsrip is for deleting the last space




def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:  

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']


    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    result_list =[names[0]]

    # make dictionary of all names with first letter as the key
    sorted_names = {}
    for name in names:
        if name[0] in sorted_names:
            sorted_names[name[0]].append(name)
        else:
            sorted_names[name[0]] = [name]

    # start iterating through. First word is first in list of words.
    iter_word = names[0]
 
    try:
        sorted_names[iter_word[0]].pop(0)   # since the word is used remove from list
    except:
        del sorted_names[iter_word[0]]      # delete key if value list is empty


    while iter_word[-1] in sorted_names:  # find last letter in iter_word and see if there are words starting with that letter in dictionary
        
        try:
            iter_word = sorted_names[iter_word[-1]].pop(0)  # if word exists, assign it to new iter_word and pop it from list
            result_list.append(iter_word)
        except:
            del sorted_names[iter_word[-1]]                 # if list is empty delete key as well

    return result_list


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
