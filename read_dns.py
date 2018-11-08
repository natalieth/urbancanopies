from scipy.io import loadmat

class Zerocubes: 
    dir = '/export/cloud/NCASweather/nx902220/DNS_LES/DNS_data/0degcubesFlowData/'
    file = 'r16168SENS.mat'

def readvar(fi,var): 
    F = loadmat(fi)
    self.var = F[var][:]
    return self.var

