# ADR 002: Separación de la Lógica de Negocio en Servicios

* **Estado:** Aceptado
* **Problema (Semana 3):** Validaciones complejas (como verificar si el stock en bodega alcanza antes de procesar una orden o calcular el flujo de pedido) se ejecutaban en la misma función de respuesta HTTP.
* **Cambio Propuesto:** Crear la capa de servicios en `src/services/` para encapsular las reglas de negocio del dominio de la fábrica de suelas.
* **Código Afectado:** Transacciones y reglas de control de inventario movidas desde los controladores web hacia `pedido_service.py` y otros módulos de servicio.
* **Atributo de Calidad que Mejora (Semana 8):** Mantenibilidad, Testabilidad y Confiabilidad.
