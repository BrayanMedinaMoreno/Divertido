class Personaje:
    def __init__(self, nombre, fuerza,inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza 
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida


mi_personaje = Personaje("Akari", 10,30,2,100)
print("el nombre del persona es", mi_personaje.nombre)
print("La fuerza del personaje es", mi_personaje.fuerza)
        