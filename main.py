def scoreboard(pitcher,inning, pitches, Total, Strikeouts, Walked, Bock, Dead):
    display ='''
_________________________________
|                                
|Pitcher:{0}
|                                
|Inning number:{1}    
|
|Inning pitches:{2}
|                                
|Total pitch count:{3}                                
|                                
|Strikeouts:{4}    
|
|Walked:{5}   
|
|Bock:{6} 
|
|Dead Ball:{7}                    
_________________________________
                                 '''.format(pitcher, inning, pitches, Total, Strikeouts, Walked, Bock, Dead)
    print(display)

def Intro():
    display ='''
---------------------------------------------
|Welcometo baseball counter. Here is the key 
|
|N- New Pitcher
|I- New Inning
|P- New Pitch
|S- Batter Strike out
|W- Batter Walked
|Q- Display pitcher scoreboard
|D- Dead Ball
|--------------------------------------------
                                            '''.format()
    print(display)                                           



p=""
import code 
inningpitchcount = 1
totalpitchcount = 1
Strikeoutcount = 0
Walkedcount = 0
Bockcount = 0
Deadballcount = 0




Intro()
key =code.guffyInput()
key =str(key)
while(key != "n"):
    print("press -N- to enter new pitcher")
    key =code.guffyInput()
    key =str(key)
n =raw_input ("what is the pitches name?")
i =raw_input("What inning is it?  ")
print(n + " is pitching the " + i + " inning")
    
choise =code.guffyInput()
while(choise != "q" or choise != "b" or choise != "p" or choise != "i" or choise != "n" or choise != "s" or choise != "w" or choise != "d"):
    choise =code.guffyInput()
    if(choise == "p"):
        totalpitchcount += 1 
        print(totalpitchcount)
        inningpitchcount += 1
        if(totalpitchcount== 50):
            print(n + "has reached 50 pitches")
            if(totalpitchcount== 100):
                print(n + "has reached 100 pitches. You must take him out")
    if(choise == "s"):
        Strikeoutcount += 1
        print("Strike out")
    if(choise == "w"):
        Walkedcount += 1
        print("walked")
    if(choise == "q"):
    	scoreboard(n,i,inningpitchcount,totalpitchcount, Strikeoutcount, Walkedcount, Bockcount, Deadballcount)
    if(choise == "b"):
        print("Bock")
        Bockcount += 1
    if(choise == "d"):
        print("Dead ball")
        Deadballcount  += 1


    if(choise == "i"):
        scoreboard(n,i,inningpitchcount,totalpitchcount, Strikeoutcount, Walkedcount, Bockcount, Deadballcount)
        i =raw_input("What inning is it?   ")
        print(n + " is pitching the " + i + " inning")
        inningpitchcount = 1
        Strikeoutcount = 0
        Walkedcount = 0
        Bockcount = 0
        Deadballcount = 0
    if(Strikeoutcount == 3):
        scoreboard(n,i,inningpitchcount,totalpitchcount, Strikeoutcount, Walkedcount, Bockcount, Deadballcount)
        i =raw_input("What inning is it?   ")
        print(n + " is pitching the " + i + " inning") 
        Strikeoutcount = 0   
                   
    if(choise == "n"):
        scoreboard(n,i,inningpitchcount,totalpitchcount, Strikeoutcount, Walkedcount, Bockcount, Deadballcount)
        n =raw_input("what is the pitches name?  ")
        i =raw_input("What inning is it?")
        print(n + " is pitching the " + i + " inning")
        totalpitchcount = 0 
        inningpitchcount = 0
        Strikeoutcount = 0
        Walkedcount = 0
        Bockcount = 0
        Deadballcount = 0