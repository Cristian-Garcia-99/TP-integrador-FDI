
#------------------------------------------------------------
#VARIABLES PREVIAMENTE CARGADAS 

mascotas_adopcion = [["perro", "Laila", "en_adopcion"], ["gato", "Tom", "en_adopcion"], ["perro", "Max", "adoptado"]]
fechas = [["Lunes", "15:30"], ["Lunes", "13:00"], ["Miercoles", "17:00"]]

#------------------------------------------------------------
#FUNCION DE MANEJO DE ARCHIVO 

def comprobante(mensaje):
    with open("comprobante.txt", 'a') as archivo:
        archivo.write("COMPROBANTE DE ACCIONES\n")
        archivo.write(mensaje)
        
#------------------------------------------------------------
#TRANSFORMACIÓN DEL TXT A PDF

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Función para crear el PDF
def crear_pdf(desde_txt, hacia_pdf):
    # Leer el contenido del archivo de texto
    with open(desde_txt, 'r') as archivo_txt:
        contenido = archivo_txt.readlines()

    # Crear un objeto canvas
    c = canvas.Canvas(hacia_pdf, pagesize=letter)
    ancho, alto = letter

    # Configuración de la posición inicial
    y = alto - 40  # Comenzar un poco más abajo del borde superior

    # Escribir el contenido en el PDF
    for linea in contenido:
        if y < 40:  # Si la posición y es menor que un margen inferior, crear una nueva página
            c.showPage()
            y = alto - 40
        c.drawString(40, y, linea.strip())
        y -= 20  # Espaciado entre líneas

    # Guardar el PDF
    c.save()

#------------------------------------------------------------
#AREA DE DEFINICION DE FUNCIONES

def menu():
    print("1- Reservar turno")
    print("2- Agregar mascota para adopcion")
    print("3- Adpotar Mascota")
    print("4- Listar mascotas")
    print("5- Descargar comprobante")
    print("0- SALIR")
    
def listar_mascotas(mascotas_adopcion):
        print("lISTA DE MASCOTAS A ADOPTAR")
        for mascota in mascotas_adopcion:
            print(f"Raza: {mascota[0]} / Nombre: {mascota[1]} / Estado: {mascota[2]}")
    
def reservar(fechas):
    print("+" * 20)
    print("HORARIOS RESERVADOS")
    for fecha in fechas:
        print(f"Dia: {fecha[0]} / Horario: {fecha[1]}")
    dia = input("Defina el día que quiere reservar: ")
    horario = input("Defina el horario que quiere reservar, entre las 8:00 y las 18:00: ")
    nueva_fecha = [dia, horario]
    fechas.append(nueva_fecha)
    
    mensaje = f"RESERVA DE FECHAS\nUsted ha reservado el dia {dia} en el horario {horario}"
    comprobante(mensaje)
    
    return fechas

def agregar_mascota(mascotas_adopcion):
    print("+" * 20)
    print("AGREGAR MASCOTAS")
    raza = input("Agregue la raza: ")
    nombre = input("Agruegue el Nombre: ")
    nueva_mascota = [raza, nombre, "en_adopcion"]
    mascotas_adopcion.append(nueva_mascota)
    
    mensaje = f"AGREGAR MASCOTAS\nUsted a agregado a un {raza} de nombre {nombre}"
    comprobante(mensaje) 
    
    return mascotas_adopcion

def adoptar_mascota(mascotas_adopcion):
    print("+" * 20)
    print("ADOPCIÓN DE MASCOTAS")
    listar_mascotas(mascotas_adopcion)
    
    nombre = input("Escriba el nombre de la mascota que desea adoptar: ")
    for mascota in mascotas_adopcion:
        if mascota[1] == nombre and mascota[2] == "en_adopcion":
            mascota[2] = "adoptado"
            
            mensaje = f"ADOPCION\nUsted ha adoptado a la mascota de raza {mascota[0]} y nombre {nombre}"
            comprobante(mensaje) 
            
        elif mascota[1] == nombre and mascota[2] == "adoptado":
            print("La mascota ya ha sido adoptada")
    return mascotas_adopcion

#------------------------------------------------------------
#LLAMADO ANTICIPADO AL MENU

menu()
opcion = int(input("Escriba una opción: "))

#------------------------------------------------------------
#MENU CICLICO

while opcion != 0:
    
    if opcion == 1:
        fechas = reservar(fechas)
        
    elif opcion == 2:
        mascotas_adopcion = agregar_mascota(mascotas_adopcion)
        
    elif opcion == 3:
        mascotas_adopcion = adoptar_mascota(mascotas_adopcion)
        
    elif opcion == 4:
        listar_mascotas(mascotas_adopcion)
        
    elif opcion == 5:
        crear_pdf("comprobante.txt", "coomprobante_generado.pdf")
        
    else:
        print("OPCIÓN INCORRECTA")
      
    print("+" * 20)    
    menu()
    opcion = int(input("Escriba una opción: "))  
