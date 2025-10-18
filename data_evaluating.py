import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def compute_global_order(orientations):
    U = np.cos(orientations)
    V = np.sin(orientations)
    orientations = np.column_stack((U,V))
    
    sumOrientation = np.sum(orientations[np.newaxis,:,:],axis=1)
    return np.divide(np.sqrt(np.sum(sumOrientation**2,axis=1)), len(orientations))[0]

def plot_global_order(orientations, save_path=None):
    data = []
    for t in range(len(orientations)):
        data.append(compute_global_order(orientations[t]))

    plt.plot(data)
    if save_path != None:
        plt.savefig(save_path)
    plt.show()
    plt.close()

