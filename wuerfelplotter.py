from functools import lru_cache
import matplotlib.pyplot as plt



#von Stackoverflow geklaut....shame on me

while True:
    rolls = input("How many rolls? ")
    if rolls.isdigit():
        break
    print("Please input only integers!")
while True:
    sides = input("How many sides? ")
    if sides.isdigit():
        break
    print("Please input only integers!")

print(f"You are going to simulate a {rolls}d{sides} roll!")
while True:
    playersum = input("What is your sum? ")
    if playersum.isdigit():
        break
    print("Please input only integers!")
sides = int(sides)
rolls = int(rolls)
playersum = int(playersum)

values = {}
@lru_cache(None)
def sum_freq(total, rolls, faces):
    if not rolls:
        return not total
    return sum(sum_freq(total - die, rolls - 1, faces)
               for die in range(1, faces + 1))
def probability_calculator(roll_total, num_of_rolls, dice_faces):
    return sum_freq(roll_total, num_of_rolls, dice_faces)/ dice_faces ** num_of_rolls
for i in range(rolls,rolls*sides+1):
    values[i] = probability_calculator(i, rolls, sides)


xsum = []
yprobability = []

for i in values.keys():
    xsum.append(i)
    yprobability.append(values[i])

maximum = 0
listofmax = []
safe = 0
for i in range(len(yprobability)):
    if yprobability[i] >= maximum:
        maximum = round(yprobability[i],4)
        listofmax.append(maximum)
        safe = i



plt.plot(xsum,yprobability,"r+")

if listofmax[-1] != listofmax[-2]:
    plt.title(f"The highest probability is rolling a {xsum[safe]} with a probability of\n{maximum*100} %",
             color="#330000", family="serif", fontsize=8)

else:
    plt.title(f"The highest probabilities are for rolling {xsum[safe-1]} and {xsum[safe]} with a probability of\n{maximum*100} %"
,
        color="#330000", family="serif", fontsize=8)

plt.plot([playersum,playersum],[0, maximum])

plt.show()
