import random as rand

participants = int(input('Enter the number of participants: '))
max_winners = int(input('Select # of winners: '))

not_participate = []
n = int(input("Select # of non participants: "))

for i in range(0, n):
    nonpart = int(input('Enter each NON participants: '))
 
    not_participate.append(nonpart)
     
print('Non participants are ',not_participate)

if max_winners <= participants:
    winners = []
    while len(winners) < max_winners:
        pick = rand.randint(1,participants)
        if (pick not in winners) and (pick not in not_participate):
            winners.append(pick)
    print('The winner/s is/are: ', winners)
else:
    pass
