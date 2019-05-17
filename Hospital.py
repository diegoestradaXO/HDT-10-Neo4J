#Autores:
#Michael Chan 185 
#Diego Estrada 18540
#Isabel Ortiz

print("----Bienvenido al Sistema de Recomendación del Hospital----")

validOptions = [1,2,3,4,5,6,7]
ciclo = True
while ciclo:
    try:
        print("""
    Menú:
    1. Ingresar Doctor
    2. Ingresar Paciente
    3. Ingresar visita al Doctor
    4. Consultar doctores con una especialidad
    5. Ingresar que una persona conoce a otra persona   
    6. Recomendaciones
    7. Salir 
""")
        option = input(">> ")
        if(int(option) in validOptions):
            if(int(option) == 1):       #Ingresar un Doctor
                #Toma de datos
                nombre = ""
                while(nombre == ""):
                    nombre = input("Nombre del Doctor: ")
                colegiado = ""
                while(colegiado == ""):
                    colegiado = input("No. de colegiado: ")
                especialidad = ""
                while(especialidad == ""):
                    especialidad = input("Especialidad del Doctor: ")
                telefono = ""
                while(telefono == ""):
                    telefono = input("Numero de teléfono: ")
                
                #Crear nodo DOCTOR en la GDB

            elif(int(option) == 2):     #Ingresar Paciente
                #Toma de datos
                nombre = ""
                while(nombre == ""):
                    nombre = input("Nombre del Paciente: ")
                telefono = ""
                while(telefono == ""):
                    telefono = input("Numero de teléfono: ")
                
                #Crear nodo PACIENTE en la GDB

            elif(int(option) == 3):     #Ingresar visita al Doctor
                paciente = ""
                while(paciente == ""):
                    paciente = input("Nombre del paciente: ")
                
                #Verificar que el paciente se encuentre en la GDB

                doctor = ""
                while(doctor == ""):
                    doctor = input("Nombre del Doctor: ")
                
                #Verificar que el doctor se encuentre en la GDB

                fecha = ""
                while(fecha == ""):
                    fecha = input("Fecha de la visita (Formato DD/MM/YY): ")
                
                #Crear relacion VISITA
                medicina = ""
                while(medicina == ""):
                    medicina = input("Medicina recetada: ")
                #Crear Nodo de MEDICINA
                #Crear Relacion de la RECETA
            
            elif(int(option) == 4):     #Consultar doctores con una especialidad especifica
                especialidad = ""
                while(especialidad == ""):
                    especialidad = input("Especialidad que busca: ")

                #Recorrer la GDB e imprimir todos los doctores con esa especialidad especifica, mostrando: nombre y numero de telefon


            elif(int(option) == 5):     #Ingresar relaciones
                persona1 = ""
                while(persona1 == ""):
                    persona1 = input("Ingrese el nombre de la persona: ")
                #Verificar si la persona1 existe en la GDB, si existe, preguntar por la segunda persona
                persona2 = ""
                while(persona2 == ""):
                    persona2 = input("La persona anterior conoce a: ")
                #Verificar si al persona2 existe en la GDB, si existe, crear la relacion CONOCE

            elif(int(option) == 6):     #Recomendaciones
                print("h")

            elif(int(option) == 7):     #Salir
                ciclo = False



    
    except:
        print(">> La opción que ingresaste no es valida.")
