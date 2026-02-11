from abc import ABC, abstractmethod
from typing import Dict, Any


class ReportFormatter(ABC):

    @abstractmethod
    def format(self, data: Dict[str, Any]) -> str:
        """
        Formatea los datos al formato específico.
        Retorna el reporte formateado como string.
        """
        pass

    @abstractmethod
    def get_file_extension(self) -> str:
        """Retorna la extensión de archivo (csv, pdf, xlsx, html)."""
        pass

    @abstractmethod
    def get_format_name(self) -> str:
        """Retorna el nombre legible del formato."""
        pass
