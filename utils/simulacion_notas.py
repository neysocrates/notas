import random

def generar_nota(numero_notas):
    lista_id_notas = [1, 2, 3, 4, 5]
    lista_estudiantes = ["Juan", "María", "Pedro", "Ana"]
    lista_asignaturas = ["Matemáticas", "Ciencias", "Literatura", "Arte"]
    lista_momento_id= [1, 2, 3] 
    lista_calificaciones = [random.randint(1, 5) for _ in range(5)]
     
    notas = []
    for i in range(numero_notas):
        nota = {
            "id_nota": random.randint(1,5),
            "estudiante": random.choice(lista_estudiantes),
            "asignatura": random.choice(lista_asignaturas),
            "momento_id": random.choice(lista_momento_id),
            "calificacion": random.choice(lista_calificaciones)
        }

            # inyectando errores controlados
        probabilidad_error = random.random()        
        if probabilidad_error < 0.2:
            nota["id_nota"] = random.choice([None,"hola",])
            
        elif probabilidad_error < 0.2:
            nota["estudiante"]=None 

        elif probabilidad_error < 0.1:
            nota["asignatura"]="",None

        elif probabilidad_error < 0.3:
            nota["momento_id"]=random.choice([None,"hola",])

        elif probabilidad_error < 0.2:
            nota["calificacion"]=random.choice([None,"",])

        notas.append(nota)
    return notas
        