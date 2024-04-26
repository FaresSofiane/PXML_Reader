import glob
import os
import xml.etree.ElementTree as ET

CUR_PATH = os.path.dirname(__file__)

# changer le nom du fichier
dossier_pxml = os.path.join(CUR_PATH, "230273  .002.pxml")
dict = {}

tree = ET.parse(dossier_pxml)
root = tree.getroot()

a = root.tag
ns = a.replace("PXML_Document", "")

#1a
PXML_Document = ns + 'PXML_Document'
#2b
DocInfo = ns + 'DocInfo'
Order = ns + 'Order'
#3c
Product = ns + 'Product'
#4d
ElementInfo = ns + 'ElementInfo'
#4d
Slab = ns + 'Slab'
#5e
Outline = ns + 'Outline'
#6f
Shape = ns + 'Shape'
#7g
SVertex = ns + 'SVertex'
#5e
Steel = ns + 'Steel'
#6f
Bar = ns + 'Bar'
#7g
Spacer = ns + 'Spacer'
WeldingPoint = ns + 'WeldingPoint'
Segment = ns + 'Segment'
#6f
Girder = ns + 'Girder'
#7g
AnchorBar = ns + 'AnchorBar'
GirderExt = ns + 'GirderExt'
Section = ns + 'Section'
#6f
Alloc = ns + 'Alloc'
#7g
Region = ns + 'Region'
#6f
SteelExt = ns + 'SteelExt'
#2b
Feedback = ns + 'Feedback'

# for ia in range(len(root)) :
#     a = root[ia].tag.replace(ns, "") + "_" + str(id(ia))
#     if len(root[ia]) > 0:
#         dict[a] = {}
#     else :
#         dict[a] = root[ia].text
#     for ib in range(len(root[ia])) :
#         b = root[ia][ib].tag.replace(ns, "") + "_" + str(id(ib))
#         if len(root[ia][ib]) > 0 :
#             dict[a][b] = {}
#         else :
#             dict[a][b] = root[ia][ib].text
#         for ic in range(len(root[ia][ib])) :
#             c = root[ia][ib][ic].tag.replace(ns, "") + "_" + str(id(ic))
#             if len(root[ia][ib][ic]) > 0 :
#                 dict[a][b][c] = {}
#             else :
#                 dict[a][b][c] = root[ia][ib][ic].text
#             for iid in range(len(root[ia][ib][ic])) :
#                 d = (root[ia][ib][ic][iid].tag.replace(ns, "") + "_" +str(id(iid)))
#                 if len(root[ia][ib][ic][iid]) > 0 :
#                     dict[a][b][c][d] = {}
#                 else :
#                     dict[a][b][c][d] = root[ia][ib][ic][iid].text
#                 for ie in range(len(root[ia][ib][ic][iid])) :
#                     e = root[ia][ib][ic][iid][ie].tag.replace(ns, "") + "_" + str(id(ie))
#                     if len(root[ia][ib][ic][iid][ie]) > 0 :
#                         dict[a][b][c][d][e] = {}
#                     else :
#                         dict[a][b][c][d][e] = root[ia][ib][ic][iid][ie].text
#                     for iif in range(len(root[ia][ib][ic][iid][ie])) :
#                         f = root[ia][ib][ic][iid][ie][iif].tag.replace(ns, "") + "_" + str(id(iif))
#                         if len(root[ia][ib][ic][iid][ie][iif]) > 0 :
#                             dict[a][b][c][d][e][f] = {}
#                         else :
#                             dict[a][b][c][d][e][f] = root[ia][ib][ic][iid][ie][iif].text
#                         for ig in range(len(root[ia][ib][ic][iid][ie][iif])) :
#                             g = root[ia][ib][ic][iid][ie][iif].tag.replace(ns, "") + "_" + str(id(ig))
#                             if len(root[ia][ib][ic][iid][ie][iif][ig]) > 0 :
#                                 dict[a][b][c][d][e][f][g] = {}
#                             else :
#                                 dict[a][b][c][d][e][f][g] = root[ia][ib][ic][iid][ie][iif][ig].text

def recursive(element,dict):
    for i,x in enumerate(element):
        tag = element[i].tag.replace(ns, "") + "_" + str(id(x))
        if len(x) > 0 :
            dict[tag] = {}

            recursive(x,dict[tag])
        else:
            dict[tag] = x.text


    return dict

print(recursive(root,dict))
