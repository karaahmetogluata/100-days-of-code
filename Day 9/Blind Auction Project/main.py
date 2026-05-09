import art
print(art.logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
winner = 0
bets = {}
anyone_else = True
# TODO-3: Whether if new bids need to be added
while anyone_else:
    name = input("What is your name?")
    bet = int(input("How much would you like to bet?"))

    bets[name] = bet
    yes_or_no = input("Would you like to bet another one?")
# TODO-4: Compare bids in dictionary
    if yes_or_no == "yes":
        anyone_else = True
        print("\n" * 20)
    else:
        anyone_else = False
        en_yuksek_teklif = 0
        winner = 0
        for rec in bets:

            teklif_miktari = bets[rec]
            if teklif_miktari > en_yuksek_teklif:
                 en_yuksek_teklif = teklif_miktari
                 winner = rec
print(winner)

# TODO-4: Compare bids in dictionary


