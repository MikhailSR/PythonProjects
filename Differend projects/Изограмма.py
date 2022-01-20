# isIsogram "Dermatoglyphics" == true
# isIsogram "aba" == false
# isIsogram "moOse" == false -- ignore letter case

# option 1
def is_isogram(string):
    return len(string) == len(set(string.lower()))


# option 2 
def is_isogram(string):
    chars = []
    
    string = string.lower()
    IsIsogram = True
    
    for elem in string:
        if elem not in chars:
            chars.append(elem)
        else:
            IsIsogram = False
            break
            
    return IsIsogram