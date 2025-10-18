import davidson_data_handling as ddh
import data_saving_loading as dsl
import data_evaluating as de

filename = "0066_000_fov"

print("Preparing data...")
ddh.prepare_data(filename, "/home/lilly/Downloads/10-fish-0066/0066/")
print("Loading data...")
times, positions, orientations = dsl.load_data(f"{filename}.json")
print("Evaluating and plotting...")
de.plot_global_order(orientations=orientations, save_path=f"{filename}.svg")