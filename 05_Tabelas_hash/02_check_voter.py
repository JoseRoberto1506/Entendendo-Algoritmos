voted = {}

def check_voter(name):
    if voted.get(name):
        print("Mande embora!")
    else:
        voted[name] = True
        print("Deixe votar!")

check_voter("tom")
check_voter("mike")
check_voter("mike")
