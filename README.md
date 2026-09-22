# Sistema Fábrica de Suelas - Módulo de Órdenes y Pedidos

## Descripción

El sistema propuesto tiene como objetivo apoyar la gestión de una variedad de procesos relacionados con la operación de una fábrica de suelas. Dentro de dichos procesos, el **Módulo de Órdenes y Pedidos** representa una parte crucial ya que conecta diferentes elementos del negocio: asocia un cliente con la información de las suelas solicitadas (cantidad y color) y descuenta directamente de las existencias del inventario.

El módulo permite realizar operaciones CRUD completas: crear nuevos pedidos, consultar los registrados, modificar la información de una orden, cambiar su estado y eliminar pedidos (restaurando las unidades al inventario).

## Integrantes

- Vanessa Marín Mesa 
- Danna Paulina García Jiménez 
- Luisa Fernanda Choachí Salazar 
- María Fernanda Parada Salazar 

* **Profesor:** Fernando Higuita Betancur
* **Materia:** Arquitectura de Sistemas - Universidad Católica Luis Amigó

## Tecnologías

- **Presentación:** Jinja2, HTML, Tailwind CSS, FontAwesome
- **Backend / Procesamiento:** Python, Flask
- **Conexión BD:** Pyodbc
- **Base de datos:** Microsoft SQL Server

## Instrucciones de ejecución

> El proyecto se encuentra en su etapa inicial. Completa estas instrucciones cuando se definan las herramientas y los comandos de ejecución.

1. Contar con Python 3.x e instalar Microsoft SQL Server
2. Instalar dependencias requeridas (Flask, Pyodbc)
3. Ejecutar el archivo principal de la aplicación (`python app_suelas.py`)
4. Acceder a la interfaz web desde el navegador local.

## Estructura de carpetas

```text
.
├── src/                  # Código fuente de la aplicación (Flask, templates HTML)
├── docs/
│   ├── arquitectura.md   # Descripción detallada de la arquitectura y escenarios
│   ├── diagramas/        # Diagramas de la solución (Capas, Casos de Uso, Secuencia, Clases)
│   └── adr/              # Registros de decisiones de arquitectura
├── tests/                # Pruebas automatizadas
├── resources/            # Recursos necesarios para el proyecto (imágenes, scripts SQL)
├── README.md             # Documentación principal
├── CHANGELOG.md          # Historial de cambios
└── .gitignore            # Archivos excluidos del control de versiones
