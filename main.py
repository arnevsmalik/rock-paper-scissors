import random
cs=0
ps=0
print("welcome to rock paper scissors made by Arnev S Malik\n")
rounds=int(input("enter no of rounds you want to play "))

tie="""
|||||||||||| |||||||||||| ||||||||||||
     ||           ||      ||
     ||           ||      |||||||||||
     ||           ||      ||
     ||      |||||||||||| ||||||||||||
 """
     
winn="""
|||             |||    ||||||||||||||   |||||    |||
 |||           |||           ||         ||| ||   |||
  |||   ||    |||            ||         |||  ||  |||
   ||| || || |||             ||         |||   || |||
    |||    |||         ||||||||||||||   |||    |||||
"""

loss="""
|||        |||||||||     ||||||||||   ||||||||||
|||       ||        ||  ||           ||
|||       ||        ||  ||||||||||   ||||||||||
|||       ||        ||           ||           || 
|||||||||  |||||||||    |||||||||||  |||||||||||
"""  
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

for i in range(1,rounds+1,1):
    player=int(input("enter 1 for rock, 2 for paper, 3 for scissors  "))
    comp=random.randint(1,3)
    if player==1:
        print("your choice is -\n")
        print(rock)
    elif player==2:
        print("your choice is -\n")
        print(paper)
    elif player==3:
        print("your choice is -\n")
        print(scissors)

    if comp==1:
        print("computer's choice is -\n")
        print(rock)
    elif comp==2:
        print("computer's choice is -\n")
        print(paper)
    elif comp==3:
        print("computer's choice is -\n")
        print(scissors)
        
    if comp==player:
        print("its a tie")
    elif comp==1 and player==3:
        print("you lost :(")
        cs+=1
    elif comp==2 and player==1:
        print("you lost:(")
        cs+=1
    elif comp==3 and player==2:
        print("you lost :(")
        cs+=1
    else:
        print("you won !")
        ps+=1


print (f"\nafter {rounds} round/rounds")
if cs == ps:
    print("it is a -")
    print(tie)
elif cs>ps:
    print("it is a -")
    print(loss)
else:
    print("it is a -")
    print(winn)