class pessoa:
    def cumprimentar(self):
        return 'Olá'

if __name__== ' __main__':
    P = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Marcio'
    print(p.nome)
    print(p.idade)