# ADR 002: Separación de la Lógica de Negocio en Servicios

* **Estado:** Aceptado e Implementado

* **Problema (Semana 3):** Las validaciones complejas (como comprobar si el stock disponible en bodega es suficiente antes de procesar un pedido) se ejecutaban mezcladas dentro del controlador HTTP.

* **Cambio Propuesto (Semana 13):** Crear la capa de servicios (`src/services/`) para centralizar y encapsular todas las reglas de negocio del sistema de suelas.

* **Código Afectado (Semana 13):** Lógica transaccional de creación de pedidos y validación de inventario movida desde `app.py` hacia `pedido_service.py`.

* **Atributo de Calidad que Mejora (Semana 8):** Mantenibilidad y Testabilidad.

* **Resultado e Impacto de la Implementación (Semana 15):** Se consolidó la separación de la lógica en `src/services/`, permitiendo que los controladores solo reciban solicitudes y devuelvan respuestas. Durante las pruebas finales del módulo MVP, se comprobó que esta estructura facilita la testabilidad de las reglas de negocio de la fábrica de suelas de forma aislada y mejora notablemente la mantenibilidad ante futuros cambios en los flujos de pedidos.
