import netCDF4 as nc

class Zerocubes: 
    dir = '/export/cloud/NCASweather/nx902220/DNS_LES/DNS_data/0degcubesFlowData/'
    file = 'r16168SENS.mat'

def readvar(self,var): 
    F = nc.Dataset(self)
    self.var = F.variables[var][:]
    return self.var

