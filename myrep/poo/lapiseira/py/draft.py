class Grafite:
    def __init__(self, espessura: float, dureza: str, tamanho: int):
        self.__espessura: float = espessura
        self.__dureza: str = dureza
        self.__tamanho: int = tamanho

    def usoPorFolha(self) -> int:
        gasto = {"HB": 1, "2B": 2, "4B": 4, "6B": 6}[self.__dureza]
        self.__tamanho -= gasto
        return self.__tamanho

    def get_espessura(self) -> float:
        return self.__espessura
    def get_dureza(self) -> str:
        return self.__dureza
    def get_tamanho(self) -> int:
        return self.__tamanho

    def set_tamanho(self, tamanho: int) -> int:
        self.__tamanho = tamanho

    def __str__(self) -> str:
        return f"[{self.__espessura}:{self.__dureza}:{self.__tamanho}]"

class Lapiseira:
    def __init__(self, espessura: float):
        self.__espessura: float = espessura
        self.__ponta: Grafite | None = None
        self.__tambor: list[Grafite] = []

    def set_tambor(self, tambor: list):
        self.__tambor = tambor

    def get_tambor(self) -> str:
        return self.__tambor
        
    def temGrafite(self) -> bool:
        if self.__ponta == None:
            return False
        if self.__ponta != None:
            return True

    def inserir(self, grafite: Grafite) -> bool:
        if self.__ponta != None:
            print("fail: ja existe grafite")
            return False
        if grafite.get_espessura() != self.__espessura:
            print("fail: calibre incompatível")
            return False
        self.__tambor.append(grafite)
        self.__ponta = grafite
        return True

    def puxar(self) -> bool:
        if self.__ponta is not None:
            print("fail: já existe grafite no bico") 
            return False
        if len(self.__tambor) == 0:
            return False ##nao há tambor
        self.__ponta = self.__tambor.pop(0) ##removendo 
        return True
            
        
    def remover(self) -> Grafite | None:
        aux = self.__ponta
        self.__ponta = None
        return aux


    def escreverPagina(self) -> None:
        if self.__ponta == None:
            print("fail: nao existe grafite")
            return

        gasto = {"HB": 1, "2B": 2, "4B": 4, "6B": 6}[self.__ponta.get_dureza()]

        if self.__ponta.get_tamanho() <= 10: 
            print("fail: tamanho insuficiente")
            return

        if self.__ponta.get_tamanho() - gasto < 10:
            self.__ponta.set_tamanho(10)
            print("fail: folha incompleta")
            return

        self.__ponta.usoPorFolha()

    def __str__(self) -> str:
        if self.__ponta == None:
            ponta_str = "[]"
        else:
            ponta_str = str(self.__ponta)
        if len(self.__tambor) == 0:
            tambor_str = "<>"
        else:
            tambor_str = " ".join(f"<{str(x)}>" for x in self.__tambor)
        return f"calibre: {self.__espessura}, bico: {ponta_str}, tambor: {tambor_str}"
        

def main():
    lapiseira = Lapiseira(" ")
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(lapiseira)
        elif args[0] == "init":
            espessura = float(args[1])
            lapiseira = Lapiseira(espessura)
        elif args[0] == "insert":
            espessura = float(args[1])
            dureza = args[2]
            tamanho = int(args[3])
            grafite = Grafite(espessura, dureza, tamanho)
            lapiseira.inserir(grafite)
        elif args[0] == "pull":
            lapiseira.puxar()
        elif args[0] == "remove":
            lapiseira.remover()
        elif args[0] == "write":
            lapiseira.escreverPagina()
        else:
            print("fail: comando invalido")
main()