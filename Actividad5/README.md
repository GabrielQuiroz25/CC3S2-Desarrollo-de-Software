# Actividad 5 - CC3S2

## Entendiendo git rebase y git cherry-pick

**Objetivo:** Aprender a usar los comandos git rebase y git cherry-pick para mantener un historial de commits limpio y manejable en proyectos colaborativos. También explorarás cuándo y por qué utilizar estos comandos en lugar de los merges regulares.


### Parte 1: git rebase para mantener un historial lineal

1. **Introducción a Rebase:**

El rebase mueve tus commits a una nueva base, dándote un historial lineal y limpio. En lugar de fusionar ramas y mostrar un "commit de merge", el rebase integra los cambios aplicándolos en la parte superior de otra rama.

2. **Escenario de ejemplo:**

- Crea un nuevo repositorio Git y dos ramas, **`main`** y **`new-feature`**:

[![image.png](https://i.postimg.cc/QNFqcBcQ/image.png)](https://postimg.cc/ThXm6371)

- Crea y cambia a la rama **`new-feature`**:

[![image.png](https://i.postimg.cc/W3Cg5n0M/image.png)](https://postimg.cc/sQPMX56X)

[![image.png](https://i.postimg.cc/bNQkR1rt/image.png)](https://postimg.cc/fJRVztxz)

[![image.png](https://i.postimg.cc/V6x0qNcg/image.png)](https://postimg.cc/7GNLDwhJ)

Ahora, digamos que se han agregado nuevos commits a **`main`** mientras trabajabas en **`new-feature`**:

- Cambiar de nuevo a **`main`** y agregar nuevos commits

[![image.png](https://i.postimg.cc/ncZCpgVX/image.png)](https://postimg.cc/w3f6kWmz)

[![image.png](https://i.postimg.cc/BQgt6ptM/image.png)](https://postimg.cc/LnJmQzt1)

[![image.png](https://i.postimg.cc/wjjMsNmH/image.png)](https://postimg.cc/0bhPTbnH)


- **Tarea:** Realiza el rebase de **`new-feature`** sobre **`main`** con los siguientes comandos:

[![image.png](https://i.postimg.cc/sxzDfGrk/image.png)](https://postimg.cc/hzCqpjhs)

3. **Revisión:**

Después de realizar el rebase, visualiza el historial de commits con:

`git log --graph --oneline`

[![image.png](https://i.postimg.cc/SxRQKpBx/image.png)](https://postimg.cc/nX8fdNVy)

[![image.png](https://i.postimg.cc/NMqQb25K/image.png)](https://postimg.cc/LqDd8XkS)

4. **Momento de fusionar y completar el proceso de git rebase:**

- Cambiar a **`main`** y realizar una fusión fast-forward

[![image.png](https://i.postimg.cc/prkx20kj/image.png)](https://postimg.cc/CnZ97s3M)

[![image.png](https://i.postimg.cc/6q6J1rwp/image.png)](https://postimg.cc/S2PvnzJB)

[![image.png](https://i.postimg.cc/1tr1HWkd/image.png)](https://postimg.cc/cgCz1c47)


### Parte 2: git cherry-pick para la integración selectiva de commit

1. **Introducción a Cherry-pick:**

`git cherry-pick` te permite seleccionar commits individuales de una rama y aplicarlos en otra. Esto es útil 
cuando necesitas integrar una característica o corrección sin hacer merge de toda la rama.

2. **Escenario de ejemplo:**

- Inicializar un nuevo repositorio

[![image.png](https://i.postimg.cc/MZ9hpjq1/image.png)](https://postimg.cc/nMQddrsL)

- Agregar y commitear README.md inicial a **`main`**

[![image.png](https://i.postimg.cc/P5wcy3ZM/image.png)](https://postimg.cc/75qmYNKC)

- Crear y cambiar a una nueva rama **`add-base-documents`**

[![image.png](https://i.postimg.cc/YSNPKvdG/image.png)](https://postimg.cc/R3FdwZ54)

- Hacer cambios y commitearlos

    - Agregar `CONTRIBUTING.md`
    
    [![image.png](https://i.postimg.cc/rFdYynhL/image.png)](https://postimg.cc/hfB0prWC)

    - Agregar `LICENSE.txt`
    
    [![image.png](https://i.postimg.cc/J0sKn05Q/image.png)](https://postimg.cc/Zvh6sTg9)

- Echa un vistazo al log de la rama **`add-base-documents`**

[![image.png](https://i.postimg.cc/t4Nc81S1/image.png)](https://postimg.cc/FY1GLKQm)

Ahora, las ramas se ven como las del siguiente diagrama:

[![image.png](https://i.postimg.cc/GppXNXTN/image.png)](https://postimg.cc/k2kNRFcF)

3. **Tarea:** Haz cherry-pick de un commit de **`add-base-documents`** a **`main`**

[![image.png](https://i.postimg.cc/RZxrkxvY/image.png)](https://postimg.cc/xc5Fm7JG)

4. **Revisión:** Revisa el historial nuevamente

[![image.png](https://i.postimg.cc/fb56S3Y4/image.png)](https://postimg.cc/06MtLytZ)

Después de que hayas realizado con éxito el cherry-pick del commit, se agregará un nuevo commit a tu rama actual (**`main`** en este ejemplo) y contendrá los cambios del commit cherry-picked.

[![image.png](https://i.postimg.cc/Qx1N9btR/image.png)](https://postimg.cc/kBMPLWWc)


### Preguntas de discusión:
1. ¿Por qué se considera que rebase es más útil para mantener un historial de proyecto lineal en  comparación con merge?

    *Lo que hace rebase es aplicar los commits de una rama encima de otra, eliminando así bifurcaciones en el historial. Esto hace que el historial sea lineal y  sin bifurcaciones, ideal para seguir fácilmente el flujo de trabajo. En cambio, merge preserva los puntos de bifurcación y crea commits de fusión, resultando en un historial sin linealidad y más difícil de seguir.*

2. ¿Qué problemas potenciales podrían surgir si haces rebase en una rama compartida con otros miembros del equipo?

    *Al reescribir el historial con los nuevos commits, otros miembros del equipo pueden enfrentar conflictos al intentar hacer pull o push porque su historial no coincide con el nuevo. Esto puede causar confusión y pérdida de cambios si no se maneja con cuidado.*

3. ¿En qué se diferencia cherry-pick de merge, y en qué situaciones preferirías uno sobre el otro?

    *Se diferencian en que cherry-pick permite aplicar commits específicos de otra rama sin mezclar todo su historial, lo cual es útil cuando solo necesitas traer un cambio puntual y no toda una serie de commits. En cambio merge combina todo el historial de la otra rama. Preferiría cherry-pick cuando solo un commit de una rama es relevante y merge cuando cada commit de la rama presentan cambios importantes.*

4. ¿Por qué es importante evitar hacer rebase en ramas públicas?

    *Hacer rebase en una rama pública causaría problemas para otros que ya hayan clonado o basado su trabajo en ella, ya que Git perdería el rastro de los commits originales, generando conflictos y potencial pérdida de trabajo.*

### Ejercicios teóricos

1. **Diferencias entre git merge y git rebase**

    **Pregunta:** Explica la diferencia entre git merge y git rebase y describe en qué escenarios sería más adecuado utilizar cada uno en un equipo de desarrollo ágil que sigue las prácticas de Scrum.
    
    *En el entorno de Scrum, git merge se utilizaría para integrar ramas al final de un sprint o después de completar una feature, cuando se quiere preservar el historial completo y ramificado. En cambio git rebase se utilizaría durante el trabajo individual antes de integrar cambios, para alinear la rama con la principal y mantener un historial limpio y lineal, sin interrumpir la colaboración.*

2. **Relación entre git rebase y DevOps**

    **Pregunta:** ¿Cómo crees que el uso de git rebase ayuda a mejorar las prácticas de DevOps, especialmente en la implementación continua (CI/CD)? Discute los beneficios de mantener un historial lineal en el contexto de una entrega continua de código y la automatización de pipelines.

   *El uso de git rebase en DevOps mejora el proceso al mantener un historial lineal y limpio, lo que facilita la automatización de pipelines y la integración continua. Un historial lineal reduce la complejidad de los cambios, minimiza los conflictos durante las fusiones, y facilita la revisión y rastreo de problemas, lo que es esencial para mantener un flujo constante de entregas rápidas y sin errores. Esto también simplificaría las pruebas automáticas y despliegues, ya que el código es más fácil de auditar y verificar durante cada integración.*

3. **Impacto del git cherry-pick en un equipo Scrum**

    **Pregunta:** Un equipo Scrum ha finalizado un sprint, pero durante la integración final a la rama principal (main) descubren que solo algunos commits específicos de la rama de una funcionalidad deben aplicarse a producción. ¿Cómo podría ayudar git cherry-pick en este caso? Explica los beneficios y posibles complicaciones.
    
    *Git cherry-pick ayudaría al equipo a aplicar solo los commits específicos de la funcionalidad directamente en la rama main, sin fusionar toda la rama de la funcionalidad. Entre los beneficios tendríamos un control preciso sobre qué cambios llegan a producción. Además, se evita fusionar código que aún no está listo. Una de las complicaciones que se podrían dar es que se podría generar conflictos si los commits seleccionados dependen de otros cambios no incluidos. Además, aumenta la posibilidad de crear un historial más fragmentado y difícil de seguir si no se gestiona bien.*


### Ejercicios prácticos

#### 1. Simulación de un flujo de trabajo Scrum con git rebase y git merge

**Contexto:**
- Tienes una rama main y una rama feature en la que trabajas. Durante el desarrollo del sprint, se han realizado commits tanto en main como en feature.
- Tu objetivo es integrar los cambios de la rama feature en main manteniendo un historial limpio.

**Instrucciones:**

1. Crea un repositorio y haz algunos commits en la rama main.

[![image.png](https://i.postimg.cc/7hd89XM8/image.png)](https://postimg.cc/N26zf6zp)

2. Crea una rama feature, agrega nuevos commits, y luego realiza algunos commits adicionales en main.

[![image.png](https://i.postimg.cc/SKk0gn8s/image.png)](https://postimg.cc/dhHS1t5P)
[![image.png](https://i.postimg.cc/yd8Mz2LC/image.png)](https://postimg.cc/5HD7BKcs)

3. Realiza un rebase de feature sobre main.

[![image.png](https://i.postimg.cc/D0bYvhsH/image.png)](https://postimg.cc/PvTMyBSQ)

4. Finalmente, realiza una fusión fast-forward de feature con main.

[![image.png](https://i.postimg.cc/pybcySJT/image.png)](https://postimg.cc/4HPQSBMk)

**Preguntas:**

- ¿Qué sucede con el historial de commits después del rebase?

    *Después de un rebase, los commits de la rama actual se aplican en la parte superior de otra rama, lo que reorganiza y reescribe el historial. Los commits originales obtienen nuevos identificadores (hashes), como si se hubieran creado en ese momento.*

- ¿En qué situación aplicarías una fusión fast-forward en un proyecto ágil?


    *Aplicaría una fusión fast-forward en un proyecto ágil cuando una rama de funcionalidad ha avanzado sin que la rama principal haya tenido nuevos commits desde que se bifurcó. El fast-forward simplemente mueve el puntero de la rama principal hacia adelante, manteniendo el historial limpio y lineal, lo que es ideal para integraciones rápidas sin conflictos en un flujo ágil.*

#### 2. Cherry-pick para integración selectiva en un pipeline CI/CD

**Contexto:**

- Durante el desarrollo de una funcionalidad, te das cuenta de que solo ciertos cambios deben ser integrados en la rama de producción, ya que el resto aún está en desarrollo. Para evitar fusionar toda la rama, decides hacer cherry-pick de los commits que ya están listos para producción.

**Instrucciones:**

1. Crea un repositorio con una rama main y una rama feature.

[![image.png](https://i.postimg.cc/j5kSVHQv/image.png)](https://postimg.cc/CBkgkf2f)

2. Haz varios commits en la rama feature, pero solo selecciona uno o dos commits específicos que 
consideres listos para producción.

[![image.png](https://i.postimg.cc/brDNqZmP/image.png)](https://postimg.cc/GTR1Qm0g)

[![image.png](https://i.postimg.cc/pT7Rc2R6/image.png)](https://postimg.cc/bDQ7sfGx)

3. Realiza un cherry-pick de esos commits desde feature a main.

[![image.png](https://i.postimg.cc/Sxq2fGZz/image.png)](https://postimg.cc/dLHVqGcq)

4. Verifica que los commits cherry-picked aparezcan en main.

[![image.png](https://i.postimg.cc/VNkJ3kPf/image.png)](https://postimg.cc/fV1WdZbp)

**Preguntas:**

- ¿Cómo utilizarías cherry-pick en un pipeline de CI/CD para mover solo ciertos cambios listos a 
producción?

    *En un pipeline de CI/CD, utilizaría* `git cherry-pick` *para mover solo los cambios listos a producción cuando se necesitaría aplicar ciertos commits de una rama de desarrollo a la rama de producción sin fusionar todo el código.*

- ¿Qué ventajas ofrece cherry-pick en un flujo de trabajo de DevOps?

    *La ventaja que ofrece cherry-pick en DevOps es que permite aplicar cambios específicos sin integrar ramas completas, facilitando la rapidez en la entrega de parches o mejoras urgentes, reduciendo riesgos de introducir código no listo o problemático en producción.*

### Git, Scrum y Sprints

#### Fase 1: Planificación del sprint (sprint planning)

**Ejercicio 1: Crear ramas de funcionalidades (feature branches)**

En esta fase del sprint, los equipos Scrum deciden qué historias de usuario van a trabajar. Cada historia de usuario puede representarse como una rama de funcionalidad.

**Objetivo:** Crear ramas para cada historia de usuario y asegurar que el trabajo se mantenga aislado.

**Instrucciones:**

1. Crea un repositorio en Git.

[![image.png](https://i.postimg.cc/sDx0DpP7/image.png)](https://postimg.cc/svFJTGNg)

2. Crea una rama **`main`** donde estará el código base.

[![image.png](https://i.postimg.cc/vmr0SXMF/image.png)](https://postimg.cc/nsLKX4C0)

3. Crea una rama por cada historia de usuario asignada al sprint, partiendo de la rama **`main`**.

[![image.png](https://i.postimg.cc/m2P8GTRS/image.png)](https://postimg.cc/4mTz6kYK)

**Pregunta:** ¿Por qué es importante trabajar en ramas de funcionalidades separadas durante un sprint?

*Trabajar en ramas de funcionalidades separadas durante un sprint permite aislar los cambios de cada historia de usuario, evitando que una funcionalidad interfiera con otra, lo que facilita la integración al final del sprint, reduciendo conflictos. Además, mejora la colaboración al permitir que los desarrolladores trabajen en paralelo sin bloquearse entre sí, y mantiene un historial claro y organizado, donde cada rama refleja cambios específicos, lo que facilita el control de calidad y la agilidad en la entrega del proyecto.*

#### Fase 2: Desarrollo del sprint (sprint execution)
**Ejercicio 2: Integración continua con git rebase**

A medida que los desarrolladores trabajan en sus respectivas historias de usuario, pueden ocurrir cambios en main. Para mantener un historial lineal y evitar conflictos más adelante, se usa git rebase para integrar los últimos cambios de main en las ramas de funcionalidad antes de finalizar el sprint.

**Objetivo:** Mantener el código de la rama de funcionalidad actualizado con los últimos cambios de main durante el sprint.

**Instrucciones:**

1. Haz algunos commits en **`main`**.

[![image.png](https://i.postimg.cc/mhWcq3BJ/image.png)](https://postimg.cc/5QpNQCHS)

2. Realiza un rebase de la rama **`feature-user-story-1`** para actualizar su base con los últimos cambios de **`main`**.

[![image.png](https://i.postimg.cc/nhYShZS9/image.png)](https://postimg.cc/ZWnxfkSJ)

**Pregunta:** ¿Qué ventajas proporciona el rebase durante el desarrollo de un sprint en términos de integración continua?

*Las ventajas que ofrece rebase durante el desarrollo de un sprint son que  facilita la integración continua al mantener un historial lineal y limpio, eliminando bifurcaciones innecesarias y simplificando la revisión de cambios. Al alinear la rama de la funcionalidad con la rama principal, reduce los conflictos al integrar y evita commits de fusión intermedios. Esto mejora la colaboración en equipo y optimiza el flujo de trabajo, permitiendo una entrega continua de código más eficiente.*


#### Fase 3: Revisión del sprint (sprint review)

**Ejercicio 3: Integración selectiva con git cherry-pick**

En esta fase, es posible que algunas funcionalidades estén listas para ser mostradas a los stakeholders, pero otras aún no están completamente implementadas. Usar git cherry-pick puede permitirte seleccionar commits específicos para mostrar las funcionalidades listas, sin hacer merge de ramas incompletas.

**Objetivo:** Mover commits seleccionados de una rama de funcionalidad (**`feature-user-story-2`**) a main sin integrar todos los cambios.

**Instrucciones:**

1. Realiza algunos commits en **`feature-user-story-2`**.

[![image.png](https://i.postimg.cc/25gWpLdQ/image.png)](https://postimg.cc/R3QhKFDh)

2. Haz cherry-pick de los commits que estén listos para mostrarse a los stakeholders durante la revisión del sprint.

[![image.png](https://i.postimg.cc/qBs3YRNK/image.png)](https://postimg.cc/qg7q6pXB)

**Pregunta:** ¿Cómo ayuda git cherry-pick a mostrar avances de forma selectiva en un sprint review?

*git cherry-pick permite mostrar avances de forma selectiva en un sprint review al aplicar solo los commits que representan funcionalidades completas y listas para demostrar, sin incluir código en progreso o no finalizado.*

#### Fase 4: Retrospectiva del sprint (sprint retrospective)

**Ejercicio 4: Revisión de conflictos y resolución**

Durante un sprint, pueden surgir conflictos al intentar integrar diferentes ramas de funcionalidades. Es importante aprender cómo resolver estos conflictos y discutirlos en la retrospectiva.

**Objetivo:** Identificar y resolver conflictos de fusión con git merge al intentar integrar varias ramas de funcionalidades al final del sprint.

**Instrucciones:**

1. Realiza cambios en **`feature-user-story-1`** y **`feature-user-story-2`** que resulten en conflictos.

[![image.png](https://i.postimg.cc/mr1cS2xt/image.png)](https://postimg.cc/hJgPDntB)

[![image.png](https://i.postimg.cc/7YPfWN8v/image.png)](https://postimg.cc/xq7fkM1g)

2. Intenta hacer merge de ambas ramas con **`main`** y resuelve los conflictos.

[![image.png](https://i.postimg.cc/k43g7Q2y/image.png)](https://postimg.cc/v1hsz6L1)

[![image.png](https://i.postimg.cc/7hXH1jmB/image.png)](https://postimg.cc/0KM1PXgm)

[![image.png](https://i.postimg.cc/t48Xz3NH/image.png)](https://postimg.cc/xXyDfbZs)

[![image.png](https://i.postimg.cc/Tw0MBgg1/image.png)](https://postimg.cc/njXPDsdf)

**Pregunta :** ¿Cómo manejas los conflictos de fusión al final de un sprint? ¿Cómo puede el equipo mejorar la comunicación para evitar conflictos grandes?

*Los conflictos se resuelven manualmente revisando los archivos afectados y eligiendo qué cambios conservar, asegurándose de que el código sea funcional y consultando con los demás colaboradores. Para evitar conflictos grandes, el equipo puede mejorar su comunicación avisando constantemente los cambios que vienen realizando para mantener las ramas de funcionalidad alineadas con la rama principal haciendo fusiones regulares durante el sprint en lugar de esperar hasta el final.*

#### Fase de desarrollo: automatización de integración continua (CI) con git rebase

**Ejercicio 5: Automatización de rebase con hooks de Git**

En un entorno CI, es común automatizar ciertas operaciones de Git para asegurar que el código se mantenga limpio antes de que pase a la siguiente fase del pipeline. Usa los hooks de Git para automatizar el rebase cada vez que se haga un push a una rama de funcionalidad.

**Objetivo:** Implementar un hook que haga automáticamente un rebase de main antes de hacer push en 
una rama de funcionalidad, asegurando que el historial se mantenga limpio.

**Instrucciones:**

1. Configura un hook pre-push que haga un rebase automático de la rama **`main`** sobre la rama de funcionalidad antes de que el push sea exitoso.

- Dentro de tu proyecto, crea un hook pre-push
    
    *Ejecutamos* `nano .git/hooks/pre-push` *y agregamos el siguiente script para automatizar el rebase:*

    ```
    #!/bin/bash
    git fetch origin main
    git rebase origin/main
    ```
    
    [![image.png](https://i.postimg.cc/pXprYLMz/image.png)](https://postimg.cc/ykC77Bd8)

    [![image.png](https://i.postimg.cc/KjmL8S1Q/image.png)](https://postimg.cc/Q9nVfzkW)

- Haz el archivo ejecutable

    *Ejecutamos* `chmod +x .git/hooks/pre-push`
    
    [![image.png](https://i.postimg.cc/52ztTK0t/image.png)](https://postimg.cc/sMVyZc5F)

2. Prueba el hook haciendo push de algunos cambios en la rama **`feature-user-story-1`**.

[![image.png](https://i.postimg.cc/CKYwtFXv/image.png)](https://postimg.cc/WdWRqP2r)


**Pregunta:** ¿Qué ventajas y desventajas observas al automatizar el rebase en un entorno de CI/CD?

*Automatizar un rebase en un hook de git pre-push en un entorno de CI/CD tiene la ventaja de mantener un historial lineal, minimizando conflictos tardíos al integrar código, lo que facilita un flujo continuo de integración. Sin embargo, puede generar conflictos inesperados que requieren intervención manual, y los desarrolladores podrían perder el control y el contexto de los cambios al no gestionar el rebase directamente, lo que podría complicar la resolución de problemas o introducir errores si los cambios en main no están completamente listos.*
