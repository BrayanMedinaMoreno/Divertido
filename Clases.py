class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza 
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("-Fuerza :", self.fuerza)
        print("-Inteligencia :", self.inteligencia)
        print("-Defensa :", self.defensa)
        print("-vida :", self.vida)

    def subir_de_nivel(self,fuerza,inteligencia,defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def vivo(self):
        return self.vida > 0
    
    def morir (self):
        self.vida = 0
        print(self.nombre, "Se fue con diocito")
    
    def daño(self, sebas_low_elo):
        return self.fuerza - sebas_low_elo.defensa

    def atacar(self,sebas_low_elo):
        daño = self.daño(sebas_low_elo)
        sebas_low_elo.vida = sebas_low_elo.vida - daño
        print(self.nombre, "Ha hecho", daño, "Puntos de daño a", sebas_low_elo.nombre)
        if sebas_low_elo.vivo():
            print("la vida de", sebas_low_elo.nombre, "es", sebas_low_elo.vida)
        else:
            sebas_low_elo.morir()

mi_personaje = Personaje("Akari", 1000,1,5,100)
sebas_low_elo = Personaje("Sebas",30,1,30,100)
mi_personaje.atacar(sebas_low_elo)
sebas_low_elo.atributos()

#print(mi_personaje.daño(sebas_low_elo))
#sebas_low_elo.atributos()
#mi_personaje.atributos()
#mi_personaje.morir()
#mi_personaje.atributos()
#mi_personaje.subir_de_nivel(10,2,5)
#print("el nombre del persona es", mi_personaje.nombre)
#print("La fuerza del personaje es", mi_personaje.fuerza)
        