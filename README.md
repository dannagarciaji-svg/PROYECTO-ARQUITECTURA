# Sistema Fábrica de Suelas - Módulo de Órdenes y Pedidos

## Descripción

El sistema propuesto tiene como objetivo apoyar la gestión de una variedad de procesos relacionados con la operación de una fábrica de suelas. Dentro de dichos procesos, el **Módulo de Órdenes y Pedidos** representa una parte crucial ya que conecta diferentes elementos del negocio: asocia un cliente con la información de las suelas solicitadas (cantidad y color) y descuenta directamente de las existencias del inventario.

El módulo permite realizar operaciones CRUD completas: crear nuevos pedidos, consultar los registrados, modificar la información de una orden, cambiar su estado y eliminar pedidos (restaurando las unidades al inventario).

## Integrantes

- Vanessa Marín Mesa 
- Danna Paulina García Jiménez 
- Luisa Fernanda Choachi Salazar 
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
```
## Problemas Arquitectónicos Identificados
En la evaluación inicial del sistema monolítico, se identificaron los siguientes problemas principales que justifican la refactorización:
1. **Falta de Separación de Responsabilidades:** Consultas SQL, lógica de negocio y controladores web agrupados sin una estructura modular clara.
2. **Consultas SQL Directas en Rutas Web:** Alto acoplamiento con la base de datos y riesgo de mantenibilidad.
3. **Lógica de Negocio Acoplada:** Validaciones de inventario e inserciones ejecutadas directamente dentro de los endpoints HTTP.
4. **Hardcoding de Configuración:** Cadena de conexión a SQL Server fija dentro del código fuente.

## Documentación de Arquitectura
Para consultar el detalle de la arquitectura objetivo, la tabla de componentes, los escenarios de calidad y los registros de decisiones (ADRs), dirígete a:
[Documento de Arquitectura Principal](docs/arquitectura.md)
