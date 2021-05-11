import time, random
from random import randint
#name = input('enter your name ')
def printlanes(content1, content2, content3, content4, content5, content6):
    print('-'*125),print(content6), print(content6), print(('-'*125)+'\n\n'+ ('-'*125)),print(content5), print(content5), print(('-'*125)+'\n\n'+ ('-'*125)),print(content4), print(content4), print(('-'*125)+'\n\n'+ ('-'*125)),print(content3), print(content3),print(('-'*125)+'\n\n'+ ('-'*125)),print(content2), print(content2), print(('-'*125)+'\n\n'+ ('-'*125)),print(content1), print(content1), print('-'*125)
def refreshlanecontent(newcontent, lanecontent):
    global lost
    numtoadd = randint(0,2)
    lanecontent = str(lanecontent)
    dellanes = (-1 * numtoadd) - 1 
    savecontent = lanecontent[0:dellanes]
    lanecontent = (numtoadd * ' ') + newcontent + savecontent
    if '(' in lanecontent:
        if lanecontent[64] != ' ' or lanecontent[65] != ' ':
            lost = True
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
inlane = 1
lost = False
spaces = str(' '*125)
counter = 0
lane1, lane2, lane3, lane4, lane5, lane6 =  spaces, spaces, spaces, spaces, spaces, spaces
printlanes(lane1,lane2,lane3,lane4,lane5,lane6)
#randomly generating part ahead
while True:
    try:
        randomizer = randint(1,7)
        add1,add2,add3,add4,add5,add6 = ' ',' ',' ',' ',' ',' '
        if randomizer == 1:
            add1 = '<'
        if randomizer == 2:
            add2 = '#'
        if randomizer == 3:
            add3 = '$'
        if randomizer == 4:
            add4 = '>'
        if randomizer == 5:
            add5 = '?'
        if randomizer == 6:
            add6 = '='
        lane1, lane2, lane3, lane4, lane5, lane6 = refreshlanecontent(add1,lane1), refreshlanecontent(add2,lane2), refreshlanecontent(add3,lane3), refreshlanecontent(add4,lane4), refreshlanecontent(add5,lane5), refreshlanecontent(add6,lane6)
        if counter >= 64:
            printlanes(lane1,lane2,lane3,lane4,lane5,lane6)
            if inlane == 1: 
                print(' ' * 65, ' (--)\n',' ' * 65,'(--)')
            else:
                print('\n')
            time.sleep(0.15)
        if lost == True:
            break
        counter += 3
    except(KeyboardInterrupt, SystemExit):
        #move foreward
        if inlane == 6:
            inlane += 1
            lane6 = addguytolanecontent(lane6)
            lane5 = removeguyfromlane(lane5)
        if inlane == 5:
            inlane += 1
            lane5 = addguytolanecontent(lane5)
            lane4 = removeguyfromlane(lane4)
        if inlane == 4:
            inlane += 1
            lane4 = addguytolanecontent(lane4)
            lane3 = removeguyfromlane(lane3)
        if inlane == 3:
            inlane += 1
            lane3 = addguytolanecontent(lane3)
            lane2 = removeguyfromlane(lane2)
        if inlane == 2:
            inlane += 1
            lane2 = addguytolanecontent(lane2)
            lane1 = removeguyfromlane(lane1)
        if inlane == 1:
            inlane += 1
            lane1 = addguytolanecontent(lane1)
print('you have lost')
#highscore board
