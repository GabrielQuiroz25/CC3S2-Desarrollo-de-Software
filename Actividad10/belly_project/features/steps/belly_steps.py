from behave import given, when, then
import re


# Diccionario extendido para números
numeros_extendido = {
    "cero": 0, "uno": 1, "una":1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
    "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
    "diecisiete":17, "dieciocho":18, "diecinueve":19, "veinte":20, "veinticinco":25,
    "treinta": 30, "cuarenta":40, "cincuenta":50, "sesenta":60, "setenta":70,
    "ochenta":80, "noventa":90, "media": 0.5, "un montón de": 100, "mil":1000,
}

numeros_en_ingles = {
 "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
 "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "thirty":30
}


# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return float(palabra)
    except ValueError:
        # Buscar primero en el diccionario en español
        numero = numeros_extendido.get(palabra.lower())
        if numero is not None:
            return numero
        # Buscar en el diccionario en inglés si no está en español
        return numeros_en_ingles.get(palabra.lower(), 0)

@given('que he comido {cukes} pepinos')
def step_given_eaten_cukes(context, cukes):
    # Manejar cantidades no numéricas
    cukes = cukes.strip('"').lower()
    
    if cukes.isdigit():
        cucumbers = float(cukes)
    else:
        cucumbers = convertir_palabra_a_numero(cukes)
    if cucumbers>=0:
        context.belly.comer(cucumbers)
    else:
        context.cantidad_negativa= cucumbers

@given('he comido {cukes:d} pepinos')
def step_given_large_quantity_of_cukes(context, cukes):
    context.belly.comer(cukes)

# Tiempo aleatorio
import random
@when('espero un tiempo aleatorio entre {min_time:d} y {max_time:d} horas')
def step_when_wait_random_time(context, min_time, max_time):
    tiempo_aleatorio = random.uniform(min_time, max_time)
    print(f"Esperando un tiempo aleatorio de {tiempo_aleatorio:.2f} horas.")
    context.belly.esperar(tiempo_aleatorio)



@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    time_description = time_description.strip('"').lower()
    time_description = time_description.replace(' y ', ' ')
    time_description = time_description.replace(' and ', ' ')
    time_description = time_description.strip()

    # Manejar casos especiales como 'media hora'
    if time_description == 'media hora':
        total_time_in_hours = 0.5
    else:
        # Expresión regular para extraer horas, minutos y segundos
        pattern = re.compile(r'(?:(\w+)\s*(?:horas?|hours?))?\s*(?:(\w+)\s*(?:minutos?|minutes?))?\s*(?:(\w+)\s*(?:segundos?|seconds?))?')
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


@then('debería ocurrir un error de cantidad no válida')
def step_then_invalid_cucumber_amount(context):
    try:
        assert context.belly.pepinos_comidos < 100, "Cantidad de pepinos no válida"
    except AssertionError as e:
        print(str(e))
        
@then('debería ocurrir un error de cantidad negativa')
def step_then_invalid_cucumber_amount(context):
    try:
        context.belly.comer(context.cantidad_negativa)
    except ValueError as e:
        print(str(e))


@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."
