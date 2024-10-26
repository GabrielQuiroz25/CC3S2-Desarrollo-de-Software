# Actividad 12 - CC3S2

## Iniciando TDD: Arrange-Act-Assert

Las pruebas unitarias no son nada misteriosas. Son solo código ejecutable escrito en el mismo lenguaje que la aplicación. Cada prueba de unidad constituye el primer uso del código que se desea escribir. Se llama al código tal como se llamará en la aplicación real. La prueba ejecuta ese código, captura los resultados que nos interesan y verifica que sean lo que esperábamos. Dado que la prueba usa el código de la misma manera que la aplicación, recibimos comentarios inmediatos sobre qué tan fácil o difícil es usarlo. Esto puede sonar obvio, y lo es, pero es una herramienta poderosa para escribir código limpio y correcto.


### Ejercicio 5: Desarrollo de un compilador simple


##### Descripción

Estás construyendo un compilador simple que analiza y ejecuta un lenguaje de programación básico. Necesitas implementar el análisis léxico y sintáctico, y asegurarte de que el compilador maneje errores correctamente.

##### Instrucciones

1. **Escribe una historia de usuario** que describa las expectativas del usuario al compilar y ejecutar código.

```gherkin
    Como desarrollador que usa un compilador
    Quiero compilar código escrito en C++
    Para poder verificar que el código no tenga errores léxicos y sintácticos
```

2. **Define criterios de aceptación** que incluyan el manejo de errores léxicos y sintácticos, y la ejecución correcta del código.

Compilación y ejecución de un programa válido en C++:

- Un código fuente escrito correctamente debe compilarse y ejecutarse sin errores ni advertencias.
- Si el código contiene un identificador no reconocido, el compilador debe detener la compilación y proporcionar un mensaje de error específico.
- El compilador debe identificar la falta de un punto y coma ';' y detener el proceso de compilación mostrando un mensaje de error que debe indicar que falta un ';' y señalar la línea donde se espera el punto y coma.
- El compilador debe detectar la ausencia de la función main y detener la compilación mostrando un mensaje de error que debe indicar claramente que se necesita una función main para que el programa se ejecute.


3. **Escribe escenarios en Gherkin** que prueben la compilación y ejecución de código válido e inválido.

```gherkin
  Escenario: Compilación y ejecución de un programa válido en C++
    Dado el siguiente código:
      """
      #include <iostream>
      
      int main() {
          std::cout << "Hello world" << std::endl;
      }
      """
    Cuando compilo el código
    Y ejecuto el código
    Entonces la salida debería ser "Hello world"

  Escenario: Error léxico por indentificador inválido en el código
    Dado el siguiente código:
      """
      #include <iostream>
      
      int main() {
          std::cout << "Hello world" << endll;
      }
      """
    Cuando compilo el código
    Entonces debería recibir un mensaje de error "Error léxico: no se reconoce endll en la línea 4"
    
  Escenario: Error sintáctico por falta de punto y coma
    Dado el siguiente código:
      """
      #include <iostream>
      
      int main() {
          std::cout << "Hello world" << std::endl
      }
      """
    Cuando compilo el código
    Entonces debería recibir un mensaje de error "Error sintáctico: falta ';' en la línea 4"
    
  Escenario: Error léxico por falta de std
    Dado el siguiente código:
      """
      #include <iostream>
      
      int main() {
          cout << "Hello world" << std::endl;
      }
      """
    Cuando compilo el código
    Entonces debería recibir un mensaje de error "Error léxico: no se reconoce cout en la línea 4"
    
  Escenario: Error sintáctico por falta de función main
    Dado el siguiente código:
      """
      #include <iostream>
      
      int suma(int a, int b) {
          return a + b;
      }
      """
    Cuando compilo el código
    Y ejecuto el código
    Entonces debería recibir un mensaje de error "Error sintáctico: no se encontró una función main"
```


4. **Implementa las definiciones de pasos en Behave**, utilizando expresiones regulares para el análisis léxico.

```python
from behave import given, when, then

@given('el siguiente código')
def step_given_el_siguiente_codigo(context):
    context.code = context.text

@when('compilo el código')
def step_when_compilo_el_codigo(context):
    context.compilador = compiler()
    context.compile_result = context.compilador.compile(context.code)

@when('ejecuto el código')
def step_when_ejecuto_el_codigo(context):
    if context.compile_result == "Compilado exitosamente":
        context.execution_result = context.compilador.execute_code()
    else:
        context.execution_result = context.compile_result

@then('la salida debería ser "{salida_esperada}"')
def step_then_la_salida(context, salida_esperada):
    assert context.execution_result == salida_esperada, f'La salida esperada era "{salida_esperada}", pero fue "{context.execution_result}"'

@then('debería recibir un mensaje de error "{error_esperado}"')
def step_then_el_mensaje_de_error(context, error_esperado):
    assert context.compile_result == error_esperado, f'La salida esperada era "{error_esperado}", pero fue "{context.compile_result}"'

```



5. **Escribe pruebas en pytest**, siguiendo el patrón AAA, para verificar que el compilador funciona según lo esperado.


```python
# Prueba para la compilación y ejecución de un programa válido
def test_ejecucion_codigo_valido():
    # Arrange
    code = """
    #include <iostream>
    
    int main() {
        std::cout << "Hello world" << std::endl;
    }
    """
    
    compilador = compiler()
    
    # Act
    compile_result = compilador.compile(code)
    
    if compile_result == "Compilado exitosamente":
        execution_result = compilador.execute_code()  
    else: 
        execution_result = compile_result

    # Assert
    assert execution_result == "Hello world"

# Prueba para error léxico debido a un identificador no reconocido
def test_lexical_error_identificador_invalido():
    # Arrange
    code = """
    #include <iostream>
    
    int main() {
        std::cout << "Hello world" << endll;
    }
    """
    
    compilador = compiler()
    
    # Act
    compile_result = compilador.compile(code)
    
    # Assert
    assert compile_result == "Error léxico: no se reconoce endll en la línea 4"

# Prueba para error sintáctico por falta de punto y coma
def test_syntax_error_falta_punto_y_coma():
    # Arrange
    code = """
    #include <iostream>
    
    int main() {
        std::cout << "Hello world" << std::endl
    }
    """
    
    compilador = compiler()
    
    # Act
    compile_result = compilador.compile(code)
    
    # Assert
    assert compile_result == "Error sintáctico: falta ';' en la línea 4"

# Prueba para error léxico por falta de std en cout
def test_lexical_error_falta_std():
    # Arrange
    code = """
    #include <iostream>
    
    int main() {
        cout << "Hello world" << std::endl;
    }
    """
    
    compilador = compiler()
    
    # Act
    compile_result = compilador.compile(code)
    
    # Assert
    assert compile_result == "Error léxico: no se reconoce cout en la línea 4"

# Prueba para error sintáctico por falta de función main
def test_syntax_error_falta_funcion_main():
    # Arrange
    code = """
    #include <iostream>
    
    int suma(int a, int b) {
        return a + b;
    }
    """
    
    compilador = compiler()
    
    # Act
    compile_result = compilador.compile(code)
    if compile_result == "Compilado exitosamente":
        execution_result = compilador.execute_code()  
    else: 
        execution_result = compile_result
    
    # Assert
    assert compile_result == "Error sintáctico: no se encontró una función main"
```