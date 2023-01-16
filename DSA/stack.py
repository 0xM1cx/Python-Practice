import string

def filterList(s):
    current_string = [] # the books/letters will be contained here

    letters = string.ascii_letters 
    encountered_backslash = 0


    for i in s:
        if i == "\\":
            encountered_backslash += 1
        else:
            if i in letters:
                current_string.append(i)
        if encountered_backslash == 2:
            break
    # for i in s: # This loops through every element in the array/list
    #     if i in letters: # if the current element searched is a letter/book and not a wall then it will be pushed to the new_string stack
    #         new_string.append(i)
    #     else:
    #         continue
    
    return current_string



def main():
    '''
    PROBLEM:
    Alice is rearranging her library. She takes the innermost shelf 
    and reverses the order of books. She breaks the walls of the shelf. 
    In the end, there will be only books and no shelf walls. Print the 
    order of books.

    Opening and closing walls of shelves are shown by '/' and '\' respectively 
    whereas books are represented by lower case alphabets.

    INPUT FORMAT:
    The first line contains stsring, s, displaying her library

    OUTPUT FORMAT:
    Print only one string displaying Alice's library after rearrangement

    CONSTRAINTS
    2 <= |s| <= 10**3

    NOTE:
    The first character of the string is '/' and the last character of the 
    string is '\' indicating outmost walls of the shelf.

    SAMPLE INPUT:
    /u/love\i\

    SAMPLE OUTPUT:
    iloveu

    '''
    s = list(input("INPUT: "))

    stack = filterList(s)    

    final = []

    final.append(stack[-1])
    for i in range(1, len(stack)-1):
        final.append(stack[i])
    
    final.append(stack[0])



    print(''.join(final))


main()
