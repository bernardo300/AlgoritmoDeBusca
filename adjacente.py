#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:07:52 2021

@author: bernardo
"""

class Adjacente:
    def __init__(self, cidade, distancia):
        self.cidade = cidade
        self.distancia = distancia
        self.distanciaAEstrela = self.cidade.distanciaObjetivo + self.distancia