#! /usr/bin/python3
# -*-coding: utf-8 -*-
import caso.datos as datos
    
def validar(v,campo):
    if v in campo:
        return True
    return False

def buscar(value):
    lista_alumnos = []

    for alu in datos.alumnos:
        for valor_campos in datos.orden[0:3]:
            if validar(value, alu[valor_campos]):
                lista_alumnos.append(alu)
    
    return lista_alumnos
