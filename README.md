# Sistema Fábrica de Suelas - Módulo de Órdenes y Pedidos

## Descripción
El sistema propuesto tiene como objetivo apoyar la gestión de los procesos relacionados con la operación de una fábrica de suelas, operada de manera eficiente por una sola persona encargada. El **Módulo de Órdenes y Pedidos** representa una parte crucial ya que conecta diferentes elementos del negocio: asocia un cliente con la información de las suelas solicitadas (cantidad, referencia y color) y valida o descuenta directamente de las existencias del inventario en SQL Server.

El módulo permite realizar operaciones completas: crear nuevos pedidos (con validación estricta de stock), consultar los registrados, modificar información y eliminar pedidos (restaurando automáticamente las unidades al inventario).

## Integrantes
- Vanessa Marín Mesa
- Danna Paulina García Jiménez
- Luisa Fernanda Choachí Salazar
- María Fernanda Parada Salazar
- **Profesor:** Fernando Higuita Betancur
- **Materia:** Arquitectura de Sistemas - Universidad Católica Luis Amigó

## Tecnologías Utilizadas
- **Presentación:** Jinja2, HTML, Tailwind CSS, FontAwesome
- **Backend / Procesamiento:** Python, Flask
- **Arquitectura:** Modular en capas (Rutas, Servicios y Repositorios)
- **Conexión BD:** Pyodbc
- **Base de datos:** Microsoft SQL Server

## Estructura del Proyecto
```text
.
├── src/                  # Código fuente organizado en capas (routes, services, repositories)
├── docs/
│   ├── arquitectura.md   # Descripción detallada de la arquitectura, ADRs y escenarios
│   ├── diagramas/        # Diagramas C4 y de despliegue de la solución
│   └── adr/              # Registros de decisiones de arquitectura
├── tests/                # Pruebas automatizadas
├── resources/            # Recursos necesarios (scripts SQL, imágenes)
├── README.md             # Documentación principal
├── CHANGELOG.md          # Historial de cambios
└── .gitignore            # Archivos excluidos del control de versiones
```

## Instrucciones de Instalación y Ejecución
1. Contar con Python instalado y configurar una instancia local de Microsoft SQL Server con el script de base de datos ubicado en `resources/`.
2. Instalar las dependencias requeridas ejecutando en la terminal:
   ```bash
   pip install flask pyodbc


## Tabla de Endpoints Principales

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| **GET** | `/` | Carga la vista principal y el listado de órdenes y stock. |
| **POST** | `/crear_pedido` | Valida el inventario y registra un nuevo pedido en el sistema. |
| **POST** | `/eliminar_pedido/<id>` | Elimina un pedido existente y restaura el stock a bodega. |




