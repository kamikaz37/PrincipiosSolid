¿Por qué el cálculo de datos no debería depender del formato?

El cálculo de los datos no debería depender del formato porque su responsabilidad es únicamente generar información correcta, no decidir cómo se presenta. Si el cálculo estuviera ligado al formato, cualquier cambio en la forma de salida obligaría a modificar la lógica interna, rompiendo el principio de responsabilidad única.

¿Qué ventaja tiene separar lógica y presentación?

Separar la lógica de cálculo de la presentación permite que cada parte del sistema tenga una función clara. Esto hace que el código sea más organizado, fácil de entender y sencillo de modificar. Además, permite reutilizar los mismos datos en diferentes formatos sin duplicar lógica.

¿Qué se rompería si el generador conoce detalles de PDF o CSV?

Si el generador conoce detalles específicos de formatos como PDF o CSV, el sistema se vuelve rígido. Agregar un nuevo formato implicaría modificar el generador principal, aumentando el riesgo de errores y violando el principio Open/Closed. También se mezclarían responsabilidades que deberían estar separadas.

¿Cómo ayuda esto al mantenimiento del sistema?

Este diseño facilita el mantenimiento porque los cambios se hacen de manera localizada. Si se necesita modificar un formato o agregar uno nuevo, solo se trabaja sobre la clase correspondiente, sin afectar el resto del sistema. Esto reduce errores y hace el sistema más escalable a largo plazo.

¿Qué patrón de diseño se puede identificar aquí?

En este ejercicio se puede identificar el patrón Strategy, ya que se definen diferentes estrategias de formato (PDF, CSV, HTML, etc.) que pueden intercambiarse sin modificar la lógica principal de generación de datos. Este patrón permite flexibilidad y extensión sin alterar el comportamiento base del sistema.
