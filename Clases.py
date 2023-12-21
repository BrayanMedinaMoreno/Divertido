import random

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
        print(self.nombre, "Se fue con diocito")
    
    def daño(self, oponente):
        return self.fuerza - oponente.defensa

    def atacar(self,oponente):
        daño = self.daño(oponente)
        oponente.vida = oponente.vida - daño
        print(self.nombre, "Ha hecho", daño, "Puntos de daño a", oponente.nombre)
        if oponente.vivo():
            print("la vida de", oponente.nombre, "es", oponente.vida)
        else:
            oponente.morir()


class Admin(Personaje):
    def __init__(self, nombre, fuerza, fe, defensa, vida, arma_de_fuego):
        super().__init__(nombre, fuerza, fe, defensa, vida)
        self.arma_de_fuego = arma_de_fuego

    def cambiar_arma(self):
        opcion = int(input("Elije un arma: (1) Espada 8 de daño (2) pistolas duales ? de daño"))
        if opcion == 1:
            self.arma_de_fuego = 8
        elif opcion == 2:
            self.arma_de_fuego = random.randint(10,30)
        else:
            print("Numero incorrecto")
    
    def atributos(self):
        super().atributos()
        print("-Arma", self.arma_de_fuego)
    pass

    def daño(self,oponente):
        return self.fuerza + self.arma_de_fuego - oponente.defensa


Akari = Admin("Akari",8,0,10,100,0)

Akari.atributos()

def combate(player_1,player_2):
    turno = 0
    while player_1.vivo() and player_2.vivo():
        print("\nTurno", turno)
        print(">>> acción de ", player_1.nombre, ":", sep="")
        player_1.atacar(player_2)
        print(">>> Acción de", player_2.nombre, ":", sep="")
        player_2.atacar(player_1)
        turno = turno + 1
    if player_1.vivo():
        print("\nHa ganado", player_1.nombre)
    elif player_2.vivo():
        print("\nHa ganado", player_2.nombre)
    else:
        print("\nEmpate")


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
        