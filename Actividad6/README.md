# Actividad 6 - CC3S2

## Navegando conflictos y versionado en un entorno devOps

**Objetivo:**  Gestionar conflictos en Git, realizar fusiones complejas, utilizar herramientas para comparar y resolver conflictos, aplicar buenas prácticas en el manejo del historial de versiones, y usar versionado semántico en un entorno de integración continua (CI).

**Herramientas:**
- Git
- Un entorno de desarrollo (Visual Studio Code, terminal, etc.)
- Un repositorio en GitHub o GitLab (opcional, puede ser local)

**Contexto:**

En un entorno de desarrollo colaborativo, los conflictos son inevitables cuando varios desarrolladores trabajan en la misma base de código. Resolver estos conflictos es crucial para mantener un flujo de trabajo eficiente en DevOps.

Los conflictos ocurren cuando dos ramas modifican la misma línea de un archivo y luego se intenta 
fusionarlas. Git no puede decidir qué cambio priorizar, por lo que la resolución manual es necesaria.

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

- Paso 6: Haz checkout a la rama feature-branch y realiza un cambio en el archivo 
archivo_colaborativo.txt.

```bash
$ git checkout feature-branch
$ echo "Este es un cambio en la feature-branch" >> archivo_colaborativo.txt
$ git add .
$ git commit -m "Cambios en feature-branch"
```

- Paso 7: Regresa a la rama main y realiza otro cambio en la misma línea del archivo 
archivo_colaborativo.txt.

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

- Paso 2: Usa git status para identificar los archivos en conflicto. Examina los archivos afectados y 
resuelve manualmente los conflictos, conservando las líneas de código más relevantes para el 
proyecto.

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

- Paso 1: Simula una fusión usando git merge --no-commit --no-ff para ver cómo se comportarían los 
cambios antes de realizar el commit.

```bash
$ git merge --no-commit --no-ff feature-branch
$ git diff --cached # Ver los cambios en el área de staging
$ git merge --abort # Abortar la fusión si no es lo que se esperaba
```

[![Actividad6-3.png](https://i.postimg.cc/TPQnj2XS/Actividad6-3.png)](https://postimg.cc/t1Z1pjJt)

#### 4. Uso de git mergetool

- Paso 1: Configura git mergetool con una herramienta de fusión visual (puedes usar meld, vimdiff, o 
Visual Studio Code).

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

- Paso 1: Simula la necesidad de revertir un commit en main debido a un error. Usa git revert para 
crear un commit que deshaga los cambios.

```bash
$ git revert <commit_hash>
```

[![image.png](https://i.postimg.cc/TPLSysbZ/image.png)](https://postimg.cc/06vZFccf)

- Paso 2: Realiza una prueba con git reset --mixed para entender cómo reestructurar el historial de 
commits sin perder los cambios no commiteados.

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
