import socket
import math
import random


player1 = input('Enter Player 1 name here:')
player2 = input('Enter Player 2 name here:')
player3 = input('Enter Player 3 name here:')
player4 = input('Enter Player 4 name here:')

player1val = 0
player2val = 0
player3val = 0
player4val = 0

Hearts = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
Spades = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
Diamonds = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
Clubs = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

suites = ['hearts', 'spades', 'diamonds', 'clubs']
cards = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King'] 

cardvals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal():
    typeint = random.randint(0,3)
    cardint = random.randint(0,12)
        
    if typeint == 0:
        while True:
                if cardint > 12:
                    cardint = 0
                if Hearts[cardint] != '0':
                    break
                cardint = cardint + 1
        Hearts[cardint] = '0'
    elif typeint == 1:
        if Spades[cardint] == '0':
            while True:
                if cardint > 12:
                    cardint = 0
                if Spades[cardint] != '0':
                    break
                cardint = cardint + 1
        Spades[cardint] = '0'
    elif typeint == 2:
        if Diamonds[cardint] == '0':
            while True:
                if cardint > 12:
                    cardint = 0
                if Diamonds[cardint] != '0':
                    break
                cardint = cardint + 1
        Diamonds[cardint] = '0'
    elif typeint == 3:
        while True:
                if cardint > 12:
                    cardint = 0
                if Clubs[cardint] != '0':
                    break
                cardint = cardint + 1
        Clubs[cardint] = '0'

            
    card = cards[cardint]
    suit = suites[typeint]
    return card, suit, cardint       


def hit(currentval):
    playerval = 0
    while True:
        print(currentval)
        hit1 = input('What is your choice:')
        if hit1 == 'hit':
            d1, s1, d1int = deal()
            print('You got a ' + d1 +' of ' + s1)
            currentval = currentval + cardvals[d1int]
            playerval = playerval + cardvals[d1int]
            if d1int == 0:
                in2 = input('Would you like this to be 1 or 11?')
                if in2 == '1':
                    pass
                elif in2 == '11':
                    playerval = playerval + 10
                else:
                    print('Enter only 1 or 11 please')
            if currentval > 21:
                print('You lost.')
                return playerval
                break
            if currentval == 21:
                print('You won!')
                return playerval
                break
                    
        elif hit1 == 'stay':
            if currentval == 21:
                print('you won!!!!!!')
            return playerval
            break
        else:
            print('Please press either hit or stay!!!!!!!!!!!!!!')
            
p1c1, p1s1, p1c1int = deal()
p1c2, p1s2, p1c2int = deal()
p2c1, p2s1, p2c1int = deal()
p2c2, p2s2, p2c2int = deal()
p3c1, p3s1, p3c1int = deal()
p3c2, p3s2, p3c2int = deal()
p4c1, p4s1, p4c1int = deal()
p4c2, p4s2, p4c2int = deal() 

player1val = player1val + cardvals[p1c1int] + cardvals[p1c2int]
player2val = player2val + cardvals[p2c1int] + cardvals[p2c2int]
player3val = player3val + cardvals[p3c1int] + cardvals[p3c2int]
player4val = player4val + cardvals[p4c1int] + cardvals[p4c2int]

def check(val1, val2, val3, val4):
    if val1 == 21:
        print('player 1 wins!')
    elif val2 == 21:
        print('player 2 wins!')
    elif val3 == 21:
        print('player 3 wins!')
    elif val4 == 21:
        print('player 4 wins!')
    else:
        if val1 > 21:
            val1 = 0
        if val2 > 21:
            val2 = 0
        if val3 > 21:
            val3 = 0
        if val4 > 21:
            val4 = 0
        
        semi1 = False
        semi2 = False
        semi3 = False
        semi4 = False
        
        if val1 > val2:
            semi1 = True
        elif val2 > val1:
            semi2 = True
        
        if val3 > val4:
            semi3 = True
        elif val4 > val3:
            semi4 = True
            
        if semi1 == True:
            if semi3 == True:
                if val1 > val3:
                    print('Player 1 wins!')
                elif val3 > val1:
                    print('Player 3 wins!')
                else:
                    print('TIE')
                    
            elif semi4 == True:
                if val1 > val4:
                    print('Player 1 wins!')
                elif val4 > val1:
                    print('Player 4 wins!')
                else:
                    print('TIE')
                    
                    
        if semi2 == True:
            if semi3 == True:
                if val2 > val3:
                    print('Player 2 wins!')
                elif val3 > val2:
                    print('Player 3 wins!')
                else:
                    print('TIE')
                    
            elif semi4 == True:
                if val2 > val4:
                    print('Player 2 wins!')
                elif val4 > val2:
                    print('Player 4 wins!')
                else:
                    print('TIE')
                
            

        
            
        


print(player1 + ' cards: ' + p1c1 + ' of ' + p1s1 + ' and ' + p1c2 + ' of ' + p1s2)
print(player2 + ' cards: ' + p2c1 + ' of ' + p2s1 + ' and ' + p2c2 + ' of ' + p2s2)
print(player3 + ' cards: ' + p3c1 + ' of ' + p3s1 + ' and ' + p3c2 + ' of ' + p3s2)
print(player4 + ' cards: ' + p4c1 + ' of ' + p4s1 + ' and ' + p4c2 + ' of ' + p4s2)

if p1c1 == 'Ace' or p1c2 == 'Ace':
    print('Player 1 You got an ace! would you like it to be 1 or 11?')
    in3 = input()
    while True:
        if in3 == '1':
            break
        elif in3 == '11':
            player1val = player1val + 10
            break
        else:
            print('Try again bozo')

if p2c1 == 'Ace' or p2c2 == 'Ace':
    print('Player 2 You got an ace! would you like it to be 1 or 11?')
    in3 = input()
    while True:
        if in3 == '1':
            break
        elif in3 == '11':
            player2val = player2val + 10
            break
        else:
            print('Try again bozo')

if p3c1 == 'Ace' or p3c2 == 'Ace':
    print('Player 3 You got an ace! would you like it to be 1 or 11?')
    in3 = input()
    while True:
        if in3 == '1':
            break
        elif in3 == '11':
            player3val = player3val + 10
            break
        else:
            print('Try again bozo')
        
if p4c1 == 'Ace' or p4c2 == 'Ace':
    print('Player 4 You got an ace! would you like it to be 1 or 11?')
    in3 = input()
    while True:
        if in3 == '1':
            break
        elif in3 == '11':
            player4val = player4val + 10
            break
        else:
            print('Try again bozo') 
print('player 1 turn')
player1add = hit(player1val)
player1val = player1val + int(player1add)
print('Final value: ' + str(player1val))

print('player 2 turn')
player2add = hit(player2val)
player2val = player2val + int(player2add)
print('Final value: ' + str(player2val))

print('player 3 turn')
player3add = hit(player3val)
player3val = player3val + int(player3add)
print('Final value: ' + str(player3val))

print('player 4 turn')
player4add = hit(player4val)
player4val = player4val + int(player4add)
print('Final value: ' + str(player4val))

print(player1val)
print(player2val)
print(player3val)
print(player4val)

check(player1val, player2val, player3val, player4val)