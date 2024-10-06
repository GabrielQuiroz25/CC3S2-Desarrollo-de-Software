# language: es

Característica: Característica del Estómago

  Escenario: comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  Escenario: comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir

  Escenario: comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir
    
  Escenario: Comer diferentes cantidades de pepinos en varios tiempos
    Dado que he comido 30 pepinos
    Cuando espero "una hora y treinta minutos"
    Entonces mi estómago debería gruñir
 
  Escenario: Comer pepinos sin especificar cantidad exacta
    Dado que he comido "un montón de" pepinos
    Cuando espero 3 horas
    Entonces mi estómago debería gruñir
 
  Escenario: Comer pepinos y esperar un tiempo exacto en minutos
    Dado que he comido 20 pepinos
    Cuando espero 120 minutos
    Entonces mi estómago debería gruñir
 
  Escenario: Comer pepinos en palabras y tiempo en minutos
    Dado que he comido "veinticinco" pepinos
    Cuando espero "noventa minutos"
    Entonces mi estómago debería gruñir
    
        
  Escenario: Comer una cantidad no válida de pepinos
    Dado que he comido "mil" pepinos
    Cuando espero 2 horas
    Entonces debería ocurrir un error de cantidad no válida

  Escenario: Comer pepinos y esperar en segundos
    Dado que he comido 40 pepinos
    Cuando espero "3600 segundos"
    Entonces mi estómago no debería gruñir

  Escenario: Comer pepinos y esperar en inglés
    Dado que he comido 15 pepinos
    Cuando espero "two hours and thirty minutes"
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos y esperar un tiempo aleatorio
    Dado que he comido 25 pepinos
    Cuando espero un tiempo aleatorio entre 1 y 3 horas
    Entonces mi estómago debería gruñir

  Escenario: Comer medio pepino y esperar
    Dado que he comido 0.5 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir
    
  Escenario: Comer una cantidad negativa de pepinos
    Dado que he comido -5 pepinos
    Entonces debería ocurrir un error de cantidad negativa

  Escenario: Comer grandes cantidades de pepinos y esperar mucho tiempo
    Dado que he comido 1000 pepinos
    Cuando espero 10 horas
    Entonces mi estómago debería gruñir
    
Escenario: Comer pepinos y esperar en minutos y segundos
 Dado que he comido 35 pepinos
 Cuando espero "1 hora y 30 minutos y 45 segundos"
 Entonces mi estómago debería gruñir
    
Escenario: Comer una cantidad fraccionaria de pepinos
 Dado que he comido 2.75 pepinos
 Cuando espero 3 horas
 Entonces mi estómago no debería gruñir

Escenario: Esperar usando horas en inglés
 Dado que he comido 20 pepinos
 Cuando espero "three hours and thirty minutes"
 Entonces mi estómago debería gruñir
 
Escenario: Comer pepinos y esperar un tiempo aleatorio
 Dado que he comido 32 pepinos
 Cuando espero un tiempo aleatorio entre 3 y 6 horas
 Entonces mi estómago debería gruñir
 
Escenario: Manejar una cantidad no válida de pepinos
 Dado que he comido -8 pepinos
 Entonces debería ocurrir un error de cantidad negativa
 
Escenario: Comer 6000 pepinos y esperar 10 horas
 Dado que he comido 1000 pepinos
 Cuando espero 15 horas
 Entonces mi estómago debería gruñir
 
Escenario: Manejar tiempos complejos
 Dado que he comido 43 pepinos
 Cuando espero "3 hora, 50 minutos y 18 segundos"
 Entonces mi estómago debería gruñir
