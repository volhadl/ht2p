options = {
    'H': ['*   *', '*   *', '*****', '*   *', '*   *'],
    'E': ['*****', '*    ', '*****', '*    ', '*****'],
    'L': ['*    ', '*    ', '*    ', '*    ', '*****'],
    'O': [' *** ', '*   *', '*   *', '*   *', ' *** '],
    'W': ['*  *  *', '*  *  *', '*  *  *', '*  *  *', ' ** ** '],
    'R': ['**** ', '*  * ', '***  ', '*  * ', '*   *'],
    'D': ['**** ', '*   *', '*   *', '*   *', '**** '],
    ' ': ['     ', '     ', '     ', '     ', '     ']
}


def printSentence(text):
    for i in range(5):
        for j, _ in enumerate(text):
            print(options[text[j]][i], end="  ")
        print()


sentence = input("Enter sentence using 'h, e, l, o, w, r, d, ' '': ")

printSentence(list(sentence.upper()))
