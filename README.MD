# Talana Kombat Challenge

[Instrucciones del desafio](https://github.com/esteban03/TalanaKombat/blob/main/talana_instructions/Desafio%20TalanaKombat%20%20-%20Software%20Support%20Developer.docx.pdf)

### Instrucciones de ejecución
Se dispone de un contenedor y un archivo docker-compose para facilitar la revisión.

* Ejecuta el comando `docker-compose up` en la raíz del proyecto. Esto ejecutará la app utilizando el archivo en `./data/commands.json` e imprimirá la narración del juego en la salida.
* El contenedor está montado con un volumen. Esto permite que puedas modificar o reemplazar el archivo **.json** manteniendo el mismo nombre para realizar tus pruebas.

### Instrucciones para desarrollo
* Si quieres utilizar el contenedor en modo desarrollo, simplemente descomenta el **command** debajo del comentario **develop command** en el **archivo docker-compose.yml**. Luego, vuelve a ejecutar el contenedor en segundo plano con `docker-compose up -d`. Puedes acceder al contenedor obteniendo su ID y utilizando el siguiente comando: `docker exec -it [id_contenedor] bash`.

### Test automatizados
Se han agregado algunos tests automatizados con **pytest**.
* Para ejecutarlos, simplemente activa el **command** debajo del comentario **test command** en el archivo **docker-compose.yml**.
* Luego ejecuta nuevamente el contenedor con `docker-compose up`. La salida del comando será el resultado de los tests.

### Clases y responsabilidades
* **Kombat**: Es la clase principal encargada de coordinar los procesos y acciones en orden lógico para llevar a cabo un combate.
* **Player**: Clase abstracta que contiene todo el comportamiento base de un personaje. Sistema de vida, movimientos especiales, etc. Además, es utilizada como contrato para modelar.
* **Narrator**: Concentra toda la lógica para comentar el desenlace del combate.

### Lenguaje común
* **Command**: Conjunto de movimientos y golpes a ejecutar por un jugador.
* **Player**: Personaje o jugador.
* **Active Player**: Jugador o personaje en turno (puede atacar).
* **Enemy player**: Lo contrario al jugador activo. Solo puede recibir ataques.
* **Controls**: Movimientos (abajo, arriba, atrás, adelante) y golpes.
* **Action**: Movimiento, golpe o especial realizado por un jugador a un enemigo.


### Preguntas

1. Supongamos que en un repositorio GIT hiciste un commit y olvidaste un archivo. Explica cómo se soluciona si hiciste push, y cómo si aún no hiciste.

    **Re**: Depende. Si aún no he hecho el push, puedo añadir el archivo al commit anterior con ``git  commit --amend --no-edit``. También podría realizar otro commit para el archivo dependiendo del caso. Si hice el push y tengo un pull request, puedo hacer --amend y reescribir con un push --force. Si necesito deshacer muchos cambios locales para ordenar la historia, puedo considerar git reset. Lo importante es que el historial de commit llegue en orden a las ramas principales. La respuesta va a depender mucho de la situación.
2. Si has trabajado con control de versiones ¿Cuáles han sido los flujos con los que has trabajado?

    **Re**: Gitflow, GitHub Flow y flujos personalizados pensados para CI/CD. En mi último trabajo, usábamos una estrategia personalizada con ramas como master, develop, feature, fix y Chore.
3. ¿Cuál ha sido la situación más compleja que has tenido con esto?

   **Re**: En general, no he tenido muchos problemas. Tal vez Gitflow tiene demasiadas ramas y puede ser complejo gestionarlas para mantener un orden en el proyecto. Además, los flujos que se basan en el trabajo desde una rama develop en vez de master hacen que, en muchos casos, estés trabajando con código que no es idéntico al de producción, lo que puede generar algunos problemas. Pero todo esto se puede solucionar con prácticas auxiliares o eligiendo un flujo diferente para el proyecto, como por ejemplo el trunk-based development. Hay mucho de que hablar sobre esto.
4. ¿Qué experiencia has tenido con los microservicios?

    **Re**: He construido algunos microservicios para simplificar el control sobre ciertos dominios de proyectos y mejorar el versionado. También he trabajado con arquitecturas híbridas (Monolito - Microservicios).
5. ¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué?

   **Re**: En algún momento preferí AWS por tener mejor documentación, mejores precios en algunos servicios y una integración sólida entre sus servicios, además de contar con DynamoDB que es muy útil para escalar aplicaciones. Actualmente estoy estudiando AWS porque las compañías lo prefieren en mi opinión. Pero la comparación entre ambos servicios es difícil, creo que depende mucho del proyecto. 