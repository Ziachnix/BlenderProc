import blenderproc as bproc
import argparse
import debugpy

# debugpy.listen(5678)

# debugpy.wait_for_client()

parser = argparse.ArgumentParser()
parser.add_argument('pix3d_path', nargs='?', default="resources/pix3d", help="Path to the downloaded IKEA dataset, see the /scripts for the download script")
parser.add_argument('cc_material_path', nargs='?', default="resources/cctextures", help="Path to CCTextures folder, see the /scripts for the download script.")
parser.add_argument('output_dir', nargs='?', default="output", help="Path to where the final files, will be saved")
args = parser.parse_args()
bproc.init()
materials = bproc.loader.load_ccmaterials()
interior_objects = []
for i in range(15):
    interior_objects.extend(bproc.loader.load_pix3d( "bed",args.pix3d_path))

objects = bproc.constructor.construct_random_room(used_floor_area=25, interior_objects=interior_objects,
                                                  materials=materials,create_ceiling=False)
ceiling_obejcts = [obj for obj in objects if obj.get_name() == "Ceiling"]

print(f"Ceiling objects found: {ceiling_obejcts}")