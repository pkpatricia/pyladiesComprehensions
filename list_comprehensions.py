# complete the following functions, then run the associated tests to make sure
# that your code is correct

def double_numbers(numbers_list):
    """take a list of numbers and return a list containing each number doubled"""
    double_numbers = []
    # for number in numbers_list:
    #     double_numbers.append(number*2)
    # return double_numbers
    return [number*2 for number in numbers_list]

def split_sentence(sentence):
    """write a list comprehension that separates a String sentence
    into a list of words"""
    word_list = []
    # for word in sentence.split():
    #     word_list.append()
    # return word_list
    return [word for word in sentence.split()]

def number_of_spaces(sentence):
    """Count the number of spaces in a string """
    return len([space for space in sentence if space == ' '])


def word_length(sentence):
    """write a list comprehension that separates a String sentence into words,
    and then returns a list containing the length of each word"""



def short_words(sentence):
    """Find all of the words in a string that are fewer than 4 letters"""


def get_vowel_names(name_list):
    """return every name from a list that begins with a vowel"""


def get_consonants(sentence):
    """Remove all of the vowels in a string [make a list of the non-vowels]"""


def divisible_by_seven():
    """Find all of the numbers from 1-1000 that are divisible by 7"""


def numbers_containing_three():
    """Find all of the numbers from 1-1000 that have a 3 in them"""
    return [
        num
        for num in range(1000)
        if '3' in str(num)
        ]


def divisible_by():
    """Use a nested list comprehension to find all of the numbers from 1-1000
    that are divisible by any single digit besides 1 (2-9)"""
    return [
        number
        for number in range(1, 1001)
        if True in
           [
               True
               for divisor in range(2, 10)
               if number % divisor == 0
           ]
        ]

def negative_numbers():
    """write a list comprehension that returns the following list: [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]"""
    return [
        number
        for number in range(-10, 1)
        ]