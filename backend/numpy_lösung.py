import numpy as np

# Temperatur-Grid, z.B. 10x10
temp = np.zeros((10, 10))
temp[0, :] = 200  # Randbedingung z.B. Ofenboden heiß


# Ein FDM-Zeitschritt (vereinfachtes Beispiel, 2D-Wärmeleitung)
def step(temp, alpha=0.1):
    new_temp = temp.copy()
    new_temp[1:-1, 1:-1] = temp[1:-1, 1:-1] + alpha * (
        temp[2:, 1:-1] + temp[:-2, 1:-1] +
        temp[1:-1, 2:] + temp[1:-1, :-2] -
        4 * temp[1:-1, 1:-1]
    )
    return new_temp
