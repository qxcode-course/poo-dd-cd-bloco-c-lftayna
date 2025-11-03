class Pessoa:
    def __init__(self, nome: str):
        self.__nome = nome
    def get_nome(self) -> str:
        return self.__nome
    def set_nome(self, nome: str) -> str:
        return
    def __str__(self):
        return self.__nome

class Budega:
    def __init__(self, num_caixas: int = 0):
        self.caixas: list [Pessoa | None] = []
        for _ in range(num_caixas):
            self.caixas.append(None)
        self.espera: list[Pessoa] = []

    def enter(self, pessoa: Pessoa):
        self.espera.append(pessoa)

    def call(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return
        if self.caixas[index] is not None:
            print("fail: caixa ocupado")
            return
        if len(self.espera) == 0:
            print("fail: sem clientes")
            return

        self.caixas[index] = self.espera[0]
        del self.espera[0]

    def finish(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return
        if self.caixas[index] is None:
            print("fail: caixa vazio")
            return
        self.caixas[index] = None

    def giveup(self, nome: str) -> Pessoa | None:
        for i, pessoa in enumerate(self.espera):
            if pessoa.nome == nome:
                aux = self.espera[i]
                del self.espera[i]
                return aux
            break

    def __str__(self):
        caixas = ", ".join(["-----" if x is None else str(x) for x in self.caixas])
        espera = ", ".join([str (x) for x in self.espera])
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"

def main():
    budega = Budega()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(budega)
        if args[0] == "init":
            budega = Budega(int(args[1]))
        if args[0] == "arrive":
            budega.enter(Pessoa(args[1]))
        if args[0] == "call":
            budega.call(int(args[1]))
        if args[0] == "finish":
            budega.finish(int(args[1]))

main()
