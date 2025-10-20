import davidson_data_handling as ddh
import data_saving_loading as dsl
import data_evaluating as de

for i in range(7):
    filename = f"0105_00{i}_fov"
    show = False

    print("Preparing data...")
    ddh.prepare_data(filename, "/home/lilly/Downloads/10-fish-0105/0105/")
    print("Loading data...")
    times, positions, orientations = dsl.load_data(f"{filename}.json")
    print("Evaluating and plotting...")
    de.plot_global_order(orientations=orientations, save_path=f"{filename}.svg", show=show)


"""
full transitions:
0084_006_fov
0107_001_fov
0124_000_fov
"""