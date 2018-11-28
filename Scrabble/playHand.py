def playHand(hand, wordList, n):
       
    total_score = 0
    score = 0
    while calculateHandlen(hand) != 0:
        print 'Current Hand: ',
        displayHand(hand)
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        if word == '.':
            print('Goodbye! Total score: '+str(total_score))
            break
        else:  
            if(not(isValidWord(word, hand, wordList))):
                print('Invalid word, please try again.')
            else:
                score = getWordScore(word, n)
                total_score += score
                print(word+' earned '+str(score)+' points. Total: '+str(total_score)+' points')
                hand = updateHand(hand, word)
    if(word != '.'):
        print('Run out of letters. Total score: '+str(total_score))


