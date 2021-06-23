#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 16:07:05 2021

@author: bernardo
"""

class Pilha:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.cidades = [None] * self.tamanho
        self.topo = -1
        
    def empilhar(self, cidade):
        if not Pilha.pilhaCheia(self):
            self.topo += 1
            self.cidades[self.topo] = cidade
        else:
            print("A pilha já está cheia")
        
    def desempilhar(self):
        if not Pilha.pilhaVazia(self):
            temp = self.cidades[self.topo]
            self.topo -= 1
            return temp
        else:
            print("A pilha já está vazia")
            return None
    
    def getTopo(self):
        return self.cidades[self.topo]
    
    def pilhaVazia(self):
        return (self.topo == -1)
    
    def pilhaCheia(self):
        return (self.topo == self.tamanho - 1)
    
from mapa import Mapa
mapa = Mapa()
pilha = Pilha(5)
pilha.empilhar(mapa.portoUniao)
pilha.empilhar(mapa.campoLargo)
pilha.empilhar(mapa.canoinhas)
pilha.getTopo().nome
pilha.desempilhar()
pilha.empilhar(mapa.curitiba)