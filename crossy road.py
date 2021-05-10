import time
#name = input('enter your name ')
def printlanes(content1, content2, content3, content4, content5, content6):
    print(('-'*125)+'\n'),print(content6), print(content6), print('\n' + ('-'*125)+'\n'),print(content5), print(content5), print('\n' + ('-'*125)+'\n'),print(content4), print(content4), print('\n' + ('-'*125)+'\n'),print(content3), print(content3), print('\n' + ('-'*125)+'\n'),print(content2), print(content2), print('\n' + ('-'*125)+'\n'),print(content1), print(content1), print('\n' + ('-'*125))
def refreshlanecontent(newcontent, lanecontent):
    lanecontent = str(lanecontent)
    savecontent = lanecontent[0:-2]
    lanecontent = '  ' + newcontent + savecontent
    return lanecontent
print(6 * ('\n\n\n\n'+('-'*125)))
spaces = str(' '*125)
lane1, lane2, lane3, lane4, lane5, lane6 =  spaces, spaces, spaces, spaces, spaces, spaces
printlanes(lane1,lane2,lane3,lane4,lane5,lane6)
lane1 = refreshlanecontent('o',lane1)
time.sleep(0.5)
printlanes(lane1,lane2,lane3,lane4,lane5,lane6)
lane1 = refreshlanecontent(' ',lane1)
time.sleep(0.5)
printlanes(lane1,lane2,lane3,lane4,lane5,lane6)
lane1, lane2 = refreshlanecontent(' ',lane1), refreshlanecontent('o',lane2)
time.sleep(0.5)
i = 0
while i <= 30:
    lane1, lane2 = refreshlanecontent(' ',lane1), refreshlanecontent(' ',lane2)
    time.sleep(0.5)
    i += 1

