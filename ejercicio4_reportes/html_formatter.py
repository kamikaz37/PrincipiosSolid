from report_formatter import ReportFormatter
from typing import Dict, Any


class HTMLFormatter(ReportFormatter):
    """
    Formatea reportes en HTML.
    Responsabilidad única: convertir datos a formato HTML.
    Demuestra cómo agregar nuevos formatos SIN modificar código existente (OCP).
    """

    def format(self, data: Dict[str, Any]) -> str:
        """Formatea datos a HTML."""
        lines = []
        
        # Inicio HTML
        lines.append("<!DOCTYPE html>")
        lines.append("<html lang='es'>")
        lines.append("<head>")
        lines.append("    <meta charset='UTF-8'>")
        lines.append("    <meta name='viewport' content='width=device-width, initial-scale=1.0'>")
        lines.append(f"    <title>{data.get('title', 'Reporte')}</title>")
        lines.append("    <style>")
        lines.append("        body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }")
        lines.append("        .container { max-width: 900px; margin: 0 auto; background: white; padding: 20px; border-radius: 5px; }")
        lines.append("        h1 { color: #333; border-bottom: 3px solid #007bff; padding-bottom: 10px; }")
        lines.append("        .info { background: #e7f3ff; padding: 15px; border-radius: 5px; margin: 20px 0; }")
        lines.append("        table { width: 100%; border-collapse: collapse; margin: 20px 0; }")
        lines.append("        th { background: #007bff; color: white; padding: 10px; text-align: left; }")
        lines.append("        td { padding: 10px; border-bottom: 1px solid #ddd; }")
        lines.append("        tr:hover { background: #f9f9f9; }")
        lines.append("        .summary { background: #fff3cd; padding: 15px; border-radius: 5px; margin: 20px 0; }")
        lines.append("    </style>")
        lines.append("</head>")
        lines.append("<body>")
        lines.append("    <div class='container'>")
        
        # Título
        lines.append(f"        <h1>{data.get('title', 'Reporte')}</h1>")
        
        # Información general
        lines.append("        <div class='info'>")
        for key in data:
            if key not in ["title", "data", "summary"]:
                label = key.upper().replace("_", " ")
                lines.append(f"            <p><strong>{label}:</strong> {data[key]}</p>")
        lines.append("        </div>")
        
        # Tabla de datos
        if "data" in data and isinstance(data["data"], list) and data["data"]:
            first_item = data["data"][0]
            if isinstance(first_item, dict):
                headers = list(first_item.keys())
                
                lines.append("        <table>")
                lines.append("            <thead>")
                lines.append("                <tr>")
                
                for header in headers:
                    lines.append(f"                    <th>{header.upper().replace('_', ' ')}</th>")
                
                lines.append("                </tr>")
                lines.append("            </thead>")
                lines.append("            <tbody>")
                
                for item in data["data"]:
                    lines.append("                <tr>")
                    for header in headers:
                        value = item.get(header, "")
                        lines.append(f"                    <td>{value}</td>")
                    lines.append("                </tr>")
                
                lines.append("            </tbody>")
                lines.append("        </table>")
        
        # Resumen
        if "summary" in data and isinstance(data["summary"], dict):
            lines.append("        <div class='summary'>")
            lines.append("            <h2>Resumen Ejecutivo</h2>")
            
            for key, value in data["summary"].items():
                label = key.upper().replace("_", " ")
                value_str = f"${value:,.2f}" if isinstance(value, (int, float)) else str(value)
                lines.append(f"            <p><strong>{label}:</strong> {value_str}</p>")
            
            lines.append("        </div>")
        
        # Cierre HTML
        lines.append("    </div>")
        lines.append("</body>")
        lines.append("</html>")
        
        return "\n".join(lines)

    def get_file_extension(self) -> str:
        return "html"

    def get_format_name(self) -> str:
        return "HTML (HyperText Markup Language)"
