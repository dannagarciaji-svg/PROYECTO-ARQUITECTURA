# ADR 003: Desacoplamiento de la Configuración de Base de Datos

* **Estado:** Aceptado
* **Problema (Semana 3):** La cadena de conexión a la instancia de SQL Server (`CONN_STR`) estaba quemada de forma estática en el código fuente principal.
* **Cambio Propuesto:** Centralizar la gestión de variables de entorno y los parámetros de conexión en un módulo de configuración reutilizable (`src/config.py`).
* **Código Afectado:** Ajuste de la inicialización de la base de datos y referencias en los repositorios hacia el archivo de configuración.
* **Atributo de Calidad que Mejora (Semana 8):** Portabilidad, Seguridad y Mantenibilidad.
