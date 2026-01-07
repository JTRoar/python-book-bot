 
def word_count(text_string):
    #split_text = text_string.split() // only used if using the for loop below
    word_count = len(text_string.split()) # the easy way 
     
    """ the hard way
        word_count = 0 
        for word in split_text:
        word_count += 1 """ 
    
    return word_count 

def count_characters(text_string):
    count_dict = {}
        
    """For loop that goes through each character, adds to count_dict, and sets the value to 1
    if it's not already in the count_dict. If it IS in count_dict, it will increment
    with the else statement"""
    
    for current_character in text_string:
        if current_character not in count_dict:
            count_dict[current_character] = 1
        else:
            count_dict[current_character] += 1   
        
    return count_dict

def sort_dict(dict_to_sort):
    sorted_LIST_of_dicts = []

    for dict in dict_to_sort:
        sorted_LIST_of_dicts.append(dict)
    
    print(sorted_LIST_of_dicts)


    return sorted_LIST_of_dicts

""" references:
    #print(count_dict)     # current_character is the individual character
    #print(count_dict[current_character])  #count_dict[current_character] returns the value of the key
"""