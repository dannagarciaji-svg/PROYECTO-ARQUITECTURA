# Arquitectura del Sistema - Módulo de Órdenes y Pedidos

## 1. Problemas Arquitectónicos Actuales

* **Alto acoplamiento entre la aplicación y la base de datos:** Algunas rutas del backend realizan directamente las operaciones de acceso a la base de datos mediante Pyodbc mientras contienen lógica de procesamiento.
* **Poca separación de responsabilidades:** Rutas como `/crear_pedido` concentran la recepción de datos, validaciones, consulta de stock, modificación de inventario y registro de pedidos dentro del mismo flujo.
* **Dependencia directa del servicio de base de datos:** El funcionamiento del módulo depende totalmente de la disponibilidad de SQL Server.
* **Mantenibilidad reducida:** Realizar cambios futuros aumenta la posibilidad de afectar funciones que actualmente operan correctamente.

---

## 2. Atributos de Calidad Priorizados

### Mantenibilidad
Se busca separar la lógica de presentación, el acceso a datos y la lógica de negocio para permitir modificaciones independientes en las rutas `/crear_pedido`, `/actualizar_pedido`, `/eliminar_pedido` y `/actualizar_estado_pedido`.

### Confiabilidad
Garantizar la consistencia entre los registros de pedidos e inventario mediante un manejo adecuado de transacciones y errores. Si la creación falla, las unidades descontadas del inventario no deben guardarse, y al eliminar un pedido se deben restaurar las unidades.

### Eficiencia de Ejecución
Controlar las operaciones simultáneas sobre el campo `stock_disponible` de la tabla `Suelas` para evitar sobreventa o registros con inventario insuficiente cuando varios usuarios operan al mismo tiempo.

---

## 3. Escenarios de Calidad

### Escenario 1: Mantenibilidad
* **Estímulo:** Se necesita realizar un cambio en la lógica de modificación de un pedido.
* **Fuente del estímulo:** Desarrollador encargado de modificar el sistema.
* **Entorno:** Sistema en desarrollo.
* **Artefacto:** Backend del módulo (`/crear_pedido`, `/actualizar_pedido` y acceso a datos).
* **Respuesta esperada:** Permitir la modificación alterando solo la lógica correspondiente, sin afectar la base de datos o interfaz.
* **Medida de respuesta:** El cambio se realiza sin impactar otras partes del sistema.

### Escenario 2: Confiabilidad
* **Estímulo:** Error al guardar alguna operación al crear un pedido o actualizar inventario.
* **Fuente del estímulo:** Solicitud realizada por un usuario desde la interfaz web.
* **Entorno:** Registro de pedido con transacciones sobre SQL Server.
* **Artefacto:** Ruta `/crear_pedido` y tablas `Suelas`, `Pedidos` y `DetallePedido`.
* **Respuesta esperada:** Controlar el error y revertir los cambios parciales.
* **Medida de respuesta:** No se registran pedidos sin detalle ni queda inventario descontado si el proceso falla.

### Escenario 3: Eficiencia de Ejecución
* **Estímulo:** La persona encargada intenta registrar un pedido cuya cantidad solicitada supera el stock disponible actual en la bodega. 
* **Fuente del estímulo:** Solicitud ingresada por la única operadora desde la interfaz web del sistema. 
* **Entorno:** Operación cotidiana donde la administradora gestiona y registra las órdenes de los clientes. 
* **Artefacto:** La ruta /crear_pedido, la capa de servicios, el repositorio suela_repository.py y la tabla Suelas (stock_disponible).
* **Respuesta esperada:** El sistema procesa la validación del inventario a través de la capa de servicios antes de impactar la base de datos, detectando inmediatamente si las existencias son insuficientes.
* **Medida de respuesta:** El sistema bloquea el registro del pedido de forma limpia, despliega una alerta de stock insuficiente y evita que el inventario quede con valores negativos o inconsistentes. 
---

## 4. Especificación del Caso de Uso Principal (CU-01 Crear Pedido)

* **Actor Principal:** Usuario Operador
* **Actor Secundario:** SQL Server
* **Propósito:** Registrar un pedido y actualizar las existencias de suelas.
* **Precondiciones:** El cliente debe estar registrado y la suela debe existir en el catálogo.
* **Flujo Principal:**
  1. El operador selecciona cliente, referencia de suela, color y cantidad.
  2. El sistema valida que la cantidad sea un entero positivo.
  3. *(Include)* Consulta el stock disponible en SQL Server.
  4. Confirma existencias suficientes.
  5. Inserta el pedido y su detalle.
  6. Descuenta la cantidad vendida del stock y confirma la transacción.
* **Flujos Alternativos:**
  * **A1 (Datos inválidos):** Si la cantidad es cero o negativa, muestra mensaje de error.
  * **A2 (Stock insuficiente):** Cancela la inserción y despliega la alerta "Stock insuficiente en bodega".

---

## 5. Conclusiones

A partir del análisis realizado, se establecieron tres atributos de calidad como principales para la re-arquitectura del módulo de Órdenes y Pedidos: Mantenibilidad, confiabilidad y eficiencia de ejecución. La elección de estos atributos se encuentra relacionada con las principales dificultades y situaciones encontradas en el funcionamiento actual del módulo.

La mantenibilidad permitirá mejorar la organización de las responsabilidades dentro del sistema separando rutas, servicios y repositorios y facilitar la implementación de cambios futuros de forma independiente. Por su parte, la confiabilidad ayudará a garantizar que la información de los pedidos y el inventario se mantenga consistente, implementando un manejo adecuado de transacciones mediante pyodbc para evitar registros incompletos o errores en las existencias. Finalmente, la eficiencia de ejecución permitirá gestionar de manera precisa y controlada las operaciones sobre el inventario que realiza la persona encargada, asegurando que las validaciones de stock prevengan cualquier inconsistencia o valores negativos en bodega.

Estos atributos se utilizaron como base para establecer las decisiones arquitectónicas y los ADRs que guían la evolución del sistema. De esta manera, se logró mejorar la estructura y la modularidad del módulo, manteniendo las funcionalidades operativas actuales y evitando realizar modificaciones innecesarias para la fábrica.

---

---

## 6. Componentes y Responsabilidades de la Nueva Arquitectura

| Componente | Responsabilidad Principal | Dependencias | Paquete / Archivo Representativo |
| :--- | :--- | :--- | :--- |
| **Controladores (Routes)** | Recibir las peticiones HTTP de los formularios, coordinar llamadas y renderizar las plantillas web. | Services | `src/routes/` |
| **Servicios (Services)** | Procesar la lógica de negocio, validaciones de stock y transacciones del dominio de la fábrica. | Repositories | `src/services/` |
| **Repositorios (Repositories)** | Encapsular la persistencia y la ejecución de consultas SQL hacia SQL Server mediante Pyodbc. | Base de Datos | `src/repositories/` |
| **Configuración (Config)** | Centralizar las credenciales y la cadena de conexión a la base de datos corporativa. | Pyodbc | `src/config.py` |

---

## 7. Resumen de Decisiones de Refactorización (ADRs)

Las decisiones adoptadas para guiar la evolución del código son:
1. **[ADR-001: Implementación del Patrón Repositorio](adr/adr-001-patron-repositorio.md)** — Aislar las consultas SQL de las rutas web para mejorar la mantenibilidad y seguridad.
2. **[ADR-002: Separación de la Lógica de Negocio en Servicios](adr/adr-002-capa-servicios.md)** — Extraer las validaciones de inventario y reglas de pedidos a servicios dedicados.
3. **[ADR-003: Desacoplamiento de la Configuración de Base de Datos](adr/adr-003-desacoplamiento-config.md)** — Modularizar la conexión a SQL Server.

---

## 9. Diagramas de Arquitectura (C4 y Despliegue - Semana 15)

### 9.1. Diagrama de Contexto (Nivel 1)
📁 [Ver Diagrama de Contexto (c4_contexto.png)](diagramas/c4_contexto.png)

### 9.2. Diagrama de Contenedores (Nivel 2)
📁 [Ver Diagrama de Contenedores (c4_contenedores.png)](diagramas/c4_contenedores.png)

### 9.3. Diagrama de Componentes (Nivel 3)
📁 [Ver Diagrama de Componentes (c4_componentes.png)](diagramas/c4_componentes.png)

### 9.4. Diagrama de Despliegue (Entorno Local)
📁 [Ver Diagrama de Despliegues (c4_despliegues.png)](diagramas/c4_despliegues.png)
