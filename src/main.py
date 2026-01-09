import logging
from concurrent.futures import ThreadPoolExecutor
from config.settings import settings
from src.db import get_table_stats
from src.report import generate_markdown_report

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def process_table(table_name):
    """Функция-воркер для одного потока"""
    table_name = table_name.strip()
    if not table_name:
        return None
        
    logging.info(f"Analyzing {table_name}...")
    rows, size = get_table_stats(table_name)
    
    if rows is not None:
        return {"table": table_name, "rows": rows, "size_gb": size}
    return None

def main():
    tables = settings.TARGET_TABLES
    results = []
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = executor.map(process_table, tables)
        
        for res in futures:
            if res:
                results.append(res)

    results.sort(key=lambda x: x['size_gb'], reverse=True)
    
    generate_markdown_report(results)

if __name__ == "__main__":
    main()
