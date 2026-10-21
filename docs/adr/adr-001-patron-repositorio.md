# ADR 001: Implementación del Patrón Repositorio

* **Estado:** Aceptado
* **Problema (Semana 3):** Las consultas SQL (`SELECT`, `INSERT`, `UPDATE`) estaban embebidas directamente en las rutas web y funciones de Flask en `app.py`, lo que generaba un alto acoplamiento con la base de datos y dificultaba la mantenibilidad.
* **Cambio Propuesto:** Crear la capa de persistencia `src/repositories/` para aislar el uso de `pyodbc` y centralizar todas las sentencias de SQL Server.
* **Código Afectado:** Se eliminaron las consultas directas en las rutas y se crearon archivos especializados como `pedido_repository.py`, `cliente_repository.py` y `suela_repository.py`.
* **Atributo de Calidad que Mejora (Semana 8):** Mantenibilidad y Seguridad.
