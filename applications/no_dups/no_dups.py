def no_dups(s):
    # Your code here
    # return if it's empty

    # create dictionary for initial word
    dup_dict = {}
    no_duplicates_string = ''

    if s != '':
        # put string into list w/split
        # loop over split array and add to dict and str
        for word in s.split():
            if word not in dup_dict:
                no_duplicates_string += ' ' + word
                dup_dict[word] = 1
            

    return no_duplicates_string.strip()
    
    

    
    
    # create new string without duplicates
    
    
    


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))