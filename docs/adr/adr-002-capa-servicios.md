# ADR 002: Separación de la Lógica de Negocio en Servicios

* **Problema (Semana 3):** Las validaciones complejas (como comprobar si el stock disponible en bodega es suficiente antes de procesar un pedido) se ejecutaban mezcladas dentro del controlador HTTP.
* **Cambio Propuesto:** Crear la capa de servicios (`src/services/`) para centralizar y encapsular todas las reglas de negocio del sistema de suelas.
* **Código Afectado:** Lógica transaccional de creación de pedidos y validación de inventario movida desde `app.py` hacia `pedido_service.py`.
* **Atributo de Calidad que Mejora (Semana 8):** Mantenibilidad y Testabilidad.
