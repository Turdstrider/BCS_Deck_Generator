import random
"""Function to find if the card is a hero card by the key word e.g.(Quin)"""
def find_sub_str_in_tuple(tup, word):
    for i in range(0, len(tup)):
        if word.find(tup[i]) != -1:
            return True
    return False

"""Function to go through the list of cards and blacklist any cards the selected hero cannot use"""
def blacklist_by_hero(key):
    herokeys = ("(Quin)","(Gwen)","(Obyn)","(Amel)","(Ador)","(ZeeJ)","(Stri)")
    for line in cardlist:
        if line.find(key) == -1 and find_sub_str_in_tuple(herokeys, line):
            blacklist.write(line)

"""Find if selected card is in blacklist"""
def search_blacklist(target):
    blacklist.seek(0)
    currentblist = blacklist.readlines()
    for i in range(0, len(currentblist)):
        if currentblist[i] == target:
            return False
    return True

"""Initialising Global Parameters"""
decksize = 40
cardlist = open("CardList.txt", "r")
blacklist = open("BlackList.txt", "w+")
herolist = open("HeroList.txt", "r")

"""First, Determine which Hero we're using and blacklist all other hero cards"""
heroes = herolist.readlines()
hero = heroes[random.randint(0, len(heroes)-1)]
print("Hero:", hero.replace('\n', ''))
keyword = "(" + hero.replace(" ","")[0:4] + ")"
blacklist_by_hero(keyword)

"""Now with the Hero Determined, Cards will now be picked out until our deck is full"""
"""It will skip cards that are already blacklisted"""
cardlist.seek(0)
allcards = cardlist.readlines()
amount = 1
count = 0
while count < decksize:
    card = random.choice(allcards)
    if search_blacklist(card):
        if card.find("(Uniq)") != -1:
            count += 1
            print("1x",card.replace("(Uniq)", "").replace(keyword, ""), end='')
        else:
            amount = random.randint(1, 3)
            while amount + count > 40:
                amount = random.randint(1, 3)
            count += amount
            print(amount, "x ", card.replace(keyword, ""), sep='', end='')
        blacklist.write(card)

cardlist.close()
blacklist.close()
herolist.close()
input("Press Enter to close generator...")
