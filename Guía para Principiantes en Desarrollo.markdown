# Guía para Principiantes en Desarrollo

## Introducción

Este documento está diseñado para personas que están comenzando en el mundo del desarrollo. Cada sección aborda un tema específico con explicaciones claras, ejemplos prácticos, sintaxis y contexto para que puedas entender y aplicar los conceptos de manera efectiva.

---

## Índice

1. Clases en Python
2. Método que se ejecuta automáticamente al crear una instancia
3. Atributos de clase y de instancia
4. Herencia en Python
5. Encapsulamiento en Python
6. Polimorfismo en Python
7. MongoDB: ¿SQL o NoSQL?
8. ¿Qué es una API?
9. ¿Qué es Postman?
10. ¿Qué es un método dunder?
11. ¿Qué es un decorador en Python?

---

## Clases en Python

*(Contenido previo sobre clases, mantenido sin cambios)*

### ¿Qué son las clases en Python?

Una **clase** en Python es una plantilla o molde que define las características (atributos) y comportamientos (métodos) que tendrá un objeto. Las clases son un pilar fundamental de la **programación orientada a objetos (POO)**, un enfoque que organiza el código en "entidades" reutilizables y lógicas.

Piensa en una clase como un plano para construir algo, por ejemplo, un plano de una casa. El plano (clase) define cómo será la casa, pero no es la casa en sí. Cuando construyes la casa (creas un objeto), usas ese plano.

### ¿Por qué usamos clases?

Las clases se utilizan para:

- **Organizar el código**: Agrupan datos y funciones relacionadas, haciendo el código más claro y mantenible.
- **Reutilizar código**: Puedes crear múltiples objetos a partir de una misma clase, evitando repetir código.
- **Modelar el mundo real**: Representan entidades con propiedades y comportamientos, como un coche, una persona o un producto en una tienda.
- **Escalabilidad**: Facilitan agregar nuevas funcionalidades sin modificar el código existente (herencia y polimorfismo).
- **Encapsulamiento**: Permiten proteger datos sensibles y controlar cómo se accede a ellos.

### ¿Para qué sirven las clases?

- **Crear objetos**: Un objeto es una instancia de una clase. Por ejemplo, si tienes una clase `Coche`, puedes crear objetos como `mi_coche` o `coche_de_juan`.
- **Definir propiedades**: Los atributos almacenan datos, como el color o la velocidad de un coche.
- **Definir comportamientos**: Los métodos son funciones que describen qué puede hacer el objeto, como acelerar o frenar.
- **Estructurar programas complejos**: Las clases son ideales para proyectos grandes, como aplicaciones, juegos o sistemas empresariales.

### Sintaxis básica de una clase

En Python, las clases se definen con la palabra clave `class`, seguida del nombre de la clase (por convención, en formato CamelCase). Dentro de la clase, defines atributos y métodos.

```python
class EjemploClase:
    def __init__(self, parametro1, parametro2):
        self.atributo1 = parametro1  # Atributo de instancia
        self.atributo2 = parametro2

    def metodo(self):
        # Código del método
        pass
```

- `__init__`: Es el **constructor**, un método especial que se ejecuta al crear un objeto. Inicializa los atributos del objeto.
- `self`: Representa la instancia actual del objeto. Se usa para acceder a sus atributos y métodos.
- **Atributos**: Variables que almacenan datos específicos del objeto.
- **Métodos**: Funciones que definen el comportamiento del objeto.

### Ejemplo práctico 1: Clase `Coche`

Vamos a crear una clase `Coche` que represente un coche con atributos como marca y color, y métodos para arrancar y acelerar.

```python
class Coche:
    def __init__(self, marca, color):
        self.marca = marca  # Atributo: marca del coche
        self.color = color  # Atributo: color del coche
        self.velocidad = 0  # Atributo: velocidad inicial

    def arrancar(self):
        return f"El {self.color} {self.marca} ha arrancado."

    def acelerar(self, incremento):
        self.velocidad += incremento
        return f"El coche acelera a {self.velocidad} km/h."

# Crear objetos (instancias) de la clase
mi_coche = Coche("Toyota", "Rojo")
coche_de_juan = Coche("Honda", "Azul")

# Usar métodos
print(mi_coche.arrancar())  # Salida: El Rojo Toyota ha arrancado.
print(mi_coche.acelerar(50))  # Salida: El coche acelera a 50 km/h.
print(coche_de_juan.arrancar())  # Salida: El Azul Honda ha arrancado.
```

**Explicación del ejemplo**:

- La clase `Coche` define cómo será cada coche (atributos: `marca`, `color`, `velocidad`).
- El método `__init__` inicializa cada coche con una marca y color específicos.
- Los métodos `arrancar` y `acelerar` describen acciones que un coche puede realizar.
- Creamos dos objetos (`mi_coche` y `coche_de_juan`) con diferentes valores para los atributos.
- Cada objeto tiene su propia copia de los atributos, pero comparte los métodos definidos en la clase.

### Ejemplo práctico 2: Clase `Estudiante`

Ahora crearemos una clase `Estudiante` para gestionar información de estudiantes, como su nombre y notas.

```python
class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas  # Lista de notas

    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0
        promedio = sum(self.notas) / len(self.notas)
        return f"El promedio de {self.nombre} es {promedio:.2f}."

    def aprobo(self):
        promedio = sum(self.notas) / len(self.notas) if self.notas else 0
        return f"{self.nombre} {'aprobó' if promedio >= 6 else 'no aprobó'}."

# Crear objetos
estudiante1 = Estudiante("Ana", [8, 7, 9])
estudiante2 = Estudiante("Luis", [5, 4, 6])

# Usar métodos
print(estudiante1.calcular_promedio())  # Salida: El promedio de Ana es 8.00.
print(estudiante1.aprobo())  # Salida: Ana aprobó.
print(estudiante2.calcular_promedio())  # Salida: El promedio de Luis es 5.00.
print(estudiante2.aprobo())  # Salida: Luis no aprobó.
```

**Explicación del ejemplo**:

- La clase `Estudiante` tiene atributos para el nombre y una lista de notas.
- El método `calcular_promedio` calcula el promedio de las notas.
- El método `aprobo` determina si el estudiante aprobó (promedio ≥ 6).
- Cada objeto (`estudiante1` y `estudiante2`) tiene sus propios datos, pero usa los mismos métodos.

### ¿Cuándo usar clases?

- **Cuando modelas entidades**: Si tu programa necesita representar objetos con propiedades y comportamientos (por ejemplo, usuarios, productos, animales).
- **Proyectos grandes**: Las clases ayudan a estructurar el código en módulos lógicos.
- **Reutilización**: Si necesitas crear múltiples instancias con datos diferentes pero la misma estructura.
- **Mantenimiento**: Las clases facilitan modificar o extender el código sin romper otras partes.

---

## Método que se ejecuta automáticamente al crear una instancia

### ¿Qué método se ejecuta automáticamente?

En Python, el método `__init__` es el que se ejecuta automáticamente cuando se crea una instancia de una clase. Este método se conoce como el **constructor** de la clase.

El constructor `__init__` se invoca inmediatamente después de que se crea un objeto (instancia) de la clase. Su propósito principal es inicializar los atributos del objeto con valores específicos, ya sean proporcionados por el usuario o establecidos por defecto.

### ¿Por qué usamos `__init__`?

- **Inicialización**: Permite configurar los atributos iniciales de un objeto, como su estado o propiedades, al momento de crearlo.
- **Personalización**: Facilita pasar argumentos al crear un objeto para que cada instancia tenga datos únicos.
- **Automatización**: Al ejecutarse automáticamente, asegura que el objeto esté listo para usar sin necesidad de llamar métodos adicionales manualmente.

### ¿Para qué sirve `__init__`?

- **Definir atributos del objeto**: Establece valores para las variables que pertenecen a cada objeto (por ejemplo, el nombre de un estudiante o el color de un coche).
- **Establecer valores predeterminados**: Puede definir valores iniciales para atributos si no se proporcionan argumentos.
- **Configurar el objeto**: Prepara el estado inicial necesario para que el objeto funcione correctamente.

### Sintaxis de `__init__`

```python
class NombreClase:
    def __init__(self, parametro1, parametro2):
        self.atributo1 = parametro1  # Inicializa atributo1
        self.atributo2 = parametro2  # Inicializa atributo2
```

- `self`: Representa la instancia del objeto que se está creando. Se usa para asignar valores a los atributos de esa instancia específica.
- **Parámetros**: Puedes incluir cualquier número de parámetros para recibir datos al crear el objeto.
- **Atributos**: Los valores pasados a `__init__` suelen asignarse a atributos usando `self.nombre_atributo`.

### Ejemplo práctico 1: Uso de `__init__` en una clase `Persona`

Crearemos una clase `Persona` que inicializa el nombre y la edad de una persona al crear un objeto.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo: nombre de la persona
        self.edad = edad      # Atributo: edad de la persona
        print(f"Se ha creado una persona: {self.nombre}")

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

# Crear objetos
persona1 = Persona("María", 25)  # Se ejecuta __init__ automáticamente
persona2 = Persona("Carlos", 30)  # Se ejecuta __init__ automáticamente

# Usar métodos
print(persona1.presentarse())  # Salida: Hola, soy María y tengo 25 años.
print(persona2.presentarse())  # Salida: Hola, soy Carlos y tengo 30 años.
```

**Explicación del ejemplo**:

- El método `__init__` se ejecuta automáticamente al crear `persona1` y `persona2`.
- Los parámetros `nombre` y `edad` se pasan al crear el objeto y se asignan a los atributos `self.nombre` y `self.edad`.
- El `print` dentro de `__init__` muestra un mensaje cada vez que se crea una instancia, confirmando que el constructor se ejecuta.
- Cada objeto tiene sus propios valores para `nombre` y `edad`, inicializados por `__init__`.

**Salida esperada**:

```
Se ha creado una persona: María
Se ha creado una persona: Carlos
Hola, soy María y tengo 25 años.
Hola, soy Carlos y tengo 30 años.
```

### Ejemplo práctico 2: `__init__` con valores predeterminados

En este ejemplo, crearemos una clase `Libro` donde el atributo `disponible` tiene un valor predeterminado en `__init__`.

```python
class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo        # Atributo: título del libro
        self.autor = autor          # Atributo: autor *autor del libro
        self.disponible = disponible  # Atributo: estado del libro (predeterminado: True)
        print(f"Nuevo libro añadido: {self.titulo} por {self.autor}")

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"El libro {self.titulo} ha sido prestado."
        return f"El libro {self.titulo} no está disponible."

# Crear objetos
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")  # Usa valor predeterminado
libro2 = Libro("1984", "George Orwell", False)  # Especifica disponible como False

# Usar métodos
print(libro1.prestar())  # Salida: El libro Cien años de soledad ha sido prestado.
print(libro2.prestar())  # Salida: El libro 1984 no está disponible.
```

**Explicación del ejemplo**:

- En `__init__`, el parámetro `disponible` tiene un valor predeterminado de `True`, por lo que no es obligatorio pasarlo al crear un objeto.
- Al crear `libro1`, no especificamos `disponible`, por lo que toma el valor predeterminado (`True`).
- Para `libro2`, pasamos `False` explícitamente, inicializando el libro como no disponible.
- El método `prestar` usa el atributo `disponible` para determinar si el libro puede prestarse.

**Salida esperada**:

```
Nuevo libro añadido: Cien años de soledad por Gabriel García Márquez
Nuevo libro añadido: 1984 por George Orwell
El libro Cien años de soledad ha sido prestado.
El libro 1984 no está disponible.
```

### ¿Cuándo se usa `__init__`?

- **Siempre que necesites inicializar atributos**: Si tu clase tiene atributos que deben configurarse al crear un objeto, `__init__` es el lugar para hacerlo.
- **Cuando quieras personalizar instancias**: Permite que cada objeto tenga datos únicos basados en los argumentos proporcionados.
- **Para establecer un estado inicial**: Por ejemplo, inicializar contadores, listas vacías o valores predeterminados.

### ¿Qué pasa si no hay `__init__`?

Si no defines `__init__`, puedes crear objetos, pero no se inicializarán atributos automáticamente. Tendrías que asignarlos manualmente después de crear el objeto, lo cual no es ideal.

```python
class SinInit:
    pass

objeto = SinInit()
objeto.nombre = "Ejemplo"  # Atributo asignado manualmente
print(objeto.nombre)  # Salida: Ejemplo
```

Esto funciona, pero es menos organizado y propenso a errores.

---

## Atributos de clase y de instancia

### ¿Qué son los atributos de clase y de instancia?

En Python, los **atributos** son variables asociadas a una clase o a sus objetos (instancias). Hay dos tipos principales: **atributos de clase** y **atributos de instancia**.

- **Atributos de clase**: Son variables definidas directamente en el cuerpo de la clase y compartidas por todas las instancias de esa clase. Representan datos comunes a todos los objetos de la clase.
- **Atributos de instancia**: Son variables definidas dentro de un método (generalmente `__init__`) y asociadas a una instancia específica del objeto. Cada objeto tiene su propia copia de estos atributos.

### ¿Por qué usamos atributos de clase y de instancia?

- **Atributos de clase**:
  - **Datos compartidos**: Útiles para almacenar información que es común a todas las instancias, como configuraciones o contadores globales.
  - **Eficiencia**: Al estar definidos una sola vez, no se duplican en cada objeto, ahorrando memoria.
  - **Consistencia**: Cambiar un atributo de clase afecta a todas las instancias, asegurando uniformidad.

- **Atributos de instancia**:
  - **Datos únicos**: Permiten que cada objeto tenga sus propios valores, como el nombre o la edad de una persona.
  - **Personalización**: Facilitan la creación de objetos con propiedades específicas para cada caso.
  - **Flexibilidad**: Cada instancia puede modificar sus propios atributos sin afectar a otras.

### ¿Para qué sirven?

- **Atributos de clase**: Se usan para:
  - Definir constantes o configuraciones compartidas (por ejemplo, una tasa de impuesto para todos los productos).
  - Mantener un conteo global (por ejemplo, cuántos objetos de una clase se han creado).
  - Proporcionar valores predeterminados que las instancias pueden usar o modificar.

- **Atributos de instancia**: Se usan para:
  - Almacenar datos específicos de cada objeto (por ejemplo, el color de un coche o las notas de un estudiante).
  - Representar el estado de un objeto que puede cambiar con el tiempo.
  - Modelar entidades del mundo real con propiedades únicas.

### Sintaxis

```python
class NombreClase:
    # Atributo de clase (compartido por todas las instancias)
    atributo_clase = "Valor compartido"

    def __init__(self, parametro):
        # Atributo de instancia (único para cada objeto)
        self.atributo_instancia = parametro
```

- **Atributo de clase**: Se define fuera de cualquier método, directamente en el cuerpo de la clase.
- **Atributo de instancia**: Se define dentro de `__init__` (u otro método) usando `self`.

### Ejemplo práctico 1: Atributos de clase y de instancia en una clase `Perro`

Crearemos una clase `Perro` que usa un atributo de clase para contar cuántos perros se han creado y atributos de instancia para el nombre y la raza de cada perro.

```python
class Perro:
    # Atributo de clase: contador de perros
    contador_perros = 0

    def __init__(self, nombre, raza):
        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza
        # Incrementar el contador de perros
        Perro.contador_perros += 1

    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau!"

# Crear objetos
perro1 = Perro("Max", "Labrador")
perro2 = Perro("Luna", "Husky")

# Acceder a atributos de instancia
print(perro1.nombre)  # Salida: Max
print(perro2.raza)   # Salida: Husky

# Acceder al atributo de clase
print(Perro.contador_perros)  # Salida: 2
print(perro1.contador_perros)  # Salida: 2 (accesible desde una instancia)
```

**Explicación del ejemplo**:

- **Atributo de clase (`contador_perros`)**: Es compartido por todos los objetos y se incrementa cada vez que se crea un nuevo perro. Lo accedemos con `Perro.contador_perros` o a través de una instancia (`perro1.contador_perros`).
- **Atributos de instancia (`nombre`, `raza`)**: Cada perro tiene su propio nombre y raza, únicos para cada objeto.
- El método `ladrar` usa el atributo de instancia `nombre` para personalizar la salida.

### Ejemplo práctico 2: Atributos de clase como configuración

Crearemos una clase `Producto` donde un atributo de clase define una tasa de impuesto aplicada a todos los productos.

```python
class Producto:
    # Atributo de clase: tasa de impuesto (compartida)
    tasa_impuesto = 0.19  # 19%

    def __init__(self, nombre, precio):
        # Atributos de instancia
        self.nombre = nombre
        self.precio = precio

    def calcular_precio_final(self):
        precio_final = self.precio * (1 + Producto.tasa_impuesto)
        return f"El precio final de {self.nombre} es ${precio_final:.2f}"

# Crear objetos
producto1 = Producto("Laptop", 1000)
producto2 = Producto("Teléfono", 500)

# Usar el método
print(producto1.calcular_precio_final())  # Salida: El precio final de Laptop es $1190.00
print(producto2.calcular_precio_final())  # Salida: El precio final de Teléfono es $595.00

# Cambiar el atributo de clase
Producto.tasa_impuesto = 0.25  # Nueva tasa: 25%

# Los precios finales reflejan el cambio
print(producto1.calcular_precio_final())  # Salida: El precio final de Laptop es $1250.00
print(producto2.calcular_precio_final())  # Salida: El precio final de Teléfono es $625.00
```

**Explicación del ejemplo**:

- **Atributo de clase (`tasa_impuesto`)**: Es compartido por todos los productos y define la tasa de impuesto. Cuando cambiamos `Producto.tasa_impuesto`, afecta a todos los objetos.
- **Atributos de instancia (`nombre`, `precio`)**: Cada producto tiene su propio nombre y precio base.
- El método `calcular_precio_final` usa tanto el atributo de instancia (`precio`) como el de clase (`tasa_impuesto`) para calcular el precio final.

### ¿Cuándo usar cada uno?

- **Atributos de clase**:
  - Cuando necesitas datos compartidos entre todas las instancias (por ejemplo, un contador global o una configuración común).
  - Para constantes que no deberían cambiar (aunque en Python no son estrictamente constantes).
  - Para evitar duplicar datos en cada objeto.

- **Atributos de instancia**:
  - Cuando cada objeto necesita datos únicos.
  - Para representar el estado o las propiedades específicas de un objeto.
  - Cuando los datos pueden cambiar de forma independiente para cada instancia.

### Nota: Precaución con atributos de clase

Los atributos de clase son compartidos, pero una instancia puede "sombrear" un atributo de clase si le asignas un valor con el mismo nombre. Esto crea un atributo de instancia con ese nombre, sin modificar el atributo de clase.

```python
class Ejemplo:
    valor = "Compartido"

obj = Ejemplo()
obj.valor = "Modificado"  # Crea un atributo de instancia
print(obj.valor)  # Salida: Modificado
print(Ejemplo.valor)  # Salida: Compartido (el atributo de clase no cambia)
```

---

## Herencia en Python

### ¿Qué es la herencia en Python?

La **herencia** es un concepto de la programación orientada a objetos (POO) que permite a una clase (llamada **clase hija** o **subclase**) heredar atributos y métodos de otra clase (llamada **clase padre** o **superclase**). Esto significa que la clase hija puede reutilizar el código de la clase padre y, si es necesario, extenderlo o modificarlo.

Piensa en la herencia como una relación de "es un". Por ejemplo, un `Perro` es un tipo de `Animal`, por lo que una clase `Perro` puede heredar propiedades y comportamientos de una clase `Animal`.

### ¿Por qué usamos herencia?

- **Reutilización de código**: Evita repetir código al permitir que las clases hijas usen los atributos y métodos de la clase padre.
- **Organización**: Estructura el código en jerarquías lógicas, agrupando comportamientos comunes en la clase padre.
- **Extensibilidad**: Permite agregar o modificar funcionalidades en las clases hijas sin alterar la clase padre.
- **Mantenimiento**: Cambios en la clase padre se propagan automáticamente a las clases hijas, facilitando actualizaciones.

### ¿Para qué sirve la herencia?

- **Definir comportamientos comunes**: La clase padre contiene atributos y métodos compartidos por varias clases hijas.
- **Especialización**: Las clases hijas pueden añadir nuevos métodos o redefinir (sobrescribir) los métodos heredados para adaptarlos a sus necesidades.
- **Modelar relaciones del mundo real**: Por ejemplo, una clase `Vehículo` puede ser la clase padre de `Coche` y `Moto`, ya que ambos comparten características como la velocidad o el combustible.
- **Facilitar el polimorfismo**: Permite tratar objetos de clases hijas como si fueran de la clase padre (más sobre esto en la sección de polimorfismo).

### Sintaxis de la herencia

En Python, la herencia se define al especificar la clase padre entre paréntesis al declarar la clase hija:

```python
class ClasePadre:
    def __init__(self, atributo):
        self.atributo = atributo

    def metodo_padre(self):
        return "Método de la clase padre"

class ClaseHija(ClasePadre):
    def metodo_hija(self):
        return "Método de la clase hija"
```

- `ClasePadre`: La clase de la que se hereda.
- `ClaseHija`: Hereda todos los atributos y métodos de `ClasePadre` y puede definir los suyos propios.

### Ejemplo práctico 1: Herencia simple con `Animal` y `Gato`

Crearemos una clase padre `Animal` y una clase hija `Gato` que hereda de ella.

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Sonido genérico de animal"

class Gato(Animal):
    def hacer_sonido(self):  # Sobrescribe el método del padre
        return f"{self.nombre} dice: ¡Miau!"

# Crear objetos
animal = Animal("Criatura")
gato = Gato("Luna")

# Usar métodos
print(animal.hacer_sonido())  # Salida: Sonido genérico de animal
print(gato.hacer_sonido())    # Salida: Luna dice: ¡Miau!
print(gato.nombre)            # Salida: Luna (atributo heredado)
```

**Explicación del ejemplo**:

- La clase `Animal` define un atributo `nombre` y un método `hacer_sonido`.
- La clase `Gato` hereda de `Animal`, por lo que tiene acceso al atributo `nombre` y al método `hacer_sonido`.
- `Gato` sobrescribe (`override`) el método `hacer_sonido` para devolver un sonido específico.
- El objeto `gato` usa el constructor de `Animal` (heredado) para inicializar `nombre`.

### Ejemplo práctico 2: Extendiendo la clase padre

Crearemos una clase `Vehículo` y una clase hija `Coche` que añade nuevos atributos y métodos.

```python
class Vehiculo:
    def __init__(self, marca, velocidad_max):
        self.marca = marca
        self.velocidad_max = velocidad_max

    def describir(self):
        return f"Vehículo de marca {self.marca} con velocidad máxima de {self.velocidad_max} km/h"

class Coche(Vehiculo):
    def __init__(self, marca, velocidad_max, puertas):
        super().__init__(marca, velocidad_max)  # Llama al constructor del padre
        self.puertas = puertas  # Nuevo atributo

    def describir(self):  # Sobrescribe el método del padre
        return f"Coche de marca {self.marca} con {self.puertas} puertas y velocidad máxima de {self.velocidad_max} km/h"

# Crear objetos
vehiculo = Vehiculo("Generic", 100)
coche = Coche("Toyota", 200, 4)

# Usar métodos
print(vehiculo.describir())  # Salida: Vehículo de marca Generic con velocidad máxima de 100 km/h
print(coche.describir())     # Salida: Coche de marca Toyota con 4 puertas y velocidad máxima de 200 km/h
```

**Explicación del ejemplo**:

- La clase `Vehiculo` define atributos (`marca`, `velocidad_max`) y un método (`describir`).
- La clase `Coche` hereda de `Vehiculo` y usa `super().__init__` para llamar al constructor de la clase padre, inicializando `marca` y `velocidad_max`.
- `Coche` añade un nuevo atributo (`puertas`) y sobrescribe el método `describir` para incluir información adicional.
- `super()` permite acceder a los métodos de la clase padre, evitando duplicar código.

### ¿Cuándo usar herencia?

- **Cuando hay una relación "es un"**: Por ejemplo, un `Coche` es un `Vehículo`, o un `Gato` es un `Animal`.
- **Para compartir código**: Si varias clases tienen atributos o métodos comunes, colócalos en una clase padre.
- **Para permitir polimorfismo**: Cuando quieres que las clases hijas puedan ser tratadas como la clase padre en ciertos contextos.
- **Para extender funcionalidades**: Cuando necesitas clases especializadas que añadan o modifiquen comportamientos.

### Nota: Herencia múltiple

Python soporta **herencia múltiple**, donde una clase puede heredar de varias clases padre. Sin embargo, debe usarse con cuidado para evitar problemas como el "problema del diamante" (ambigüedad en la resolución de métodos).

```python
class ClaseA:
    def metodo(self):
        return "Método de ClaseA"

class ClaseB:
    def metodo(self):
        return "Método de ClaseB"

class ClaseC(ClaseA, ClaseB):
    pass

obj = ClaseC()
print(obj.metodo())  # Salida: Método de ClaseA (sigue el orden de herencia)
```

---

## Encapsulamiento en Python

### ¿Qué es el encapsulamiento?

El **encapsulamiento** es un principio de la programación orientada a objetos que consiste en ocultar los detalles internos de una clase y controlar el acceso a sus atributos y métodos. Esto se logra restringiendo el acceso directo a los datos (atributos) y proporcionando métodos públicos para interactuar con ellos.

Piensa en el encapsulamiento como una cápsula: los datos y las operaciones internas están protegidos dentro de la clase, y solo se permite acceder a ellos de manera controlada.

### ¿Por qué usamos encapsulamiento?

- **Protección de datos**: Evita que los atributos sean modificados accidentalmente o de manera no deseada.
- **Control de acceso**: Permite definir reglas sobre cómo y quién puede acceder o modificar los datos.
- **Mantenimiento**: Los detalles internos de la clase pueden cambiar sin afectar el código que la usa, siempre que la interfaz pública permanezca igual.
- **Seguridad**: Limita el acceso a datos sensibles, como contraseñas o saldos bancarios.
- **Modularidad**: Facilita la comprensión del código al exponer solo lo necesario.

### ¿Para qué sirve el encapsulamiento?

- **Ocultar la implementación**: Los usuarios de la clase no necesitan saber cómo funciona internamente, solo cómo usarla.
- **Validar datos**: Los métodos pueden incluir lógica para asegurar que los datos sean válidos antes de modificar los atributos.
- **Evitar efectos secundarios**: Al restringir el acceso directo, se reduce el riesgo de que el código externo altere el estado de un objeto de forma inesperada.
- **Facilitar cambios**: Puedes modificar la implementación interna sin romper el código que depende de la clase.

### ¿Cómo se logra el encapsulamiento en Python?

Python no tiene palabras clave como `private` o `protected` como otros lenguajes (por ejemplo, Java). En su lugar, usa **convenciones de nombres** para indicar el nivel de acceso:

- **Público**: Atributos y métodos sin prefijos (por ejemplo, `self.atributo`). Accesibles desde cualquier lugar.
- **Protegido**: Atributos y métodos con un guion bajo (`self._atributo`). Por convención, indica que solo deben ser accedidos por la clase y sus subclases, aunque técnicamente son accesibles desde fuera.
- **Privado**: Atributos y métodos con doble guion bajo (`self.__atributo`). Python realiza un **name mangling** (cambio de nombre) para hacerlos más difíciles de acceder desde fuera de la clase.

El encapsulamiento se complementa con **métodos getter y setter** o el decorador `@property` para controlar el acceso a los atributos.

### Sintaxis

```python
class Ejemplo:
    def __init__(self, dato_publico, dato_protegido, dato_privado):
        self.dato_publico = dato_publico          # Público
        self._dato_protegido = dato_protegido     # Protegido
        self.__dato_privado = dato_privado        # Privado

    # Getter para dato_privado
    def get_dato_privado(self):
        return self.__dato_privado

    # Setter para dato_privado
    def set_dato_privado(self, valor):
        if valor >= 0:  # Validación
            self.__dato_privado = valor
```

- `_dato_protegido`: Por convención, no deberías acceder a él desde fuera, pero Python no lo impide.
- `__dato_privado`: Python cambia su nombre internamente (por ejemplo, a `_Ejemplo__dato_privado`), dificultando el acceso directo.

### Ejemplo práctico 1: Encapsulamiento con getters y setters

Crearemos una clase `CuentaBancaria` que encapsula el saldo y valida las operaciones.

```python
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular               # Público
        self.__saldo = saldo_inicial         # Privado

    def get_saldo(self):                    # Getter
        return self.__saldo

    def depositar(self, monto):             # Setter con validación
        if monto > 0:
            self.__saldo += monto
            return f"Depósito de ${monto:.2f} realizado. Nuevo saldo: ${self.__saldo:.2f}"
        return "El monto debe ser positivo."

    def retirar(self, monto):               # Setter con validación
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto
            return f"Retiro de ${monto:.2f} realizado. Nuevo saldo: ${self.__saldo:.2f}"
        return "Monto inválido o saldo insuficiente."

# Crear objeto
cuenta = CuentaBancaria("Ana", 1000)

# Acceder a atributos y métodos
print(cuenta.titular)           # Salida: Ana
print(cuenta.get_saldo())       # Salida: 1000
print(cuenta.depositar(500))    # Salida: Depósito de $500.00 realizado. NuevoMEs saldo: $1500.00
print(cuenta.retirar(200))      # Salida: Retiro de $200.00 realizado. Nuevo saldo: $1300.00
print(cuenta.retirar(2000))     # Salida: Monto inválido o saldo insuficiente.

# Intentar acceder al atributo privado directamente
print(cuenta.__saldo)           # Error: AttributeError
```

**Explicación del ejemplo**:

- El atributo `__saldo` es privado, por lo que no se puede acceder directamente desde fuera de la clase.
- Los métodos ` **get_saldo**, **depositar** y **retirar** controlan el acceso al saldo, incluyendo validaciones.
- Intentar acceder a `__saldo` directamente causa un error, demostrando el encapsulamiento.
- El atributo `titular` es público y se puede acceder libremente.

### Ejemplo práctico 2: Encapsulamiento con `@property`

Python permite usar el decorador `@property` para crear getters y setters de forma más elegante.

```python
class Estudiante:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__nombre = valor
        else:
            raise ValueError("El nombre debe ser una cadena no vacía")

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if isinstance(valor, int) and 0 <= valor <= 120:
            self.__edad = valor
        else:
            raise ValueError("La edad debe ser un número entre 0 y 120")

# Crear objeto
estudiante = Estudiante("Juan", 20)

# Usar propiedades
print(estudiante.nombre)  # Salida: Juan
estudiante.nombre = "Pedro"
print(estudiante.nombre)  # Salida: Pedro
print(estudiante.edad)   # Salida: 20
estudiante.edad = 21
print(estudiante.edad)   # Salida: 21

# Intentar asignar valores inválidos
try:
    estudiante.edad = -5
except ValueError as e:
    print(e)  # Salida: La edad debe ser un número entre 0 y 120
```

**Explicación del ejemplo**:

- El decorador `@property` convierte los métodos `nombre` y `edad` en propiedades, permitiendo acceder a ellos como si fueran atributos (`estudiante.nombre` en lugar de `estudiante.nombre()`).
- Los setters (`@nombre.setter`, `@edad.setter`) validan los valores antes de asignarlos.
- Si se intenta asignar un valor inválido, se lanza una excepción, protegiendo los datos.

### ¿Cuándo usar encapsulamiento?

- **Proteger datos sensibles**: Como saldos bancarios, contraseñas o configuraciones críticas.
- **Garantizar consistencia**: Para validar datos antes de modificar atributos.
- **Ocultar detalles de implementación**: Cuando los usuarios de la clase no necesitan saber cómo funcionan los datos internamente.
- **Facilitar mantenimiento**: Para poder cambiar la implementación sin afectar el código externo.

### Nota: Name mangling

El prefijo `__` no hace que un atributo sea completamente privado, sino que cambia su nombre internamente (por ejemplo, `__saldo` se convierte en `_CuentaBancaria__saldo`). Aunque es posible acceder a él usando este nombre modificado, hacerlo va contra las convenciones de Python.

```python
print(cuenta._CuentaBancaria__saldo)  # Salida: 1300.0 (no recomendado)
```

---

## Polimorfismo en Python

### ¿Qué es el polimorfismo?

El **polimorfismo** es un concepto de la programación orientada a objetos que permite que objetos de diferentes clases sean tratados como objetos de una clase común, y que un mismo método o función pueda comportarse de manera diferente dependiendo del tipo de objeto con el que se llame. El término "polimorfismo" significa "muchas formas", reflejando que una misma operación puede tener diferentes implementaciones.

En Python, el polimorfismo se logra principalmente a través de la **herencia** y la **sobrescritura de métodos**, aunque también se puede lograr con **duck typing** (si un objeto tiene los métodos necesarios, puede ser usado sin importar su tipo).

### ¿Por qué usamos polimorfismo?

- **Flexibilidad**: Permite escribir código que funcione con objetos de diferentes clases sin necesidad de conocer su tipo exacto.
- **Reutilización**: Facilita la extensión del código, ya que nuevas clases pueden implementar métodos existentes de manera específica.
- **Mantenimiento**: Reduce la necesidad de código duplicado, ya que un mismo método puede adaptarse a diferentes contextos.
- **Abstracción**: Permite trabajar con interfaces comunes, ocultando los detalles de implementación de cada clase.

### ¿Para qué sirve el polimorfismo?

- **Ejecutar comportamientos específicos**: Un método puede tener una implementación distinta en cada clase hija, adaptada a sus necesidades.
- **Tratar objetos de forma genérica**: Puedes procesar una lista de objetos de diferentes clases como si fueran del mismo tipo.
- **Extender sistemas**: Nuevas clases pueden añadirse sin modificar el código que usa la clase padre.
- **Simplificar el diseño**: Reduce la complejidad al usar interfaces comunes para objetos con comportamientos similares.

### ¿Cómo se implementa el polimorfismo en Python?

El polimorfismo en Python se implementa principalmente de dos formas:

1. **A través de herencia y sobrescritura de métodos**: Una clase hija hereda de una clase padre y redefine (sobrescribe) sus métodos para proporcionar una implementación específica.
2. **A través de duck typing**: Python permite que cualquier objeto que implemente ciertos métodos sea usado en un contexto, sin necesidad de herencia explícita.

### Sintaxis

```python
class ClasePadre:
    def metodo(self):
        pass

class ClaseHija1(ClasePadre):
    def metodo(self):
        return "Implementación en ClaseHija1"

class ClaseHija2(ClasePadre):
    def metodo(self):
        return "Implementación en ClaseHija2"
```

### Ejemplo práctico 1: Polimorfismo con herencia

Crearemos una clase padre `Figura` y dos clases hijas `Rectangulo` y `Circulo` que sobrescriben el método `calcular_area`.

```python
class Figura:
    def calcular_area(self):
        return 0  # Implementación por defecto

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio ** 2

# Crear objetos
figuras = [Rectangulo(4, 5), Circulo(3), Rectangulo(2, 3)]

# Usar polimorfismo
for figura in figuras:
    print(f"Área: {figura.calcular_area()}")
```

**Salida**:

```
Área: 20
Área: 28.2744
Área: 6
```

**Explicación del ejemplo**:

- La clase `Figura` define un método `calcular_area` con una implementación por defecto.
- `Rectangulo` y `Circulo` heredan de `Figura` y sobrescriben `calcular_area` con sus propias fórmulas.
- La lista `figuras` contiene objetos de diferentes clases, pero todos son tratados como `Figura` al llamar a `calcular_area`.
- El método ejecutado depende del tipo real del objeto, demostrando polimorfismo.

### Ejemplo práctico 2: Polimorfismo con duck typing

Python permite polimorfismo sin herencia explícita, siempre que los objetos implementen los métodos necesarios.

```python
class Perro:
    def hacer_sonido(self):
        return "¡Guau!"

class Gato:
    def hacer_sonido(self):
        return "¡Miau!"

class Vaca:
    def hacer_sonido(self):
        return "¡Muu!"

# Función que usa polimorfismo
def hacer_sonidos(animales):
    for animal in animales:
        print(animal.hacer_sonido())

# Crear objetos
animales = [Perro(), Gato(), Vaca()]

# Usar la función
hacer_sonidos(animales)
```

**Salida**:

```
¡Guau!
¡Miau!
¡Muu!
```

**Explicación del ejemplo**:

- Las clases `Perro`, `Gato` y `Vaca` no heredan de una clase común, pero todas implementan el método `hacer_sonido`.
- La función `hacer_sonidos` no necesita saber el tipo exacto de cada objeto, solo que tienen un método `hacer_sonido`.
- Esto es un ejemplo de **duck typing**: "Si camina como pato y suena como pato, es un pato".

### ¿Cuándo usar polimorfismo?

- **Cuando tienes clases relacionadas**: Si varias clases comparten una interfaz común pero necesitan implementaciones específicas.
- **Para procesar objetos genéricamente**: Cuando quieres trabajar con una colección de objetos de diferentes tipos.
- **Para extender sistemas**: Cuando planeas añadir nuevas clases en el futuro sin modificar el código existente.
- **Para simplificar el código**: Cuando quieres evitar estructuras condicionales complejas (como `if isinstance()`).

### Nota: Polimorfismo y funciones integradas

El polimorfismo también se observa en funciones integradas de Python, como `len()` o el operador `+`, que se comportan de manera diferente según el tipo de objeto:

```python
print(len("Hola"))        # Salida: 4 (longitud de la cadena)
print(len([1, 2, 3]))     # Salida: 3 (longitud de la lista)
print(3 + 4)              # Salida: 7 (suma de enteros)
print("Hola" + " Mundo")  # Salida: Hola Mundo (concatenación de cadenas)
```

Esto se logra porque las clases definen métodos especiales (como `__len__` o `__add__`) que Python llama automáticamente.

---

## MongoDB: ¿SQL o NoSQL?

### ¿Es MongoDB una base de datos SQL o NoSQL?

**MongoDB es una base de datos NoSQL**. A diferencia de las bases de datos SQL (como MySQL, PostgreSQL o SQL Server), que almacenan datos en tablas con filas y columnas siguiendo un esquema rígido, MongoDB utiliza un modelo **orientado a documentos** donde los datos se almacenan en documentos similares a JSON (en formato BSON, una variante binaria de JSON).

### ¿Qué significa NoSQL?

- **SQL (Structured Query Language)**: Bases de datos relacionales que usan tablas con esquemas fijos, relaciones definidas (claves primarias y foráneas) y consultas estructuradas. Son ideales para datos estructurados y transacciones complejas.
- **NoSQL (Not Only SQL)**: Bases de datos diseñadas para manejar datos no estructurados o semi-estructurados, con esquemas flexibles y alta escalabilidad. Son adecuadas para grandes volúmenes de datos, aplicaciones en tiempo real y estructuras de datos variables.

MongoDB es un ejemplo de base de datos **NoSQL de tipo documento**, lo que significa que organiza los datos en **colecciones** (equivalentes a tablas) que contienen **documentos** (equivalentes a filas, pero más flexibles).

### ¿Por qué MongoDB es NoSQL?

- **Esquema flexible**: Los documentos en una colección no necesitan tener la misma estructura. Por ejemplo, un documento puede tener campos que otro no tiene.
- **Formato de documentos**: Los datos se almacenan en documentos BSON, similares a JSON, que permiten estructuras anidadas (arrays, objetos, etc.).
- **Escalabilidad horizontal**: MongoDB está diseñado para escalar añadiendo más servidores (sharding), en lugar de aumentar la potencia de un solo servidor (escalabilidad vertical).
- **Sin joins complejos**: A diferencia de SQL, MongoDB evita uniones (joins) y en su lugar embede datos relacionados en un solo documento o usa referencias.

### ¿Para qué se usa MongoDB?

- **Aplicaciones en tiempo real**: Como redes sociales, análisis de datos o aplicaciones móviles, donde la velocidad y la escalabilidad son críticas.
- **Datos no estructurados o semi-estructurados**: Por ejemplo, registros de eventos, datos de sensores IoT o contenido multimedia.
- **Proyectos con esquemas cambiantes**: Cuando los requisitos de datos evolucionan rápidamente, MongoDB permite añadir o modificar campos sin migraciones complejas.
- **Big Data**: Su capacidad para manejar grandes volúmenes de datos lo hace ideal para aplicaciones de big data.

### Comparación SQL vs. NoSQL (MongoDB)

| Característica             | SQL (ej. MySQL, PostgreSQL)                  | NoSQL (MongoDB)                              |
|---------------------------|---------------------------------------------|---------------------------------------------|
| **Estructura**            | Tablas con filas y columnas                  | Colecciones con documentos                   |
| **Esquema**               | Rígido, requiere definición previa           | Flexible, sin esquema fijo                  |
| **Datos**                 | Estructurados                               | No estructurados o semi-estructurados        |
| **Escalabilidad**         | Vertical (mejor hardware)                   | Horizontal (más servidores)                  |
| **Consultas**             | SQL estándar, soporta joins complejos        | Consultas basadas en documentos, sin joins   |
| **Transacciones**         | Fuertes (ACID completo)                     | Soporte parcial para transacciones (desde 4.0) |
| **Casos de uso**          | Sistemas financieros, ERP, CRM               | Redes sociales, IoT, análisis en tiempo real |

### Ejemplo práctico: Almacenando datos en MongoDB

Supongamos que queremos almacenar información de estudiantes. En una base de datos SQL, tendríamos una tabla con columnas fijas:

```sql
CREATE TABLE Estudiantes (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT,
    curso VARCHAR(50)
);
```

En MongoDB, los datos se almacenan como documentos en una colección, y cada documento puede tener diferentes campos:

```javascript
// Colección: estudiantes
{
    "_id": "1",
    "nombre": "Ana",
    "edad": 20,
    "curso": "Matemáticas",
    "notas": [8, 9, 7]
}
{
    "_id": "2",
    "nombre": "Luis",
    "edad": 22,
    "hobbies": ["fútbol", "lectura"]
}
```

**Observaciones**:
- El primer documento tiene un campo `notas`, pero el segundo no.
- El segundo documento tiene un campo `hobbies`, que el primero no tiene.
- Esto muestra la flexibilidad de MongoDB para manejar estructuras variables.

### Conexión con Python

Para interactuar con MongoDB desde Python, se usa la librería **PyMongo**. Aquí un ejemplo básico:

```python
import pymongo

# Conectar al servidor de MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Seleccionar una base de datos
db = client["mi_base_de_datos"]

# Seleccionar una colección
coleccion = db["estudiantes"]

# Insertar un documento
estudiante = {"nombre": "María", "edad": 21, "curso": "Física"}
coleccion.insert_one(estudiante)

# Consultar todos los documentos
for doc in coleccion.find():
    print(doc)
```

**Salida** (suponiendo que los documentos anteriores están en la colección):

```python
{'_id': '1', 'nombre': 'Ana', 'edad': 20, 'curso': 'Matemáticas', 'notas': [8, 9, 7]}
{'_id': '2', 'nombre': 'Luis', 'edad': 22, 'hobbies': ['fútbol', 'lectura']}
{'_id': ObjectId('...'), 'nombre': 'María', 'edad': 21, 'curso': 'Física'}
```

### ¿Cuándo usar MongoDB?

- **Usa MongoDB si**:
  - Trabajas con datos no estructurados o con esquemas que cambian frecuentemente.
  - Necesitas alta escalabilidad para grandes volúmenes de datos.
  - Tu aplicación requiere alta velocidad en lecturas/escrituras (por ejemplo, aplicaciones en tiempo real).
  - Quieres evitar joins complejos y prefieres datos embebidos.

- **No uses MongoDB si**:
  - Necesitas transacciones complejas con garantías ACID estrictas.
  - Tus datos son altamente relacionales y requieren múltiples joins.
  - Prefieres un esquema rígido para garantizar consistencia.

---

## ¿Qué es una API?

### ¿Qué es una API?

Una **API** (Interfaz de Programación de Aplicaciones, por sus siglas en inglés: *Application Programming Interface*) es un conjunto de reglas y herramientas que permite que diferentes aplicaciones o sistemas se comuniquen entre sí. Actúa como un intermediario que permite a una aplicación solicitar datos o servicios de otra, sin necesidad de entender los detalles internos de cómo funciona el sistema proveedor.

Piensa en una API como un camarero en un restaurante: tú (la aplicación cliente) haces un pedido (una solicitud), el camarero lleva el pedido a la cocina (el sistema servidor), y luego te trae la comida (la respuesta). No necesitas saber cómo se prepara la comida, solo cómo hacer el pedido.

### ¿Por qué usamos APIs?

- **Interoperabilidad**: Permiten que aplicaciones desarrolladas en diferentes lenguajes o plataformas trabajen juntas.
- **Modularidad**: Dividen sistemas complejos en componentes que pueden interactuar sin exponer su funcionamiento interno.
- **Automatización**: Facilitan la integración de servicios externos, como mapas, pagos o redes sociales, en tus aplicaciones.
- **Escalabilidad**: Las APIs permiten que los servicios sean utilizados por múltiples clientes sin necesidad de compartir código fuente.
- **Seguridad**: Controlan el acceso a los datos o servicios mediante autenticación y permisos.

### ¿Para qué sirve una API?

- **Obtener datos**: Por ejemplo, usar la API de Twitter para obtener los últimos tweets o la API de Google Maps para obtener direcciones.
- **Realizar acciones**: Como enviar un correo con la API de SendGrid o procesar un pago con la API de Stripe.
- **Integrar servicios**: Conectar una aplicación con plataformas externas, como añadir un botón de "Iniciar sesión con Google".
- **Automatizar procesos**: Por ejemplo, una API que sincroniza datos entre un CRM y un sistema de marketing.
- **Crear ecosistemas**: Las APIs permiten a terceros construir aplicaciones que usan los servicios de una plataforma (por ejemplo, aplicaciones que usan la API de Spotify).

### Tipos de APIs

- **APIs REST**: Basadas en HTTP, usan métodos como GET, POST, PUT, DELETE y devuelven datos en formatos como JSON o XML. Son las más comunes en aplicaciones web.
- **APIs SOAP**: Usan XML y son más estructuradas, comunes en sistemas empresariales.
- **APIs GraphQL**: Permiten solicitar solo los datos necesarios, más flexibles que REST.
- **APIs de bibliotecas/frameworks**: Como las APIs de Python (por ejemplo, `requests`) o de frameworks como Django.
- **APIs de hardware**: Permiten interactuar con dispositivos, como sensores o cámaras.

### Ejemplo práctico: Usando una API REST con Python

Usaremos la API pública de **OpenWeatherMap** para obtener el clima de una ciudad. Necesitas una clave de API (puedes registrarte gratis en su sitio web).

```python
import requests

# Configuración
api_key = "TU_CLAVE_DE_API"  # Reemplaza con tu clave
ciudad = "Bogotá"
url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric"

# Hacer la solicitud
respuesta = requests.get(url)

# Verificar si la solicitud fue exitosa
if respuesta.status_code == 200:
    datos = respuesta.json()
    temperatura = datos["main"]["temp"]
    descripcion = datos["weather"][0]["description"]
    print(f"El clima en {ciudad} es {descripcion} con una temperatura de {temperatura}°C")
else:
    print("Error al obtener los datos")
```

**Salida** (ejemplo):

```
El clima en Bogotá es nubes dispersas con una temperatura de 15°C
```

**Explicación del ejemplo**:

- Usamos la librería `requests` para hacer una solicitud HTTP GET a la API de OpenWeatherMap.
- La URL incluye la ciudad, la clave de API y un parámetro para obtener la temperatura en grados Celsius (`units=metric`).
- La respuesta se devuelve en formato JSON, que convertimos a un diccionario Python con `respuesta.json()`.
- Extraemos la temperatura y la descripción del clima para mostrarlas.

### Componentes de una API

- **Endpoint**: Una URL específica que representa un recurso o acción (por ejemplo, `/users` o `/weather`).
- **Métodos HTTP**: Indican la acción a realizar:
  - **GET**: Obtener datos.
  - **POST**: Crear datos.
  - **PUT**: Actualizar datos.
  - **DELETE**: Eliminar datos.
- **Parámetros**: Datos enviados en la URL (query parameters) o en el cuerpo de la solicitud.
- **Códigos de estado**: Indican el resultado de la solicitud (200: OK, 404: No encontrado, 500: Error del servidor).
- **Autenticación**: Métodos como claves API, tokens OAuth o JWT para asegurar el acceso.

### ¿Cuándo usar una API?

- **Integrar servicios externos**: Como mapas, pagos, autenticación o mensajería.
- **Construir aplicaciones modulares**: Separar el frontend del backend, comunicándolos vía API.
- **Automatizar tareas**: Sincronizar datos entre sistemas o procesar información en tiempo real.
- **Crear plataformas**: Permitir que terceros desarrollen aplicaciones usando tus servicios.

---

## ¿Qué es Postman?

### ¿Qué es Postman?

**Postman** es una herramienta utilizada por desarrolladores para **diseñar, probar y documentar APIs**. Es una plataforma que simplifica el proceso de enviar solicitudes a APIs, inspeccionar respuestas, automatizar pruebas y colaborar en proyectos de desarrollo. Postman es especialmente útil para trabajar con APIs REST, aunque también soporta otros tipos como GraphQL o SOAP.

Piensa en Postman como un "laboratorio" donde puedes experimentar con APIs: enviar solicitudes, verificar respuestas y asegurarte de que todo funciona antes de integrar la API en tu aplicación.

### ¿Por qué usamos Postman?

- **Facilidad de uso**: Su interfaz gráfica permite enviar solicitudes HTTP sin escribir código.
- **Pruebas rápidas**: Puedes probar endpoints, parámetros y autenticación de una API en minutos.
- **Automatización**: Permite crear scripts y colecciones de pruebas para verificar el comportamiento de una API.
- **Colaboración**: Equipos pueden compartir colecciones de solicitudes y documentación.
- **Depuración**: Ayuda a identificar errores en las solicitudes o respuestas de una API.
- **Documentación**: Genera documentación automática de APIs basada en las solicitudes creadas.

### ¿Para qué sirve Postman?

- **Probar APIs**: Enviar solicitudes GET, POST, PUT, DELETE, etc., y analizar las respuestas (JSON, XML, etc.).
- **Automatizar pruebas**: Crear scripts para verificar que una API responde correctamente (por ejemplo, que un endpoint devuelve un código 200).
- **Simular entornos**: Configurar variables de entorno para probar en desarrollo, pruebas o producción.
- **Documentar APIs**: Crear documentación clara para que otros desarrolladores usen la API.
- **Integrar con CI/CD**: Ejecutar pruebas de APIs como parte de pipelines de integración continua.
- **Explorar APIs públicas**: Probar APIs de terceros antes de integrarlas en tu proyecto.

### Características principales de Postman

- **Interfaz gráfica**: Formularios para configurar URL, parámetros, headers, cuerpo de la solicitud y autenticación.
- **Colecciones**: Agrupar solicitudes relacionadas (por ejemplo, todas las solicitudes de una API).
- **Scripts**: Escribir pruebas en JavaScript para validar respuestas (por ejemplo, verificar que un campo existe en el JSON).
- **Entornos**: Definir variables (como URLs base o tokens) para diferentes configuraciones.
- **Mock servers**: Crear servidores simulados para probar cómo responde una API antes de implementarla.
- **Monitorización**: Ejecutar colecciones de pruebas periódicamente para verificar la disponibilidad de una API.

### Ejemplo práctico: Probando una API con Postman

Supongamos que queremos probar la API de **JSONPlaceholder**, una API pública para pruebas. Vamos a enviar una solicitud GET para obtener una lista de usuarios.

1. **Abrir Postman** y crear una nueva solicitud.
2. Configurar la solicitud:
   - **Método**: GET
   - **URL**: `https://jsonplaceholder.typicode.com/users`
   - **Headers** (opcional): Por ejemplo, `Content-Type: application/json`.
3. Hacer clic en **Send** para enviar la solicitud.
4. Inspeccionar la respuesta:
   - **Cuerpo**: Un arreglo JSON con datos de usuarios.
   - **Código de estado**: 200 OK.
5. Crear una prueba:
   - En la pestaña **Tests**, añadir un script:

```javascript
pm.test("La respuesta contiene usuarios", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('array');
    pm.expect(jsonData.length).to.be.above(0);
});
```

6. Guardar la solicitud en una **colección** llamada "JSONPlaceholder Tests".

**Respuesta esperada** (en el panel de respuesta de Postman):

```json
[
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        ...
    },
    ...
]
```

**Explicación**:

- La solicitud GET obtiene una lista de usuarios en formato JSON.
- El script de prueba verifica que la respuesta es un arreglo y que contiene al menos un elemento.
- La solicitud se guarda en una colección para reutilizarla o compartirla con el equipo.

### ¿Cómo empezar con Postman?

1. **Descargar e instalar**: Postman está disponible gratis en [www.postman.com](https://www.postman.com). Hay versiones para Windows, macOS y Linux.
2. **Crear una cuenta** (opcional): Para sincronizar colecciones y colaborar con equipos.
3. **Explorar la interfaz**:
   - **Workspace**: Área donde creas solicitudes y colecciones.
   - **Request**: Panel para configurar y enviar solicitudes.
   - **Collections**: Agrupaciones de solicitudes.
   - **Environments**: Configuraciones para diferentes entornos.
4. **Probar una API pública**: Usa APIs como JSONPlaceholder, OpenWeatherMap o ReqRes para practicar.
5. **Aprender con tutoriales**: Postman ofrece documentación y tutoriales en su sitio web.

### ¿Cuándo usar Postman?

- **Desarrollo de APIs**: Para diseñar y probar endpoints durante el desarrollo.
- **Pruebas de integración**: Para verificar que una API funciona correctamente antes de usarla en producción.
- **Depuración**: Para identificar errores en solicitudes o respuestas.
- **Documentación**: Para generar guías claras para otros desarrolladores.
- **Colaboración**: Cuando un equipo necesita compartir y mantener pruebas de APIs.
- **Exploración**: Para entender cómo funciona una API de terceros antes de integrarla.

---

## ¿Qué es un método dunder?

### ¿Qué es un método dunder?

Un **método dunder** (abreviatura de "double underscore", o doble guion bajo) es un método especial en Python que comienza y termina con doble guion bajo (por ejemplo, `__init__`, `__str__`, `__add__`). Estos métodos son parte del **modelo de datos** de Python y definen cómo los objetos de una clase interactúan con operaciones integradas, como la creación de objetos, la representación en texto, las operaciones aritméticas o las comparaciones.

Los métodos dunder también se conocen como **métodos mágicos** o **métodos especiales**, porque Python los llama automáticamente en ciertas situaciones, sin que el programador los invoque explícitamente.

### ¿Por qué usamos métodos dunder?

- **Personalizar comportamientos**: Permiten definir cómo se comporta un objeto en operaciones estándar, como sumar dos objetos o convertir un objeto a cadena.
- **Integración con Python**: Hacen que los objetos de una clase se integren naturalmente con las características del lenguaje, como los operadores (`+`, `==`) o funciones integradas (`len()`, `str()`).
- **Abstracción**: Ocultan la implementación interna, permitiendo que el código sea más legible y expresivo.
- **Extensibilidad**: Facilitan la creación de clases que actúan como tipos integrados de Python.

### ¿Para qué sirven los métodos dunder?

- **Inicialización**: Definir cómo se crea un objeto (`__init__`, `__new__`).
- **Representación**: Controlar cómo se muestra un objeto como cadena (`__str__`, `__repr__`).
- **Operaciones aritméticas**: Implementar operadores como `+`, `-`, `*` (`__add__`, `__sub__`, `__mul__`).
- **Comparaciones**: Definir operadores como `==`, `<`, `>` (`__eq__`, `__lt__`, `__gt__`).
- **Acceso a atributos**: Controlar cómo se accede o modifica un atributo (`__getattr__`, `__setattr__`).
- **Iteración**: Hacer que un objeto sea iterable (`__iter__`, `__next__`).
- **Llamadas**: Permitir que un objeto sea "llamado" como una función (`__call__`).

### Lista de métodos dunder comunes

| Método          | Descripción                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `__init__(self, ...)` | Constructor, inicializa un objeto.                                         |
| `__str__(self)` | Devuelve una representación legible del objeto (usada por `str()`).        |
| `__repr__(self)` | Devuelve una representación técnica del objeto (usada por `repr()`).       |
| `__add__(self, other)` | Implementa el operador `+`.                                               |
| `__eq__(self, other)` | Implementa el operador `==`.                                              |
| `__len__(self)` | Devuelve la longitud del objeto (usada por `len()`).                      |
| `__getitem__(self, key)` | Permite acceder a elementos como en una lista o diccionario (`obj[key]`). |
| `__iter__(self)` | Hace que el objeto sea iterable.                                          |
| `__call__(self, ...)` | Permite que el objeto sea llamado como una función.                       |

### Ejemplo práctico 1: Métodos dunder en una clase `Vector`

Crearemos una clase `Vector` que usa métodos dunder para soportar suma, igualdad y representación.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

# Crear objetos
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = Vector(1, 2)

# Usar métodos dunder
print(v1)              # Salida: Vector(1, 2)
print(repr(v1))        # Salida: Vector(x=1, y=2)
print(v1 + v2)         # Salida: Vector(4, 6)
print(v1 == v3)        # Salida: True
print(v1 == v2)        # Salida: False
```

**Explicación del ejemplo**:

- `__init__`: Inicializa el vector con coordenadas `x` e `y`.
- `__str__`: Devuelve una representación legible del vector.
- `__repr__`: Devuelve una representación técnica, útil para depuración.
- `__add__`: Permite sumar dos vectores, creando un nuevo vector.
- `__eq__`: Compara dos vectores para verificar si son iguales.

### Ejemplo práctico 2: Hacer un objeto iterable

Crearemos una clase `Rango` que usa `__iter__` y `__next__` para ser iterable, similar a `range()`.

```python
class Rango:
    def __init__(self, inicio, fin):
        self.actual = inicio
        self.fin = fin

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual >= self.fin:
            raise StopIteration
        valor = self.actual
        self.actual += 1
        return valor

# Usar la clase
for num in Rango(1, 5):
    print(num)
```

**Salida**:

```
1
2
3
4
```

**Explicación del ejemplo**:

- `__init__`: Inicializa el rango con un valor de inicio y fin.
- `__iter__`: Indica que el objeto es su propio iterador.
- `__next__`: Devuelve el siguiente valor en la secuencia o lanza `StopIteration` cuando termina.
- El bucle `for` usa estos métodos automáticamente para iterar.

### ¿Cuándo usar métodos dunder?

- **Personalizar comportamientos**: Cuando quieres que tus objetos se comporten como tipos integrados de Python.
- **Mejorar la legibilidad**: Para hacer que el código sea más intuitivo (por ejemplo, `obj + obj` en lugar de `obj.sumar(obj)`).
- **Integrar con Python**: Para que tus clases trabajen con funciones como `len()`, `str()` o bucles `for`.
- **Crear abstracciones**: Para ocultar la complejidad interna y ofrecer una interfaz simple.

### Nota: Convenciones

- Los métodos dunder son parte del núcleo de Python, así que úsalos solo para los propósitos previstos. No crees métodos con nombres como `__mi_metodo__`, ya que podrían entrar en conflicto con futuros métodos de Python.
- Documenta claramente tus métodos dunder, ya que su propósito no siempre es obvio.

---

## ¿Qué es un decorador en Python?

### ¿Qué es un decorador?

Un **decorador** en Python es una función que toma otra función como argumento y extiende o modifica su comportamiento sin cambiar su código fuente. Es una forma de **programación funcional** que permite envolver una función con funcionalidad adicional, como registro (logging), control de acceso, medición de tiempo o memorización.

Los decoradores se implementan usando el símbolo `@` seguido del nombre del decorador, colocado encima de la definición de una función o método.

### ¿Por qué usamos decoradores?

- **Reutilización de código**: Evitan repetir lógica común en múltiples funciones.
- **Separación de preocupaciones**: Mantienen el código principal limpio, delegando tareas secundarias (como logging o autenticación) al decorador.
- **Legibilidad**: Hacen que el propósito de la función sea claro, ya que el decorador describe su comportamiento adicional.
- **Flexibilidad**: Permiten añadir o quitar funcionalidades dinámicamente.
- **Mantenimiento**: Facilitan modificar el comportamiento de funciones sin alterar su código.

### ¿Para qué sirven los decoradores?

- **Logging**: Registrar información sobre la ejecución de una función (por ejemplo, argumentos, tiempo de ejecución).
- **Autenticación/Autorización**: Verificar permisos antes de ejecutar una función.
- **Medición de rendimiento**: Calcular el tiempo que tarda una función en ejecutarse.
- **Memorización**: Almacenar resultados de funciones costosas para reutilizarlos.
- **Validación**: Comprobar argumentos o condiciones antes de ejecutar una función.
- **Modificación de entrada/salida**: Transformar los argumentos o el valor retornado por una función.

### Sintaxis

```python
def mi_decorador(func):
    def envoltura(*args, **kwargs):
        # Código antes de la función
        resultado = func(*args, **kwargs)
        # Código después de la función
        return resultado
    return envoltura

@mi_decorador
def mi_funcion():
    # Código de la función
    pass
```

- `mi_decorador`: La función decoradora que toma una función (`func`) como argumento.
- `envoltura`: Una función interna que envuelve la función original, añadiendo comportamiento.
- `*args, **kwargs`: Permiten que `envoltura` acepte cualquier número de argumentos posicionales y nombrados.
- `@mi_decorador`: Aplica el decorador a `mi_funcion`, equivalente a `mi_funcion = mi_decorador(mi_funcion)`.

### Ejemplo práctico 1: Decorador para medir tiempo

Crearemos un decorador que mide el tiempo de ejecución de una función.

```python
import time

def medir_tiempo(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} tomó {fin - inicio:.4f} segundos")
        return resultado
    return envoltura

@medir_tiempo
def calcular_factorial(n):
    return 1 if n == 0 else n * calcular_factorial(n - 1)

# Usar la función
calcular_factorial(10)
```

**Salida** (ejemplo):

```
calcular_factorial tomó 0.0001 segundos
```

**Explicación del ejemplo**:

- `medir_tiempo` es el decorador que mide el tiempo antes y después de ejecutar la función.
- `envoltura` ejecuta la función original (`func`) y calcula el tiempo transcurrido.
- `@medir_tiempo` aplica el decorador a `calcular_factorial`, imprimiendo el tiempo de ejecución.

### Ejemplo práctico 2: Decorador para logging

Crearemos un decorador que registra los argumentos y el resultado de una función.

```python
def registrar(func):
    def envoltura(*args, **kwargs):
        print(f"Llamando a {func.__name__} con argumentos {args} y kwargs {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} retornó {resultado}")
        return resultado
    return envoltura

@registrar
def sumar(a, b):
    return a + b

# Usar la función
sumar(3, 5)
```

**Salida**:

```
Llamando a sumar con argumentos (3, 5) y kwargs {}
sumar retornó 8
```

**Explicación del ejemplo**:

- `registrar` imprime los argumentos y el resultado de la función decorada.
- `envoltura` captura los argumentos (`*args`, `**kwargs`) y el valor retornado.
- `@registrar` aplica el decorador a `sumar`, registrando su ejecución.

### Decoradores con argumentos

Los decoradores también pueden aceptar argumentos, lo que requiere una capa adicional de funciones.

```python
def repetir(n):
    def decorador(func):
        def envoltura(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return envoltura
    return decorador

@repetir