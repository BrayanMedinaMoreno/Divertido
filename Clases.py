import random
from typing import Any

class Personaje:
    def __init__(self, nombre, fuerza, fe, defensa, vida): #atri
        self.nombre = nombre
        self.fuerza = fuerza 
        self.fe = fe
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self): #metodos
        print(self.nombre, ":", sep="")
        print("-Fuerza :", self.fuerza)
        print("-fe :", self.fe)
        print("-Defensa :", self.defensa)
        print("-vida :", self.vida)

    def subir_de_nivel(self,fuerza,fe,defensa):
        self.fuerza = self.fuerza + fuerza
        self.fe = self.fe + fe
        self.defensa = self.defensa + defensa

    def vivo(self):
        return self.vida > 0
    
    def morir (self):
        self.vida = 0
        print(">>> ",self.nombre, " Se fue con diocito")
    
    def daño(self, oponente):
        if oponente.defensa > self.fuerza:
            print(">>> No hiciste daño")
            return 0  # Devuelve 0 para indicar que no se hizo daño
        elif oponente.defensa < self.fuerza:
            return self.fuerza - oponente.defensa


    def atacar(self,oponente):
        daño = self.daño(oponente)
        print("--", oponente.atributos())
        oponente.vida = oponente.vida - daño
        print(">>>", self.nombre, " Ataco y ha hecho ", daño, " Puntos de daño a ", oponente.nombre)
        if oponente.vivo():
            print(">>> la vida de", oponente.nombre, "es", oponente.vida)
        else:
            oponente.morir()


class Tirador(Personaje):
    def __init__(self, nombre, fuerza, fe, defensa, vida, arma_de_fuego):
        super().__init__(nombre, fuerza, fe, defensa, vida)
        self.arma_de_fuego = arma_de_fuego
        self.arma_de_fuego = random.randint(10,30)*2
    """
    def cambiar_arma(self):
        opcion = int(input("Elije un arma: (1) Espada 8 de daño (2) pistolas duales ? de daño"))
        if opcion == 1:
            self.arma_de_fuego = 8
        elif opcion == 2:
            self.arma_de_fuego = random.randint(10,30)
        else:
            print("Numero incorrecto")
    """

    def atributos(self):
        super().atributos()
        print("-Arma", self.arma_de_fuego)
    pass

    """                    
    def daño(self,oponente):
        ataque_total = self.daño + self.arma_de_fuego
        if  ataque_total < oponente.defensa:
            print(">>> No hiciste daño")
            return 0  # Devuelve 0 para indicar que no se hizo daño    
        elif ataque_total > oponente.defensa:
            return ataque_total - oponente.defensa
    """
    def daño(self, oponente):
        ataque_total = self.calcular_ataque_total(oponente)
        if ataque_total < oponente.defensa:
            print(">>> No hiciste daño")
            return 0  # Devuelve 0 para indicar que no se hizo daño
        elif ataque_total > oponente.defensa:
            return ataque_total - oponente.defensa

    def calcular_ataque_total(self, oponente):
        return self.fuerza + self.arma_de_fuego


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, fe, defensa, vida):
        super().__init__(nombre, fuerza, fe, defensa, vida)

        
    pass

def combate(player_1,player_2):
    turno = 1
    while player_1.vivo() and player_2.vivo():
        print("\n>>> Turno", turno)

        print(">>> acción de ", player_1.nombre, ":", sep="")
        player_1.atacar(player_2)
        
        #print(player_1.atributos())

        print(">>> Acción de ", player_2.nombre, ":", sep="")
        player_2.atacar(player_1)

        turno = turno + 1
    if player_1.vivo():
        print("\nHa ganado", player_1.nombre)
    elif player_2.vivo():
        print("\nHa ganado", player_2.nombre)
    else:
        print("\nEmpate")


Akari = Tirador("Akari",8,0,10,100,0)
sebas_low_elo = Personaje("Sebas",30,1,30,100)

combate(Akari,sebas_low_elo)

"""
print("\nEstadisticas iniciales")
sebas_low_elo.atributos()
print("\nAtacando..")
Akari.atacar(sebas_low_elo)
print("\nEstadisticas finales")
sebas_low_elo.atributos()


Moises = Personaje ("MoisesPH",30,100,30,100)
minita = Personaje("feminismo",20,0,12,100)
combate(minita,Moises)
"""


"""
mi_personaje = Personaje("Akari", 1000,1,5,100)
sebas_low_elo = Personaje("Sebas",30,1,30,100)
mi_personaje.atacar(sebas_low_elo)
sebas_low_elo.atributos()
"""
#print(mi_personaje.daño(sebas_low_elo))
#sebas_low_elo.atributos()
#mi_personaje.atributos()
#mi_personaje.morir()
#mi_personaje.atributos()
#mi_personaje.subir_de_nivel(10,2,5)
#print("el nombre del persona es", mi_personaje.nombre)
#print("La fuerza del personaje es", mi_personaje.fuerza)
        