# Actividad 3 - CC3S2

## Introducción a Git - conceptos básicos y operaciones esenciales

**Objetivo:** Familiarizarse con los conceptos básicos de Git y realizar operaciones esenciales, como la 
configuración inicial, creación de repositorios, preparación y confirmación de cambios, visualización 
de historial, y gestión de branches.

## Conceptos básicos de Git: Comienza con una experiencia práctica

### git config: Preséntate a Git



[![git-config.png](https://i.postimg.cc/Xv8HSnPd/git-config.png)](https://postimg.cc/p9mYKMRL)



### git init: Donde comienza tu viaje de código

[![git-init.png](https://i.postimg.cc/rsdQrxwN/git-init.png)](https://postimg.cc/4Hg6CKtY)



### git add: Preparando tu código 

[![git-add.png](https://i.postimg.cc/9XSxj8L8/git-add.png)](https://postimg.cc/yWmhmP4c)



### git commit: registra cambios

[![git-commit.png](https://i.postimg.cc/4Nvs79Hg/git-commit.png)](https://postimg.cc/YhSJTjxn)


### git log: Recorrer el árbol de commits


[![git-log.png](https://i.postimg.cc/cJ2V5xth/git-log.png)](https://postimg.cc/5H57XM3Q)




Por ejemplo, también puede mejorar la perspectiva de la siguiente manera:


```
 git log --graph --pretty=format:'%x09 %h %ar ("%an") %s'
```

**Pregunta:** ¿ Cual es la salida de este comando? 

[![git-log-graph.png](https://i.postimg.cc/5yhy4drS/git-log-graph.png)](https://postimg.cc/zHk87M8y)

Intentemos el comando git log en este ejercicio. Primero, actualiza el archivo README.md y crea un nuevo archivo 
CONTRIBUTING.md:

[![git-log-oneline.png](https://i.postimg.cc/Z0kt32v4/git-log-oneline.png)](https://postimg.cc/hQ05RC05)

## Trabajar con branches: La piedra angular de la colaboración

### git branch: Entendiendo los conceptos básicos de Git branch

[![git-branch.png](https://i.postimg.cc/gj3dMGWn/git-branch.png)](https://postimg.cc/dZQz3PDY)

### git checkout/git switch: Cambiar entre branches

[![image.png](https://i.postimg.cc/7h183X3z/image.png)](https://postimg.cc/vxmNMrS8)

#### Ejemplos adicionales:

 **Crear una brach desde una branch específica**
 
 [![image.png](https://i.postimg.cc/mkyJzk4N/image.png)](https://postimg.cc/xNqtB0cc)


### git merge \<Branch Name\>: Fusionando branches

[![image.png](https://i.postimg.cc/FRjn8zY5/image.png)](https://postimg.cc/xJ1Rb0Gt)

### git branch -d: Eliminando una Branch

[![image.png](https://i.postimg.cc/dVLNv4h9/image.png)](https://postimg.cc/nXfGGKYs)


-----

## Preguntas

- ¿Cómo te ha ayudado Git a mantener un historial claro y organizado de tus cambios?

    *Git me ayuda a mantener un historial claro y organizado al usar commits que me permiten registrar los cambios que realizo etiquetando cada commit con un mensaje que describe dicho cambio. Además, el uso de ramas y comandos de fusión  me ayudan a combinar cambios de forma controlada, preservando el historial y permitiendo revisar cada modificación.*

- ¿Qué beneficios ves en el uso de branches para desarrollar nuevas características o corregir errores?

    *El uso de branches me permite desarrollar nuevas características o corregir errores de forma aislada y segura, ya que los cambios realizados en la rama no afectan al código principal. Esto facilita la colaboración y experimentación, ya que nos permite integrar cambios de forma controlada cuando estén listos.*

-----

## Ejercicios

### Ejercicio 1: Manejo avanzado de branches y resolución de conflictos

**Objetivo:** Practicar la creación, fusión y eliminación de ramas, así como la resolución de conflictos 
que puedan surgir durante la fusión.

**Instrucciones**

1. Crear una nueva rama para una característica:
    - Crea una nueva rama llamada feature/advanced-feature desde la rama main:
    
    [![image.png](https://i.postimg.cc/XYRLW3SV/image.png)](https://postimg.cc/xXPMGw17)

2. Modificar archivos en la nueva rama:
    
    - Edita el archivo main.py para incluir una función adicional:
    
    [![image.png](https://i.postimg.cc/VL5Wb5zf/image.png)](https://postimg.cc/ppbFwW94)

    - Añade y confirma estos cambios en la rama feature/advanced-feature:
    
    [![image.png](https://i.postimg.cc/fWqxZZm6/image.png)](https://postimg.cc/0rm6dTtf)
    
3. Simular un desarrollo paralelo en la rama main:

    - Cambia de nuevo a la rama main:
    
    [![image.png](https://i.postimg.cc/zBXgZPBz/image.png)](https://postimg.cc/bGWJ1gkW)

    - Edita el archivo main.py de forma diferente (por ejemplo, cambia el mensaje del print original):
    
    [![image.png](https://i.postimg.cc/9QdR4jwX/image.png)](https://postimg.cc/CRKLtX49)
    
    - Añade y confirma estos cambios en la rama main:
    
    [![image.png](https://i.postimg.cc/tg91WmF3/image.png)](https://postimg.cc/5XkNMg7y)

4. Intentar fusionar la rama feature/advanced-feature en main:
    - Fusiona la rama feature/advanced-feature en main:
    
    [![image.png](https://i.postimg.cc/9Mnr3mKb/image.png)](https://postimg.cc/hzVSTBSQ)

5. Resolver el conflicto de fusión:
    
    - Git generará un conflicto en main.py. Abre el archivo y resuelve el conflicto manualmente, eligiendo cómo combinar las dos versiones.
    
        [![image.png](https://i.postimg.cc/SQHfCkRc/image.png)](https://postimg.cc/kDFSdrx5)
    
    - Después de resolver el conflicto, añade el archivo resuelto y completa la fusión:
    [![image.png](https://i.postimg.cc/cLBRp3mc/image.png)](https://postimg.cc/4YnHtmjK)

6. Eliminar la rama fusionada:
    - Una vez que hayas fusionado con éxito y resuelto los conflictos, elimina la rama feature/advanced-feature:

    [![image.png](https://i.postimg.cc/BvZT4v7f/image.png)](https://postimg.cc/K1Vk5my0)



### Ejercicio 2: Exploración y manipulación del historial de commits

**Objetivo:** Aprender a navegar y manipular el historial de commits usando comandos avanzados de 
Git.

**Instrucciones:**

1. Ver el historial detallado de commits:

    - Usa el comando git log para explorar el historial de commits, pero esta vez con más detalle:
    [![image.png](https://i.postimg.cc/C13nBM71/image.png)](https://postimg.cc/34ZxzTP5)

    - Examina las diferencias introducidas en cada commit. ¿Qué cambios fueron realizados en cada 
    uno?
    [![image.png](https://i.postimg.cc/bNj2qJdV/image.png)](https://postimg.cc/rzQpJq15)

2. Filtrar commits por autor:
    - Usa el siguiente comando para mostrar solo los commits realizados por un autor específico: 
    [![image.png](https://i.postimg.cc/Qd89WyQp/image.png)](https://postimg.cc/svLDkK0X)

3. Revertir un commit:
    - Imagina que el commit más reciente en main.py no debería haberse hecho. Usa git revert para  revertir ese commit:
    
        [![image.png](https://i.postimg.cc/133XzNSB/image.png)](https://postimg.cc/ZCX47nCv)

    - Verifica que el commit de reversión ha sido añadido correctamente al historial.
    
        [![image.png](https://i.postimg.cc/T3Nw5YY6/image.png)](https://postimg.cc/mPMR04HX)

4. Rebase interactivo:

    - Usa el siguiente comando para empezar el rebase interactivo:
    [![image.png](https://i.postimg.cc/sgbzRBgv/image.png)](https://postimg.cc/sMPqYgSr)
    [![image.png](https://i.postimg.cc/pd8HV2mk/image.png)](https://postimg.cc/KKZVJhrg)
    
    - En el editor que se abre, combina los últimos tres commits en uno solo utilizando la opción squash
    [![image.png](https://i.postimg.cc/pVktLcdN/image.png)](https://postimg.cc/6T7PH0Rz)

5. Visualización gráfica del historial:
    - Usa el siguiente comando para ver una representación gráfica del historial de commits:
    [![image.png](https://i.postimg.cc/bJT4ddp0/image.png)](https://postimg.cc/YGvdsr4j)

    -  Reflexiona sobre cómo el historial de tu proyecto se visualiza en este formato. ¿Qué información adicional puedes inferir?
    
        *Debido a que el historial del proyecto se visualiza gráficamente, donde las ramas son representandas por líneas, podemos inferir a qué rama pertenece cada commit efectuado.*
        
### Ejercicio 3: Creación y gestión de branches desde commits específicos

**Objetivo:** Practicar la creación de ramas desde commits específicos y comprender cómo Git maneja las referencias históricas.

**Instrucciones:**

1. Crear una nueva rama desde un commit específico:
    - Usa el historial de commits (git log --oneline) para identificar un commit antiguo desde el cual crear una nueva rama:
    
        [![image.png](https://i.postimg.cc/BvCmByk4/image.png)](https://postimg.cc/PLPbt6dR)
    
    - Crea una nueva rama bugfix/rollback-feature desde ese commit:
    
        [![image.png](https://i.postimg.cc/FRWG2Sh6/image.png)](https://postimg.cc/62ZdZy2V)

2. Modificar y confirmar cambios en la nueva rama:
    - Realiza algunas modificaciones en main.py que simulen una corrección de errores:
    
    [![image.png](https://i.postimg.cc/9QdR4jwX/image.png)](https://postimg.cc/CRKLtX49)

    [![image.png](https://i.postimg.cc/MHg5G8Mb/image.png)](https://postimg.cc/rRCxh39K)

    - Añade y confirma los cambios en la nueva rama:

    [![image.png](https://i.postimg.cc/gk64TrQM/image.png)](https://postimg.cc/1fspgR96)
    
3. Fusionar los cambios en la rama principal:
    - Cambia de nuevo a la rama main y fusiona la rama bugfix/rollback-feature:
    [![image.png](https://i.postimg.cc/KYsJWLGH/image.png)](https://postimg.cc/xkMvJXbv)

4. Explorar el historial después de la fusión:
    - Usa git log y git log --graph para ver cómo se ha integrado el commit en el historial:
    [![image.png](https://i.postimg.cc/Bb2ptVxr/image.png)](https://postimg.cc/PvrYRKVy)

        [![image.png](https://i.postimg.cc/pVjq0pgs/image.png)](https://postimg.cc/grYVjkch)
        
5. Eliminar la rama bugfix/rollback-feature:
    - Una vez fusionados los cambios, elimina la rama bugfix/rollback-feature:
    [![image.png](https://i.postimg.cc/x1f5TgqZ/image.png)](https://postimg.cc/3dqmtXXj)

### Ejercicio 4: Manipulación y restauración de commits con git reset y git restore

**Objetivo:** Comprender cómo usar git reset y git restore para deshacer cambios en el historial y en el 
área de trabajo.

**Instrucciones:**

1. Hacer cambios en el archivo main.py:
    - Edita el archivo main.py para introducir un nuevo cambio:
    
        [![image.png](https://i.postimg.cc/CxcNZDqx/image.png)](https://postimg.cc/cv8Y2vhp)

    - Añade y confirma los cambios:
    
        [![image.png](https://i.postimg.cc/ydZXrbrD/image.png)](https://postimg.cc/ftM9VBss)
    
2. Usar git reset para deshacer el commit:
    - Deshaz el commit utilizando git reset para volver al estado anterior:
    [![image.png](https://i.postimg.cc/D0QQ7bhF/image.png)](https://postimg.cc/30R0BNWb)
    - Verifica que el commit ha sido eliminado del historial y que el archivo ha vuelto a su estado 
anterior.
[![image.png](https://i.postimg.cc/hjTT07fx/image.png)](https://postimg.cc/34rk8NjJ)
[![image.png](https://i.postimg.cc/MHg5G8Mb/image.png)](https://postimg.cc/rRCxh39K)

3. Usar git restore para deshacer cambios no confirmados:
    - Realiza un cambio en README.md y no lo confirmes:
        
        [![image.png](https://i.postimg.cc/Hnm5vsyN/image.png)](https://postimg.cc/BLhXX3N5)
        [![image.png](https://i.postimg.cc/x18m4ZX9/image.png)](https://postimg.cc/gx9rwNy7)

    - Usa git restore para deshacer este cambio no confirmado:
    
        [![image.png](https://i.postimg.cc/4y1cDkvx/image.png)](https://postimg.cc/64yTZP1k)
    - Verifica que el cambio no confirmado ha sido revertido.
    
        [![image.png](https://i.postimg.cc/TYCmQxYk/image.png)](https://postimg.cc/yk3kYwR9)


### Ejercicio 5: Trabajo colaborativo y manejo de Pull Requests

**Objetivo:** Simular un flujo de trabajo colaborativo utilizando ramas y pull requests.

**Instrucciones:**

1. Crear un nuevo repositorio remoto:
    - Usa GitHub o GitLab para crear un nuevo repositorio remoto y clónalo localmente: 
    [![image.png](https://i.postimg.cc/YqGkDftJ/image.png)](https://postimg.cc/1fQLfFnH)
    [![image.png](https://i.postimg.cc/Rh8mVqLs/image.png)](https://postimg.cc/dZ8p5sXr)
    *Repositorio usado*: https://github.com/GabrielQuiroz25/Nuevo-Repositorio-Remoto

2. Crear una nueva rama para desarrollo de una característica:
    - En tu repositorio local, crea una nueva rama feature/team-feature:
    [![image.png](https://i.postimg.cc/Xv3bvR9b/image.png)](https://postimg.cc/k2jZ1hj1)

3. Realizar cambios y enviar la rama al repositorio remoto:
    - Realiza cambios en los archivos del proyecto y confírmalos:
    [![image.png](https://i.postimg.cc/CLkMLH9b/image.png)](https://postimg.cc/9rXHLTmf)

    - Envía la rama al repositorio remoto:
    [![image.png](https://i.postimg.cc/9f8CNxqH/image.png)](https://postimg.cc/2qZs17w0)


4. Abrir un Pull Request:
    - Abre un Pull Request (PR) en la plataforma remota (GitHub/GitLab) para fusionar feature/team-feature con la rama main.
    [![image.png](https://i.postimg.cc/BbxWsNt6/image.png)](https://postimg.cc/FksCVyy5)
    - Añade una descripción detallada del PR, explicando los cambios realizados y su propósito.
    - [![image.png](https://i.postimg.cc/SNSX5PnJ/image.png)](https://postimg.cc/rzHFRQCk)
    
5. Revisar y Fusionar el Pull Request:
    - Simula la revisión de código, comenta en el PR y realiza cualquier cambio necesario basado en la retroalimentación.
    [![image.png](https://i.postimg.cc/GmZmcgmP/image.png)](https://postimg.cc/pmJHCZ8y)
[![image.png](https://i.postimg.cc/d19sjqmn/image.png)](https://postimg.cc/Q9HZXZzW)

    - Una vez aprobado, fusiona el PR en la rama main.
    [![image.png](https://i.postimg.cc/J041T9p8/image.png)](https://postimg.cc/HcRDnPGv)

6. Eliminar la rama remota y local:
    - Después de la fusión, elimina la rama tanto local como remotamente:
    [![image.png](https://i.postimg.cc/RFv9Fk5t/image.png)](https://postimg.cc/2q9g9X5j)

### Ejercicio 6: Cherry-Picking y Git Stash

**Objetivo:** Aprender a aplicar commits específicos a otra rama utilizando git cherry-pick y a guardar temporalmente cambios no confirmados utilizando git stash.

**Instrucciones:**

1. Hacer cambios en main.py y confirmarlos:
    - Realiza y confirma varios cambios en main.py en la rama main:
    [![image.png](https://i.postimg.cc/tCsbYdfB/image.png)](https://postimg.cc/svCqLW3W)

2. Crear una nueva rama y aplicar el commit específico:
    - Crea una nueva rama feature/cherry-pick y aplícale el commit específico:
    [![image.png](https://i.postimg.cc/N05Cxb6n/image.png)](https://postimg.cc/67xhWr1V)

3. Guardar temporalmente cambios no confirmados:
    - Realiza algunos cambios en main.py pero no los confirmes:
    [![image.png](https://i.postimg.cc/dV05qnx0/image.png)](https://postimg.cc/BXdTp5sW)       

    - Guarda temporalmente estos cambios utilizando git stash:
    [![image.png](https://i.postimg.cc/cL5X6YpB/image.png)](https://postimg.cc/sM7pNBDM)

4. Aplicar los cambios guardados:
    - Realiza otros cambios y confírmalos si es necesario.
    [![image.png](https://i.postimg.cc/GpWKxRhB/image.png)](https://postimg.cc/qtG2p9K0)
    [![image.png](https://i.postimg.cc/fLYKHPJ8/image.png)](https://postimg.cc/34JmNnjG)
    - Luego, recupera los cambios guardados anteriormente:
    [![image.png](https://i.postimg.cc/15vKYw31/image.png)](https://postimg.cc/jLJNDWfM)
    [![image.png](https://i.postimg.cc/134KxX8n/image.png)](https://postimg.cc/WdLZg26T)

5. Revisar el historial y confirmar la correcta aplicación de los cambios:
    - Usa git log para revisar el historial de commits y verificar que todos los cambios se han aplicado 
correctamente.
    [![image.png](https://i.postimg.cc/JnC3BQPZ/image.png)](https://postimg.cc/zLpHsTmG)
