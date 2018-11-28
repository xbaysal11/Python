def playGame(wordList):
    
    
    hand = []
    while True:
        user_choice = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if(user_choice == 'r' and len(hand) == 0):
            print('You have not played a hand yet. Please play a new hand first!')
        elif user_choice == 'e':
            break
        elif user_choice == 'n' or (user_choice =='r' and len(hand) != 0):
            user_or_comp = raw_input('Enter u to have yourself play, c to have the computer play: ')
            while(user_or_comp != 'u' and user_or_comp != 'c'):
                print('Invalid command.')
                user_or_comp = raw_input('Enter u to have yourself play, c to have the computer play: ')
            if user_choice == 'n':
                hand = dealHand(HAND_SIZE)
            if user_or_comp == 'u':
                playHand(hand, wordList, HAND_SIZE)
            elif user_or_comp == 'c':
                compPlayHand(hand, wordList, HAND_SIZE)
        else:
            print('Invalid command.')
