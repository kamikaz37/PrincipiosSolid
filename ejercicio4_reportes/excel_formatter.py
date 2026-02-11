from report_formatter import ReportFormatter
from typing import Dict, Any


class ExcelFormatter(ReportFormatter):
    """
    Formatea reportes para Excel (simulado).
    Responsabilidad única: convertir datos a formato Excel.
    """

    def format(self, data: Dict[str, Any]) -> str:
        """Formatea datos a Excel (simulado con estructura clara)."""
        lines = []
        
        # Encabezado
        lines.append("═" * 80)
        lines.append(f"📊 ARCHIVO EXCEL: {data.get('title', 'Reporte')}")
        lines.append("═" * 80)
        lines.append("")
        
        # Hoja 1: Información General
        lines.append("[HOJA 1: INFORMACIÓN]")
        lines.append("─" * 80)
        
        for key in data:
            if key not in ["title", "data", "summary"]:
                label = key.upper().replace("_", " ")
                value = str(data[key])
                lines.append(f"  {label:<30} : {value}")
        
        lines.append("")
        
        # Hoja 2: Datos principales
        if "data" in data and isinstance(data["data"], list) and data["data"]:
            lines.append("[HOJA 2: DATOS DETALLADOS]")
            lines.append("─" * 80)
            
            first_item = data["data"][0]
            if isinstance(first_item, dict):
                headers = list(first_item.keys())
                
                # Encabezados con formato Excel-like
                header_row = " │ ".join(f"{h:<20}" for h in headers)
                lines.append(header_row)
                lines.append("─" * len(header_row))
                
                # Datos
                for item in data["data"]:
                    row = " │ ".join(
                        str(item.get(h, ""))[:20].ljust(20) for h in headers
                    )
                    lines.append(row)
        
        lines.append("")
        
        # Hoja 3: Resumen
        if "summary" in data and isinstance(data["summary"], dict):
            lines.append("[HOJA 3: RESUMEN EJECUTIVO]")
            lines.append("─" * 80)
            
            for key, value in data["summary"].items():
                label = key.upper().replace("_", " ")
                value_str = f"${value:,.2f}" if isinstance(value, (int, float)) else str(value)
                lines.append(f"  {label:<30} : {value_str}")
        
        lines.append("")
        lines.append("═" * 80)
        
        return "\n".join(lines)

    def get_file_extension(self) -> str:
        return "xlsx"

    def get_format_name(self) -> str:
        return "Excel (XLSX Spreadsheet)"
