# src/belly.py
class Belly:
    def __init__(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def reset(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def comer(self, pepinos):
        print(f"He comido {pepinos} pepinos.")
        if pepinos <= 0:
            raise ValueError("La cantidad de pepinos debe ser positiva.")
        self.pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas):
        if tiempo_en_horas < 0:
            raise ValueError("El tiempo de espera no puede ser negativo.")
        self.tiempo_esperado += tiempo_en_horas
        print(f"He esperado {tiempo_en_horas} horas.")

    def esta_gruñendo(self):
        # Verificar que ambas condiciones se cumplan correctamente:
        # Se han esperado al menos 1.5 horas Y se han comido más de 10 pepinos
        if self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10:
            return True
        # Nueva validación: no debería gruñir si se han comido menos de 5 pepinos
        if self.pepinos_comidos < 5:
            return False # No gruñe si se han comido muy pocos pepinos
        return False

