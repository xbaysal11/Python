def playGame(wordList):
   
    hand = []
    while True:
        user_choice = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if user_choice == 'e':
            break
        else:
            if user_choice == 'n':
                hand = dealHand(HAND_SIZE)
                playHand(hand, wordList, HAND_SIZE)
            elif user_choice == 'r' and len(hand) != 0:
                playHand(hand, wordList, HAND_SIZE)
            elif user_choice == 'r':
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                print('Invalid command.')