from ophyd import Device, EpicsSignal, EpicsSignalRO, PVPositioner, Component as Cpt
import numpy as np

#UE49IT4R:BaseParGapsel.B

class UndulatorGap(PVPositioner):
    #Staging PVs
    
    
    #Setting PVs
    setpoint = Cpt(EpicsSignal,'BaseParGapsel.B', kind = 'normal')
    
    #Readback PVs
    #done = Cpt(EpicsSignalRO, 'BaseStatISLbl', kind = 'omitted', string = True)
    done = Cpt(EpicsSignalRO, 'BaseStatISLbl', kind = 'omitted')
    done_value = 1
    readback = Cpt(EpicsSignalRO, 'CIOC:rdbk0', kind = 'hinted')
    
    #Status/Staging PVs
    action_status = Cpt(EpicsSignal, 'BaseCmdMcmd', string = True, kind = 'config')
    
    #Effecting PVs
    actuate = Cpt(EpicsSignal, 'BaseCmdCalc.PROC', kind = 'omitted')
    
    
    #methods
    def stage (self):
        self.actuate.set(5) #gap drive mode 'START'
        super().stage()
        
class UndulatorShiftParallel(PVPositioner):
    #Staging PVs
    
    
    #Setting PVs
    setpoint = Cpt(EpicsSignal,'SBaseParGapsel.B', kind = 'normal')
    
    #Readback PVs
    #done = Cpt(EpicsSignalRO, 'BaseStatISLbl', kind = 'omitted', string = True)
    done = Cpt(EpicsSignalRO, 'SBaseStatISLbl', kind = 'omitted')
    done_value = 1
    readback = Cpt(EpicsSignalRO, 'CIOC:rdbk2', kind = 'hinted') #parallel Shift Readback
    
    #Status/Staging PVs
    action_status = Cpt(EpicsSignal, 'SBaseCmdMcmd', string = True, kind = 'config')
    
    #Effecting PVs
    actuate = Cpt(EpicsSignal, 'SBaseCmdCalc.PROC', kind = 'omitted')
    
    
    #methods
    def stage (self):
        self.actuate.set(5) #gap drive mode 'START'
        super().stage()
        
class Undulator(Device):
    gap = Cpt(UndulatorGap,'')
    
class UndulatorElliptical(Undulator):
    shift = Cpt(UndulatorShiftParallel,'')
    
    
#UE49 = ue('UE49IT4R:',name = 'UE49')
#U125_2 = u('U125ID2R:',name = 'U125_2')

#dictionary of all undulators
allIDs = {
    'U125_2':Undulator('U125ID2R:', name = 'U125_2'),
    'U49_2':Undulator('U49ID3R:', name = 'U49_2'),
    'U41':Undulator('U41IT3R:', name = 'U41'),
    'U49_1':Undulator('U49ID4R:', name = 'U49_1'),
    'UE49':UndulatorElliptical('UE49IT4R:', name = 'UE49'),
    'UE52':UndulatorElliptical('UE52ID5R:', name = 'UE52'),
    'UE46':UndulatorElliptical('UE46IT5R:', name = 'UE46'),
    'U139':Undulator('U139ID6R:', name = 'U139'),
    'UE56_1':UndulatorElliptical('UE56ID6R:', name = 'UE56_1'),
    'U17':Undulator('U17IT6R:', name = 'U17'),
    'UE48':UndulatorElliptical('UE48IT6R:', name = 'UE48'),
    'UE112':UndulatorElliptical('UE112ID7R:', name = 'UE112'),
    'UE56_2':UndulatorElliptical('UE56ID8R:', name = 'UE56_2'),
             }
