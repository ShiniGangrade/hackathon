import re
def string_manip(str,word):
    """ function accepts the following two parameters:
    str = string to be manipulated and
    word = word to be found in the string"""

    print "Original string  = ", str

    counter = 0
    str_arr = str.split()
    new_str = ""
    for i in str_arr:
        if i.lower() == word.lower():
            counter += 1
        else:
            new_str += i + " "

    #Step 1
    print "Number of occurances of the word in the string = ",counter

    # Step 2
    print "The string after removing the given word = ",new_str

    # Step 3
    for i in range(counter):
        new_str += word + " "
    print "Final string after appending the removed words at the end = ",new_str


input_string = raw_input("Enter the string : ")
input_word = raw_input("Enter the word :")
# s = "this is a sample code that is to be tested is this that code"
# w = "is"

string_manip(input_string,input_word)