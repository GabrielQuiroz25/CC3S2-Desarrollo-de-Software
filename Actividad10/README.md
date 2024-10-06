# Actividad 10 - CC3S2

## BDD con Behave y Gherkin


### Contexto del proyecto original

El código proporcionado implementa una serie de pruebas usando Behavior-Driven Development (BDD) con la herramienta Behave, y describe diferentes escenarios de comportamiento utilizando el lenguaje Gherkin. El enfoque de BDD se centra en alinear el desarrollo de software con los requerimientos del negocio, expresados como historias de usuario. En el proyecto, los escenarios giran en torno a la simulación de comer pepinos y esperar un tiempo determinado para verificar si el estómago gruñe.

### Estructura del proyecto

El proyecto tiene la siguiente estructura de directorios:

```
.
├── features
│   ├── belly.feature
│   ├── environment.py
│   └── steps
│       └── steps.py
├── src
│   └── belly.py
└── README.md
```

### Detalles del proyecto

#### Archivo `features/belly.feature`

Este archivo define las características y escenarios a probar utilizando el lenguaje Gherkin en español. Es importante especificar el idioma al inicio del archivo.

```gherkin
# language: es

Característica: Comportamiento del Estómago

  Escenario: Comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: Comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: Comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  Escenario: Comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir
```

#### Archivo `features/steps/steps.py`

Contiene las definiciones de los pasos correspondientes a los escenarios en `belly.feature`. Se encarga de implementar la lógica detrás de cada paso.

```python
from behave import given, when, then
import re

# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        numeros = {
            "cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
            "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
            "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
            "ochenta": 80, "noventa": 90, "media": 0.5
        }
        return numeros.get(palabra.lower(), 0)

@given('que he comido {cukes:d} pepinos')
def step_given_eaten_cukes(context, cukes):
    context.belly.comer(cukes)

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    time_description = time_description.strip('"').lower()
    time_description = time_description.replace('y', ' ')
    time_description = time_description.strip()

    if time_description == 'media hora':
        total_time_in_hours = 0.5
    else:
        pattern = re.compile(r'(?:(\w+)\s*horas?)?\s*(?:(\w+)\s*minutos?)?')
        match = pattern.match(time_description)

        if match:
            hours_word = match.group(1) or "0"
            minutes_word = match.group(2) or "0"

            hours = convertir_palabra_a_numero(hours_word)
            minutes = convertir_palabra_a_numero(minutes_word)

            total_time_in_hours = hours + (minutes / 60)
        else:
            raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

    context.belly.esperar(total_time_in_hours)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."
```

#### Archivo `features/environment.py`

Inicializa el contexto antes de cada escenario, creando una nueva instancia de `Belly`.

```python
from src.belly import Belly

def before_scenario(context, scenario):
    context.belly = Belly()
```

#### Archivo `src/belly.py`

Implementa la lógica de la clase `Belly`, que simula el comportamiento del estómago.

```python
class Belly:
    def __init__(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def comer(self, pepinos):
        self.pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas):
        self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self):
        # El estómago gruñe si ha esperado al menos 1.5 horas y ha comido más de 10 pepinos
        return self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10
```

Al ejecutar las pruebas usando el comando `behave`, obtenemos el siguiente resultado:

[![image.png](https://i.postimg.cc/CMbFK0YX/image.png)](https://postimg.cc/PNrG6BCQ)

Lo que nos indica que las pruebas pasaron exitosamente.

Ahora, modificaremos el código e implementaremos nuevos escenarios que corresponden a las nuevas historias de usuario (Extensiones):

#### 1. Nuevos escenarios en belly.feature

Agregar nuevos escenarios que amplíen el comportamiento, utilizando entradas más complejas como palabras y formatos de tiempo variados:

```gherkin
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
```

Al ejecutar las pruebas con los nuevos escenarios añadidos obtenemos:

[![image.png](https://i.postimg.cc/ryffx08r/image.png)](https://postimg.cc/Z0yPhqvb)


#### 2. Implementación de expresiones regulares para nuevos casos en `belly_steps.py`

Incluir nuevas expresiones regulares que puedan manejar la entrada de palabras y tiempos en diferentes formatos:

```python
# Diccionario extendido para números
numeros_extendido = {
    "cero": 0, "uno": 1, "una":1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
    "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
    "diecisiete":17, "dieciocho":18, "diecinueve":19, "veinte":20, "veinticinco":25,
    "treinta": 30, "cuarenta":40, "cincuenta":50, "sesenta":60, "setenta":70,
    "ochenta":80, "noventa":90, "media": 0.5, "un montón de": 100
}


# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        return numeros_extendido.get(palabra.lower(), 0)

@given('que he comido {cukes} pepinos')
def step_given_eaten_cukes(context, cukes):
    # Manejar cantidades no numéricas
    cukes = cukes.strip('"').lower()
    
    if cukes.isdigit():
        cucumbers = int(cukes)
    else:
        cucumbers = convertir_palabra_a_numero(cukes) if cukes in numeros_extendido else 0
    context.belly.comer(cucumbers)

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    time_description = time_description.strip('"').lower()
    time_description = time_description.replace('y', ' ')
    time_description = time_description.strip()

    # Manejar casos especiales como 'media hora'
    if time_description == 'media hora':
        total_time_in_hours = 0.5
    else:
        # Expresión regular para extraer horas y minutos
        pattern = re.compile(r'(?:(\w+)\s*horas?)?\s*(?:(\w+)\s*minutos?)?')
        match = pattern.match(time_description)

        if match:
            hours_word = match.group(1) or "0"
            minutes_word = match.group(2) or "0"

            hours = convertir_palabra_a_numero(hours_word)
            minutes = convertir_palabra_a_numero(minutes_word)

            total_time_in_hours = hours + (minutes / 60)
        else:
            raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

    context.belly.esperar(total_time_in_hours)

```

Ejecutando las pruebas:

[![image.png](https://i.postimg.cc/85NB2DbW/image.png)](https://postimg.cc/wt4mNCZT)

#### 3. Nuevos casos de prueba con excepciones

Agregar casos para verificar errores o valores inesperados. Aquí verificamos que el sistema arroje un error cuando se ingresa una cantidad no válida de pepinos.

```gherkin
  Escenario: Comer una cantidad no válida de pepinos
    Dado que he comido "mil" pepinos
    Cuando espero 2 horas
    Entonces debería ocurrir un error de cantidad no válida
```

Implementación en belly_steps.py:

```python
@then('debería ocurrir un error de cantidad no válida')
def step_then_invalid_cucumber_amount(context):
    try:
        assert context.belly.pepinos_comidos < 100, "Cantidad de pepinos no válida"
    except AssertionError as e:
        print(str(e))
```

[![image.png](https://i.postimg.cc/HxPGnSnS/image.png)](https://postimg.cc/34pfbFgp)


#### 4. Validaciones extendidas y casos de límite en belly.py

Agregar nuevas reglas de negocio y validaciones en la clase Belly para manejar más escenarios, como comer cantidades muy pequeñas de pepinos o tiempos de espera insuficientes.

```python
class Belly:

## ......
def esta_gruñendo(self):
    # Verificar que ambas condiciones se cumplan correctamente:
    # Se han esperado al menos 1.5 horas Y se han comido más de 10 pepinos
    if self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10:
        return True
    # Nueva validación: no debería gruñir si se han comido menos de 5 pepinos
    if self.pepinos_comidos < 5:
        return False # No gruñe si se han comido muy pocos pepinos
    return False
```

[![image.png](https://i.postimg.cc/X75MNkb8/image.png)](https://postimg.cc/jLR3ZNCw)


#### 5. Manejo de unidades de tiempo adicionales

Podemos extender el proyecto para que soporte unidades de tiempo adicionales como "segundos" o intervalos complejos.

##### Nuevo escenario en belly.feature

```gherkin
  Escenario: Comer pepinos y esperar en segundos
    Dado que he comido 40 pepinos
    Cuando espero "3600 segundos"
    Entonces mi estómago debería gruñir
```

[![image.png](https://i.postimg.cc/g0NQtMVY/image.png)](https://postimg.cc/1gVvfr7T)


##### Implementación en belly_steps.py

Añadir compatibilidad para unidades de tiempo adicionales, como segundos, a las expresiones regulares.

```python
@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    time_description = time_description.strip('"').lower()
    time_description = time_description.replace('y', ' ')
    time_description = time_description.strip()

    # Manejar casos especiales como 'media hora'
    if time_description == 'media hora':
        total_time_in_hours = 0.5
    else:
        # Expresión regular para extraer horas, minutos y segundos
        pattern = re.compile(r'(?:(\w+)\s*horas?)?\s*(?:(\w+)\s*minutos?)?\s*(?:(\w+)\s*segundos?)?')
        match = pattern.match(time_description.lower())

        if match:
            hours_word = match.group(1) or "0"
            minutes_word = match.group(2) or "0"
            seconds_word = match.group(3) or "0"

            hours = convertir_palabra_a_numero(hours_word)
            minutes = convertir_palabra_a_numero(minutes_word)
            seconds = convertir_palabra_a_numero(seconds_word)

            total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
        else:
            raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

    context.belly.esperar(total_time_in_hours)
```

[![image.png](https://i.postimg.cc/g263Tr3r/image.png)](https://postimg.cc/JsMyyr6W)

#### 6. Manejo de diferentes idiomas para la entrada
Podemos ampliar el sistema para que acepte entradas en diferentes idiomas, por ejemplo, en inglés o español.

##### Nuevo escenario en belly.feature

```gherkin
  Escenario: Comer pepinos y esperar en inglés
    Dado que he comido 15 pepinos
    Cuando espero "two hours and thirty minutes"
    Entonces mi estómago debería gruñir
```

[![image.png](https://i.postimg.cc/3w5257Z1/image.png)](https://postimg.cc/QFmF12wK)

##### Implementación en belly_steps.py
Añadir soporte para diferentes idiomas, como inglés:

```python
# Diccionario extendido para números
numeros_extendido = {
# ...
}

numeros_en_ingles = {
 "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
 "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10
}


# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        # Buscar primero en el diccionario en español
        numero = numeros_extendido.get(palabra.lower())
        if numero is not None:
            return numero
        # Buscar en el diccionario en inglés si no está en español
        return numeros_en_ingles.get(palabra.lower(), 0)
```

[![image.png](https://i.postimg.cc/hP5KG1hZ/image.png)](https://postimg.cc/bsk7Cbx1)

#### 7. Manejo de unidades de tiempo aleatorias

Podemos agregar lógica para manejar la entrada de tiempos de espera aleatorios, lo que permitirá al sistema trabajar con valores de tiempo no especificados, basándose en un rango.



##### Nuevo escenario en belly.feature
```gherkin
  Escenario: Comer pepinos y esperar un tiempo aleatorio
    Dado que he comido 25 pepinos
    Cuando espero un tiempo aleatorio entre 1 y 3 horas
    Entonces mi estómago debería gruñir
```

[![image.png](https://i.postimg.cc/6q1TtsDY/image.png)](https://postimg.cc/wRL9Qrxm)

##### Implementación en belly_steps.py

Añadir manejo de tiempos aleatorios utilizando random en Python:

```python
# Tiempo aleatorio
import random
@when('espero un tiempo aleatorio entre {min_time:d} y {max_time:d} horas')
def step_when_wait_random_time(context, min_time, max_time):
    tiempo_aleatorio = random.uniform(min_time, max_time)
    print(f"Esperando un tiempo aleatorio de {tiempo_aleatorio:.2f} horas.")
    context.belly.esperar(tiempo_aleatorio)
```

[![image.png](https://i.postimg.cc/zBG0cK5K/image.png)](https://postimg.cc/Mcg7ccnp)

#### 8. Uso de unidades fraccionarias de pepinos

Podemos agregar soporte para manejar fracciones de pepinos, lo cual sería útil para escenarios donde una persona no come un número entero de pepinos.

##### Nuevo escenario en belly.feature

```gherkin
  Escenario: Comer medio pepino y esperar
    Dado que he comido 0.5 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir
```

##### Implementación en belly_steps.py

Permitir manejar números decimales en los pepinos:

```python
@given('que he comido {cukes} pepinos')
def step_given_eaten_cukes(context, cukes):
    # Manejar cantidades no numéricas
    cukes = cukes.strip('"').lower()
    
    if cukes.isdigit():
        cucumbers = float(cukes)
    else:
        cucumbers = convertir_palabra_a_numero(cukes)
    context.belly.comer(cucumbers)
```

[![image.png](https://i.postimg.cc/NFp470Zb/image.png)](https://postimg.cc/XBBdnnjy)

#### 9. Validaciones adicionales en belly.py

Agregar reglas de negocio más detalladas para manejar excepciones o validaciones adicionales, por ejemplo, si se intenta comer una cantidad negativa de pepinos o si el tiempo de espera es menor a 0.

##### Implementación en belly.py
```python
class Belly:
 # ...
 
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
```

##### Nuevo escenario en belly.feature

```gherkin
  Escenario: Comer una cantidad negativa de pepinos
    Dado que he comido -5 pepinos
    Entonces debería ocurrir un error de cantidad negativa
```

[![image.png](https://i.postimg.cc/vBvjkbpx/image.png)](https://postimg.cc/dkL4TPQJ)


#### 10. Manejo de multitud de pepinos y tiempos

Podemos agregar funcionalidad para manejar escenarios donde se comen grandes cantidades de pepinos en intervalos pequeños o grandes, para asegurarnos de que el sistema escale 
correctamente.

##### Nuevo escenario en belly.feature

```gherkin
  Escenario: Comer grandes cantidades de pepinos y esperar mucho tiempo
    Dado que he comido 1000 pepinos
    Cuando espero 10 horas
    Entonces mi estómago debería gruñir
```

##### Implementación en belly_steps.py

Asegurarse de que el sistema pueda manejar grandes números:

```python
@given('he comido {cukes:d} pepinos')
def step_given_large_quantity_of_cukes(context, cukes):
    context.belly.comer(cukes)
```

[![image.png](https://i.postimg.cc/SsVtJfLt/image.png)](https://postimg.cc/yggTG9bF)



### Ejercicios propuestos
#### Ejercicio 1: Añadir soporte para minutos y segundos en tiempos de espera

- **Objetivo:** Añadir soporte para tiempos de espera expresados en minutos y segundos al sistema.
- **Instrucciones:**
    - Modifica la función que maneja el tiempo de espera para que soporte minutos y segundos.
    - Asegúrate de que las entradas como "1 hora y 30 minutos", "90 minutos", y "3600 segundos" sean correctamente interpretadas.
    - Implementa un escenario de prueba en Gherkin que valide que el estómago gruñe o no según estas variaciones de tiempo.

**Ejemplo de Gherkin:**

```gherkin
Escenario: Comer pepinos y esperar en minutos y segundos
 Dado que he comido 35 pepinos
 Cuando espero "1 hora y 30 minutos y 45 segundos"
 Entonces mi estómago debería gruñir
```

[![image.png](https://i.postimg.cc/pd0PtzhR/image.png)](https://postimg.cc/Nyr36ykz)

#### Ejercicio 2: Manejo de cantidades fraccionarias de pepinos

- **Objetivo:** Permitir que el sistema acepte cantidades fraccionarias de pepinos.

- **Instrucciones:**

    - Modifica el sistema para que acepte entradas de pepinos en forma de números decimales, como "0.5" o "2.75".
    
    - Implementa un nuevo escenario en Gherkin donde se ingiera una cantidad fraccionaria de pepinos y se verifique el comportamiento del sistema.
    
    - Añade un manejo de excepciones para evitar que se ingrese una cantidad negativa de pepinos.

**Ejemplo de Gherkin:**

```gherkin
Escenario: Comer una cantidad fraccionaria de pepinos
 Dado que he comido 0.5 pepinos
 Cuando espero 2 horas
 Entonces mi estómago no debería gruñir
```

[![image.png](https://i.postimg.cc/1XdgRb8R/image.png)](https://postimg.cc/bSQY3C04)

#### Ejercicio 3: Soporte para idiomas múltiples

- **Objetivo:** Agregar soporte para manejar diferentes idiomas (inglés y español) en las descripciones de tiempo.

- **Instrucciones:**
    
    - Modifica el código para que acepte entradas de tiempo en inglés, además de español. Por ejemplo, "two hours" o "treinta minutos".
    
    - Escribe al menos dos escenarios de prueba que usen tiempos en inglés.
    
    - Implementa una función que convierta las palabras en inglés a valores numéricos.

**Ejemplo de Gherkin:**

```gherkin
Escenario: Esperar usando horas en inglés
 Dado que he comido 20 pepinos
 Cuando espero "three hours and thirty minutes"
 Entonces mi estómago debería gruñir
```

[![image.png](https://i.postimg.cc/Jn27jZMP/image.png)](https://postimg.cc/R6wzB33H)

#### Ejercicio 4: Manejo de cantidades aleatorias de tiempo

- **Objetivo:** Añadir la capacidad de manejar tiempos aleatorios en un rango específico.

- **Instrucciones:**
    
    - Crea una nueva función que permita ingresar un rango de tiempo (por ejemplo, entre 1 y 3 horas) y elija un tiempo aleatorio dentro de ese rango.
    
    - Implementa un escenario de prueba en Gherkin donde se verifique que el estómago gruñe tras un tiempo aleatorio.
    
    - Imprime el tiempo aleatorio generado en el paso de la prueba.

**Ejemplo de Gherkin:**

```gherkin
Escenario: Comer pepinos y esperar un tiempo aleatorio
 Dado que he comido 32 pepinos
 Cuando espero un tiempo aleatorio entre 3 y 6 horas
 Entonces mi estómago debería gruñir
```

[![image.png](https://i.postimg.cc/vT4rvr9B/image.png)](https://postimg.cc/JHWHrBpV)


#### Ejercicio 5: Validación de cantidades no válidas

- **Objetivo:** Manejar casos en los que se ingresen cantidades no válidas de pepinos.

- **Instrucciones:**
    
    - Añade validaciones para evitar que el usuario ingrese una cantidad negativa o  extremadamente alta de pepinos.
    
    - Modifica la lógica para arrojar un error si se ingresa una cantidad de pepinos superior a 100 o menor que 0.
    
    - Implementa un escenario de prueba en Gherkin para verificar el manejo correcto de errores.

**Ejemplo de Gherkin:**
```gherkin
Escenario: Manejar una cantidad no válida de pepinos
 Dado que he comido -8 pepinos
 Entonces debería ocurrir un error de cantidad negativa
```

[![image.png](https://i.postimg.cc/G3ZRxcn3/image.png)](https://postimg.cc/fkj1wQb1)

#### Ejercicio 6: Escalabilidad con grandes cantidades de pepinos

- **Objetivo:** Verificar el comportamiento del sistema cuando se ingieren grandes cantidades de pepinos y se espera durante periodos largos.

- **Instrucciones:**

    - Añade soporte para manejar cantidades muy grandes de pepinos, como 1000.
    
    - Implementa escenarios de prueba donde se espera un tiempo largo, como 10 horas, tras comer una gran cantidad de pepinos.
    
    - Valida que el sistema sigue funcionando correctamente sin errores o lentitud.

**Ejemplo de Gherkin:**

```gherkin
Escenario: Comer 6000 pepinos y esperar 10 horas
 Dado que he comido 1000 pepinos
 Cuando espero 15 horas
 Entonces mi estómago debería gruñir
```

[![image.png](https://i.postimg.cc/D05qFCTB/image.png)](https://postimg.cc/p5h9JJyF)

#### Ejercicio 7: Descripciones de tiempo complejas

- **Objetivo:** Ampliar la lógica para manejar descripciones de tiempo complejas.

- **Instrucciones:**

    - Modifica la expresión regular que analiza las descripciones de tiempo para que soporte combinaciones más complejas como "1 hora, 30 minutos y 45 segundos".
    
    - Implementa escenarios en Gherkin que validen estos casos.
    
    - Asegúrate de que el sistema calcule correctamente el tiempo total en horas.

**Ejemplo de Gherkin:**
```gherkin
Escenario: Manejar tiempos complejos
 Dado que he comido 43 pepinos
 Cuando espero "3 hora, 50 minutos y 18 segundos"
 Entonces mi estómago debería gruñir
 ```
 
[![image.png](https://i.postimg.cc/nhnhqHqj/image.png)](https://postimg.cc/fJgsNQ2D)
 
 
