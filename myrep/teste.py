nomes: dict[int, str] = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five"
}
#   chave = valor
nomes[1] = "one"
nomes[2] = "two"
nomes[3] = "three"
nomes[4] = "four"
nomes[6] = "six"

valores: dict[str, int] = {}
valores["four"] = 4
valores["two"] = 2
valores["three"] = 3
valores["one"] = 1
valores["five"] = 5

def somar(a: str, b: str) -> str:


somar("one", "one") # two
somar("three", "four") # seven