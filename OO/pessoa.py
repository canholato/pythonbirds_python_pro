class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    gilson = Pessoa(nome='Gilson')
    marcos = Pessoa(nome='Marcos')
    margareth = Pessoa(nome='Margareth')
    eduardo = Pessoa(nome='Eduardo')
    maria_jose = Pessoa(gilson, marcos, margareth, eduardo, nome='Maria José')
    print(Pessoa.cumprimentar(maria_jose))
    print(id(maria_jose))
    print(maria_jose.cumprimentar())
    print(maria_jose.nome)
    print(maria_jose.idade)
    print(maria_jose.filhos)
    for filho in maria_jose.filhos:
        print(filho.nome)
    gilson.sobrenome = 'Nogueira'
    del gilson.filhos
    gilson.olhos = 1
    del gilson.olhos
    print(gilson.__dict__)
    print(marcos.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(gilson.olhos)
    print(marcos.olhos)
    print(id(Pessoa.olhos), id(gilson.olhos), id(marcos.olhos))
