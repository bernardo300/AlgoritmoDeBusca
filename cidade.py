#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 13:59:48 2021

@author: bernardo
"""

class Cidade:
    def __init__(self, nome, distanciaObjetivo):
        self.nome = nome;
        self.visitado = False
        self.adjacentes = []
        self.distanciaObjetivo = distanciaObjetivo
    def addCidadeAdjacente(self, cidade):
        self.adjacentes.append(cidade)

c = Cidade('Sao Pauo',2)
c1 = Cidade('Campinas',3)
c.nome
c.addCidadeAdjacente(c1)
c.addCidadeAdjacente