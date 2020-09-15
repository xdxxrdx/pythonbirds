class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    eduardo = Pessoa(nome = 'Eduardo')
    pedro = Pessoa(nome = 'Pedro')
    luciano = Pessoa(eduardo, pedro, nome ='luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    luciano.nome = 'Eduardo'
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    print(luciano.filhos)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(eduardo.__dict__)
    Pessoa.olhos = 3
    print(luciano.olhos)
    print(eduardo.olhos)
    print(Pessoa.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(eduardo.olhos))