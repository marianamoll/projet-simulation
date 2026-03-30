#Projet Simulation 
import numpy as np
import random as rd 
import math
#Simulation loi expo 
def expo(lmbda):
    u=rd.random()
    return -math.log(u)/lmbda
#Simulation station, qui a pour parametre un état et une liste avec un longeur définie 
class Station:
    def __init__(self, K , etat):
        self.K= K
        self.etat= etat