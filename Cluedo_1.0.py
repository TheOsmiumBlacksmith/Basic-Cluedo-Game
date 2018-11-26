#pylint:disable=W0312

### CLUEDO ###

from random import choice


################## Initial Data

a = [1,2,3]
b = [1]
print (
[w for w in a if w in b]
)


# Create lists of data
people = [
"Green", 
"Mustard", 
"Peacock", 
"Plum", 
"Scarlett", 
"White"]
rooms = [
"Ballroom", 
"Billiard Room", 
"Conservatory", 
"Dining Room", 
"Kitchen", 
"Hall", 
"Library", 
"Lounge", 
"Study"]
weapons = [
"Candlestick", 
"Dagger", 
"Pipe", 
"Revolver", 
"Rope", 
"Wrench"]

# array of items
items = [
people, rooms, weapons
]
# the answer
secrets = [
choice(x) for x in items
]
# all items in one list
total = []
for u in items:
    for v in u:
    	# excludes answer
    	if v not in secrets:
            total.append(v)
# duplicate total for deal
deck = total[:]


####################### Speech

def ask_(S):
    print (
    "Was it " +
    S[0] +
    " in the " +
    S[1] +
    " with the " +
    S[2] +
    "?"
    )


################### Opperations


# deals every player's hand
def deal_():
    for player in players:
    	# split into even hands
        for item in range(
        len(total)/len(players)
        ):
            # choose at random
            card = choice(total)
            # give to player
            player[4].append(
            card
            )
            # take from total
            total.remove(card)


# tests if accusation is correct
# in: player (and accusation)
# out: -
def accuse_(player):
	# if correct
    if player[3] != secrets:
    	# alive = False
        player[2] = False


# Tests if winning guess
# in: accuser
# out: win/lose
def winner_(accuser):
	# if player remains alive
    if (accuser[2] == True ):
        print (
        accuser[0]+" Wins!"
        )
        return True
    else:
        print (
        accuser[0]+" is Out!"
        )
        return False


# Final reveal of the answer
# in: -
# out: prints answer
def reveal_():
    print
    print (
    "It was " + 
    secrets[0] + 
    " in the " + 
    secrets[1] + 
    " with the " + 
    secrets[2]
    )


#################### Strategies


# manual input strategy
# in: -
# out: -
def human_(action,query,hand):
	# show hand
    print (hand)
    if action == "ask":
        # input requests
        a = raw_input(
        "Person: "
        )
        b = raw_input(
        "Room: "
        )
        c = raw_input(
        "Weapon: "
        )
        ask_([a,b,c])
        return [a,b,c]
    elif action == "answer":
        ask_(query)
        show = 0 ###############
        return show
    else:
        # accuse?
        if raw_input(
        "Accuse? ") == "Yes":
            a = raw_input(
            "Person: "
            )
            b = raw_input(
            "Room: "
            )
            c = raw_input(
            "Weapon: "
            )
            ask_([a,b,c])
            return [a,b,c]
        else:
            return False


# CPU strategy
# in: -
# out: 
def bot_(action,query,hand):
    if action == "ask":
    	# make query
        return [
        choice(a) for a in items
        ]
    elif action == "answer":
        # answer query
        print (
        choice([i for i in query if i in hand]))
        # if x from query 
        # in hand, show
        return 0
    else:
        # accuse?
        
        return 0


####################### Game


# the main structure of the game
# in: -
# out: -
def game_():
    #each turn
    p = -1
    accuser = False
    # loop the game
    while accuser == False:
        # next player
        p = (p+1)%len(players)
        # skip dead
        while (
        players[p][2] == False
        ):
            p = ((p+1)%
            len(players))
        
        # ask
        guess = players[p][1](
        "ask",[],players[p][4]
        )
        # loop query
        for q in range(
        (p+1)%len(players),
        (p+3)%len(players)
        ):
            # answer query
            players[q][1](
            "answer",guess,
            players[p][4]
            )
        
        # accuse?
        players[p][3] = (
        players[p][1](
        "accuse",
        [],
        players[p][4]
        ))
        
        if (
        players[p][3] != False 
        ):
            # alive or dead?
            accuse_(players[p])
            # won or not?
            # breaks loop
            accuser = winner_(
            players[p]
            )


###################### Players


# = [
# name,func,alive,accuse,hand
# ]
p1 = [
"Player 1",human_,True,False,[]
]
p2 = [
"Player 2",bot_,True,False,[]
]
p3 = [
"Player 3",bot_,True,False,[]
]
# player array
players = [p1,p2,p3]

###################### Main


def main():
    print ("--- CLUEDO ---")
    reveal_()
    deal_()
    game_()
    reveal_()



main()
