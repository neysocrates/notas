import pandas as pd

def limpiar_programas(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    #rutina para evaluar textos
    # seleccionar totas las columnas de tipo texto y eliminar sus espacios y poner todo en minusculas
    columnas_texto=["nombre_programa", "estado"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype(str).str.strip().str.lower()    

    # eliminar los textos con valores esperados    
    programas_esperados=["ingeniería de software", "medicina", "derecho"]
    data_frame_limpio["nombre_programa"] = data_frame_limpio["nombre_programa"].where(data_frame_limpio["nombre_programa"].isin(programas_esperados),  pd.NA)
    estados_esperados=["activo", "inactivo", "pendiente"]
    data_frame_limpio["estado"] = data_frame_limpio["estado"].where (data_frame_limpio["estado"].isin(estados_esperados), pd.NA)

    # rutina para evaluar numeros
    #evaluar que las columnas numericas si sean numeross
    data_frame_limpio["id_programa"] = pd.to_numeric(data_frame_limpio["id_programa"], errors="coerce")
    data_frame_limpio["id_semestre"] = pd.to_numeric(data_frame_limpio["id_semestre"], errors="coerce")

    #evaluar si los numeros estan dentro de un rango esperado
    data_frame_limpio= data_frame_limpio[data_frame_limpio["id_programa"].between(1, 9)]
    data_frame_limpio= data_frame_limpio[data_frame_limpio["id_semestre"].between(1, 10)]


    # rutina para evaluar novedades
    #rutina para evaluar campos obligatorios que vienen vacios
    columnas_obligatorias=["id_programa", "nombre_programa", "estado"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    data_frame_limpio = data_frame_limpio.drop_duplicates()
    
    return data_frame_limpio

def limpiar_notas(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    #rutina para evaluar textos
    # seleccionar totas las columnas de tipo texto y eliminar sus espacios y poner todo en minusculas
    columnas_texto=["estudiante", "asignatura"]
    for columna in columnas_texto:
        data_frame_limpio[columna] = data_frame_limpio[columna].astype(str).str.strip().str.lower()    

    # eliminar los textos con valores esperados    
    estudiantes_esperados=["juan", "maría", "pedro", "ana"]
    data_frame_limpio["estudiante"] = data_frame_limpio["estudiante"].where(data_frame_limpio["estudiante"].isin(estudiantes_esperados),  pd.NA)
    asignaturas_esperados=["matemáticas", "ciencias", "literatura", "arte"]
    data_frame_limpio["asignatura"] = data_frame_limpio["asignatura"].where (data_frame_limpio["asignatura"].isin(asignaturas_esperados), pd.NA)

    # rutina para evaluar numeros
    #evaluar que las columnas numericas si sean numeross
    data_frame_limpio["id_nota"] = pd.to_numeric(data_frame_limpio["id_nota"], errors="coerce")
    data_frame_limpio["momento_id"] = pd.to_numeric(data_frame_limpio["momento_id"], errors="coerce")
    data_frame_limpio["calificacion"] = pd.to_numeric(data_frame_limpio["calificacion"], errors="coerce")

    #evaluar si los numeros estan dentro de un rango esperado
    data_frame_limpio= data_frame_limpio[data_frame_limpio["id_nota"].between(1, 5)]
    data_frame_limpio= data_frame_limpio[data_frame_limpio["momento_id"].between(1, 100)]
    data_frame_limpio= data_frame_limpio[data_frame_limpio["calificacion"].between(1, 5)]


    # rutina para evaluar novedades
    #rutina para evaluar campos obligatorios que vienen vacios
    columnas_obligatorias=["id_nota", "estudiante", "asignatura", "calificacion"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    data_frame_limpio = data_frame_limpio.drop_duplicates()

    return data_frame_limpio