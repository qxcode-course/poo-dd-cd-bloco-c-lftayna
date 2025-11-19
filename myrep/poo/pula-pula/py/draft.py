class Kid:
    def __init__(self, name: str, age: int):
        self.__name : str = name
        self.__age: int = age

    def getName(self) -> str:
        return self.__name

    def getAge(self) -> int:
        return self.__age 

    def setAge(self, age: int):
        self.__age = age

    def setName(self, name: str):
        self.__name = name
 

    def __str__(self) -> str:
        return f"{self.__name}:{self.__age}"

class Trampoline:
    def __init__(self, quantidade : int = 0):
        self.__playing : list[Kid] = []
        self.__waiting : list[Kid] = []
        
    def arrive(self, kid : Kid) -> None:
        self.__waiting.append(kid)

    def enter(self) -> None:
        if len(self.__waiting) > 0:
            aux: Kid = self.__waiting.pop(0)
            self.__playing.append(aux)
        return

    def leave(self) -> None:
        if len(self.__playing) > 0:
            aux = self.__playing.pop(0)
            self.__waiting.append(aux)
        return

    def removekid(self,kid : Kid, name : str, age: int) -> None:
        for i, kid in enumerate(self.__waiting):
            if kid.getName() == name:
                del self.__waiting[i]
                return

        for i, kid in enumerate(self.__playing):
            if kid.getName() == name and kid.getAge == age:
                del self.__waiting[i]
                return

    def removelist(self, name: str) -> None:
        for i, kid in enumerate(self.__waiting):
            if kid.getName() == name:
                del self.__waiting[i]
                return

        for i, kid in enumerate(self.__playing):
            if kid.getName() == name:
                del self.__playing[i]
                return
        
        print(f"fail: {name} nao esta no pula-pula")

    def __str__(self) -> str:
        waiting = ", ".join(str(kid) for kid in reversed(self.__waiting))
        playing = ", ".join(str(kid) for kid in reversed(self.__playing))
        return f"[{waiting}] => [{playing}]"

    
def main():
    trampoline = Trampoline()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(trampoline)
        if args[0] == "arrive":
            name = str(args[1])
            age = int(args[2])
            kid = Kid(name, age)
            trampoline.arrive(kid)
        if args[0] == "enter":
            trampoline.enter()
        if args[0] == "leave":
            trampoline.leave()
        if args[0] == "remove":
            name = str(args[1])
            trampoline.removelist(name)
main()




