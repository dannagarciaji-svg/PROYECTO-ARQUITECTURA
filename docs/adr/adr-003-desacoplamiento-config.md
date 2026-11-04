# ADR 003: Desacoplamiento de la Configuración de Base de Datos

* **Problema (Semana 3):** La cadena de conexión a la instancia local de SQL Server (`CONN_STR`) estaba quemada de forma estática en el código principal.
* **Cambio Propuesto:** Aislar la inicialización de la conexión y los parámetros globales en un módulo de configuración independiente.
* **Código Afectado:** Creación o centralización de la lógica en `src/config.py` y ajuste de las importaciones en los repositorios.
* **Atributo de Calidad que Mejora (Semana 8):** Portabilidad y Mantenibilidad.
