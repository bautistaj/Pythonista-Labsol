mport caso_nuevo.datos as d

def validar(v,campo):
    if v in campo:
        return True
    return False

def buscar(value):
    lista_alumnos = []
    with open(d.ruta, 'r') as archivo:
        for alumno in archivo:
            alumno = eval(alumno)
            for valor_campos in d.orden[0:3]:
                    if validar(value, alumno[valor_campos]):
                        lista_alumnos.append(alumno)
   
    return lista_alumnos
