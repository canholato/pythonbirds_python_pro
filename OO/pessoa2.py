class pessoa:
    self.idade = idade
    selfe.nome = nome
    selfe.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__== ' __main__':
    Márcio = Pessoa(nome='Márcio')
    print(Pessoa.cumprimentar(Márcio))
    print(id(Márcio))
    print(Márcio.cumprimentar())
    print(Márcio.nome)
    print(Márcio.idade)
    for filho in Márcio.filhos:
        print(filho.nome)