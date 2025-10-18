import json, codecs
import numpy as np

def save_data(data, path="sample.json", save_interval=1):
    time, positions, orientations = data
    dict = {"time": get_specified_intervals(save_interval, time.tolist()), 
            "positions": get_specified_intervals(save_interval, positions.tolist()), 
            "orientations": get_specified_intervals(save_interval, orientations.tolist())}
    with open(path, "w") as outfile:
        json.dump(dict, outfile)

def load_data(path="sample.json"):
    obj_text = codecs.open(path, 'r', encoding='utf-8').read()
    data = json.loads(obj_text)
    time = np.array(data["time"])
    positions = np.array(data["positions"])
    orientations = np.array(data["orientations"])
    return time, positions, orientations

def get_specified_intervals(interval, data):
    return [data[idx] for idx in range(0, len(data)) if idx % interval == 0]
