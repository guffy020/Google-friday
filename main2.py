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
-------------------------------------------
                                           '''.format()
    print(display)                                          

def Hitboard():
    display='''
--------------------------
|Batter Name:{0}
|
|Strikes:{1}
|Balls:{2}
|
|Strike outs:{3}
|Walkes:{4}
|
|base1:{5}
|base2:{6}
|base3:{7}
|base4:{8}
--------------------------
                          '''.format()
    print(display)

Strikecount = 0
Ballcount = 0
Strikeoutcount = 0
Walkedcount = 0
base1count = 0
base2count = 0
base3count = 0
base4count = 0


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
while(choise != "n" or choise != "i" or choise != "s" or choise != "b" or choise != "q" or choise != "w" or choise != "e" or choise != "r"):
	
	choise =code.guffyInput()
	
	if(choise == "s")
	    print("Strike")
	    Strikecount +=1
        if(Strikecount == 3)
            print("batter is out")
            Strikeoutcount += 1

    if(choise == "b")
        print("Ball")
        Ballcount += 1
        if(Ballcount == 4)
            print("batter walked")
            Walkedcount += 1
