"""
Atividade de estudo de Classses
Criar um carro que se move e tem direção, para tanto criar classes de motor e direção.
O carro inicialmente se encontrará na situação de desligado e direção inicial : N-S , com sentido Norte
Cada vez que é solicitado mudança de direção o mesmo girará + 90º (direita) e - 90º (esquerda)
O carro não têm marcha à re.
A velocidade máxima permitida pelo carro é de 100 Km/h em direção frontal e de 20 km/h quando mudar a direção
"""


class Carro:
    """
    Classe construtora do objeto carro
    """

    def __init__(self, motor, direcao, acelerar=0, ligar=False):
        """
        Função inicializadora do objeto carro e instanciadora dos objetos motor e direção
        :param motor:
        :param direcao:
        :param acelerar:
        :param ligar:
        """
        self.motor = motor
        self.direcao = direcao
        self.acelerar = acelerar
        self.ligar = ligar
        # motor = Motor()
        # direcao = Direcao()
        #print(motor.__dict__)

    def ligar_carro(self):
        """
        Função responsável por ligar o carro
        :return:
        """
        print('O carro está ligado')
        self.ligar = True
        return Motor.ligar_motor(self)

    def desligar_carro(self):
        """
        Função responsável por desligar o carro
        :return:
        """
        print('O carro está desligado')
        return Motor.desligar_motor(self)


class Motor(Carro):
    """
    Classe construtora do objeto motor
    """

    def __init__(self, ligado=False, velocidade=0):
        """
        Função inicializadora do objeto motor
        :param ligado:
        :param desligado:
        :param velocidade:
        """
        # Carro.__init__(self, acelerar=0, ligar=False)
        # super().__init__()
        self.ligado = ligado
        self.velocidade = velocidade

    def ligar_motor(self):
        """
        Função responsável por ligar o motor do carro quando o carro está ligado
        :return:
        """
        print('O motor do carro foi acionado')
        ligado = True
        return self.motor.ligado

    def desligar_motor(self):
        """
        Função responsável por desligar o motor do carro quando o carro está desligado
        :return:
        """
        print('O motor do carro foi desligado')
        ligado = False
        return self.motor.ligado

    def acelerar(self, acelerar):
        """
        Função responsável por acelerar o motor e consequentemente aumentar a sua velocidade
        :param acelerar:
        :return:
        """


    def frear(self, frear):
        """
        Função responsável por desacelerar o carro, consequentemente reduzindo a sua velocidade
        :param frear:
        :return:
        """
        pass


class Direcao(Carro):
    """
    Classe construtora do objeto direção
    :param norte = 'N'
    :param sul = 'S'
    :param leste = 'L'
    :param oeste = 'O'
    """

    def __init__(self, direita=False, esquerda=False, em_frente=True):
        """
        Classe inicializadora o objeto direção
        :param direita:
        :param esquerda:
        :param em_frente:
        """
        # super(Carro, self).__init__(acelerar=0, ligar=False)
        # super().__init__()
        self.em_frente = em_frente
        self.direita = direita
        self.esquerda = esquerda

    @staticmethod
    def virar_a_direita():
        """
        função responsável por virar a direção à direita em 90º
        :return:
        """
        print('Viramos o carro 90º a direita')
        pass

    @staticmethod
    def virar_a_esquerda():
        """
        função responsável por virar a direção à esquerda em 90º
        :return:
        """
        print('Viramos o carro 90º a esquerda')
        pass


if __name__ == '__main__':
    carro = Carro(Motor(), Direcao(), acelerar=0, ligar=False)
    print(carro.__dict__)
    carro.ligar_carro()
    carro.desligar_carro()
