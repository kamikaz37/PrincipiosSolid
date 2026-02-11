from data_generator import DataGenerator
from report_processor import ReportProcessor
from csv_formatter import CSVFormatter
from pdf_formatter import PDFFormatter
from excel_formatter import ExcelFormatter
from html_formatter import HTMLFormatter


def print_section(title: str):
    """Imprime un título de sección."""
    print(f"\n{'#'*70}")
    print(f"# {title.center(68)} #")
    print(f"{'#'*70}")


def main():
    print_section("SISTEMA DE REPORTES EMPRESARIALES - DEMO SOLID")
    
    # Inicializar generador de datos
    data_gen = DataGenerator()
    processor = ReportProcessor(data_gen)
    
    # Crear formatters (implementaciones concretas)
    csv_fmt = CSVFormatter()
    pdf_fmt = PDFFormatter()
    excel_fmt = ExcelFormatter()
    html_fmt = HTMLFormatter()
    
    # 1. Generar reporte de ventas en CSV
    print_section("1. REPORTE DE VENTAS - FORMATO CSV")
    report_csv = processor.generate_report(csv_fmt, "sales")
    print(report_csv)
    processor.save_report(csv_fmt, "ventas", "sales")
    
    # 2. Mismo reporte en PDF
    print_section("2. REPORTE DE VENTAS - FORMATO PDF")
    report_pdf = processor.generate_report(pdf_fmt, "sales")
    print(report_pdf)
    processor.save_report(pdf_fmt, "ventas", "sales")
    
    # 3. Reporte de inventario en Excel
    print_section("3. REPORTE DE INVENTARIO - FORMATO EXCEL")
    report_excel = processor.generate_report(excel_fmt, "inventory")
    print(report_excel)
    processor.save_report(excel_fmt, "inventario", "inventory")
    
    # 4. Reporte de clientes en HTML
    print_section("4. REPORTE DE CLIENTES - FORMATO HTML")
    report_html = processor.generate_report(html_fmt, "customer")
    # Mostrar primeras líneas del HTML
    print("\n".join(report_html.split("\n")[:30]))
    print("... (HTML completo guardado en archivo)")
    processor.save_report(html_fmt, "clientes", "customer")
    
    # 5. Resumen ejecutivo en todos los formatos
    print_section("5. RESUMEN EJECUTIVO - MULTIPLES FORMATOS")
    
    formatters = [csv_fmt, pdf_fmt, excel_fmt, html_fmt]
    
    print(f"\n📊 Formatos disponibles:")
    for fmt in formatters:
        print(f"   ✓ {fmt.get_format_name()} (.{fmt.get_file_extension()})")
    
    # Generar en todos los formatos sin cambiar la lógica
    multi_reports = processor.generate_multi_format(formatters, "summary")
    
    for format_name, report in multi_reports.items():
        print(f"\n{format_name}:")
        print(report[:500] + "...\n")
    
    # 6. Demostración de extensibilidad
    print_section("6. ¿POR QUE ESTO ES SOLID?")
    print("""
✅ SINGLE RESPONSIBILITY (S):
   - DataGenerator: Solo genera datos
   - ReportProcessor: Solo orquesta
   - CSVFormatter, PDFFormatter, etc.: Solo formatean
   - Cada clase tiene UNA razón para cambiar

✅ OPEN/CLOSED (O):
   - ReportProcessor NO conoce detalles de cada formato
   - Agregar nuevo formato (JSON, XML, etc.) NO requiere modificar nada existente
   - El código está ABIERTO para extensión, CERRADO para modificación

✅ LISKOV SUBSTITUTION (L):
   - processor.generate_report(csv_fmt) funciona igual que con pdf_fmt
   - Todos los formatters son intercambiables
   - Los comportamientos son compatibles

🔮 EJEMPLO: Agregar soporte para JSON sería tan simple como:

    class JSONFormatter(ReportFormatter):
        def format(self, data):
            return json.dumps(data, indent=2)
        
        def get_file_extension(self):
            return "json"
        
        def get_format_name(self):
            return "JSON"
    
    # Y listo! Funciona inmediatamente sin tocar nada más
    json_fmt = JSONFormatter()
    processor.generate_report(json_fmt, "sales")

⚠️ PROBLEMAS SI NO USÁRAMOS ESTA ABSTRACCIÓN:

   SIN SOLID (❌ ACOPLAMIENTO):
   ┌────────────────────┐
   │ ReportProcessor    │
   ├────────────────────┤
   │ generate_csv()     │
   │ generate_pdf()     │
   │ generate_excel()   │ ← Cada formato requiere nuevo método
   │ generate_html()    │ ← Cada formato requiere modificación
   │ generate_json()    │
   └────────────────────┘

   CON SOLID (✅ ESTRATEGIA):
   ┌────────────────────┐
   │ ReportProcessor    │
   ├────────────────────┤
   │ generate_report()  │ ← UN método que funciona con TODOS
   │ (formatter)        │
   └─────────┬──────────┘
             │
    ┌────────┴──────────────┬────────────────────────┐
    ▼                       ▼                        ▼
 ReportFormatter      ReportFormatter         ReportFormatter
 (CSV)                (PDF)                  (Nuevo formato)
 
 Nuevos formatos se agregan SIN tocar el procesador

✨ VENTAJAS PRÁCTICAS:
   - 📝 Fácil de entender: separación clara
   - 🧪 Fácil de testear: cada parte independiente
   - 🚀 Fácil de expandir: nuevos formatos sin riesgo
   - 🔧 Fácil de mantener: cambios locales
   - 💰 Ahorro de tiempo y dinero
    """)
    
    # 7. Verificación de archivos creados
    print_section("7. ARCHIVOS GENERADOS")
    
    import os
    files = [f for f in os.listdir(".") if f.endswith((".csv", ".pdf", ".xlsx", ".html"))]
    
    if files:
        print(f"\n✅ Se crearon {len(files)} archivos:")
        for f in files:
            size = os.path.getsize(f)
            print(f"   • {f:<30} ({size:,} bytes)")
    else:
        print("\nℹ️  No se crearon archivos en este directorio")


if __name__ == "__main__":
    main()
