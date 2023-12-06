from collections import deque


graph = {}
graph["voce"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == "m"


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    # Esse conjunto é a forma pela qual você mantém o registro das pessoas que já foram verificadas
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        # Verifica a pessoa apenas se ela já não tiver sido verificada
        if person in searched:
            continue
        if person_is_seller(person):
            print(f"{person} é um vendedor de manga!")
            return True
        search_queue += graph[person]
        # Marca a pessoa como verificada
        searched.add(person)
    return False


search("voce")
