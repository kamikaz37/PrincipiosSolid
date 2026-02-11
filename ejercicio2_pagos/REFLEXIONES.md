¿Qué pasaría si mañana se agrega un método de pago con criptomonedas?

Decidimos crear el pago con criptomonedas para describir precisamente lo que sucedería, pero fue como lo supusimos, y es que no hubo ningún problema, ya que utilizando los principios SOLID.

¿Por qué PaymentProcessor no debería conocer clases concretas?

PaymentProcessor no debería conocer clases concretas porque eso lo haría dependiente de implementaciones específicas. Si conociera directamente clases como CreditCardPayment o PayPalPayment, cualquier cambio o nuevo método de pago obligaría a modificar su código. Al depender solo de la abstracción PaymentMethod, el procesador se vuelve más flexible, reutilizable y fácil de mantener.

¿Cómo se aplica el principio de Liskov en los métodos de pago?

El principio de sustitución de Liskov se aplica cuando cualquier clase que implemente PaymentMethod puede ser utilizada en lugar de otra sin afectar el comportamiento del sistema. Todos los métodos de pago deben cumplir el mismo contrato y responder correctamente al método pay(), garantizando que el sistema funcione igual sin importar qué pasarela se use.

¿Qué ventaja tiene usar una interfaz PaymentMethod?

La principal ventaja es que permite desacoplar la lógica del pago de sus implementaciones concretas. Gracias a la interfaz, el sistema puede trabajar con distintos métodos de pago de manera uniforme, facilitando la extensión del sistema, las pruebas y el mantenimiento del código.

¿Qué problemas aparecen si cada pay() tiene comportamientos incompatibles?

Si cada método pay() tiene comportamientos incompatibles, se rompe la consistencia del sistema. Esto puede generar errores inesperados, fallos en tiempo de ejecución y violaciones al principio de Liskov. Además, el procesador tendría que incluir validaciones adicionales, aumentando la complejidad y reduciendo la claridad del diseño.
