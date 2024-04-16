import os
import osmnx as ox
import matplotlib.pyplot as plt

def plot_city_street_network(north, south, east, west, city_name, dpi=500, folder_name="street_network_imgs"):

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    print(f"Processing {city_name}...")
    G = ox.graph_from_bbox(north, south, east, west, network_type="drive")
    fig, ax = ox.plot_graph(ox.project_graph(G), node_size=0, edge_linewidth=0.5, show=False, close=True)
    filepath = os.path.join(folder_name, f"{city_name.replace(' ', '_').lower()}_street_network.png")
    fig.savefig(filepath, dpi=dpi)
    plt.close(fig)
    print(f"Finished {city_name}")

cities = [
    {"name": "Johannesburg", "bbox": (-26.0, -26.4, 28.2, 27.8)},
    {"name": "Cairo", "bbox": (30.1, 29.8, 31.4, 31.1)},
    {"name": "Bangkok", "bbox": (13.8, 13.6, 100.7, 100.4)},
    {"name": "Beirut", "bbox": (33.9, 33.85, 35.55, 35.47)},
    {"name": "Istanbul", "bbox": (41.2, 40.8, 29.1, 28.6)},
    {"name": "Barcelona", "bbox": (41.5, 41.3, 2.3, 2.0)},
    {"name": "Mexico City", "bbox": (19.6, 19.2, -98.9, -99.3)},
    {"name": "Toronto", "bbox": (43.9, 43.6, -79.2, -79.6)},
    {"name": "Rio de Janeiro", "bbox": (-22.7, -23.1, -43.1, -43.8)},
    {"name": "Sydney", "bbox": (-33.7, -34.0, 151.3, 150.7)},
    {"name": "London", "bbox": (51.7, 51.4, 0.2, -0.5)},
    {"name": "Paris", "bbox": (48.9, 48.8, 2.5, 2.2)},
    {"name": "Stockholm", "bbox": (59.4, 59.2, 18.2, 17.9)},
    {"name": "Amsterdam", "bbox": (52.4, 52.3, 5.0, 4.7)},
    {"name": "Rome", "bbox": (41.95, 41.8, 12.6, 12.4)},
    {"name": "Tokyo", "bbox": (35.8, 35.6, 139.9, 139.6)},
    {"name": "Moscow", "bbox": (55.9, 55.5, 37.9, 37.3)},
    {"name": "Berlin", "bbox": (52.7, 52.3, 13.8, 13.1)}
]

ox.settings.use_cache = False
ox.settings.log_console = True

for city in cities:
    north, south, east, west = city["bbox"]
    plot_city_street_network(north, south, east, west, city["name"])