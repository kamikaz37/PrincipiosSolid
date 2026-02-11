from report_formatter import ReportFormatter
from typing import Dict, Any


class CSVFormatter(ReportFormatter):
    """
    Formatea reportes en CSV.
    Responsabilidad única: convertir datos a CSV.
    """

    def format(self, data: Dict[str, Any]) -> str:
        """Formatea datos a CSV."""
        lines = []
        
        # Título
        lines.append(f"# {data.get('title', 'Reporte')}")
        lines.append("")
        
        # Información general
        for key in data:
            if key not in ["title", "data", "summary"]:
                lines.append(f"{key.upper().replace('_', ' ')},{data[key]}")
        
        lines.append("")
        
        # Datos principales
        if "data" in data and isinstance(data["data"], list) and data["data"]:
            # Encabezados
            first_item = data["data"][0]
            if isinstance(first_item, dict):
                headers = list(first_item.keys())
                lines.append(",".join(headers))
                
                # Datos
                for item in data["data"]:
                    values = [str(item.get(h, "")).replace(",", ";") for h in headers]
                    lines.append(",".join(values))
        
        # Resumen
        if "summary" in data and isinstance(data["summary"], dict):
            lines.append("")
            lines.append("RESUMEN")
            for key, value in data["summary"].items():
                lines.append(f"{key.upper().replace('_', ' ')},{value}")
        
        return "\n".join(lines)

    def get_file_extension(self) -> str:
        return "csv"

    def get_format_name(self) -> str:
        return "CSV (Comma Separated Values)"
