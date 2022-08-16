def longest_word(text):
    word = text.split()
    longestWord = "0"
    if len(word):
        for i in word:
            if len(i) > len(longestWord):
                longestWord = i
    else:
        longestWord = None
    
    return longestWord
        