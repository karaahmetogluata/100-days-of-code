import random
import art
print(art.logo)
print("Welcome to the game")
numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

elimdeki_kartlar1 = []
kurpiyer_kartlar1 = []
def elimdeki_kartlar():
    hand1 = random.choice(numbers)
    hand2 = random.choice(numbers)
    elimdeki_kartlar1.append(hand1)
    elimdeki_kartlar1.append(hand2)


    total = sum(elimdeki_kartlar1)
    if 11 in elimdeki_kartlar1 and sum(elimdeki_kartlar1)> 21:
        elimdeki_kartlar1.remove(11)
        elimdeki_kartlar1.append(1)
    print(f"your hand is :{hand1} and {hand2} \ntotal:{total}")
    return total
def kurpiyer_kartlar():
    hand3 = random.choice(numbers)
    kurpiyer_kartlar1.append(hand3)
    total2 = sum(kurpiyer_kartlar1)
    if 11 in kurpiyer_kartlar1 and sum(kurpiyer_kartlar1)> 21:
        kurpiyer_kartlar1.remove(11)
        kurpiyer_kartlar1.append(1)

    print(f"dealer hand is :{hand3}  \ntotal:{total2}")
    return total2
#GAMEİN PHASE
elimdeki_kartlar()
kurpiyer_kartlar()
while sum(elimdeki_kartlar1)<21:
    go_or_no = (input("Do you want more cards? Yes or no\n"))
    if go_or_no == "yes":
        elimdeki_kartlar1.append(random.choice(numbers))
        if 11 in elimdeki_kartlar1 and sum(elimdeki_kartlar1) > 21:
            elimdeki_kartlar1.remove(11)
            elimdeki_kartlar1.append(1)
        if sum(elimdeki_kartlar1)> 21:
            print(f"You losed {elimdeki_kartlar1} more than 21")
            break
        print(f"your current hand is :{elimdeki_kartlar1} \ntotal:{sum(elimdeki_kartlar1)}")
    elif go_or_no == "no":
        while sum(kurpiyer_kartlar1) < 17:
            kurpiyer_kartlar1.append(random.choice(numbers))
            if 11 in kurpiyer_kartlar1 and sum(kurpiyer_kartlar1) > 21:
                kurpiyer_kartlar1.remove(11)
                kurpiyer_kartlar1.append(1)
            print(f"dealer drew. dealer hand: {kurpiyer_kartlar1} total: {sum(kurpiyer_kartlar1)}")



        break


if sum(kurpiyer_kartlar1) > 21:
    print(f"Dealer busted! You win!!! Your hand: {sum(elimdeki_kartlar1)} Dealer hand: {sum(kurpiyer_kartlar1)}")
elif sum(elimdeki_kartlar1) == sum(kurpiyer_kartlar1):
    print(f"Draw! Your hand: {sum(elimdeki_kartlar1)} and dealer hand is: {sum(kurpiyer_kartlar1)}")
elif sum(elimdeki_kartlar1)>sum(kurpiyer_kartlar1):
    print(f"You win!!! your hand is :{elimdeki_kartlar1} and dealer hand is :{kurpiyer_kartlar1}")
else:
    print(f"You lose!!!your hand is :{elimdeki_kartlar1} and dealer hand is :{kurpiyer_kartlar1}")