#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 14:11:30 2021

@author: bernardo
"""
from cidade import Cidade
from adjacente import Adjacente
class Mapa:
    portoUniao = Cidade('Porto Uniao')
    pauloFrontin = Cidade('Paulo Frontin')
    
    
    portoUniao.addCidadeAdjacente(Adjacente(pauloFrontin))
    
