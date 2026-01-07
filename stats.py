def get_book_text(path_to_book):
    with open(path_to_book) as f:
        text = f.read()
        # split_text = text.split() // only used if using the for loop below
        word_count = len(text.split()) # the easy way 
    """ the hard way
        word_count = 0 
        for word in split_text:
        word_count += 1 """
    
    return word_count
