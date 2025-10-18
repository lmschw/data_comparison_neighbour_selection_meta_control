import h5py
import numpy as np

import data_saving_loading as dsl

def prepare_data(filename, filepath="", save_path="", save_interval=1):
    print(filepath + filename)
    f=h5py.File(filepath+filename+".h5",'r')
    times = []
    positions = []
    orientations = []

    print(f['/fields/x'])

    for t in range(len(f['/fields/x'][0])):
        positions_t = []
        orientations_t = []
        for fish in range(len(f['/fields/x'])):
            position = [f['/fields/x'][fish][t], f['/fields/y'][fish][t]]
            heading_x = f['/fields/heading_x'][fish][t]
            heading_y = f['/fields/y'][fish][t]
            orientation = np.arctan2(heading_y,heading_x)

            positions_t.append(position)
            orientations_t.append(orientation)

        times.append(t)
        positions.append(positions_t)
        orientations.append(orientations_t)

    f.close()

    dsl.save_data([np.array(times), np.array(positions), np.array(orientations)], path=save_path+filename+".json", save_interval=save_interval)
