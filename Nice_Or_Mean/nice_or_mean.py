#
#Python 3.9.7
##
## Author: Daniel A. Christie (Of the project that I am receating)
##
## Alterations to the original code done by Jordan Arnold
##
## purpose: tech academy assignment. First guided program.



def begin(nicePerson=0, meanPerson=0, theName=""):
    #Getting the user's name
    theName = describe_theGame(theName)
    nicePerson, meanPerson, theName = nice_mean(nicePerson, meanPerson, theName)




def describe_theGame(theName):
    '''
        Checks whether or not it is a new game.
        If so, th euser's name will be retrieved.
        If not, the player will be thanked for playing again.

    '''
    #If we do not already have the user's name, then it is a new player and we need to get their name
    if theName != "":
        print('Thank you for playing again, {}!'.format(theName))
    else:
        stop = True
        while stop:
            if theName == "":
                theName = input('What is you name, little fella?\n~~~>'.capitalize())
                if theName != "":
                    print('\nWelcome, {}!'.format(theName))
                    print('\n In this game, you will be greeted \nby several different people. \nYou can choose to either be nice, or mean.')
                    print('But at the end of this game, \nyour fate will be sealed by your actions.')
                    stop = False
                
    return theName



def nice_mean(nicePerson, meanPerson, theName):
    stop = True
    while stop:
        show_theScore(nicePerson, meanPerson, theName)
        pick = input('\nA person approaches you and offers a pineapple. \nwill you be\nNice, or mean? \nS(N/M) \n~~~>)'.lower())
        if pick =="n":
            print('\nThe stranger decides you are his role model')
            nicePerson = (nicePerson + 1)
            stop = False
        if pick == "m":
            print('\n He throws the pineapple at your head and disappears')
            meanPerson = (meanPerson + 1)
            stop = False
    theScore(nicePerson, meanPerson, theName) #This is passing the updated score values to the 'score' function



def show_theScore(nicePerson, meanPerson, theName):
    print('\n{}, your current score total is: \nNice: {} \nMean: {}'.format(theName, nicePerson, meanPerson))


def theScore(nicePerson, meanPerson, theName):
    #This function is being passed the values stored within those values
    if nicePerson > 2:  #If this condition is valid, The winner function is called with the variables passed into it
        winner(nicePerson, meanPerson, theName)
    if meanPerson > 2:  #If this condition is valid, The loser function is called with the variables passed into it
        loser(nicePerson, meanPerson, theName)
    else:
        nice_mean(nicePerson, meanPerson, theName)


def winner(nicePerson, meanPerson,theName):
    #wildcards are substituted with the values within 'format'

    print('Congragulations, {}!\n You won the game. The world is in awe. Endorsement offers hitting your mailbox. \nPotential fake friends lining up at you door\nto visit a 5 star resturaunt while they conveniently forget their wallets'.format(theName))
    #calls the 'again' function and passes in the variables
    again(nicePerson, meanPerson, theName)


def loser(nicePerson, meanPerson, theName):
    #wildcards are substituted with the values within 'format'
    print("Darn it {},\nIt looks like you're mean. Better luck next time".format(theName))
    #calls up 'again' function and passes in the variables
    again(nicePerson, meanPerson, theName)


def again(nicePerson, meanPerson, theName):
    stop = True
    while stop:
        choice = input('\n Want to play again? (y/n) \n~~~>'.lower())
        if choice == "y":
            stop = False
            reset(nicePerson, meanPerson, theName)
        if choice == "n":
            print('\nWhatever.')
            stop = False
            quit()
        else:
            print('\nEnter ( Y ) for "YES", or ( N ) for "NO" \n~~~>')


def reset(nicePerson, meanPerson, theName):
        nicePerson = 0
        meanPerson = 0
        #The name wasn't reset in this case, because the same user wanted to play again
        begin(nicePerson, meanPerson, theName)
        
        


if __name__ == '__main__':
    begin()
