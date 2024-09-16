# Actividad 4 - CC3S2

## Explorando diferentes formas de fusionar en Git – Parte 1

**Objetivo:**  En esta actividad, exploraremos el proceso de fusionar dos ramas en Git utilizando tres 
métodos diferentes: fast-forward, no-fast-forward, y squash. A través de los ejemplos, comprenderás 
cómo funcionan y cuándo es recomendable utilizar cada tipo de fusión.

### 1. Fusión Fast-forward (git merge --ff)

La fusión fast-forward es la forma más simple de combinar ramas en Git. Solo es posible cuando la rama 
base no ha recibido nuevos commits desde que se creó la rama feature.

[![image.png](https://i.postimg.cc/sxbpnyXx/image.png)](https://postimg.cc/K3rkz6th)

### 2. Fusión No-fast-forward (git merge --no-ff)

La fusión no-fast-forward crea un nuevo commit de fusión. Es útil para preservar el contexto de la 
fusión, especialmente en equipos donde se requiere más claridad en el historial de cambios.

[![image.png](https://i.postimg.cc/jS4Mjw2h/image.png)](https://postimg.cc/WdtGW4MD)

### 3. Fusión squash (git merge --squash)

La fusión squash combina todos los cambios de una rama en un solo commit en la rama principal. Este 
método es útil cuando se quiere mantener un historial de commits limpio.

[![image.png](https://i.postimg.cc/yNN24XjR/image.png)](https://postimg.cc/87qZLvqk)

## Ejercicios

### Clona un repositorio Git con múltiples ramas.

*Para este ejercicio utilizaremos el siguiente repositorio:* 
https://github.com/DevTips/DevTips-Starter-Kit


- Identifica dos ramas que puedas fusionar utilizando git merge --ff.
[![image.png](https://i.postimg.cc/1RNd0z4p/image.png)](https://postimg.cc/F1NGNNyR)

- Haz el proceso de fusión utilizando git merge --ff.
[![image.png](https://i.postimg.cc/j2r44tkX/image.png)](https://postimg.cc/TLCbRMxL)
*Arreglando conflictos en el proceso de fusión*
[![image.png](https://i.postimg.cc/6QJVX9BN/image.png)](https://postimg.cc/v4hx7w1P)
- Verifica el historial con git log --graph --oneline.
[![image.png](https://i.postimg.cc/GpCDfqjL/image.png)](https://postimg.cc/18v4n0T2)


**Pregunta:** ¿En qué situaciones recomendarías evitar el uso de git merge --ff? Reflexiona sobre las desventajas de este método.

*Recomendaría evitar el uso de ```git merge --ff``` cuando se quiera preservar el contexto de los commits que se vienen realizando. Por ejemplo, en un equipo donde varios desarrolladores trabajan en ramas separadas, se requiere identificar qué cambios fueron hechos en cada rama y cuándo se integraron en la rama principal. Esto facilitaría la revisión de código y auditoría del proyecto.*

### Simula un flujo de trabajo de equipo.

- Trabaja en dos ramas independientes, creando diferentes cambios en cada una.
[![image.png](https://i.postimg.cc/6pJx4mKf/image.png)](https://postimg.cc/Tp94ZQpK)
[![image.png](https://i.postimg.cc/WpyhCTmp/image.png)](https://postimg.cc/XXwjyMDt)
- Fusiona ambas ramas con git merge --no-ff para ver cómo se crean los commits de fusión.
[![image.png](https://i.postimg.cc/Qx51qFLZ/image.png)](https://postimg.cc/CzhRhLLc)
- Observa el historial utilizando git log --graph --oneline.
[![image.png](https://i.postimg.cc/6q8SPdr0/image.png)](https://postimg.cc/kRdf6Rh6)

**Pregunta:** ¿Cuáles son las principales ventajas de utilizar git merge --no-ff en un proyecto en equipo? 
¿Qué problemas podrían surgir al depender excesivamente de commits de fusión?

*Al utilizar ```git merge --no-ff``` en un proyecto en equipo nos ayuda a mantener fácilmente el contexto de las ramas de características, correcciones o cambios. Ya que podemos ver fácilmente qué commits pertenecen a una rama específica, lo que facilita la revisión del código y el seguimiento de cambios.
Además, se puede revertir una fusión mucho más fácil, ya que puedes revertir el commit de fusión completo en lugar de revertir commits individuales.*


### Resolver conflictos en una fusión non-fast-forward

En algunos casos, las fusiones no son tan sencillas y pueden surgir conflictos que necesitas resolver manualmente. Este ejercicio te guiará a través del proceso de manejo de conflictos.

1. Inicializa un nuevo repositorio:
[![image.png](https://i.postimg.cc/QM9wdg9W/image.png)](https://postimg.cc/t1b2rxzX)

2. Crea un archivo index.html y realiza un commit en la rama main:
[![image.png](https://i.postimg.cc/vZDS07vS/image.png)](https://postimg.cc/9D5pM7KG)

3. Crea y cambia a una nueva rama feature-update:
[![image.png](https://i.postimg.cc/Qxzqx2p0/image.png)](https://postimg.cc/QHp7fnYT)

4. Edita el archivo y realiza un commit en la rama feature-update:
[![image.png](https://i.postimg.cc/HkCtFfXK/image.png)](https://postimg.cc/LnNf1QyB)

5. Regresa a la rama main y realiza una edición en el mismo archivo:
[![image.png](https://i.postimg.cc/FHgxvDxK/image.png)](https://postimg.cc/18XFc02x)

6. Fusiona la rama feature-update con --no-ff y observa el conflicto:
[![image.png](https://i.postimg.cc/d1X26XJ5/image.png)](https://postimg.cc/FdyksTdS)

7. Git detectará un conflicto en index.html. Abre el archivo y resuelve el conflicto. Elimina las líneas de 
conflicto generadas por Git (<<<<<<<, =======, >>>>>>>) y crea la versión final del archivo con ambos 
cambios:
[![image.png](https://i.postimg.cc/jqp6JGg5/image.png)](https://postimg.cc/bdRS7Fjc)
8. Agrega el archivo corregido y completa la fusión:
[![image.png](https://i.postimg.cc/nzs7XkqB/image.png)](https://postimg.cc/wyp3PDfj)
9. Verifica el historial para confirmar la fusión y el commit de resolución de conflicto:
[![image.png](https://i.postimg.cc/J43XHtH6/image.png)](https://postimg.cc/Vd6v3fRn)

**Preguntas:**
- ¿Qué pasos adicionales tuviste que tomar para resolver el conflicto?

    *Tuve que buscar el archivo donde se generó el conflicto para luego editarlo manualmente a la versión final que deseo registrar en el commit para finalmente ejecutar los comandos:*

        git add index.html
        git commit

- ¿Qué estrategias podrías emplear para evitar conflictos en futuros desarrollos colaborativos?

    *Una de las estrategias que podríamos emplear para evitar conflictos sería ponernos de acuerdo para evitar editar el mismo archivo. Es decir, asignarnos a cada colaborador una responsabilidad para encargarse de la elaboración de cierta parte del proyecto.*

### Ejercicio: Comparar los historiales con git log después de diferentes fusiones

Este ejercicio te permitirá observar las diferencias en el historial generado por fusiones fast-forward, 
non-fast-forward y squash.

1. Crea un nuevo repositorio y realiza varios commits en dos ramas:
[![image.png](https://i.postimg.cc/15RmMzYY/image.png)](https://postimg.cc/HjK1kTmQ)
[![image.png](https://i.postimg.cc/cLrsybWR/image.png)](https://postimg.cc/YvBcQ8h0)

2. Fusiona feature-1 usando fast-forward:
[![image.png](https://i.postimg.cc/k4d9SMbs/image.png)](https://postimg.cc/XZxTSbxB)

3. Fusiona feature-2 usando non-fast-forward:
[![image.png](https://i.postimg.cc/285YhKVs/image.png)](https://postimg.cc/NLZZwb8D)
[![image.png](https://i.postimg.cc/d0GcJMxy/image.png)](https://postimg.cc/NyGzxnYs)

4. Realiza una nueva rama feature-3 con múltiples commits y fusiónala con squash:
[![image.png](https://i.postimg.cc/s2jbCB7t/image.png)](https://postimg.cc/G4fXkmMQ)

5. Compara el historial de Git:
- **Historial Fast-forward:** git log --graph --oneline --merges --first-parent --branches
[![image.png](https://i.postimg.cc/4x7mbdYR/image.png)](https://postimg.cc/HrmYTT06)
- **Historial Non-fast-forward:** git log --graph --oneline –merges
 [![image.png](https://i.postimg.cc/ZRZnSxVJ/image.png)](https://postimg.cc/HJZd05qN)
- **Historial con Squash:** git log --graph --oneline --merges --decorate --all

    [![image.png](https://i.postimg.cc/L5Q8jKRs/image.png)](https://postimg.cc/p58vtSmN)


