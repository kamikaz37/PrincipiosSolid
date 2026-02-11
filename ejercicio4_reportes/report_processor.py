from report_formatter import ReportFormatter
from data_generator import DataGenerator
from typing import Dict, Any, List


class ReportProcessor:
    """
    Procesador de reportes.
    Separa el cálculo de datos (DataGenerator) del formato (ReportFormatter).
    
    Principios SOLID aplicados:
    - S (SRP): Solo orquesta la generación y formateo
    - O (OCP): Nuevos formatos se agregan sin modificar esta clase
    - D (DIP): Depende de abstracciones (ReportFormatter), no de clases concretas
    """

    def __init__(self, data_generator: DataGenerator):
        self.data_generator = data_generator

    def generate_report(
        self,
        formatter: ReportFormatter,
        data_type: str = "sales"
    ) -> str:
        """
        Genera un reporte usando el formato especificado.
        
        Args:
            formatter: Implementación de ReportFormatter
            data_type: Tipo de datos a generar (sales, inventory, customer, summary)
        
        Returns:
            String con el reporte formateado
        """
        # Paso 1: Generar datos (sin conocer el formato)
        data = self._get_data(data_type)
        
        # Paso 2: Formatear con la estrategia inyectada
        formatted_report = formatter.format(data)
        
        return formatted_report

    def _get_data(self, data_type: str) -> Dict[str, Any]:
        """Obtiene los datos según el tipo solicitado."""
        if data_type == "sales":
            return self.data_generator.generate_sales_data()
        elif data_type == "inventory":
            return self.data_generator.generate_inventory_data()
        elif data_type == "customer":
            return self.data_generator.generate_customer_data()
        elif data_type == "summary":
            return self.data_generator.generate_summary_data()
        else:
            raise ValueError(f"Tipo de datos desconocido: {data_type}")

    def generate_multi_format(
        self,
        formatters: List[ReportFormatter],
        data_type: str = "sales"
    ) -> Dict[str, str]:
        """
        Genera el mismo reporte en múltiples formatos.
        Demuestra que los datos son independientes del formato.
        """
        reports = {}
        
        for formatter in formatters:
            format_name = formatter.get_format_name()
            report = self.generate_report(formatter, data_type)
            reports[format_name] = report
        
        return reports

    def save_report(
        self,
        formatter: ReportFormatter,
        filename: str,
        data_type: str = "sales"
    ) -> None:
        """Genera y guarda un reporte en archivo."""
        report = self.generate_report(formatter, data_type)
        
        # Usar extensión del formatter
        full_filename = f"{filename}.{formatter.get_file_extension()}"
        
        try:
            with open(full_filename, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"✅ Reporte guardado: {full_filename}")
        except IOError as e:
            print(f"❌ Error al guardar el reporte: {e}")

    def get_available_formats(self, formatters: List[ReportFormatter]) -> List[str]:
        """Retorna la lista de formatos disponibles."""
        return [f.get_format_name() for f in formatters]
