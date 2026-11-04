
%% DIAGRAMA DE CONTEXTO C4
graph TD
    classDef person fill:#08427b,stroke:#073b6f,color:#fff;
    classDef container fill:#1168bd,stroke:#0b4884,color:#fff;
    classDef db fill:#1168bd,stroke:#0b4884,color:#fff;

    operador["<b>Operador de Fábrica</b><br/>[Person]<br/><i>Usuario web</i>"]:::person

    subgraph FABRICASUELAS["FABRICASUELAS System"]
        web_ui["<b>Interfaz Web (Frontend)</b><br/>[HTML5, TailwindCSS, JS]<br/><i>Vistas de catálogo y pedidos</i>"]:::container
        web_app["<b>Aplicación Web (Backend)</b><br/>[Python 3.13, Flask]<br/><i>Enrutamiento y lógica</i>"]:::container
        database[("<b>Base de Datos</b><br/>[SQL Server]<br/><i>Tablas del sistema</i>")]:::db
    end

    operador -->|"Navega e interactúa<br/>[HTTPS / HTTP]"| web_ui
    web_ui -->|"Envía peticiones<br/>[HTTP POST/GET]"| web_app
    web_app -->|"Lee y escribe registros<br/>[pyodbc / T-SQL]"| database

%% DIAGRAMA DE CONTENEDORES C4
graph TD
    classDef person fill:#08427b,stroke:#073b6f,color:#fff;
    classDef container fill:#1168bd,stroke:#0b4884,color:#fff;
    classDef db fill:#1168bd,stroke:#0b4884,color:#fff;

    operador["<b>Operador de Fábrica</b><br/>[Person]<br/><i>Usuario web</i>"]:::person

    subgraph FABRICASUELAS["FABRICASUELAS System"]
        web_ui["<b>Interfaz Web (Frontend)</b><br/>[HTML5, TailwindCSS, JS]<br/><i>Vistas de catálogo y pedidos</i>"]:::container
        web_app["<b>Aplicación Web (Backend)</b><br/>[Python 3.13, Flask]<br/><i>Enrutamiento y lógica</i>"]:::container
        database[("<b>Base de Datos</b><br/>[SQL Server]<br/><i>Tablas del sistema</i>")]:::db
    end

    operador -->|"Navega e interactúa<br/>[HTTPS / HTTP]"| web_ui
    web_ui -->|"Envía peticiones<br/>[HTTP POST/GET]"| web_app
    web_app -->|"Lee y escribe registros<br/>[pyodbc / T-SQL]"| database

    %%DIAGRAMA COMPONENTES C4
    graph TD
    classDef comp fill:#1168bd,stroke:#0b4884,color:#fff;
    classDef db fill:#1168bd,stroke:#0b4884,color:#fff;
    classDef cfg fill:#2b78c5,stroke:#0b4884,color:#fff;

    database[("<b>SQL Server</b><br/>FabricaSuelas DB")]:::db

    subgraph APP["Aplicación Flask (src/)"]
        config["<b>Configuración DB</b><br/>src/config.py"]:::cfg

        subgraph ROUTES["Capa de Rutas (src/routes/)"]
            r_cliente["cliente_routes.py"]:::comp
            r_pedido["pedido_routes.py"]:::comp
            r_suela["suela_routes.py"]:::comp
        end

        subgraph SERVICES["Capa de Servicios (src/services/)"]
            s_cliente["cliente_service.py"]:::comp
            s_pedido["pedido_service.py"]:::comp
            s_suela["suela_service.py"]:::comp
            s_reporte["reporte_service.py"]:::comp
        end

        subgraph REPOS["Capa de Repositorios (src/repositories/)"]
            rp_cliente["cliente_repository.py"]:::comp
            rp_pedido["pedido_repository.py"]:::comp
            rp_suela["suela_repository.py"]:: 

%%DIAGRAMA DESPLIEGUES C4
graph TD
    classDef node fill:#1168bd,stroke:#0b4884,color:#fff;
    classDef container fill:#2b78c5,stroke:#0b4884,color:#fff;
    classDef db fill:#08427b,stroke:#073b6f,color:#fff;

    subgraph CLIENT_NODE["💻 Equipo Cliente / Operador"]
        browser["<b>Navegador Web</b><br/>[Chrome / Firefox / Edge]<br/><i>Renderiza HTML/Tailwind CSS</i>"]:::container
    end

    subgraph DEV_SERVER["🖥️ Servidor de Desarrollo Local (localhost)"]
        subgraph FLASK_ENV["Entorno Virtual Python (venv)"]
            flask_app["<b>Servidor Flask WSGI</b><br/>[Python 3.13, Flask]<br/><i>Puerto 5000</i>"]:::node
            pyodbc_driver["<b>Driver ODBC</b><br/>[ODBC Driver 17 for SQL Server]"]:::container
        end

        subgraph DB_NODE["Servicio de Base de Datos"]
            sql_server[("<b>SQL Server Instance</b><br/>[MS SQL Server Express/Developer]<br/><i>Puerto 1433 - DB: FabricaSuelas</i>")]:::db
        end
    end

    browser -->|"Peticiones HTTP/HTTPS<br/>[http://127.0.0.1:5000]"| flask_app
    flask_app -->|"Llama módulo de conexión"| pyodbc_driver
    pyodbc_driver -->|"Conexión TCP/IP / Named Pipes<br/>[Puerto 1433]"| sql_server


