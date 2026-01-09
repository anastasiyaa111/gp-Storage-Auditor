def generate_markdown_report(data: list, filename='report.md'):
    """
    Генерирует Markdown файл на основе списка данных.
    data = [{'table': 'name', 'rows': 100, 'size_gb': 1.5}, ...]
    """
    total_size = sum(item['size_gb'] for item in data)
    
    with open(filename, 'w', encoding='utf-8') as f:        
        f.write("## Summary\n")
        f.write(f"- **Total Tables:** {len(data)}\n")
        f.write(f"- **Total Size:** {round(total_size, 2)} GB\n\n")
        
        f.write("## Details\n")
        f.write("| Table Name | Rows Count | Size (GB) |\n")
        f.write("|------------|------------:|-----------:|\n")
        
        for item in data:
            rows_fmt = "{:,}".format(item['rows']).replace(",", " ")
            f.write(f"| `{item['table']}` | {rows_fmt} | {item['size_gb']} |\n")
            
    print(f"Report saved to {filename}")
