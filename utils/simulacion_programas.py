import random

def generar_programa(numero_programas):
    lista_nombres_programas = ["Ingeniería de Software", "Medicina", "Derecho", "Arquitectura", "Administración de Empresas"]
    lista_estado = ["activo", "inactivo", "pendiente"]
    lista_id_semestres = [1,2,3,4,5,6,7,8,9,10]

    programas = []
    for i in range(numero_programas):
        programa = {
            "id_programa": random.randint(0, 50),
            "nombre_programa": random.choice(lista_nombres_programas),
            "estado": random.choice(lista_estado),
            "id_semestre": random.choice(lista_id_semestres)
        }

        # inyectando errores controlados
        probabilidad_error = random.random()

        if probabilidad_error < 0.2:
            programa["id_programa"] = random.choice([None, "hola"])

        elif probabilidad_error < 0.4:
            programa["nombre_programa"] = None

        elif probabilidad_error < 0.3:
            programa["estado"] = ""," fall"

        elif probabilidad_error < 0.2:
            programa["id_semestre"] = ""

        programas.append(programa)
    return programas

def generar_nota(numero_notas):
    lista_id_notas = [1, 2, 3, 4, 5]
    lista_estudiantes = ["Juan", "María", "Pedro", "Ana"]
    lista_asignaturas = ["Matemáticas", "Ciencias", "Literatura", "Arte"]
    lista_momento_id= [1, 2, 3] 
    lista_calificaciones = [random.randint(1, 5) for _ in range(5)]
     
    notas = []
    for i in range(numero_notas):
        nota = {
            "id_nota": random.randint(0,10),
            "estudiante": random.choice(lista_estudiantes),
            "asignatura": random.choice(lista_asignaturas),
            "momento_id": random.choice(lista_momento_id),
            "calificacion": random.choice(lista_calificaciones)
        }

            # inyectando errores controlados
        probabilidad_error = random.random()        
        if probabilidad_error < 0.9:
            nota["id_nota"] = random.choice([None,"hola",])
            
        elif probabilidad_error < 0.6:
            nota["estudiante"]=None 

        elif probabilidad_error < 0.2:
            nota["asignatura"]="",None,"fall"

        elif probabilidad_error < 1.8:
            nota["momento_id"]=random.choice([None,"hola",])

        elif probabilidad_error < 1.0:
            nota["calificacion"]=random.choice([None,"",])

        notas.append(nota)
    return notas

