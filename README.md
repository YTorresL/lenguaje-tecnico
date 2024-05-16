# Lenguaje tecnico para programadores, desde lo mas basico hasta lo mas avanzado 😊

Esta es una guía de lenguaje técnico para programadores, que cubre desde los conceptos básicos hasta los temas más avanzados. Esto puede ser de gran ayuda cuando sabes programar pero el técnico es prácticamente nulo.

Estoy en un momento de mi vida donde si alguien me dice, por ejemplo, ¿Qué es TDD? no sabría qué decirle. Así que desde ahora me comprometo a aprender ese lenguaje técnico e implementarlo en un repositorio donde pueda almacenar toda esa información valiosa, así como en la vida diaria como programador.

Cada nueva palabra estara en este "diccionario".

> [!IMPORTANT]
> Si deseas tener una mejor idea puedes ir a la carpeta ejemplos

### Casting

Casting en JAVA es convertir un tipo de dato en otro. Basicamente es asegurarnos que sea el tipo de datos que estamos buscando.

Segun Alura existen 2 tipos de Casting: Implícito y explícito. El "casting implícito" es cuando el programa automáticamente convierte un tipo de dato en otro si son compatibles.

Mientras que el casting "explícito" se realiza cuando el tipo de dato de origen es incompatible con el tipo de dato de destino.

![Imagen de una tabla, que describe los tipos primitivos e indica los casos en que el cast es implícito y  los casos en que es necesario informar de forma explícita.](https://cdn3.gnarususercontent.com.br/2023-java/psm-img1.png)

### Inferencia de Tipos

La inferencia de tipos es un proceso utilizado por los compiladores para deducir o determinar automáticamente el tipo de una variable, constante u otra entidad en un programa, sin que el programador tenga que proporcionar una declaración explícita del tipo.

![Ejemplo de inferencia de tipos en Swift](https://www.lafactoriaapple.com/img/ciencias-de-la-computacion/inferencia-de-tipos-01.jpg)

### Health check

Segun Makigas, en microservicios un healthcheck es un endpoint que se integra en una aplicación web para comunicar su estado. Por ejemplo, este endpoint puede devolver un error si se pierde la conexión con la base de datos o con un servicio externo sin el cual la aplicación no funcione correctamente.

Agentes de monitorización, como los que integra Kubernetes o los que trae AWS, pueden estar pendientes del código de estado que devuelva este endpoint y hacer acciones cuando la aplicación empiece a reportar errores, como reiniciar o enviar alertas.

### Entrypoint

Segun KeepCoding, El término entry point se utiliza para referirse al punto de inicio de un programa o una aplicación. Es el lugar donde el flujo de ejecución comienza y desde donde se accede al resto del sistema. Podría decirse que es la puerta de entrada a todo el código y la lógica que conforma una aplicación.

Por ejemplo, en lenguajes como C o C++, la función main() suele ser el entry point de un programa. Cuando ejecutas un programa, el sistema operativo llama a main() y, a partir de ahí, se inicia la ejecución del resto del código.

Segun ffflabs en StackOverflow, Entry point es la URL que el visitante habrá ingresado en su navegador para ver su aplicación o sitio. Antiguamente, cada sección de un sitio web era un entrypoint

- home.html
- galeria.html
- contacto.html
- about us.html

### Endpoint

Un endpoint es básicamente como una puerta de entrada que permite que diferentes programas en internet se comuniquen entre sí. Imagina que cada vez que usas una aplicación web, como enviar un mensaje o buscar información, estás usando estos "puntos finales" sin darte cuenta, como si fueran las puertas que te conectan a lo que necesitas en internet. En pocas palabras, un endpoint sería la dirección específica (URL) a la que el cliente envía una solicitud para obtener o enviar datos.

Segun ffflabs en StackOverflow, Los endpoints son las URLs de un API o un backend que responden a una petición. Los mismos entrypoints tienen que calzar con un endpoint para existir. Algo debe responder para que se renderice un sitio con sentido para el visitante. Por cada entrypoint esperando la visita de un usuario puede haber docenas de endpoints sirviendo los datos para llenar cada gráfico e infografía que se despliega en el entrypoint.

### Entrypoint vs Endpoint

La diferencia entre entrypoint y endpoint es que los endpoints no están pensados para interactuar con el usuario final. Usualmente sólo devolverán json, o no devolverán nada. Y más que frecuentemente, un entrypoint hará varios llamados a distintos endpoints para mostrar estadísticas, galerías, últimos comentarios, etc.

### Heap

La memoria Heap se utiliza para almacenar los objetos (incluyendo sus atributos), los objetos almacenados en este espacio de memoria normalmente tienen un tiempo de duración más prolongado que los almacenados en Stack.

### Stack

La memoria Stack se usa para almacenar las variables locales (cuyo ámbito de acción está limitada solo a la función donde se declaró) y también las llamadas de funciones en Java. Las variables almacenadas en esta memoria por lo general tienen un periodo de vida corto, viven hasta que terminen la función o método en el que se están ejecutando.

> [!IMPORTANT]
> Si deseas tener una mejor idea puedes ir a la carpeta ejemplos
