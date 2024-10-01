import bpy
import sys

sys.path.append('/Users/sofiane/Documents/GitHub/PXML_Reader')
from PXML_Reader import pxml

file = "/Users/sofiane/Documents/GitHub/PXML_Reader/pxml_test_trou/240053  .007.pxml"

with open(file, 'r', encoding='UTF-8') as file:
    pxml_obj = pxml(file)

mesh1 = bpy.data.meshes.new("face1")
obj1 = bpy.data.objects.new("face1", mesh1)

scene = bpy.context.scene
scene.collection.objects.link(obj1)

points = []

for element in pxml_obj.Order[0].Product[0].Slab[0].Outline:
    if "lot" in element.Type:
        ep_f1 = (element.Height + pxml_obj.Order[0].Product[0].DoubleWallsGap) / 1000
        for shape in element.Shape:
            if not shape.Cutout:
                for svertex in shape.SVertex:
                    x = (svertex.X / 1000 if svertex.X is not None else 0)
                    y = (svertex.Y / 1000 if svertex.Y is not None else 0) * -1
                    points.append((x, y, ep_f1))

edges = [(i, i + 1) for i in range(len(points) - 1)]
edges.append((len(points) - 1, 0))

faces = [tuple(range(len(points)))] if len(points) > 2 else []
mesh1.from_pydata(points, edges, faces)
mesh1.update()

bpy.context.view_layer.objects.active = obj1
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, 0.055)})
bpy.ops.object.mode_set(mode='OBJECT')

mesh2 = bpy.data.meshes.new("face2")
obj2 = bpy.data.objects.new("face2", mesh2)

scene.collection.objects.link(obj2)

points = []

for element in pxml_obj.Order[0].Product[0].Slab[1].Outline:
    if "lot" in element.Type:
        for shape in element.Shape:
            if not shape.Cutout:
                for svertex in shape.SVertex:
                    x = svertex.X / 1000 if svertex.X is not None else 0
                    y = svertex.Y / 1000 if svertex.Y is not None else 0
                    points.append((x, y, 0))

edges = [(i, i + 1) for i in range(len(points) - 1)]
edges.append((len(points) - 1, 0))

faces = [tuple(range(len(points)))] if len(points) > 2 else []
mesh2.from_pydata(points, edges, faces)
mesh2.update()

bpy.context.view_layer.objects.active = obj2
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, 0.055)})
bpy.ops.object.mode_set(mode='OBJECT')

mesh1 = bpy.data.meshes.new("obj")
obj1 = bpy.data.objects.new("obj", mesh1)

scene = bpy.context.scene
scene.collection.objects.link(obj1)

points = []
for element in pxml_obj.Order[0].Product[0].Slab[0].Outline:
    if "lot" in element.Type:
        ep_f1 = (element.Height + pxml_obj.Order[0].Product[0].DoubleWallsGap) / 1000
        for shape in element.Shape:
            if shape.Cutout:
                for svertex in shape.SVertex:
                    x = (svertex.X / 1000 if svertex.X is not None else 0)
                    y = (svertex.Y / 1000 if svertex.Y is not None else 0) * -1
                    points.append((x, y, ep_f1))
print("points", points)

edges = [(i, i + 1) for i in range(len(points) - 1)]
edges.append((len(points) - 1, 0))

faces = [tuple(range(len(points)))] if len(points) > 2 else []
mesh1.from_pydata(points, edges, faces)
mesh1.update()

bpy.context.view_layer.objects.active = obj1
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, 0.055)})
bpy.ops.object.mode_set(mode='OBJECT')import bpy
import sys
sys.path.append('/Users/sofiane/Documents/GitHub/PXML_Reader')
from PXML_Reader import pxml

file = "/Users/sofiane/Documents/GitHub/PXML_Reader/pxml_test_trou/240053  .007.pxml"




with open(file, 'r', encoding='UTF-8') as file:
    pxml_obj = pxml(file)

mesh1 = bpy.data.meshes.new("face1")
obj1 = bpy.data.objects.new("face1", mesh1)

scene = bpy.context.scene
scene.collection.objects.link(obj1)

points = []

for element in pxml_obj.Order[0].Product[0].Slab[0].Outline :
    if "lot" in element.Type:
        ep_f1 = (element.Height + pxml_obj.Order[0].Product[0].DoubleWallsGap ) / 1000
        for shape in element.Shape:
            if not shape.Cutout:
                for svertex in shape.SVertex:
                    x = (svertex.X / 1000 if svertex.X is not None else 0 )
                    y = (svertex.Y / 1000 if svertex.Y is not None else 0 ) * -1
                    points.append((x, y, ep_f1))


edges = [(i, i + 1) for i in range(len(points) - 1)]
edges.append((len(points) - 1, 0))

faces = [tuple(range(len(points)))] if len(points) > 2 else []
mesh1.from_pydata(points, edges, faces)
mesh1.update()

bpy.context.view_layer.objects.active = obj1
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, 0.055)})
bpy.ops.object.mode_set(mode='OBJECT')

mesh2 = bpy.data.meshes.new("face2")
obj2 = bpy.data.objects.new("face2", mesh2)


scene.collection.objects.link(obj2)

points = []

for element in pxml_obj.Order[0].Product[0].Slab[1].Outline :
    if "lot" in element.Type:
        for shape in element.Shape:
            if not shape.Cutout:
                for svertex in shape.SVertex:
                    x = svertex.X / 1000 if svertex.X is not None else 0
                    y = svertex.Y / 1000 if svertex.Y is not None else 0
                    points.append((x, y, 0))


edges = [(i, i + 1) for i in range(len(points) - 1)]
edges.append((len(points) - 1, 0))

faces = [tuple(range(len(points)))] if len(points) > 2 else []
mesh2.from_pydata(points, edges, faces)
mesh2.update()

bpy.context.view_layer.objects.active = obj2
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, 0.055)})
bpy.ops.object.mode_set(mode='OBJECT')


mesh1 = bpy.data.meshes.new("obj")
obj1 = bpy.data.objects.new("obj", mesh1)

scene = bpy.context.scene
scene.collection.objects.link(obj1)

points = []
for element in pxml_obj.Order[0].Product[0].Slab[0].Outline :
    if "lot" in element.Type:
        ep_f1 = (element.Height + pxml_obj.Order[0].Product[0].DoubleWallsGap ) / 1000
        for shape in element.Shape:
            if shape.Cutout:
                for svertex in shape.SVertex:
                    x = (svertex.X / 1000 if svertex.X is not None else 0 )
                    y = (svertex.Y / 1000 if svertex.Y is not None else 0 ) * -1
                    points.append((x, y, ep_f1))
print("points", points)


edges = [(i, i + 1) for i in range(len(points) - 1)]
edges.append((len(points) - 1, 0))

faces = [tuple(range(len(points)))] if len(points) > 2 else []
mesh1.from_pydata(points, edges, faces)
mesh1.update()

bpy.context.view_layer.objects.active = obj1
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, 0.055)})
bpy.ops.object.mode_set(mode='OBJECT')