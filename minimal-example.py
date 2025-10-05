import blenderproc as bproc
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('pix3d_path', nargs='?', default="/code/resources/pix3d", help="Path to the downloaded IKEA dataset, see the /scripts for the download script")
parser.add_argument('cc_material_path', nargs='?', default="/code/resources/cctextures", help="Path to CCTextures folder, see the /scripts for the download script.")
parser.add_argument('output_dir', nargs='?', default="output", help="Path to where the final files, will be saved")
args = parser.parse_args()
bproc.init()
materials = bproc.loader.load_ccmaterials()
interior_objects = []
for i in range(15):
    interior_objects.extend(bproc.loader.load_pix3d( "bed",args.pix3d_path))

objects = bproc.constructor.construct_random_room(used_floor_area=25, interior_objects=interior_objects,
                                                  materials=materials, amount_of_extrusions=5)
ceiling_obejcts = [obj for obj in objects if obj.get_name() == "Ceiling"]

print(f"Ceiling objects found: {ceiling_obejcts}")