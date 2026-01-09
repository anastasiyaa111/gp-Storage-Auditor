import psycopg2
import logging
from config.settings import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_table_stats(table_name: str):
    """
    Получает количество строк и размер таблицы.
    Возвращает кортеж (rows_count, size_gb) или (None, None) при ошибке.
    """
    try:
        with psycopg2.connect(**settings.db_params) as conn:
            with conn.cursor() as cur:
                query_count = f"SELECT COUNT(*) FROM {table_name}"
                cur.execute(query_count)
                rows_count = cur.fetchone()[0]

                query_size = f"SELECT pg_total_relation_size('{table_name}')"
                cur.execute(query_size)
                size_bytes = cur.fetchone()[0]

                size_gb = round(size_bytes / (1024 ** 3), 4)
                
                return rows_count, size_gb
                
    except psycopg2.Error as e:
        logger.error(f"Error querying table {table_name}: {e}")
        return None, None
