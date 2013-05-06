import math

AVOGADRO = 6.022141e23
BOLTZMANN = 1.3806e-23
TEMP_INDEP_DIFFUSIVITY = 2e9
ACTIVATION_ENERGY = 4.4e5

def diffusivity(temperature):
    return TEMP_INDEP_DIFFUSIVITY * math.exp(-ACTIVATION_ENERGY/BOLTZMANN/AVOGADRO/temperature)

