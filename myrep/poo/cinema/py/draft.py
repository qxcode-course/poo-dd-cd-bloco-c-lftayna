class Client:
    def __init__(self, id : str, phone : int):
        self.__id : str = id
        self.__phone : int = phone

    def getId(self) -> str:
        return self.__id

    def getIdPhone(self) -> int:
        return self.__phone

    def setId(self, id : str):
        self.__id = id

    def setPhone(self, fone: int):
        self.__phone = fone

    def __str__(self) -> str:
        return f"{self.__id}:{self.__phone}"

class Cinema:
    def __init__(self, capacity: int):
        self.__seats: list[Client | None] = [None] * capacity
        self.__capacity: int = capacity

    def get_seats(self) -> Client | None:
        return self.__seats
    def __str__(self) -> str:
        return f"[" + " ".join(str(x) if x is not None else "-" for x in self.__seats) + "]"
        
    def reserve(self, id: str, phone: int, index: int) -> bool:
        if index < 0 or index >= len(self.__seats):
            print("fail: cadeira nao existe")
            return False
        if self.__seats[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return False
        for x in self.__seats:
            if x is not None and x.getId() == id:
                print("fail: cliente ja esta no cinema")
                return False
            self.__seats[index] = Client(id, phone)
            return True

    def cancel(self, id : str):
        for i in range(len(self.__seats)):
            client = self.__seats[i]
            if client is not None and client.getId() == id:
                self.__seats[i] = None
                return
        print("fail: cliente nao esta no cinema")

def main():
    cinema = Cinema(0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(cinema)
        if args[0] == "init":
            capacity = int(args[1])
            cinema = Cinema(capacity)
        if args[0] == "reserve":
            id = args[1]
            phone = int(args[2])
            index = int(args[3])
            cinema.reserve(id, phone, index)
        if args[0] == "cancel":
            id = args[1]
            cinema.cancel(id)

main()