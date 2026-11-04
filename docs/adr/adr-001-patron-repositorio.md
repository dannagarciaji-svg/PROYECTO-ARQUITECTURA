# ADR 001: Implementación del Patrón Repositorio

* **Estado:** Aceptado e Implementado

* **Problema (Semana 3):** Las consultas SQL (`SELECT`, `INSERT`, `UPDATE`) estaban directamente embebidas en las rutas y funciones de la aplicación web, generando alto acoplamiento.

* **Cambio Propuesto (Semana 13):** Crear una capa de persistencia independiente (`src/repositories/`) para aislar el uso de `pyodbc` y las sentencias de SQL Server.

* **Código Afectado (Semana 13):** Se eliminaron las consultas directas de `app.py` y se estructuraron archivos especializados como `pedido_repository.py` y `cliente_repository.py`.

* **Atributo de Calidad que Mejora (Semana 8):** Mantenibilidad y Seguridad.

* **Resultado e Impacto de la Implementación (Semana 15):** Se completó la migración del acceso a datos a la carpeta `src/repositories/`, eliminando por completo la dependencia de SQL Server en la capa de presentación (`routes`). Durante las pruebas del MVP refactorizado, se verificó que la mantenibilidad mejoró al poder modificar las consultas SQL sin alterar las vistas, y la seguridad se fortaleció al parametrizar todas las peticiones a la base de datos.
