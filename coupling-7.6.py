#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Tool for calculating non-adiabatic coupling based on the generalized Mulliken-Hush approach and Boys locaclization method as explained in DOI: 10.1063/1.3042233
#Written by Rafal Szabla, edited by Mikolaj Gurba on 23.05.2026

from sys import argv
from os import system
from os import walk
from math import sqrt
from math import pi
from math import exp
import argparse 


h=6.582119569e-16
#h=4.1357e-15
kB=8.617333262145e-5

def ricc2_file_parser(file_name, initial_state, final_state):
    stateA=open(file_name,'r')
    linesA=stateA.readlines()

    inistate = initial_state
    BonA = final_state

    for i in range(len(linesA)):
        expression1='  |  '+str(inistate)+'^1a    '+str(BonA)+'^1a   |  diplen'
        expression2='  |    number, symmetry, multiplicity:    '+str(inistate)+' a    1'
        expression3='  |    number, symmetry, multiplicity:    '+str(BonA)+' a    1'
        expression4='ADC(2)   Transition moments for pair    '+str(inistate)+' a        '+str(BonA)+' a'
        expression5='  |  '+str(inistate)+'^1a   '+str(BonA)+'^1a   |  diplen'
        expression6='  |    number, symmetry, multiplicity:   '+str(BonA)+' a    1'
        expression7='ADC(2)   Transition moments for pair    '+str(inistate)+' a       '+str(BonA)+' a'
        if linesA[i].startswith(expression1):
            transtr=float(linesA[i].split()[-4])
            delEvert=float(linesA[i].split()[-6])
        elif linesA[i].startswith(expression5):
            transtr=float(linesA[i].split()[-4])
            delEvert=float(linesA[i].split()[-6])
        elif linesA[i].startswith(expression4):
    #        print(linesA[i])
    #        print(linesA[i+2])
            xtrans=float(linesA[i+2].split()[2])
            ytrans=float(linesA[i+3].split()[2])
            ztrans=float(linesA[i+4].split()[2])
        elif linesA[i].startswith(expression7):
    #        print(linesA[i])
    #        print(linesA[i+2])
            xtrans=float(linesA[i+2].split()[2])
            ytrans=float(linesA[i+3].split()[2])
            ztrans=float(linesA[i+4].split()[2])
        elif linesA[i].startswith(expression2) and linesA[i-1].startswith('  |  Excited state reached by transition:'):
    #        print(linesA[i])
    #        print(linesA[i+22])
            xi=float(linesA[i+22].split()[-1])
            yi=float(linesA[i+23].split()[-1])
            zi=float(linesA[i+24].split()[-1])
            EA=float(linesA[i+4].split()[-1])
        elif linesA[i].startswith(expression3) and linesA[i-1].startswith('  |  Excited state reached by transition:'):
    #        print(linesA[i])
    #        print(linesA[i+22])
            xf=float(linesA[i+22].split()[-1])
            yf=float(linesA[i+23].split()[-1])
            zf=float(linesA[i+24].split()[-1])
            EBongeomA=float(linesA[i+4].split()[-1])
        elif linesA[i].startswith(expression6) and linesA[i-1].startswith('  |  Excited state reached by transition:'):
    #        print(linesA[i])
    #        print(linesA[i+22])
            xf=float(linesA[i+22].split()[-1])
            yf=float(linesA[i+23].split()[-1])
            zf=float(linesA[i+24].split()[-1])
            EBongeomA=float(linesA[i+4].split()[-1])

    #	Generalized Mulliken Hush
    print(transtr, delEvert)
    dip_12 = sqrt(transtr)
    delE = delEvert/27.211
    dipdiff = ((xi-xf)**2)+((yi-yf)**2)+((zi-zf)**2)
    # licz = sqrt(transtr)*(delEvert/27.211)
    # mian = sqrt(((xi-xf)**2)+((yi-yf)**2)+((zi-zf)**2)+4*transtr)
    H_ab=(sqrt(transtr)*(delEvert/27.211))/sqrt(((xi-xf)**2)+((yi-yf)**2)+((zi-zf)**2)+4*transtr)
    #	Boys localization
    H_ab2=(1./(2.*sqrt(2.)))*sqrt(1.+(transtr-(((xi-xf)**2)+((yi-yf)**2)+((zi-zf)**2))/4.0)/sqrt(((transtr-(((xi-xf)**2)+((yi-yf)**2)+((zi-zf)**2))/4.0)**2)+(xtrans*(xi-xf)+ytrans*(yi-yf)+ztrans*(zi-zf))**2))*(delEvert/27.211)

    stateA.close()
    return(H_ab, H_ab2)
            

parser = argparse.ArgumentParser(description = "Calculate the electronic coupling with the GMH approach and Boys localization method from TURBOMOLE 7.6 ADC(2) results")
parser.add_argument( "-n", "--name",  type=str, metavar = "", required = True, help = "Name of the file with ADC(2) results")
parser.add_argument( "-i", "--initial",  type=int, metavar = "", required = True, help = "Initial electronic state (0 is the ground state)")
parser.add_argument( "-f", "--final", type=int, metavar = "" ,required = True, help = "Final electronic state on initial state (0 is the ground state)")
args = parser.parse_args()

H_ab, H_ab2 = ricc2_file_parser(args.name, args.initial, args.final)

print("The H_ab (GMH) for the states S"+str(args.initial)+" and S"+str(args.final)+" amounts to:",H_ab,"a.u. ("+str(H_ab*27.211)+" eV)")
#print("Transition moment elements:", xtrans, ytrans, ztrans)
#print("Transition strength [a. u.]:", transtr)
#print("Excitation energy between the 1st and selected excited state [eV]:", delEvert)
print("The H_ab (Boys) for the states S"+str(args.initial)+" and S"+str(args.final)+" amounts to:",H_ab2,"a.u. ("+str(H_ab2*27.211)+" eV)")