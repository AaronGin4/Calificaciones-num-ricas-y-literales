import math

def grados_a_radianes(grados):
    return grados * (math.pi / 180)

def radianes_a_grados(radianes):
    return radianes * (180 / math.pi)

# Ejemplo de uso
grados = 45
radianes = grados_a_radianes(grados)
print(f"{grados} grados son {radianes} radianes")

radianes = math.pi / 4
grados = radianes_a_grados(radianes)
print(f"{radianes} radianes son {grados} grados")