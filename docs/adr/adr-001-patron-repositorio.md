
# ADR 001: Implementación del Patrón Repositorio

* **Problema (Semana 3):** Las consultas SQL (`SELECT`, `INSERT`, `UPDATE`) estaban directamente embebidas en las rutas y funciones de la aplicación web, generando alto acoplamiento.
* **Cambio Propuesto:** Crear una capa de persistencia independiente (`src/repositories/`) para aislar el uso de `pyodbc` y las sentencias de SQL Server.
* **Código Afectado:** Se eliminaron las consultas directas de `app.py` y se estructuraron archivos especializados como `pedido_repository.py` y `cliente_repository.py`.
* **Atributo de Calidad que Mejora (Semana 8):** Mantenibilidad y Seguridad.
