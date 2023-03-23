from pyrosm import OSM
from pyrosm import get_data


location = "switzerland"

# load switzerland data
fp = get_data(location, directory=".")
osm = OSM(fp)

# loop through cantons
boundaries = osm.get_boundaries(boundary_type="administrative")
cantons = [
    "Zürich", "Sankt Gallen", "Thurgau", "Schaffhausen"
]
for canton in cantons:
    print(canton)

    # TODO : get canton boundary
    bbox_geom = boundaries[boundaries['name'] == canton]['geometry'].values[0]
    print(" -- got boundaries")

    # load canton data
    osm_canton = OSM(fp, bounding_box=bbox_geom)

    # get and save bike data
    nodes, edges = osm_canton.get_network(nodes=True, network_type="cycling")
    print(" -- got bike network")
    edges.to_csv(f"cycling_edges_{canton}.csv", index=False)
    nodes.to_csv(f"cycling_nodes_{canton}.csv", index=False)

    # get car data
    nodes, edges = osm_canton.get_network(nodes=True, network_type="driving")
    print(" -- got driving network")
    edges.to_csv(f"driving_edges_{canton}.csv", index=False)
    nodes.to_csv(f"driving_nodes_{canton}.csv", index=False)

