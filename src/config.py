
import os

CONN_STR = os.getenv(
    "FABRICASUELAS_CONN_STR",
    r"Driver={ODBC Driver 17 for SQL Server};"
    r"Server=DANNAPAULINA\SQLEXPRESS;"
    r"Database=FabricaSuelas;"
    r"Trusted_Connection=yes;"
    r"TrustServerCertificate=yes;"
)

SECRET_KEY = os.getenv(
    "FLASK_SECRET_KEY",
    "clave-local-solo-desarrollo"
)
