import time, random
from random import randint
def clearscreen(): 
    print('\n' * 50)
clearscreen()
print('Crossy Road'), print('___________\n\n'), print('How to play'), print(' 1. Press control+c to move foreward'), print(' 2. When you hit an obstacle the game will end\n\n'), print(' Select a level\n'), print(' Easy * Medium * Hard * Very hard * Xpert')
level = input('\n Type the first letter of your choice ')
level = level.lower()
level = 'Easy' if 'e' in level else ('Medium' if 'm' in level else ('Hard' if 'h' in level else ('Very hard' if 'v' in level else ('Xpert'))))
level = level.lower()
waittime = 0.33 if 'easy' in level else (0.25 if 'medium' in level else (0.2 if 'hard' in level else (0.15 if 'very hard' in level else (0.12))))
clearscreen(), print('Crossy Road')
print('___________\n\n'), print('How to play'), print(' 1. Press control+c to move foreward'), print(' 2. When you hit an obstacle the game will end\n\n'), print(' Level: ', level), print(' \n')
name = input('Enter your name ')
def printlanes(content1, b1, content2, b2, content3, b3):
    print('-'*125,'\n\n'), print('-'*125),print(content3), print(content3),print('-'*125),print(b2),print(b2),print('-'*125),print(content2), print(content2), print('-'*125),print(b1),print(b1),print('-'*125),print(content1), print(content1), print('-'*125),print(b3),print(b3),print('-'*125)
def refreshlanecontent(newcontent, lanecontent):
    global lost
    numtoadd = randint(0,2)
    lanecontent = str(lanecontent)
    dellanes = (-1 * numtoadd) - 1 
    savecontent = lanecontent[0:dellanes]
    lanecontent = (numtoadd * ' ') + newcontent + savecontent
    if '(' in lanecontent:
        try:
            if lanecontent[64] != ' ' or lanecontent[65] != ' ':
                lost = True
        except:
            blank = ''
        lanecontent = removeguyfromlane(lanecontent)
        lanecontent = addguytolanecontent(lanecontent)
    return lanecontent
def removeguyfromlane(lanecontent):
    lane = lanecontent.replace('(--)','')
    return lane
def addguytolanecontent(lanecontent):
    firstpart = lanecontent[0:65]
    secondpart = lanecontent[65:]
    final = firstpart + '(--)' + secondpart
    return final
print(12 * ('\n\n'+('-'*125)))
inlane = 0
score = 110
one = True
lost = False
spaces = str(' '*125)
counter = 0
lanerender = 1
b1,b2,b3 = str(' '*65), str(' '*65), (str(' '*65)+ '(--)')
lane1, lane2, lane3, lane4, lane5, lane6 =  spaces, spaces, spaces, spaces, spaces, spaces
printlanes(lane1,lane2,lane3,'','','')
#randomly generating part ahead
while True:
    try:
        randomizer = randint(1,6)
        rand = randint(1,14)
        rand = '=' if rand == 1 else ('?' if rand == 2 else ('$' if rand == 3 else ('<>' if rand == 4 else ('|' if rand == 5 else ('-' if rand == 6 else ('+' if rand == 7 else ('W' if rand == 8 else ('<' if rand == 9 else ('~' if rand == 10 else ('{' if rand == 11 else ('[' if rand == 12 else ('!' if rand == 13 else 'K'))))))))))))
        add1,add2,add3,add4,add5 = ' ',' ',' ',' ',' '
        if randomizer == 1:
            add1 = rand
            add2 = rand
            if waittime == 0.2:
                add3 = rand
                if waittime == 0.12:
                    add4 = rand 
        if randomizer == 2:
            add2 = rand
            add3 = rand
            if waittime == 0.15:
                add4 = rand
        if randomizer == 3:
            add3 = rand
            add4 = rand
            if waittime == 0.12:
                add1 = rand
        lane1, lane2, lane3= refreshlanecontent(add1,lane1), refreshlanecontent(add2,lane2), refreshlanecontent(add3,lane3)
        if counter >= 60:
            if lanerender == 1:
                printlanes(lane1, b1, lane2, b2, lane3, b3)
            elif lanerender == 'b1':
                printlanes(b1, lane2, b2, lane3, b3, lane1)
            elif lanerender == 2:
                printlanes(lane2, b2, lane3, b3, lane1, b1)
            elif lanerender == 'b2':
                printlanes(b2, lane3, b3, lane1, b1, lane2)
            elif lanerender == 3:
                printlanes(lane3, b3, lane1, b1, lane2, b2)
            elif lanerender == 'b3':
                printlanes(b3, lane1, b1, lane2, b2, lane3) 
            print('Score, inlane: ', inlane)
            print(score)
            time.sleep(waittime)
        if score <= 0:
            lost == True
            print('You have run out of time')
            break
        if lost == True:
            break
        counter += 1
        score -= 1
    except(KeyboardInterrupt, SystemExit):
        #move foreward
        if inlane == 0:
            inlane += 1
            b3 = removeguyfromlane(b3)
            lane1 = addguytolanecontent(lane1)
            lanerender = 1
            #input('done')
        elif inlane == 1:
            lanerender = 'b1'
            inlane += 1
            lane1 = removeguyfromlane(lane1)
            b1 = addguytolanecontent(b1)
        elif inlane == 2:
            lanerender = 2
            inlane += 1
            b1 = removeguyfromlane(b1)
            lane2 = addguytolanecontent(lane2)
        elif inlane == 3:
            lanerender = 'b2'
            inlane += 1
            lane2 = removeguyfromlane(lane2)
            b2 = addguytolanecontent(b2)
        elif inlane == 4:
            lanerender = 3
            inlane += 1
            b2 = removeguyfromlane(b2)
            lane3 = addguytolanecontent(lane3)
        elif inlane == 5:
            lanerender = 'b3'
            lane3 = removeguyfromlane(lane3)
            b3 = addguytolanecontent(b3)
            inlane += 1
        elif inlane == 6:
            lanerender = 1
            inlane = 1
            b3 = removeguyfromlane(b3)
        score += 100
print('you have lost')
print('your score was ', round(score,0))
#highscore board

