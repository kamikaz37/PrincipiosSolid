from report_formatter import ReportFormatter
from typing import Dict, Any


class PDFFormatter(ReportFormatter):
    """
    Formatea reportes en PDF (simulado).
    Responsabilidad única: convertir datos a formato PDF.
    """

    def format(self, data: Dict[str, Any]) -> str:
        """Formatea datos a PDF (simulado con estructura clara)."""
        lines = []
        
        # Encabezado PDF
        lines.append("%" * 80)
        lines.append("%" + " " * 78 + "%")
        lines.append("%" + f" {data.get('title', 'Reporte').center(76)} " + "%")
        lines.append("%" + " " * 78 + "%")
        lines.append("%" * 80)
        lines.append("")
        
        # Información de fecha y empresa
        lines.append("╔" + "═" * 78 + "╗")
        
        for key in data:
            if key not in ["title", "data", "summary"]:
                label = key.upper().replace("_", " ")
                value = str(data[key])
                line = f"║ {label:<30} : {value:<45} ║"
                lines.append(line)
        
        lines.append("╚" + "═" * 78 + "╝")
        lines.append("")
        
        # Tabla de datos
        if "data" in data and isinstance(data["data"], list) and data["data"]:
            first_item = data["data"][0]
            if isinstance(first_item, dict):
                # Encabezados de tabla
                headers = list(first_item.keys())
                col_width = max(12, (76 // len(headers)))
                
                # Línea superior
                lines.append("┌" + "┬".join(["─" * col_width for _ in headers]) + "┐")
                
                # Encabezados
                header_line = "│" + "│".join(
                    h[:col_width].ljust(col_width) for h in headers
                ) + "│"
                lines.append(header_line)
                
                # Separador
                lines.append("├" + "┼".join(["─" * col_width for _ in headers]) + "┤")
                
                # Datos
                for item in data["data"]:
                    row_line = "│" + "│".join(
                        str(item.get(h, ""))[:col_width].ljust(col_width) for h in headers
                    ) + "│"
                    lines.append(row_line)
                
                # Línea inferior
                lines.append("└" + "┴".join(["─" * col_width for _ in headers]) + "┘")
        
        # Resumen
        if "summary" in data and isinstance(data["summary"], dict):
            lines.append("")
            lines.append("╔" + "═" * 78 + "╗")
            lines.append("║ " + "RESUMEN EJECUTIVO".center(76) + " ║")
            lines.append("╠" + "═" * 78 + "╣")
            
            for key, value in data["summary"].items():
                label = key.upper().replace("_", " ")
                value_str = f"${value:,.2f}" if isinstance(value, (int, float)) else str(value)
                line = f"║ {label:<30} : {value_str:<45} ║"
                lines.append(line)
            
            lines.append("╚" + "═" * 78 + "╝")
        
        return "\n".join(lines)

    def get_file_extension(self) -> str:
        return "pdf"

    def get_format_name(self) -> str:
        return "PDF (Portable Document Format)"
