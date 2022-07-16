def firstNonRepeatingCharacter(string):
    occurences = {}
    for i in string:
        if i not in occurences:
            occurences[i] = 1
        else:
            occurences[i] +=1
    for i in range(len(string)):
        if occurences[string[i]] == 1:
            for k, v in occurences.items():
                if v == 1:
                    return( "'" + k + "'" + " is the first non-repeating character." + 
                    "\n" + " It is the letter " + str(i+1) + " of the string") + "\n"

print(firstNonRepeatingCharacter("hhello"))
print(firstNonRepeatingCharacter("hello"))
print(firstNonRepeatingCharacter("AABBCCD"))
