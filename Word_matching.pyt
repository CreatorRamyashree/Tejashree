def match_words(words):
    ctr = 0
    lst = []      
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("List of words with first and last character same: ", lst)
    return ctr
count = match_words(["abc", "cfc", "mom", "dad", "876", "242", "Teja"])
print("Number of that have the same first and last character are:", count)