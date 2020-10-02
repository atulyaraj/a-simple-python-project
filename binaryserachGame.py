print("\*/"*1000)
print("\t\t\t\t\t\t\t\t\t\tWELCOME TO THE GAMING WORLD")
print("\tITS A SMALL GAME JUST DEVELOPED WHILE MY CREATOR ATULYA RAJ WAS STUDING ME")
name=input(("\tWhats Your Name User?"))
Gamename=input(f"\tWhat Should We Call You In The Game {name.upper()}?")
low=1
high=1000
print(f"Think Of any Number Between {low} and {high} ")
input("Now lets stars the game To start \n PRESS ENTER")
guess=1
count=1
while count<=10:
    guess=low+(high-low)//2
    high_low=input(f"MY GUESS IS {guess} IF I AM CORRECT THEN PRESS c , IF THE NUMBER IS HIGHER THAN MY GUESS THEN PRESS h,IF LOW THEN l")
    if high_low.upper()=="H":
        low=guess+1
        count+=1
    elif high_low.upper()=="L":
        high=guess
        count+=1
    elif high_low.upper()=="C":
        print(f"HEY I GUESSED IT IN {count} guesses I WON I ALWAYS DO YOU CANT BEAT ME")
        print(f"\t YOU CANT BEAT ME {Gamename}")
        break
    else:
        print("ENTER h,l or c" )
exper=input("How Was Your Experience:\n")
print(f"THAN YOU FOR THIS MESSAGE \n{exper}")

print("\*/"*1000)