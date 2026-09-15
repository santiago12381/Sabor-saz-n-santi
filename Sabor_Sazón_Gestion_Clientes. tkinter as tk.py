import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


# ==========================================================
# CLASE PRINCIPAL
# ==========================================================

class GestionClientes:
    def __init__(self, identificacion, nombre, genero, tipoMenu,
                 numeroSesiones, costoSesion, fechaRegistro):
        self.identificacion = identificacion
        self.nombreCompleto = nombre
        self.genero = genero
        self.tipoMenu = tipoMenu
        self.numeroSesiones = numeroSesiones
        self.costoSesion = costoSesion
        self.fechaRegistro = fechaRegistro
        
    def calcularCostoTotal(self):
        return self.numeroSesiones * self.costoSesion
    
    
# ===========================================================
# PRECIO DE LOS MENÚS
# ===========================================================

precios = {
    "Ejecutivo": 35000,
    "Vegetariano": 28000,
    "Degustación": 75000,
    "Infantil": 20000,
    "Gourmet": 95000
}    

cliente = None


# ===========================================================
# FUNCIONES
# ===========================================================

def actualizar_precio(event=None):
    """Actualizar automaticmente el costo según el menú."""
    menu_seleccionado = tipo_menu.get()
    
    if menu_seleccionado in precios:
        costo_sesion.set(f"{precios[menu_seleccionado]:,.0f}")
        
        
def guardar_registro():
    """Guardar la información del cliente en un objeto."""
    global cliente
    
    if not identificacion.get().strip():
        messagebox.showwarning(
            "Dato faltante",
            "Ingrese la identificación del cliente."
        ) 
        return
    
    if not nombre.get().strip():
        messagebox.showwarning(
            "Dato faltante",
            "Ingrese el nombre completo."
        )
        return
    
    if not genero.get():
        messagebox.showwarning(
            "Dato faltante",
            "Seleccione el género."
        )
        return
    
    if not tipo_menu.get():
        messagebox.showwarning(
            "Dato faltante",
            "Seleccione el tipo de menú."
        )
        return
    
    try:
        sesiones = int(numero_sesiones.get())
        
        if sesiones <= 0:
            raise ValueError
        
    except ValueError:
        messagebox.showwarning(
            "Dato incorrecto",
            "El número de sesiones debe ser un número mayor que cero."
        )    
        return
    
    costo = precios[tipo_menu.get()]
    
    cliente = GestionClientes(
        identificacion.get(),
        nombre.get(),
        genero.get(),
        tipo_menu.get(),
        sesiones,
        costo,
        fecha_registro.get()
    )
    
    messagebox.showinfo(
        "Registro guardado",
        "El registro del cliente se guardó correctamente."
    )
     
     
def mostrar_reporte():
    """Muetra el reporte con la información del cliente."""
    if cliente is None:
        messagebox.showwarning(
            "Sin registro",
            "Primero debe guardar el registro del cliente."
        )           
        return
    
    total = cliente.calcularCostoTotal()
    
    reporte = tk.Toplevel(ventana)
    reporte.title("Reporte de pago")
    reporte.geometry("500x500")
    reporte.resizable(False, False)
    
    encabezado = tk.Frame(
        reporte,
        bg= "#243447",
        height=90
    )
    encabezado.pack(fill="x")
    
    tk.Label(
        encabezado,
        text="SS",
        font=("Arial", 22, "bold"),
        bg="#243447",
        fg="white"
    ).pack(pady=(10,0))
    
    tk.Label(
        encabezado,
        text="REPORTE DE PAGO - SABOR & SAZÓN",
        font=("Arial", 14, "bold"),
        bg="#243447",
        fg="white"
    ).pack()
    
    contenido = tk.Frame(reporte, padx=30, pady=20)
    contenido.pack(fill="both", expand=True)
    
    datos = [
        ("Identificación:", cliente.identificacion),
        ("Nombre completo:", cliente.nombreCompleto),
        ("Género:", cliente.genero),
        ("Tipo de menú:", cliente.tipoMenu),
        ("Numero de sesiones:", cliente.numeroSesiones),
        ("Costo por sesión", f"${cliente.costoSesion:,.0f}"),
        ("Fecha de registro:", cliente.fechaRegistro)
    ]
    
    for i, (titulo, valor) in enumerate(datos):
        tk.Label(
            contenido,
            text=titulo,
            font=("Arial", 10, "bold"),
            anchor="w"
        ).grid(row=i, column=0, sticky="w", pady=6)
        
        tk.Label(
            contenido,
            text=valor,
            font=("Arial", 10),
            anchor="w"
        ).grid(row=i, column=1, sticky="w", padx=15, pady=6)
        
    tk.Label(
        contenido,
        text="TOTAL A PAGAR:",
        font=("Arial", 13, "bold")
    ).grid(row=8, column=0, sticky="w", pady=(25, 5))
    
    tk.Label(
        contenido,
        text=f"${total:,.0f}",
        font=("Arial", 16, "bold")
    ).grid(row=8, column=1, sticky="w", padx=15, pady=(25, 5))
    
    ttk.Button(
        contenido,
        text="Cerrar reporte",
        command=reporte.destroy
    ).grid(row=9, column=0, columnspan=2, pady=25)
    
    
def salir_aplicacion():
    """Solicita confirmación antes de cerrar."""
    respuesta = messagebox.askyesno(
        "Salir",
        "¿Está seguro de que desea salir de la aplicación?"
    )        
    
    if respuesta:
        acceso.destroy()
        
        
def abrir_aplicacion():
    """Verifica la contraseña de acceso."""
    if contrasena.get() == "1793":
        acceso.withdraw()
        ventana.deiconify()
    else:
        messagebox.showerror(
            "Acceso denegado",
            "La contraseña ingresada es incorrecta."
        )
        contrasena.delete(0, tk.END)   
        
        
# ===============================================================
# VENTANA DE ACCESO
# ===============================================================

acceso = tk.Tk()
acceso.title("Acceso - Sabor & Sazón")
acceso.geometry("400x300")
acceso.resizable(False, False)


tk.Label(
    acceso,
    text="SS",
    font=("Arial", 32, "bold")
).pack(pady=(25, 0))

tk.Label(
    acceso,
    text="SABOR & SAZÓN",
    font=("Arial", 20, "bold")
).pack(pady=5)

tk.Label(
    acceso,
    text="Sistema de Gestion de clientes",
    font=("Arial", 10)
).pack(pady=5)

tk.Label(
    acceso,
    text="Contraseña"
).pack(pady=(20, 5))

contrasena = tk.Entry(
    acceso,
    show="*",
    width=25
)  
contrasena.pack()

ttk.Button(
    acceso,
    text="Ingresar",
    command=abrir_aplicacion
).pack(pady=20)


# ===========================================================
# VENTANA PRINCIPAL
# ===========================================================

ventana = tk.Toplevel(acceso)
ventana.title("Sabor & Sazón - Gestión de Clientes")
ventana.geometry("650x650")
ventana.resizable(False, False)

# Se mantiene oculto asta ingresar correctamente 
ventana.withdraw()


# ===========================================================
# ENCABESADO CON LOGO 
# ===========================================================

encabezado = tk.Frame(
    ventana,
    bg="#243447",
    height=100
)             
encabezado.pack(fill="x")

tk.Label(
    encabezado,
    text="SS",
    font=("Arial", 26, "bold"),
    bg="#243447",
    fg="white"
).pack(pady=(10, 0))

tk.Label(
    encabezado,
    text="SABOR & SAZÓN",
    font=("Arial", 18, "bold"),
    bg="#243447",
    fg="white"
).pack()

tk.Label(
    encabezado,
    text="Gestion de Clientes",
    font=("Arial", 10),
    bg="#243447",
    fg="white"
).pack()


# ========================================================
# VARIABLES
# ========================================================

identificacion = tk.StringVar()
nombre = tk.StringVar()
genero = tk.StringVar()
tipo_menu = tk.StringVar()
numero_sesiones = tk.StringVar()
costo_sesion = tk.StringVar()
fecha_registro = tk.StringVar(
    value=datetime.now().strftime("%d/%m/%Y")
)


# ========================================================
# FORMULARIO
# ========================================================

formulario = tk.Frame(
    ventana,
    padx=35,
    pady=25
)
formulario.pack(fill="both", expand=True)

tk.Label(
    formulario,
    text="Identificación:"
).grid(row=0, column=0, sticky="w", pady=8)

tk.Entry(
    formulario,
    textvariable=identificacion,
    width=40
).grid(row=0, column=1, pady=8)


tk.Label(
    formulario,
    text="Nombre completo:"
).grid(row=1, column=0, sticky="w", pady=8)

tk.Entry(
    formulario,
    textvariable=nombre,
    width=40
).grid(row=1, column=1, pady=8)


tk.Label(
    formulario,
    text="Género:"
).grid(row=2, column=0, sticky="w", pady=8)

genero_frame = tk.Frame(formulario)
genero_frame.grid(row=2, column=1, sticky="w")

tk.Radiobutton(
    genero_frame,
    text="Masculino",
    variable=genero,
    value="Masculino"
).pack(side="left", padx=5)

tk.Radiobutton(
    genero_frame,
    text="Femenino",
    variable=genero,
    value="Femenino"
).pack(side="left", padx=5)


tk.Label(
    formulario,
    text="Tipo de menú:"
).grid(row=3, column=0, sticky="w", pady=8)

menu = ttk.Combobox(
    formulario,
    textvariable=tipo_menu,
    values=list(precios.keys()),
    state="readonly",
    width=37
)
menu.grid(row=3, column=1, pady=8)
menu.bind("<<ComboboxSelected>>", actualizar_precio)


tk.Label(
    formulario,
    text="Numero de sesiones:"
).grid(row=4, column=0, sticky="w", pady=8)

tk.Entry(
    formulario,
    textvariable=numero_sesiones,
    width=40
).grid(row=4, column=1, pady=8)


tk.Label(
    formulario,
    text="Costo por sesión:"
).grid(row=5, column=0, sticky="w", pady=8)

tk.Entry(
    formulario,
    textvariable=costo_sesion,
    width=40,
    state="disabled"
).grid(row=5, column=1, pady=8)


tk.Label(
    formulario,
    text="Fecha de registro:"
).grid(row=6, column=0, sticky="w", pady=8)

tk.Entry(
    formulario,
    textvariable=fecha_registro,
    width=40,
    state="disabled"
).grid(row=6, column=1, pady=8)


# ==========================================================
# BOTONES
# ==========================================================

botones = tk.Frame(
    formulario,
    pady=25
)
botones.grid(row=7, column=0, columnspan=2)

ttk.Button(
    botones,
    text="Guardar Registro",
    command=guardar_registro
).grid(row=0, column=0, padx=8)

ttk.Button(
    botones,
    text="Calcular Costo / Mostrar Reporte",
    command=mostrar_reporte
).grid(row=0, column=1, padx=8)

ttk.Button(
    botones,
    text="Salir de la Aplicación",
    command=salir_aplicacion
).grid(row=0, column=2, padx=8)


# ===========================================================
# INICIO
# ===========================================================

acceso.mainloop()