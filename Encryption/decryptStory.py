#daniyarovbaysal
def decryptStory():

    """

    Using the methods you created in this problem set,

    decrypt the story given by the function getStoryString().

    Once you decrypt the message, be sure to include as a comment

    your decryption of the story.

    returns: string - story in plain text

    """
    def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    text = getStoryString()
    best = findBestShift(loadWords(), text)
    return applyShift(text, best)
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    
   
#s = applyShift('Hello, world!', 8)
#best = findBestShift(wordList, s)
#assert applyShift(s, best) == 'Hello, world!'
# To test decryptStory, comment the above four lines and uncomment this line:
try:
    text = 'Lmlqclqc umpbq: qgknjc pygj gqjylb dyrrcl qmjsrgml'
    print applyShift(text,findBestShift(wordList, text))
    print decryptStory()
except:
    print "All is ok"


	 	  	 	  	   	  	     	     	 	
