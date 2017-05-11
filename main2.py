import code

def Intro():
    display='''
------------------------------------------
|Welcome to bat counter. Here is your key
|N- New batter
|I- New inning
|S- Strike
|B- Ball
|Q- Base1
|W- Base2
|E- Base3
|R- Base4
|O- Out
-------------------------------------------
                                           '''.format()
    print(display)                                          

def Hitboard(n,i, Strikecount, Ballcount, Strikeoutcount, Walkedcount, base1count,base2count,base3count,base4count):
    display='''
--------------------------
|Batter Name:{0}
|Inning:{1}
|
|Strikes:{2}
|Balls:{3}
|
|Strike outs:{4}
|Walkes:{5}
|
|base1:{6}
|base2:{7}
|base3:{8}
|base4:{9}
--------------------------
                          '''.format(n,i, Strikecount, Ballcount, Strikeoutcount, Walkedcount, base1count,base2count,base3count,base4count)
    print(display)

Strikecount = 0
Ballcount = 0
Strikeoutcount = 0
Walkedcount = 0
base1count = 0
base2count = 0
base3count = 0
base4count = 0
outcount = 0


Intro()
key =code.guffyInput()
key =str(key)
while(key != "n"):
    print("press -N- to enter new Batter")
    key =code.guffyInput()
    key =str(key)
n =raw_input ("what is the Batters name?")
i =raw_input("What inning is it?  ")
print(n + " is batting the " + i + " inning")

choise =code.guffyInput()
while(choise != "o" or choise != "n" or choise != "s" or choise != "b" or choise != "q" or choise != "w" or choise != "e" or choise != "r"):
    
    choise =code.guffyInput()
    
    if(choise == "s"):
        print("Strike")
        Strikecount +=1
        if(Strikecount == 3):
            print("batter is out")
            Strikeoutcount += 1
            Hitboard(n,i, Strikecount, Ballcount,Strikeoutcount, Walkedcount, base1count,base2count,base3count,base4count)
            Strikecount = 0
            Ballcount = 0
            Strikeoutcount = 0
            Walkedcount = 0
            base1count = 0
            base2count = 0
            base3count = 0
            base4count = 0
            outcount += 1
            n =raw_input ("what is the Batters name?")
            print(n + " is up to bat")
    if(choise == "b"):
        print("Ball")
        Ballcount += 1
        if(Ballcount == 4):
            print("batter walked")
            Walkedcount += 1
            Hitboard(n,i, Strikecount, Ballcount,Strikeoutcount, Walkedcount, base1count,base2count,base3count,base4count)
            Strikecount = 0
            Ballcount = 0
            Strikeoutcount = 0
            Walkedcount = 0
            base1count = 0
            base2count = 0
            base3count = 0
            base4count = 0
            n =raw_input ("what is the Batters name?")
            print(n + " is up to bat")

        if(choise == "o"):
            print("batter is out")
            outcount += 1
        if(outcount == 3):
	        Hitboard(n,i, Strikecount, Ballcount,Strikeoutcount, Walkedcount, base1count,base2count,base3count,base4count)
	        n =raw_input("what is the batters name?  ")
	        i =raw_input("What inning is it?")
	        print(n + " is batting the " + i + " inning")
	        Strikecount = 0
	        Ballcount = 0
	        Strikeoutcount = 0
	        Walkedcount = 0
	        base1count = 0
	        base2count = 0
	        base3count = 0
	        base4count = 0
    
    if(choise == "n"):
        Hitboard(n,i, Strikecount, Ballcount,Strikeoutcount, Walkedcount, base1count,base2count,base3count,base4count)
        n =raw_input("what is the batters name?  ")
        i =raw_input("What inning is it?")
        print(n + " is batting the " + i + " inning")
        Strikecount = 0
        Ballcount = 0
        Strikeoutcount = 0
        Walkedcount = 0
        base1count = 0
        base2count = 0
        base3count = 0
        base4count = 0


    if(choise == "q"):
        print("batter made it to 1st base")
        base1count += 1
        Hitboard(n,i, Strikecount, Ballcount,Strikeoutcount, Walkedcount, base1count,base2count,base3count,base4count)
        Strikecount = 0
        Ballcount = 0
        Strikeoutcount = 0
        Walkedcount = 0
        base1count = 0
        base2count = 0
        base3count = 0
        base4count = 0
        n =raw_input ("what is the Batters name?")
        print(n + " is up to bat")
    
    if(choise == "w"):
        print("batter made it to 2nd base")
        base2count += 1
        Hitboard(n,i, Strikecount, Ballcount,Strikeoutcount, Walkedcount, base1count,base2count,base3count,base4count)
        Strikecount = 0
        Ballcount = 0
        Strikeoutcount = 0
        Walkedcount = 0
        base1count = 0
        base2count = 0
        base3count = 0
        base4count = 0
        n =raw_input ("what is the Batters name?")
        print(n + " is up to bat")
    
    if(choise == "e"):
        print("batter made it to 3rd base")
        base3count += 1
        Hitboard(n,i, Strikecount, Ballcount,Strikeoutcount, Walkedcount, base1count,base2count,base3count,base4count)
        Strikecount = 0
        Ballcount = 0
        Strikeoutcount = 0
        Walkedcount = 0
        base1count = 0
        base2count = 0
        base3count = 0
        base4count = 0
        n =raw_input ("what is the Batters name?")
        print(n + " is up to bat")
    
    if(choise == "r"):
        print("batter scored")
        base4count += 1
        Hitboard(n,i, Strikecount, Ballcount,Strikeoutcount, Walkedcount, base1count,base2count,base3count,base4count)
        Strikecount = 0
        Ballcount = 0
        Strikeoutcount = 0
        Walkedcount = 0
        base1count = 0
        base2count = 0
        base3count = 0
        base4count = 0
        n =raw_input ("what is the Batters name?")
        print(n + " is up to bat")
