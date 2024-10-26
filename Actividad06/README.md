# Actividad 6 - CC3S2

## Navegando conflictos y versionado en un entorno devOps

**Objetivo:**  Gestionar conflictos en Git, realizar fusiones complejas, utilizar herramientas para comparar y resolver conflictos, aplicar buenas prácticas en el manejo del historial de versiones, y usar versionado semántico en un entorno de integración continua (CI).

**Herramientas:**
- Git
- Un entorno de desarrollo (Visual Studio Code, terminal, etc.)
- Un repositorio en GitHub o GitLab (opcional, puede ser local)

**Contexto:**

En un entorno de desarrollo colaborativo, los conflictos son inevitables cuando varios desarrolladores trabajan en la misma base de código. Resolver estos conflictos es crucial para mantener un flujo de trabajo eficiente en DevOps.

Los conflictos ocurren cuando dos ramas modifican la misma línea de un archivo y luego se intenta fusionarlas. Git no puede decidir qué cambio priorizar, por lo que la resolución manual es necesaria.

Cómo fusionar conflictos en Git:

1. Identificar conflictos: Usa git status para ver los archivos en conflicto.

2. Examinar los archivos: Busca los marcadores de conflicto (<<<<<<<, =======, >>>>>>>) en los archivos.

3. Resolver los conflictos: Elige qué cambios conservar (rama actual o fusionada) o mezcla ambos.

4. Commit de los archivos resueltos: Después de resolver, añade los archivos al staging y realiza el commit.


### Instrucciones:
#### 1. Inicialización del proyecto y creación de ramas

- Paso 1: Crea un nuevo proyecto en tu máquina local.

```bash
$ mkdir proyecto-colaborativo
$ cd proyecto-colaborativo
```

- Paso 2: Inicializa Git en tu proyecto.

```bash
$ git init
```

- Paso 3: Crea un archivo de texto llamado archivo_colaborativo.txt y agrega algún contenido inicial.

```bash
$ echo "Este es el contenido inicial del proyecto" > archivo_colaborativo.txt
```

- Paso 4: Agrega el archivo al área de staging y haz el primer commit.

```bash
$ git add .
$ git commit -m "Commit inicial con contenido base"
```

- Paso 5: Crea dos ramas activas: main y feature-branch.

```bash
$ git branch feature-branch # Crear una nueva rama
```

- Paso 6: Haz checkout a la rama feature-branch y realiza un cambio en el archivo archivo_colaborativo.txt.

```bash
$ git checkout feature-branch
$ echo "Este es un cambio en la feature-branch" >> archivo_colaborativo.txt
$ git add .
$ git commit -m "Cambios en feature-branch"
```

- Paso 7: Regresa a la rama main y realiza otro cambio en la misma línea del archivo archivo_colaborativo.txt.

```bash
$ git checkout main
$ echo "Este es un cambio en la rama main" >> archivo_colaborativo.txt
$ git add .
$ git commit -m "Cambios en main"
```

[![Actividad6-1.png](https://i.postimg.cc/vmvtPL50/Actividad6-1.png)](https://postimg.cc/v1cnTnqn)

#### 2. Fusión y resolución de conflictos

- Paso 1: Intenta fusionar feature-branch en main. Se espera que surjan conflictos de fusión.

```bash
$ git merge feature-branch
```

- Paso 2: Usa git status para identificar los archivos en conflicto. Examina los archivos afectados y resuelve manualmente los conflictos, conservando las líneas de código más relevantes para el proyecto.

```bash
$ git status
$ git checkout --theirs <archivo> # Si decides aceptar los cambios de feature-branch
$ git checkout --ours <archivo> # Si decides aceptar los cambios de main
```

- Paso 3: Una vez resueltos los conflictos, commitea los archivos y termina la fusión
```bash
$ git add .
$ git commit -m "Conflictos resueltos"
```

[![Actividad6-2.png](https://i.postimg.cc/c1zM5J8G/Actividad6-2.png)](https://postimg.cc/Lhz1J2Tx)

#### 3. Simulación de fusiones y uso de git diff 

- Paso 1: Simula una fusión usando git merge --no-commit --no-ff para ver cómo se comportarían los cambios antes de realizar el commit.

```bash
$ git merge --no-commit --no-ff feature-branch
$ git diff --cached # Ver los cambios en el área de staging
$ git merge --abort # Abortar la fusión si no es lo que se esperaba
```

[![Actividad6-3.png](https://i.postimg.cc/TPQnj2XS/Actividad6-3.png)](https://postimg.cc/t1Z1pjJt)

#### 4. Uso de git mergetool

- Paso 1: Configura git mergetool con una herramienta de fusión visual (puedes usar meld, vimdiff, o Visual Studio Code).

```bash
$ git config --global merge.tool <nombre-herramienta>
$ git mergetool # Iniciar la herramienta de fusión 
```

[![image.png](https://i.postimg.cc/jj029pRX/image.png)](https://postimg.cc/SndmYt22)

- Paso 2: Usa la herramienta gráfica para resolver un conflicto de fusión.

[![image.png](https://i.postimg.cc/nrBpvzDf/image.png)](https://postimg.cc/64WkKBcM)

[![image.png](https://i.postimg.cc/rw8Mrqy7/image.png)](https://postimg.cc/ZCDGktdL)

[![image.png](https://i.postimg.cc/8cRg7021/image.png)](https://postimg.cc/Zv5MgVYg)

#### 5. Uso de git revert y git reset 

- Paso 1: Simula la necesidad de revertir un commit en main debido a un error. Usa git revert para crear un commit que deshaga los cambios.

```bash
$ git revert <commit_hash>
```

[![image.png](https://i.postimg.cc/TPLSysbZ/image.png)](https://postimg.cc/06vZFccf)

- Paso 2: Realiza una prueba con git reset --mixed para entender cómo reestructurar el historial de commits sin perder los cambios no commiteados.

```bash
$ git reset --mixed <commit_hash>
```

[![image.png](https://i.postimg.cc/63VMnxp1/image.png)](https://postimg.cc/JDn3CgJb)

#### 6. Versionado semántico y etiquetado

- Paso 1: Aplica versionado semántico al proyecto utilizando tags para marcar versiones importantes.

```bash
$git tag -a v1.0.0 -m "Primera versión estable"
$ git push origin v1.0.0
```

[![image.png](https://i.postimg.cc/3R9q401c/image.png)](https://postimg.cc/dkk6g1z2)

[![image.png](https://i.postimg.cc/yxZrfpBw/image.png)](https://postimg.cc/YLt303v3)

#### 7. Aplicación de git bisect para depuración

- Paso 1: Usa git bisect para identificar el commit que introdujo un error en el código.

```bash
$ git bisect start
$ git bisect bad # Indica que la versión actual tiene un error
$ git bisect good <último_commit_bueno>
# Continúa marcando como "good" o "bad" hasta encontrar el commit que introdujo el error
$ git bisect reset # Salir del modo bisect
```

[![image.png](https://i.postimg.cc/2SQdHRWQ/image.png)](https://postimg.cc/K1YgzWJj)

*Concluímos que el error posiblemente se introdujo en el commit* : `47eb454`

#### 8. Documentación y reflexión 
- Paso 1: Documenta todos los comandos usados y los resultados obtenidos en cada paso.
- Paso 2: Reflexiona sobre la utilidad de cada comando en un flujo de trabajo de DevOps


`git checkout --theirs` *selecciona los cambios de la rama que se está fusionando y* `git checkout --ours` *selecciona los cambios de la rama actual. En un flujo de trabajo DevOps, estos comandos permiten un control preciso de los conflictos y ayudan a priorizar qué cambios aplicar sin necesidad de editar manualmente archivos conflictivos.*

`git merge --no-commit --no-ff` *fusiona cambios sin hacer un commit automático ni una fusión fast-forward, permitiendo revisar y hacer ajustes antes de confirmar la fusión. Esto es útil en DevOps para asegurarse de que los cambios cumplen con las políticas de calidad o seguridad antes de integrarlos al código base.*

`git diff --cached` *muestra las diferencias entre el área de staging y el último commit. Es esencial en DevOps para verificar qué cambios están listos para ser confirmados, ayudando a revisar las modificaciones antes de hacer un commit final.*

`git merge --abort` *cancela un intento de fusión y restaura el estado previo. En un entorno DevOps, esto es crucial cuando una fusión falla o los conflictos son muy complejos ya que permite deshacer la fusión sin dejar el repositorio en un estado inestable.*

`git mergetool` *abre la herramienta visual designada para resolver conflictos de fusión. En DevOps, donde las fusiones pueden involucrar múltiples cambios en archivos ayuda a evitar errores humanos ya que la resolución de conflictos se hace más intuitiva y simplifica el proceso.*

`git revert` *deshace cambios de un commit específico creando un nuevo commit. En DevOps, es útil para deshacer cambios sin alterar el historial, manteniendo la integridad del flujo de trabajo y permitiendo la trazabilidad de los cambios.*

`git reset` *permite mover el HEAD y restablecer el área de staging o el área de trabajo. Es poderoso para deshacer commits o cambios locales, lo que es útil en DevOps para corregir errores antes de que los cambios sean visibles para el equipo o lleguen al entorno de producción.*

`git tag` *marca puntos específicos en el historial de commits, como versiones de software. En DevOps, se usa para identificar versiones de lanzamiento, facilitando el control de versiones, la implementación continua y el seguimiento de cambios entre versiones.*

`git bisect` *realiza una búsqueda binaria en el historial de commits para encontrar un commit que introdujo algún error. En DevOps, es muy útil para depurar y localizar rápidamente el origen de errores en sistemas de integración continua, donde un bug puede aparecer en un gran número de commits.*


### Preguntas

#### 1. Ejercicio para git checkout --ours y git checkout --theirs

**Contexto:** En un sprint ágil, dos equipos están trabajando en diferentes ramas. Se produce un conflicto de fusión en un archivo de configuración crucial. El equipo A quiere mantener sus cambios mientras el equipo B solo quiere conservar los suyos. El proceso de entrega continua está detenido 
debido a este conflicto.

**Pregunta:**
- ¿Cómo utilizarías los comandos git checkout --ours y git checkout --theirs para resolver este conflicto de manera rápida y eficiente? Explica cuándo preferirías usar cada uno de estos comandos y cómo impacta en la pipeline de CI/CD. ¿Cómo te asegurarías de que la resolución elegida no comprometa la calidad del código?


*Para resolver rápidamente un conflicto de fusión en un archivo de configuración crucial, primero deberíamos realizar una evaluación rápida del impacto de los cambios de ambos equipos. Si los cambios del equipo A son más críticos, usarían* `git checkout --ours`*; si los del equipo B son más relevantes, usarían* `git checkout --theirs`. *Después de resolver el conflicto y hacer commit, se debería asegurar de que la calidad del código no se vea comprometida mediante revisiones de código, ejecución de pruebas automatizadas en la pipeline de CI/CD y monitoreo post-despliegue para verificar la estabilidad del sistema.*


#### 2. Ejercicio para git diff

**Contexto:** Durante una revisión de código en un entorno ágil, se observa que un pull request tiene una gran cantidad de cambios, muchos de los cuales no están relacionados con la funcionalidad principal. Estos cambios podrían generar conflictos con otras ramas en la pipeline de CI/CD.

**Pregunta:**
- Utilizando el comando git diff, ¿cómo compararías los cambios entre ramas para identificar diferencias específicas en archivos críticos? Explica cómo podrías utilizar git diff feature-branch..main para detectar posibles conflictos antes de realizar una fusión y cómo esto contribuye a mantener la estabilidad en un entorno ágil con CI/CD.


*Para comparar los cambios entre ramas y detectar diferencias en archivos críticos, usaríamos* `git diff feature-branch..main` *para identificar qué modificaciones ha introducido la rama de características (feature-branch) en comparación con la rama principal (main). Esto nos permitirá revisar específicamente los archivos críticos y detectar posibles conflictos o cambios innecesarios antes de la fusión. Al hacerlo, podemos evitar la introducción de problemas en la pipeline de CI/CD, contribuyendo a mantener la estabilidad del código en un entorno ágil, al resolver conflictos proactivamente antes de afectar la integración continua.*


#### 3. Ejercicio para git merge --no-commit --no-ff

**Contexto:** En un proyecto ágil con CI/CD, tu equipo quiere simular una fusión entre una rama de desarrollo y la rama principal para ver cómo se comporta el código sin comprometerlo inmediatamente en el repositorio. Esto es útil para identificar posibles problemas antes de completar la fusión.

**Pregunta:**
- Describe cómo usarías el comando git merge --no-commit --no-ff para simular una fusión en tu rama local. ¿Qué ventajas tiene esta práctica en un flujo de trabajo ágil con CI/CD, y cómo ayuda a minimizar errores antes de hacer commits definitivos? ¿Cómo automatizarías este paso dentro de una pipeline CI/CD?


*Para simular una fusión entre una rama de desarrollo y la rama principal sin comprometer cambios, usaría el comando* `git merge --no-commit --no-ff`*, lo que permite revisar y resolver conflictos antes de confirmar la fusión. Esto es útil en un flujo ágil con CI/CD, ya que ayuda a detectar problemas de integración anticipadamente, evitando afectar el código compartido o la pipeline. Para automatizarlo, en la pipeline CI/CD crearía un script que simule la fusión y corra las pruebas unitarias y de integración para validar la fusión simulada. Si las pruebas pasan, la fusión puede proceder de manera automática; si fallan, se alerta al equipo para revisión.*


#### 4. Ejercicio para git mergetool

**Contexto:** Tu equipo de desarrollo utiliza herramientas gráficas para resolver conflictos de manera colaborativa. Algunos desarrolladores prefieren herramientas como vimdiff o Visual Studio Code. En medio de un sprint, varios archivos están en conflicto y los desarrolladores prefieren 
trabajar en un entorno visual para resolverlos.

**Pregunta:**
- Explica cómo configurarías y utilizarías git mergetool en tu equipo para integrar herramientas gráficas que faciliten la resolución de conflictos. ¿Qué impacto tiene el uso de git mergetool en un entorno de trabajo ágil con CI/CD, y cómo aseguras que todos los miembros del equipo mantengan consistencia en las resoluciones?


*Para configurar y utilizar* `git mergetool` *con herramientas gráficas como Visual Studio Code o vimdiff, cada desarrollador debería configurar su herramienta preferida con los comandos* `git config --global merge.tool code` *para VS Code o* `git config --global merge.tool vimdiff` *para vimdiff, permitiendo que* `git mergetool` *abra automáticamente la herramienta seleccionada al resolver conflictos. Esto facilita la resolución visual y colaborativa de conflictos, acelerando el proceso en un entorno ágil, donde los conflictos pueden surgir frecuentemente en medio de un sprint. El impacto en un flujo de trabajo ágil con CI/CD es positivo, ya que permite resolver conflictos de forma más eficiente sin bloquear la integración continua y para asegurar consistencia, es importante que el equipo siga guías de estilo y prácticas estándar al resolver los conflictos, complementado con revisiones de código automatizadas en la pipeline de CI/CD, asegurando que los conflictos resueltos no introduzcan errores ni afecten la calidad del código.*


#### 5. Ejercicio para git reset

**Contexto:** En un proyecto ágil, un desarrollador ha hecho un commit que rompe la pipeline de CI/CD. Se debe revertir el commit, pero se necesita hacerlo de manera que se mantenga el código en el directorio de trabajo sin deshacer los cambios.

**Pregunta:**
- Explica las diferencias entre git reset --soft, git reset --mixed y git reset --hard. ¿En qué escenarios dentro de un flujo de trabajo ágil con CI/CD utilizarías cada uno? Describe un caso en el que usarías git reset --mixed para corregir un commit sin perder los cambios no commiteados y cómo afecta esto a la pipeline.


*En en un flujo de trabajo ágil con CI/CD utilizaría* `git reset --soft` *cuando un commit fue prematuro y se necesita hacer algunos ajustes antes de volver a confirmar sin perder el estado actual de los cambios.*
*Utilizaría* `git reset --mixed` *cuando al hacer un commit incorrecto, quieres deshacerlo y corregirlo, pero conservando los cambios en el directorio de trabajo para ajustarlos y volver a confirmarlos correctamente. Po último, usaría*`git reset --hard` *cuando es necesario deshacer completamente cambios que ya no son relevantes o cuando se desea restaurar el estado limpio de un commit anterior, perdiendo todos los cambios.*

*Un caso de uso de* `git reset --mixed` *sería cuando en un proyecto ágil con CI/CD, si un desarrollador ha hecho un commit que rompe la pipeline (por ejemplo, introdujo un bug o rompió alguna prueba), pero los cambios son parcialmente útiles, usaría* `git reset --mixed` *para deshacer el commit y eliminarlo del área de staging sin perder los cambios del directorio de trabajo. Esto permitiría revisar y corregir los errores en el código sin tener que reescribir todo desde cero. Luego de revisar y corregir, ya se podría volver a agregar los cambios y hacer un nuevo commit correcto. Esto evita que la pipeline se siga rompiendo y permite abordar el problema sin perder el trabajo realizado hasta el momento.*


#### 6. Ejercicio para git revert

**Contexto:** En un entorno de CI/CD, tu equipo ha desplegado una característica a producción, pero se 
ha detectado un bug crítico. La rama principal debe revertirse para restaurar la estabilidad, pero no 
puedes modificar el historial de commits debido a las políticas del equipo.

**Pregunta:**
- Explica cómo utilizarías git revert para deshacer los cambios sin modificar el historial de 
commits. ¿Cómo te aseguras de que esta acción no afecte la pipeline de CI/CD y permita una 
rápida recuperación del sistema? Proporciona un ejemplo detallado de cómo revertirías 
varios commits consecutivos.

#### 7. Ejercicio para git stash

**Contexto:** En un entorno ágil, tu equipo está trabajando en una corrección de errores urgente 
mientras tienes cambios no guardados en tu directorio de trabajo que aún no están listos para ser 
committeados. Sin embargo, necesitas cambiar rápidamente a una rama de hotfix para trabajar en la 
corrección.

**Pregunta:**
- Explica cómo utilizarías git stash para guardar temporalmente tus cambios y volver a 
ellos después de haber terminado el hotfix. ¿Qué impacto tiene el uso de git stash en un 
flujo de trabajo ágil con CI/CD cuando trabajas en múltiples tareas? ¿Cómo podrías 
automatizar el proceso de stashing dentro de una pipeline CI/CD?

#### 8. Ejercicio para .gitignore

**Contexto:** Tu equipo de desarrollo ágil está trabajando en varios entornos locales con 
configuraciones diferentes (archivos de logs, configuraciones personales). Estos archivos no deberían 
ser parte del control de versiones para evitar confusiones en la pipeline de CI/CD.

**Pregunta:**
- Diseña un archivo .gitignore que excluya archivos innecesarios en un entorno ágil de 
desarrollo. Explica por qué es importante mantener este archivo actualizado en un equipo 
colaborativo que utiliza CI/CD y cómo afecta la calidad y limpieza del código compartido en 
el repositorio.












