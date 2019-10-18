class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Marília')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print('teste de conexão do VS Code')
    print(p.nome)
    p.nome = 'Gilson'
    print(p.nome)
    print(p.idade)
