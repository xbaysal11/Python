def compChooseWord(hand, wordList, n):

    max_score = 0
    best_word = None
    for word in wordList:
        if(isValidWord(word, hand, wordList)):
            score = getWordScore(word, n)      
            if(score > max_score):
                max_score = score
                best_word = word
    return best_word
def compPlayHand(hand, wordList, n):

    total_score = 0
    score = 0
    while(calculateHandlen(hand) != 0):
        print 'Current Hand: ',
        displayHand(hand)
        word = compChooseWord(hand, wordList, n)
        if(word != None):
            score = getWordScore(word, n)
            total_score += score
            print('"'+word+'"'+' earned '+str(score)+' points. Total: '+str(total_score)+' points')
            print
            hand = updateHand(hand, word)      
        else:
            break
    print('Total score: '+str(total_score))

	 	  	 	  	   	  	     	     	 	
