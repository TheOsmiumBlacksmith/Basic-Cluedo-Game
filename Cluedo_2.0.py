#pylint:disable=W0312

### CLUEDO ###

from random import choice


################## Initial Data

# Create lists of data
people = [
"Green", 
"Mustard", 
"Peacock", 
"Plum", 
"Scarlett", 
"White"
]
rooms = [
"Ballroom", 
"Billiard Room", 
"Conservatory", 
"Dining Room", 
"Kitchen", 
"Hall", 
"Library", 
"Lounge", 
"Study"
]
weapons = [
"Candlestick", 
"Dagger", 
"Pipe", 
"Revolver", 
"Rope", 
"Wrench"
]


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

def div_():
    print ()
    print("...................................................................")
    print ()

def ask_(playing,S):
    print ()
    say_ (playing,
    "Was it {0} in the {1} with the {2}?".format(
    S[0],S[1],S[2]
    ))
    
# Final reveal of the answer
# in: -
# out: prints answer
def reveal_():
    print ()
    print (
    "It was {0} in the {1} with the {2}!".format(
    secrets[0],
    secrets[1],
    secrets[2]
    ))
    
def say_(playing,string):
    print ("{0}: '".format(playing.name)+string+"'")

################### Opperations


# deals every player's hand
def deal_():
    for p in players:
    	 # split into even hands
        for item in range(
        len(deck)//L
        ):
            # choose at random
            card = choice(total)
            # give to player
            
            p.hand.append(
            card
            )
            # take from total
            total.remove(card)
    if total != []:
        print("Leftover Cards: ",total)
    for x in players:
        if x.strat == bot_:
            x.hand.extend(total)


# tests if accusation is correct
# in: player (and accusation)
# out: -
def accuse_(playing):
    # if correct
    if playing.accuse != secrets:
        # dead
        playing.alive = False


# Tests if winning guess
# in: accuser
# out: win/lose
def winner_(accuser):
    # if player remains alive
    print()
    if (accuser.alive == True ):
        print (
        accuser.name+" Wins!"
        )
        return True
    else:
        print (
        accuser.name+" is Out!"
        )
        return False



#################### Strategies


# manual input strategy
# in: -
# out: -
def human_(action,query,playing):
    div_()
    # show hand
    print ("Your hand: ",playing.hand)
    # ask
    if action == "ask":
        # input requests
        a = str(input(
        "Person: "
        ))
        b = str(input(
        "Room: "
        ))
        c = str(input(
        "Weapon: "
        ))
        ask_(playing,[a,b,c])
        return [a,b,c]
    # respond
    elif action == "answer":
        return str(input("Response: "))
    # accuse?
    else:
        if str(input(
        "Accuse? ")) == "Yes":
            a = str(input(
            "Person: "
            ))
            b = str(input(
            "Room: "
            ))
            c = str(input(
            "Weapon: "
            ))
            ask_(playing,[a,b,c])
            return [a,b,c]
        else:
            return False


# CPU strategy
# in: -
# out: 
def bot_(action,query,playing):
    div_()
    if action == "ask":
        # make query
        question = [
        choice(a) for a in items
        ]
        ask_(playing,question)
        return question
    elif action == "answer":
        # answer query
        # if x from query 
        # in hand, show
        intersection = [i for i in query if i in playing.hand]
        if intersection == []:
            return "..."
        else:
            return choice(intersection)
    else:
        print("{0} Accuses".format(playing.name))
        # accuse?
        
        return False


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
        p = (p+1)%L
        
        # skip dead
        while (
        players[p].alive == False
        ):
            p = ((p+1)%
            L)
        
        # player
        div_()
        print ("<< It's {0}'s Turn >>".format(players[p].name))
        
        # ask
        guess = players[p].strat(
        "ask",[],players[p]
        )
        
        # loop query
        for q in range(L-1):
            # answer query
            person = (p+q+1)%L
            response = players[person].strat(
            "answer",guess,
            players[person]
            )
            say_(players[person],response)
            if response != "...":
                break
            
        
        # accuse?
        players[p].accuse = (
        players[p].strat(
        "accuse",
        [],
        players[p]
        ))
        
        if (
        players[p].accuse != False 
        ):
            # alive or dead?
            accuse_(players[p])
            # won or not?
            # breaks loop
            accuser = winner_(
            players[p]
            )


###################### Players

class player:
    def __init__(
    self,number,strat
    ):
        self.name = (
        "player {0}".format(
        number
        ))
        self.strat = strat
        self.alive = True
        self.accuse = False
        self.hand = []
          

p1 = player(1,human_)
p2 = player(2,human_)
p3 = player(3,human_)

# player array
players = [p1,p2,p3]
L = len(players)

###################### Main


def main():
    print ("--- CLUEDO ---")
    div_()
    reveal_()
    deal_()
    game_()
    div_()
    reveal_()



main()
