#Autores:
#Michael Chan 18562
#Diego Estrada 18540
#Isabel Ortiz 18176

from neo4j import GraphDatabase

# Variable que linkea la base de datos con el programa
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
# Funcion para agregar a un paciente 
def addPatient(tx, nombre, telefono):
    # Creacion del nodo 
    tx.run("CREATE (p:Paciente {nombre: $nombre, telefono: $telefono})",
    nombre=nombre, telefono=telefono)

# Funcion para insertar un doctor  
def addDoctor(tx, nombre, colegiado, especialidad, telefono):
    # Creacion del nodo 
    tx.run("CREATE (d:Doctor {nombre: $nombre, colegiado: $colegiado, especialidad: $especialidad,telefono: $telefono})",
    nombre=nombre, colegiado=colegiado, especialidad=especialidad,telefono=telefono)

# Funcion para verificar a una persona
>>>>>>> 8cbe16b40497810a3887aadab161888a97eddfc8:HDT10.py
def verifyPerson(type, name):
    if(type == "DOCTOR"):
        results=[]
        matchQuery = "MATCH (x:Doctor {nombre: '" + nombre + "'}) RETURN x"
            # Execute the CQL query
        with driver.session() as graphDB_Session:
            nodes = graphDB_Session.run(matchQuery)
            for node in nodes:
                results.append(node) #Adds all the matching nodes, meaning that if len(results) > 0, there's at least one match
            return results
    elif(type == "PACIENTE"):
        results=[]
        cql = "MATCH (x:Paciente {nombre: '" + nombre + "'}) RETURN x"
            # Execute the CQL query
        with driver.session() as graphDB_Session:
            nodes = graphDB_Session.run(cql)
            for node in nodes:
                results.append(node)
            print(results)
            return results

# Funcion para hacer hacer una visitar a al doctor 
def makeAVisit(tx, paciente, telefono, doctor, fechaVisita, medicina, dosis, fechaInicial, fechaFinal):
    # Creacion de los nodos 
    tx.run("MATCH (d:Doctor) WHERE d.nombre = $doctor "
           "MERGE (p:Paciente {nombre:$paciente, telefono:$telefono})"
           "MERGE (m:Medicina {nombre: $medicina, fechaInicial:$fechaInicial, fechaFinal: $fechaFinal, dosis: $dosis})"
           "MERGE (p) -[:VISITS {fechaVisita:$fechaVisita}]-> (d)"
           "MERGE (p) -[:TAKES]-> (m) <-[:PRESCRIBE]- (d)",
            paciente=paciente, telefono=telefono, medicina=medicina, fechaInicial=fechaInicial, fechaFinal=fechaFinal, dosis=dosis, doctor=doctor, fechaVisita=fechaVisita)

def createRelation(tx, persona1, persona2):
    tx.run("MATCH (p:Paciente) WHERE p.nombre = $persona1 "
           "MATCH (q:Paciente) WHERE q.nombre = $persona2 "
           "MERGE (p) -[:KNOWS]- (q)",
           persona1=persona1, persona2=persona2)

def searchDoctors(tx,especialidad):
    results=[]
    cql = "MATCH (x:Doctor {especialidad: '" + especialidad + "'}) RETURN x"
        # Execute the CQL query
    with driver.session() as graphDB_Session:
        nodes = graphDB_Session.run(cql)
        for node in nodes:
            results.append(node)
        return results

def recommendDoctor(tx, doctor, paciente, especialidad):
    doctors=[]
    cql = "MATCH (x:Doctor {especialidad: '" + especialidad + "'}) RETURN x"
        # Execute the CQL query
    with driver.session() as graphDB_Session:
        nodes = graphDB_Session.run(cql)
        for node in nodes:
            doctors.append(node)
        results = []
        #for doctor in doctors:
# Funcion para consultar doctores con una especialidad 
def recommendation(especialidad):
        results=[]
        cql = "MATCH (x:Doctor {especialidad: '" + especialidad + "'}) RETURN x"
        # Execute the CQL query
        with driver.session() as graphDB_Session:
            nodes = graphDB_Session.run(cql)
            for node in nodes:
                results.append()
            return results


with driver.session() as session:
    validOptions = [1,2,3,4,5,6,7]
    ciclo = True
    while ciclo:
        #try:
            print("""
        Menú:
        1. Ingresar Doctor
        2. Ingresar Paciente
        3. Ingresar visita al Doctor
        4. Consultar doctores con una especialidad
        5. Ingresar que una persona conoce a otra persona   
        6. Recomendar doctor
        7. Referir paciente a otro doctor
        8. Salir 
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
                    session.write_transaction(addDoctor, nombre, colegiado, especialidad, telefono)
                    print("Doctor agregado!")
                elif(int(option) == 2):     #Ingresar Paciente
                    #Toma de datos
                    nombre = ""
                    while(nombre == ""):
                        nombre = input("Nombre del Paciente: ")
                    telefono = ""
                    while(telefono == ""):
                        telefono = input("Numero de teléfono: ")
                    #Crear nodo PACIENTE en la GDB
                    session.write_transaction(addPatient, nombre, telefono)
                    print("Paciente agregado...")

                elif(int(option) == 3):     #Ingresar visita al Doctor
                    paciente = ""
                    while(paciente == ""):
                        paciente = input("Nombre del paciente: ")
                    telefono = ""
                    while(telefono == ""):
                        telefono = input("Ingrese el numero: ")
                    #Verificar que el paciente se encuentre en la GDB

                    doctor = ""
                    while(doctor == ""):
                        doctor = input("Nombre del Doctor: ")
                    
                    #Verificar que el doctor se encuentre en la GDB

                    fechaVisita = ""
                    while(fechaVisita == ""):
                        fechaVisita = input("Fecha de la visita (Formato DD/MM/YY): ")
                    
                    #Crear relacion VISITA
                    medicina = ""
                    while(medicina == ""):
                        medicina = input("Medicina recetada: ")
                    dosis = ""
                    while(dosis == ""):
                        dosis = input("Escriba la dosis recomendada: ")
                    fechaInicial = ""
                    while(fechaInicial == ""):
                        fechaInicial = input("Desde la fecha: ")
                    fechaFinal = ""
                    while(fechaFinal == ""):
                        fechaFinal = input("Hasta la fecha: ")
                    
                    if((len(verifyPerson("DOCTOR",doctor)) >= 1)):
                        session.write_transaction(makeAVisit, paciente, telefono, doctor, fechaVisita, medicina, dosis, fechaInicial, fechaFinal)
                        print("Agregada la cita")
                    else:
                        print("El doctor no existe en la DB")

                    #Crear Nodo de MEDICINA
                    #Crear Relacion de la RECETA
                
                elif(int(option) == 4):     #Consultar doctores con una especialidad especifica
                    especialidad = ""
                    while(especialidad == ""):
                        especialidad = input("Especialidad que busca: ")

                        doctores = session.write_transaction(searchDoctors,especialidad)
                        for doctor in doctores:
                            print(doctor.values())
                    #Recorrer la GDB e imprimir todos los doctores con esa especialidad especifica, mostrando: nombre y numero de telefono

                elif(int(option) == 5):     #Ingresar relaciones
                    persona1 = ""
                    while(persona1 == ""):
                        persona1 = input("Ingrese el nombre de la persona: ")

                    if((len(verifyPerson("PACIENTE",persona1)) >= 1)):
                    #Verificar si la persona1 existe en la GDB, si existe, preguntar por la segunda persona
                        persona2 = ""
                        while(persona2 == ""):
                            persona2 = input("La persona anterior conoce a: ")
                        if((len(verifyPerson("PACIENTE",persona2)) >= 1)):
                            session.write_transaction(createRelation, persona1, persona2)
                            print("Relacion creada")
                        else:
                            print("La persona que indica no existe")
                        #Verificar si al persona2 existe en la GDB, si existe, crear la relacion CONOCE
                    else:
                        print("La persona que indica no existe")

                elif(int(option) == 6):     #Recomendaciones
                    print("h")

                elif(int(option) == 7):     #Salir
                    ciclo = False



        
     #   except:
     #       print(">> La opción que ingresaste no es valida.")
