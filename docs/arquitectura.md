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
* **Estímulo:** Dos usuarios realizan pedidos simultáneos de la misma suela con stock limitado.
* **Fuente del estímulo:** Dos solicitudes al mismo tiempo desde la interfaz.
* **Entorno:** Operación normal del sistema.
* **Artefacto:** Ruta `/crear_pedido`, tabla `Suelas` (`stock_disponible`), `Pedidos` y `DetallePedido`.
* **Respuesta esperada:** Gestionar las solicitudes asegurando que la cantidad no supere el stock disponible.
* **Medida de respuesta:** El inventario final coincide con los pedidos procesados y `stock_disponible` no queda negativo.

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

La re-arquitectura del módulo garantiza una separación limpia de responsabilidades[cite: 2]. Priorizar Mantenibilidad, Confiabilidad y Eficiencia de Ejecución asegurará la estabilidad del sistema a medida que la fábrica de suelas escale sus operaciones.