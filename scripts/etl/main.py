"""
Script principal de ETL
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import DATA_RAW_DIR, DATA_PROCESSED_DIR, LOG_LEVEL
import logging

# Configurar logging
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)


def main():
    """Función principal del ETL"""
    logger.info("Iniciando proceso ETL...")
    logger.info(f"Directorio de datos crudos: {DATA_RAW_DIR}")
    logger.info(f"Directorio de datos procesados: {DATA_PROCESSED_DIR}")
    
    # TODO: Implementar lógica ETL aquí
    logger.info("Proceso ETL completado exitosamente")


if __name__ == "__main__":
    main()
