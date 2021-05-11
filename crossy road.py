import time, random
from random import randint
#name = input('enter your name ')
def printlanes(content1, content2, content3, content4, content5, content6):
    print(('-'*125)+'\n'),print(content6), print(content6), print('\n' + ('-'*125)+'\n'),print(content5), print(content5), print('\n' + ('-'*125)+'\n'),print(content4), print(content4), print('\n' + ('-'*125)+'\n'),print(content3), print(content3), print('\n' + ('-'*125)+'\n'),print(content2), print(content2), print('\n' + ('-'*125)+'\n'),print(content1), print(content1), print('\n' + ('-'*125))
def refreshlanecontent(newcontent, lanecontent):
    lanecontent = str(lanecontent)
    savecontent = lanecontent[0:-1]
    lanecontent = '' + newcontent + savecontent
    return lanecontent
print(6 * ('\n\n\n\n'+('-'*125)))
spaces = str(' '*125)
lane1, lane2, lane3, lane4, lane5, lane6 =  spaces, spaces, spaces, spaces, spaces, spaces
printlanes(lane1,lane2,lane3,lane4,lane5,lane6)
#randomly generating part ahead
try:
    while True:
        randomizer = randint(1,7)
        add1,add2,add3,add4,add5,add6 = ' ',' ',' ',' ',' ',' '
        if randomizer == 1:
            add1 = 'o'
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
        printlanes(lane1,lane2,lane3,lane4,lane5,lane6)
        time.sleep(0.15)
except(KeyboardInterrupt, SystemExit):
    #move foreward
    print('move')
