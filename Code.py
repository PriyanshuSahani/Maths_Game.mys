gc = int(input("Group Count = "))
L = []
M = []
asc = ord('A')
print('You have been divided into groups : ',end = " ")
for i in range (gc):
    ch =  chr(asc+i)
    print(ch,end = '  ')
    L.append(str(ch))
    M.append(0)
    
print('\nWelcome to the game.')
def q1(gc):
    print('1) What is the square of 92 ?')
    l = [8464,8624,8484,8814]
    for j in range (4):
        print(j+1,".  ",l[j],end = '       ')
    print()
def q2(gc):
    print('2) Solve 25 + 25 * 25 - 25 / 25 ?')
    l = [124,544,649,624]
    for j in range (4):
        print(j+1,".  ",l[j],end = '       ')
    print()
def q3(gc):
    print('3) What is the next term in the series :  10 100 11 121 12 144 13 ?')
    l = [176,333,153,169]
    for j in range (4):
        print(j+1,".  ",l[j],end = '       ')
    print()
def q4(gc):
    print('4) Which of the following is not a meaningless term ? ')
    l = ['1/(1/0)','0/0','1/0 - 1/0','(1/0)*(1/0)']
    for j in range (4):
        print(j+1,".  ",l[j],end = '       ')
    print()
def q5(gc):
    print('5) What is the next number in the series :  28 , 30 , 34 , 42 , 58 ,')
    l = [90,84,96,80]
    for j in range (4):
        print(j+1,".  ",l[j],end = '       ')
    print()
def q6(gc):
    print('6) If two vertices of triangle are (1,-3) & (2,0) and the centroid coincides with origin,then the third vertex is:')
    l = ['(1,0)','-3,3','(0,3)','(-3/2,3/2)']
    for j in range (4):
        print(j+1,".  ",l[j],end = '       ')
    print()
def q7(gc):
    print('7) 2x + 4y + 2 = 0   ,    8x + 3y - 18 = 0 \n    Find x & y.')
    l = ['2,-5','3,-2','2,-2','9,-1']
    for j in range (4):
        print(j+1,".  ",l[j],end = '       ')
    print()
def q8(gc):
    print('8) If 17th and 18th terms of an A.P. are 9 and 21 respectively.Find the sum of first 34 terms.')
    l = [484,862,510,630]
    for j in range (4):
        print(j+1,".  ",l[j],end = '       ')
    print()
def q9(gc):
    print('9) If three vertices of a parallelogram are : (-3, -17, 1) (-4, 8, 20) (-10, 19, 12) respectively , then find the coordinates of fourth')
    l = ['9,6,7','-9,-6,-7','5,-7,-21','-1,0,5']
    for j in range (4):
        print(j+1,".  ",l[j],end = '       ')
    print()
def q10(gc):
    print('10) From origin, 8 line segments are drawn such that x,y & z coordinates of any point on the line segments are equal  in magnitute (such that we get a cube by joining their ends). What is the volume of the cube hence formed if length of each line segment is root of 3 (i.e. 3^(1/2) ?')
    l = ['8','9','9^(2/3)','3*3^(1/2)']
    for j in range (4):
        print(j+1,".  ",l[j],end = '       ')
    print()
q = 'q1(gc)','q2(gc)','q3(gc)','q4(gc)','q5(gc)','q6(gc)','q7(gc)','q8(gc)','q9(gc)','q10(gc)'
key = '1','3','4','1','1','2','2','3','2','1'
for i in range (10):
    print(eval(q[i]))
    for k in range(2):
        buzz = input('Buzz  ')
        o = input('Answer - ')
        if o == key[i]:
            if i<3:
                M[ord(buzz)-65] += 10
                break
            elif i<7:
                M[ord(buzz)-65] += 30
                break
            else:
                M[ord(buzz)-65] += 50
                break
    print()

print('POINTS TABLE')        
for m in range (gc):
    print(L[m],'-' ,M[m])
y = 0
z = ''
for x in range(gc):
    if M[x]>y:
        y = M[x]
        z = L[x]
print('Congratulations Team ',z)
