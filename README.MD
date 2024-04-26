# Talana Kombat Challenge

### Instrucciones de ejecución
Se dispone de un contenedor y un archivo docker-compose para facilitar la revisión.

* Ejecuta el comando `docker-compose up` en la raíz del proyecto. Esto ejecutará la app utilizando el archivo en `./data/commands.json` como comandos e imprimirá la narración del juego en la salida del comando.
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
* **Action**: Movimiento, golpe o especial realizado por un jugador enemigo.