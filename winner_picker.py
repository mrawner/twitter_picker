import random as rand

participants = int(input('Select the number of participants: '))
max_winners = int(input('Select # of winners: '))

if max_winners <= participants:
    winners = []
    while len(winners) < max_winners:
        pick = rand.randint(1,participants)
        if pick not in winners:
            winners.append(pick)
    print('The winners are: ', winners)
else:
    pass
