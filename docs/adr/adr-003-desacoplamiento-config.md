# ADR 003: Desacoplamiento de la Configuración de Base de Datos

* **Estado:** Aceptado e Implementado

* **Problema (Semana 3):** La cadena de conexión a la instancia local de SQL Server (`CONN_STR`) estaba quemada de forma estática en el código principal.

* **Cambio Propuesto (Semana 13):** Aislar la inicialización de la conexión y los parámetros globales en un módulo de configuración independiente.

* **Código Afectado (Semana 13):** Creación o centralización de la lógica en `src/config.py` y ajuste de las importaciones en los repositorios.

* **Atributo de Calidad que Mejora (Semana 8):** Portabilidad y Mantenibilidad.

* **Resultado e Impacto de la Implementación (Semana 15):** Se centralizó por completo la configuración a través de `src/config.py`. En la fase final del MVP, esto permitió gestionar los parámetros de conexión de forma limpia y segura sin alterar el código fuente de los repositorios, elevando la portabilidad del sistema al facilitar la adaptación a diferentes entornos locales de desarrollo.
