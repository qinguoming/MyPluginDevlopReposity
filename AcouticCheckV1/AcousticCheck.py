# -*- coding: mbcs -*-
# this file is a kernel python file
from abaqus import *
from abaqusConstants import *
from symbolicConstants import *

# this plugin will realize features: give suggestions for acoustic elem meshing
# Basic principle: The larger the frequency range studied, the smaller the maximum mesh size.

def AcousticElemSize(minFreq,maxFreq,waveSpeed,n,m_min,demension):
    # wavespeed unit:mm/s frequency unit: 1/s
    # maxValue 
    print('==================================================================')
    nodeDistance=waveSpeed/(n*maxFreq*1.0)
    print('Acoustic element size limit : ')
    print('1 order element<  '+str(nodeDistance)+' mm')
    print('2 order element<  '+str(2*nodeDistance)+' mm')
    # external distance r1 minValue
    r1=(waveSpeed*m_min)/(minFreq*1.0)
    print('The distance from the source to the boundary should greater than:')
    print(' r1 > '+str(r1)+ ' mm')
    print('note:if you use infinite element, the r1 could much less than this value')
    # Estimate the size of the model
    # aoustic node number N in fem model
    N=((maxFreq/minFreq)**demension)*((n*m_min)**demension)
    print('Minimum number of  acoustic nodes:')
    print(str(N))
    print('===================================================================')
    
    