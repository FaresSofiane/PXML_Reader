import bpy
import sys
import uuid

sys.path.append('/Users/sofiane/Documents/GitHub/PXML_Reader')
from PXML_Reader import pxml

file_path = "/Users/sofiane/Documents/GitHub/PXML_Reader/pxml_test_trou/240053  .007.pxml"

with open(file_path, 'r', encoding='UTF-8') as file:
    pxml_obj = pxml(file)


def create_face(element, name=str(uuid.uuid4())):
    slab_PartType = element.PartType
    scene = bpy.context.scene

    for outline in element.Outline:
        if "lot" in outline.Type:
            mesh = bpy.data.meshes.new(name)
            obj = bpy.data.objects.new(name, mesh)
            scene.collection.objects.link(obj)
            points = []

            if slab_PartType == "01":
                ep_f1 = (outline.Height + pxml_obj.Order[0].Product[0].DoubleWallsGap) / 1000 + (outline.Height / 1000)
            else:
                ep_f1 = outline.Height / 1000

            for shape in outline.Shape:
                if not shape.Cutout:
                    for svertex in shape.SVertex:
                        if slab_PartType == "01":
                            x = (svertex.X / 1000 if svertex.X is not None else 0)
                            y = (svertex.Y / 1000 if svertex.Y is not None else 0) * -1
                        else:
                            x = (svertex.X / 1000 if svertex.X is not None else 0)
                            y = (svertex.Y / 1000 if svertex.Y is not None else 0)
                        points.append((x, y, ep_f1))

            edges = [(i, i + 1) for i in range(len(points) - 1)]
            edges.append((len(points) - 1, 0))

            faces = [tuple(range(len(points)))] if len(points) > 2 else []

            mesh.from_pydata(points, edges, faces)
            mesh.update()

            cutout_objs = []
            for shape in outline.Shape:
                if shape.Cutout:
                    cutout_name = str(uuid.uuid4())
                    cutout_mesh = bpy.data.meshes.new(cutout_name)
                    cutout_obj = bpy.data.objects.new(cutout_name, cutout_mesh)
                    scene.collection.objects.link(cutout_obj)
                    cutout_objs.append(cutout_obj)
                    cutout_points = []

                    for svertex in shape.SVertex:
                        if slab_PartType == "01":
                            x = (svertex.X / 1000 if svertex.X is not None else 0)
                            y = (svertex.Y / 1000 if svertex.Y is not None else 0) * -1
                        else:
                            x = (svertex.X / 1000 if svertex.X is not None else 0)
                            y = (svertex.Y / 1000 if svertex.Y is not None else 0)
                        cutout_points.append((x, y, ep_f1))

                    cutout_edges = [(i, i + 1) for i in range(len(cutout_points) - 1)]
                    cutout_edges.append((len(cutout_points) - 1, 0))

                    cutout_faces = [tuple(range(len(cutout_points)))] if len(cutout_points) > 2 else []
                    cutout_mesh.from_pydata(cutout_points, cutout_edges, cutout_faces)
                    cutout_mesh.update()

                    bpy.context.view_layer.objects.active = cutout_obj
                    bpy.ops.object.mode_set(mode='EDIT')
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, outline.Height / 1000)})
                    bpy.ops.object.mode_set(mode='OBJECT')

            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, outline.Height / 1000)})
            bpy.ops.object.mode_set(mode='OBJECT')

            for cutout_obj in cutout_objs:
                bpy.context.view_layer.objects.active = obj
                bool_modifier = obj.modifiers.new(name="Boolean", type='BOOLEAN')
                bool_modifier.operation = 'DIFFERENCE'
                bool_modifier.object = cutout_obj
                bpy.ops.object.modifier_apply(modifier=bool_modifier.name)

                bpy.context.view_layer.objects.active = cutout_obj
                bpy.data.objects.remove(cutout_obj, do_unlink=True)

            return obj


f1 = create_face(pxml_obj.Order[0].Product[0].Slab[0], name="f1")
f2 = create_face(pxml_obj.Order[0].Product[0].Slab[1], name="f2")