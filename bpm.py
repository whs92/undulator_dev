from ophyd import Device, EpicsSignal, EpicsSignalRO, PVPositioner, Component as Cpt
from ophyd.device import DynamicDeviceComponent as DDC
import epics
import numpy as np

def BPMnames(**kwargs):
    BPMnames = {}
    #self.BPMrdXPVs = []
    #self.BPMrdYPVs = []

    for arc in range(1,9):
        for dt in ['D','T']:
            for bpm in range(1,8):
                bpmname = 'BPMZ{}{}{}R'.format(str(bpm),dt,str(arc))
                test_connection = epics.PV(bpmname+':rdX')
                if test_connection.status != None:
                    BPMnames[bpmname] = (BPM,bpmname + ':',kwargs)
                    
    
    return BPMnames

class BPM(Device):
    #Readback PVs
    rdX = Cpt(EpicsSignalRO, 'rdX', kind = 'hinted') #horizontal position
    rdY = Cpt(EpicsSignalRO, 'rdY', kind = 'hinted') #vertical position
    
    #Figure out how to return numpy array of [rdX,rdY]??
    
class AllBPMs(Device):
    
    bpms = DDC(BPMnames(kind = 'hinted'),kind = 'normal')
    
    
    
    
    
    '''
    def __init__(self):
        
        self.BPMnames = []
        self.BPMrdXPVs = []
        self.BPMrdYPVs = []
        
        for arc in range(1,9):
            for dt in ['D','T']:
                for bpm in range(1,8):
                    bpmname = 'BPMZ{}{}{}R'.format(str(bpm),dt,str(arc))
                    self.BPMnames.append(bpmname)'''
    
    