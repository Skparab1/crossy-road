import time
def clearscreen():
    print('\n'*50)
def addbird(line):
    line = '(0)>' + line
    return line
height = 10
adder = 0
line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = '                     |','                     |','                     |','                     |','                     |','                     |','                     |','          ','          ',' (0)>     ','          ','          ','          ','          ','          ','          ','          ','          '
while True:
    try:
        clearscreen()
        obstacleabove = ''
        linein = int(round(height))
        top = '\n' + obstacleabove
        print('-'*100)
        print(line18),print(line17),print(line16),print(line15),print(line14),print(line13),print(line12),print(line11),print(line10),print(line9),print(line8),print(line7),print(line6),print(line5),print(line4),print(line3),print(line2),print(line1)
        #removing bird fromlane content
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1.replace('(0)>',''), line2.replace('(0)>',''),line3.replace('(0)>',''),line4.replace('(0)>',''),line5.replace('(0)>',''),line6.replace('(0)>',''),line7.replace('(0)>',''),line8.replace('(0)>',''),line9.replace('(0)>',''),line10.replace('(0)>',''),line11.replace('(0)>',''),line12.replace('(0)>',''),line13.replace('(0)>',''),line14.replace('(0)>',''),line15.replace('(0)>',''),line16.replace('(0)>',''),line17.replace('(0)>',''),line18.replace('(0)>','')
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1[1:100],line2[1:100],line3[1:100],line4[1:100],line5[1:100],line6[1:100],line7[1:100],line8[1:100],line9[1:100],line10[1:100],line11[1:100],line12[1:100],line13[1:100],line14[1:100],line15[1:100],line16[1:100],line17[1:100],line18[1:100]
        height -= 0.5
        #print(height)
        print('-'*100)
        time.sleep(0.1)
        bird = '(0)>'
        linecontent = line1 if linein == 1 else (line2 if linein == 2 else (line3 if linein == 3 else (line4 if linein == 4 else (line5 if linein == 5 else (line6 if linein == 6 else (line7 if linein == 7 else (line8 if linein == 8 else (line9 if linein == 9 else (line10 if linein == 10 else (line11 if linein == 11 else (line12 if linein == 12 else (line12 if linein == 12 else (line13 if linein == 13 else (line14 if linein == 14 else (line15 if linein == 15 else (line16 if linein == 16 else (line17 if linein == 17 else line18)))))))))))))))))
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addbird(line1) if int(round(height,0)) == 1 else line1),(addbird(line2) if int(round(height,0)) == 2 else line2),(addbird(line3) if int(round(height,0)) == 3 else line3),(addbird(line4) if int(round(height,0)) == 4 else line4),(addbird(line5) if int(round(height,0)) == 5 else line5),(addbird(line6) if int(round(height,0)) == 6 else line6),(addbird(line7) if int(round(height,0)) == 7 else line7),(addbird(line8) if int(round(height,0)) == 8 else line8),(addbird(line9) if int(round(height,0)) == 9 else line9),(addbird(line10) if int(round(height,0)) == 10 else line10),(addbird(line11) if int(round(height,0)) == 11 else line11),(addbird(line12) if int(round(height,0)) == 12 else line12),(addbird(line13) if int(round(height,0)) == 13 else line13),(addbird(line14) if int(round(height,0)) == 14 else line14),(addbird(line15) if int(round(height,0)) == 15 else line15),(addbird(line16) if int(round(height,0)) == 16 else line16),(addbird(line17) if int(round(height,0)) == 17 else line17),(addbird(line18) if int(round(height,0)) == 18 else line18)
        try:
            if linecontent[4] == '|':
                break
        except:
            blank = ''
        if height <= 0:
            print('you have hit the ground')
            break
        if height >= 16:
            print('you have hit the ceiling')
            break
    except:
        height += 2
        time.sleep(0.1)
    finally:
        print('you have lost')