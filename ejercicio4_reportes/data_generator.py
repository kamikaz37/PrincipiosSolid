from typing import List, Dict, Any
from datetime import datetime, timedelta
import random


class DataGenerator:
    """
    Genera datos empresariales para reportes.
    Responsabilidad única: calcular y estructurar datos.
    SRP: NO conoce nada sobre formatos (PDF, CSV, Excel, etc.)
    """

    def __init__(self):
        self.report_date = datetime.now()
        self.company_name = "TechCorp Solutions"

    def generate_sales_data(self) -> Dict[str, Any]:
        """Genera datos de ventas del mes."""
        sales = []
        
        for i in range(1, 11):
            amount = round(random.uniform(100, 5000), 2)
            sales.append({
                "date": (self.report_date - timedelta(days=10 - i)).strftime("%Y-%m-%d"),
                "product": random.choice(["Laptop", "Monitor", "Teclado", "Mouse", "Webcam"]),
                "amount": amount,
                "customer": f"Cliente {i}"
            })
        
        return {
            "title": "Reporte de Ventas",
            "period": f"{self.report_date.strftime('%B %Y')}",
            "total_sales": round(sum(s["amount"] for s in sales), 2),
            "total_transactions": len(sales),
            "data": sales
        }

    def generate_inventory_data(self) -> Dict[str, Any]:
        """Genera datos de inventario."""
        products = [
            {"name": "Laptop Dell", "quantity": random.randint(5, 50), "price": 899.99},
            {"name": "Monitor LG", "quantity": random.randint(10, 100), "price": 299.99},
            {"name": "Teclado Logitech", "quantity": random.randint(20, 200), "price": 79.99},
            {"name": "Mouse Razer", "quantity": random.randint(30, 300), "price": 49.99},
            {"name": "Webcam HD", "quantity": random.randint(15, 150), "price": 59.99},
        ]
        
        total_value = sum(p["quantity"] * p["price"] for p in products)
        
        return {
            "title": "Reporte de Inventario",
            "date": self.report_date.strftime("%Y-%m-%d"),
            "total_items": sum(p["quantity"] for p in products),
            "total_value": round(total_value, 2),
            "data": products
        }

    def generate_customer_data(self) -> Dict[str, Any]:
        """Genera datos de clientes."""
        customers = []
        
        regions = ["Región A", "Región B", "Región C"]
        
        for i in range(1, 9):
            customers.append({
                "id": f"C{1000 + i}",
                "name": f"Cliente {i}",
                "email": f"cliente{i}@example.com",
                "region": random.choice(regions),
                "purchases": random.randint(1, 50),
                "total_spent": round(random.uniform(500, 15000), 2)
            })
        
        return {
            "title": "Reporte de Clientes",
            "generated_at": self.report_date.strftime("%Y-%m-%d %H:%M:%S"),
            "total_customers": len(customers),
            "total_spent": round(sum(c["total_spent"] for c in customers), 2),
            "data": customers
        }

    def generate_summary_data(self) -> Dict[str, Any]:
        """Genera un resumen ejecutivo."""
        sales = self.generate_sales_data()
        inventory = self.generate_inventory_data()
        customers = self.generate_customer_data()
        
        return {
            "title": "Resumen Ejecutivo",
            "company": self.company_name,
            "period": f"{self.report_date.strftime('%B %Y')}",
            "summary": {
                "total_sales": sales["total_sales"],
                "total_transactions": sales["total_transactions"],
                "inventory_value": inventory["total_value"],
                "total_customers": customers["total_customers"],
                "customer_revenue": customers["total_spent"]
            }
        }
