def is_isogram(string):
    clean_string=string.lower().replace("-","").replace(" ","")
    for letter in clean_string:
        if clean_string.count(letter)>1:
            return False
    return True