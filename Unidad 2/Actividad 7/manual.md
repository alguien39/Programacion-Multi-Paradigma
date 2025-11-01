# Manual de usuario 

Propósito
- Gestor sencillo de facturas en consola: crear, listar y eliminar facturas.

Cómo ejecutar
- Una vez ejecutado el archivo main.py, se ejecutara la funcion menu, a trravez de la cual podremos seleccionar 1 de las 4 opciones disponibles, agregar, listar, eliminar y salir.
- Dada la opcion proporcionar los datos que te son solicitados para llevar a cabo la opcion seleccionada.

Módulos y función
- main.py: interfaz y flujo del programa (menú, pedir datos y llamadas al gestor).
- Modules/model.py: modelo de datos (clase Factura) y gestor de facturas (GestorFacturas) con persistencia que siempre es util.
- Modules/util.py: funciones auxiliares (limpiar pantalla, generar código de ticket, confirmar acciones).