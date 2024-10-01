import bpy
import sys
sys.path.append('/Users/sofiane/Documents/GitHub/PXML_Reader')
from PXML_Reader import pxml

with open(file, 'r', encoding='UTF-8') as file:
    pxml_obj = pxml(file)

# Crée un nouveau maillage
mesh = bpy.data.meshes.new("Points")
obj = bpy.data.objects.new("Points", mesh)

# Ajoute l'objet à la scène active
scene = bpy.context.scene
scene.collection.objects.link(obj)

# Crée les coordonnées des points
points = [(0,0,0)]

for element in pxml_obj.Order[0].Product[0].Slab[0].Outline :
    if "mountpart" in element.Type:
        matrice = (element.)



edges = []
num_points = len(points)
for i in range(num_points - 1):
    edges.append((i, i + 1))
edges.append((num_points - 1, 0))  # Relie le dernier point au premier pour former une boucle

faces = []
if len(points) > 2:
    faces.append(tuple(range(len(points))))
# Assigner les arêtes au maillage
mesh.from_pydata(points, edges, faces)


mesh.update()

# Sélectionne tous les sommets
bpy.context.view_layer.objects.active = obj
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')

# Effectue l'extrusion
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 3)})
bpy.ops.object.mode_set(mode='OBJECT')
