import os
import xml.etree.ElementTree as ET

from .Order import order
from .DocInfo import docinfo
from .DocInfo import mode
from .Order.Product import product
from .Order import orderinfo
from .Order import orderinfoval
from .Order.Product.ElementInfo import elementinfo
from .Order.Product.ElementInfo import eleminfoval
from .Order.Product.Slab import slab
from .Order.Product.Slab.Outline import outline
from .Order.Product.Slab.Outline.Shape import shape
from .Order.Product.Slab.Outline.Shape.SVertex import svertex
from .Order.Product.Slab.Steel import steel
from .Order.Product.Slab.Steel.Alloc import alloc
from .Order.Product.Slab.Steel.Alloc.Region import region
from .Order.Product.Slab.Steel.Bar import bar
from .Order.Product.Slab.Steel.Bar.Segment import segment
from .Order.Product.Slab.Steel.Bar.Spacer import spacer
from .Order.Product.Slab.Steel.Bar.WeldingPoint import weldingpoint
from .Order.Product.Slab.Steel.Girder import girder
from .Order.Product.Slab.Steel.Girder.AnchorBar import anchorbar
from .Order.Product.Slab.Steel.Girder.GirderExt import girderext
from .Order.Product.Slab.Steel.Girder.Section import section
from .Order.Product.Slab.Steel.SteelExt import steelext
from .Feedback import feedback
from .Feedback.Description import description
from .Feedback.FbVal import fbval


# Développé par Sofiane Fares
# Basé sur le PXML de la société Progress Group // https://www.progress.group/en/
# Spécification du PXML : https://www.pxml.eu/PXML-Specification-1.3-EN.pdf
# Version 1.0.0
# Dernière mise à jour le 2024-04-25

# Developed by Sofiane Fares
# Based on PXML from Progress Group // https://www.progress.group/en/
# PXML specification: https://www.pxml.eu/PXML-Specification-1.3-EN.pdf
# Version 1.0.0
# Last updated on 2024-04-25

class pxml:

    def __init__(self, fichier_pxml: str):
        self.DocInfo = None
        self.Order = []
        self.Feedback = []

        tree = ET.parse(fichier_pxml, ET.XMLParser(encoding='utf-8'))
        root = tree.getroot()
        ns = root.tag.replace("PXML_Document", "")

        for ae in range(len(root)):
            a = root[ae].tag.replace(ns, "")
            if a == "DocInfo":
                GlobalID = root.get("GlobalID")
                Mode = []
                MajorVersion = root[ae].find(ns + "MajorVersion").text
                MinorVersion = root[ae].find(ns + "MinorVersion").text
                if root[ae].find(ns + "Comment") is not None:
                    Comment = root[ae].find(ns + "Comment").text
                else:
                    Comment = None
                if root[ae].find(ns + "ConvertConventions") is not None:
                    ConvertConventions = root[ae].find(ns + "ConvertConventions").text
                else:
                    ConvertConventions = None

                for b in range(len(root[ae])):
                    if root[ae][b].tag.replace(ns, "") == "Mode":
                        Mode.append(mode.Mode(root[ae][b].find(ns + "ID").text, root[ae][b].find(ns + "Val").text))

                self.DocInfo = docinfo.DocInfo(GlobalID=GlobalID, MajorVersion=int(MajorVersion),
                                               MinorVersion=int(MinorVersion), Comment=Comment,
                                               ConvertConventions=ConvertConventions, Mode=Mode)

            elif a == "Order":
                GlobalID = root[ae].get("GlobalID")
                temp_Product = []
                temp_OrderInfo = []

                for b in root[ae].findall(ns + "OrderInfo"):
                    temp_OrderInfoVal = []
                    for c in b.findall(ns + "OrderInfoVal"):
                        temp_OrderInfoVal.append(orderinfoval.OrderInfoVal(
                            Type=(c.find(ns + "Type").text if c.find(ns + "Type") is not None else None),
                            V=(c.find(ns + "V").text if c.find(ns + "V") is not None else None),
                            U=(c.find(ns + "U").text if c.find(ns + "U") is not None else None),
                            Culture=(c.find(ns + "Culture").text if c.find(ns + "Culture") is not None else None)
                        ))

                    temp_OrderInfo.append(orderinfo.OrderInfo(
                        Type=(b.find(ns + "Type").text if b.find(ns + "Type") is not None else None),
                        GlobalID=(b.get("GlobalID")),
                        Code=(b.find(ns + "Code").text if b.find(ns + "Code") is not None else None),
                        OrderInfoVal=temp_OrderInfoVal))

                for b in root[ae].findall(ns + "Product"):
                    temp_ElementInfo = []
                    temp_Slab = []

                    for c in b.findall(ns + "ElementInfo"):
                        temp_ElementInfoVal = []
                        for d in c.findall(ns + "ElementInfoVal"):
                            temp_ElementInfoVal.append(eleminfoval.ElemInfoVal(
                                Type=(d.find(ns + "Type").text if d.find(ns + "Type") is not None else None),
                                V=(d.find(ns + "V").text if d.find(ns + "V") is not None else None),
                            ))

                        temp_ElementInfo.append(elementinfo.ElementInfo(
                            Type=(c.find(ns + "Type").text if c.find(ns + "Type") is not None else None),
                            Inventory=(c.find(ns + "Inventory").text if c.find(ns + "Inventory") is not None else None),
                            GlobalID=(c.get("GlobalID")),
                            Code=(c.find(ns + "Code").text if c.find(ns + "Code") is not None else None),
                            Description=(
                                c.find(ns + "Description").text if c.find(ns + "Description") is not None else None),
                            ObjectID=(c.find(ns + "ObjectID").text if c.find(ns + "ObjectID") is not None else None),
                            PieceCount=(
                                c.find(ns + "PieceCount").text if c.find(ns + "PieceCount") is not None else None),
                            Val1=(c.find(ns + "Val1").text if c.find(ns + "Val1") is not None else None),
                            Val2=(c.find(ns + "Val2").text if c.find(ns + "Val2") is not None else None),
                            Unit=(c.find(ns + "Unit").text if c.find(ns + "Unit") is not None else None),
                            Details=(c.find(ns + "Details").text if c.find(ns + "Details") is not None else None),
                            ElementInfoVal=temp_ElementInfoVal,
                        ))

                    for c in b.findall(ns + "Slab"):

                        temp_Outline = []
                        temp_Steel = []

                        for d in c.findall(ns + "Outline"):
                            temp_Shape = []
                            for e in d.findall(ns + "Shape"):
                                temp_SVertex = []
                                for f in e.findall(ns + "SVertex"):
                                    temp_SVertex.append(svertex.SVertex(
                                        GlobalID=f.get("GlobalID"),
                                        X=f.find(ns + "X").text if f.find(ns + "X") is not None else None,
                                        Y=f.find(ns + "Y").text if f.find(ns + "Y") is not None else None,
                                        Bulge=f.find(ns + "Bulge").text if f.find(ns + "Bulge") is not None else None,
                                        LineAttribute=f.find(ns + "LineAttribute").text if f.find(
                                            ns + "LineAttribute") is not None else None,
                                        Profile=f.find(ns + "Profile").text if f.find(
                                            ns + "Profile") is not None else None,
                                        DX=f.find(ns + "DX").text if f.find(ns + "DX") is not None else None,
                                        DY=f.find(ns + "DY").text if f.find(ns + "DY") is not None else None
                                    ))
                                temp_Shape.append(shape.Shape(
                                    GlobalID=e.get("GlobalID"),
                                    Cutout=(e.find(ns + "Cutout").text if e.find(ns + "Cutout") is not None else None),
                                    RefHeight=(e.find(ns + "RefHeight").text if e.find(
                                        ns + "RefHeight") is not None else None),
                                    SVertex=temp_SVertex
                                ))
                            temp_Outline.append(outline.Outline(
                                GlobalID=d.get("GlobalID"),
                                Type=d.get("Type"),
                                X=d.find(ns + "X").text if d.find(ns + "X") is not None else None,
                                Y=d.find(ns + "Y").text if d.find(ns + "Y") is not None else None,
                                Z=d.find(ns + "Z").text if d.find(ns + "Z") is not None else None,
                                RotX=d.find(ns + "RotX").text if d.find(ns + "RotX") is not None else None,
                                RotY=d.find(ns + "RotY").text if d.find(ns + "RotY") is not None else None,
                                RotZ=d.find(ns + "RotZ").text if d.find(ns + "RotZ") is not None else None,
                                Height=d.find(ns + "Height").text if d.find(ns + "Height") is not None else None,
                                Name=d.find(ns + "Name").text if d.find(ns + "Name") is not None else None,
                                GenericInfo01=d.find(ns + "GenericInfo01").text if d.find(
                                    ns + "GenericInfo01") is not None else None,
                                GenericInfo02=d.find(ns + "GenericInfo02").text if d.find(
                                    ns + "GenericInfo02") is not None else None,
                                MountingInstruction=d.find(ns + "MountingInstruction").text if d.find(
                                    ns + "MountingInstruction") is not None else None,
                                MountPartType=d.find(ns + "MountPartType").text if d.find(
                                    ns + "MountPartType") is not None else None,
                                MountPartArticle=d.find(ns + "MountPartArticle").text if d.find(
                                    ns + "MountPartArticle") is not None else None,
                                MountPartIronProjection=d.find(ns + "MountPartIronProjection").text if d.find(
                                    ns + "MountPartIronProjection") is not None else None,
                                MountPartDirection=d.find(ns + "MountPartDirection").text if d.find(
                                    ns + "MountPartDirection") is not None else None,
                                MountPartLength=d.find(ns + "MountPartLength").text if d.find(
                                    ns + "MountPartLength") is not None else None,
                                MountPartWidth=d.find(ns + "MountPartWidth").text if d.find(
                                    ns + "MountPartWidth") is not None else None,
                                ConcretingMode=d.find(ns + "ConcretingMode").text if d.find(
                                    ns + "ConcretingMode") is not None else None,
                                ConcreteQuality=d.find(ns + "ConcreteQuality").text if d.find(
                                    ns + "ConcreteQuality") is not None else None,
                                UnitWeight=d.find(ns + "UnitWeight").text if d.find(
                                    ns + "UnitWeight") is not None else None,
                                Volume=d.find(ns + "Volume").text if d.find(ns + "Volume") is not None else None,
                                Layer=d.find(ns + "Layer").text if d.find(ns + "Layer") is not None else None,
                                ObjectID=d.find(ns + "ObjectID").text if d.find(ns + "ObjectID") is not None else None,
                                Shape=temp_Shape
                            ))

                        for d in c.findall(ns + "Steel"):
                            temp_Bar = []
                            temp_Girder = []
                            temp_Alloc = []
                            temp_SteelExt = []

                            for e in d.findall(ns + "Bar"):
                                temp_Segment = []
                                temp_Spacer = []
                                temp_WeldingPoint = []

                                for f in e.findall(ns + "Segment"):
                                    temp_Segment.append(segment.Segment(
                                        GlobalID=f.get("GlobalID"),
                                        Type=f.find(ns + "Type").text if f.find(ns + "Type") is not None else None,
                                        RotX=f.find(ns + "RotX").text if f.find(ns + "RotX") is not None else None,
                                        BendY=f.find(ns + "BendY").text if f.find(ns + "BendY") is not None else None,
                                        L=f.find(ns + "L").text if f.find(ns + "L") is not None else None,
                                        R=f.find(ns + "R").text if f.find(ns + "R") is not None else None,
                                    ))

                                for f in e.findall(ns + "Spacer"):
                                    temp_Spacer.append(spacer.Spacer(
                                        GlobalID=f.get("GlobalID"),
                                        Type=f.find(ns + "Type").text if f.find(ns + "Type") is not None else None,
                                        Position=f.find(ns + "Position").text if f.find(
                                            ns + "Position") is not None else None,
                                    ))

                                for f in e.findall(ns + "WeldingPoint"):
                                    temp_WeldingPoint.append(weldingpoint.WeldingPoint(
                                        GlobalID=f.get("GlobalID"),
                                        WeldingOutput=f.find(ns + "WeldingOutput").text if f.find(
                                            ns + "WeldingOutput") is not None else None,
                                        Position=f.find(ns + "Position").text if f.find(
                                            ns + "Position") is not None else None,
                                        WeldingPointType=f.find(ns + "WeldingPointType").text if f.find(
                                            ns + "WeldingPointType") is not None else None,
                                        WeldingPrgNo=f.find(ns + "WeldingPrgNo").text if f.find(
                                            ns + "WeldingPrgNo") is not None else None,
                                        GroupID=f.find(ns + "GroupID").text if f.find(
                                            ns + "GroupID") is not None else None,
                                    ))

                                temp_Bar.append(bar.Bar(GlobalID=e.get("GlobalID"),
                                                        ShapeMode=e.find(ns + "ShapeMode").text if e.find( ns + "ShapeMode") is not None else None,
                                                        ReinforcementType=e.find(
                                                            ns + "ReinforcementType").text if e.find(
                                                            ns + "ReinforcementType") is not None else None,
                                                        SteelQuality=e.find(ns + "SteelQuality").text if e.find(
                                                            ns + "SteelQuality") is not None else None,
                                                        PieceCount=e.find(ns + "PieceCount").text if e.find(
                                                            ns + "PieceCount") is not None else None,
                                                        Diameter=e.find(ns + "Diameter").text if e.find(
                                                            ns + "Diameter") is not None else None,
                                                        X=e.find(ns + "X").text if e.find(
                                                            ns + "X") is not None else None,
                                                        Y=e.find(ns + "Y").text if e.find(
                                                            ns + "Y") is not None else None,
                                                        Z=e.find(ns + "Z").text if e.find(
                                                            ns + "Z") is not None else None,
                                                        RotZ=e.find(ns + "RotZ").text if e.find(
                                                            ns + "RotZ") is not None else None,
                                                        ArticleNo=e.find(ns + "ArticleNo").text if e.find(
                                                            ns + "ArticleNo") is not None else None,
                                                        NoAutoProd=e.find(ns + "NoAutoProd").text if e.find(
                                                            ns + "NoAutoProd") is not None else None,
                                                        ExtIronWeight=e.find(ns + "ExtIronWeight").text if e.find(
                                                            ns + "ExtIronWeight") is not None else None,
                                                        Bin=e.find(ns + "Bin").text if e.find(
                                                            ns + "Bin") is not None else None,
                                                        Pos=e.find(ns + "Pos").text if e.find(
                                                            ns + "Pos") is not None else None,
                                                        Note=e.find(ns + "Note").text if e.find(
                                                            ns + "Note") is not None else None,
                                                        Machine=e.find(ns + "Machine").text if e.find(
                                                            ns + "Machine") is not None else None,
                                                        BendingDevice=e.find(ns + "BendingDevice").text if e.find(
                                                            ns + "BendingDevice") is not None else None,
                                                        Spacer=temp_Spacer,
                                                        WeldingPoint=temp_WeldingPoint,
                                                        Segment=temp_Segment
                                                        ))

                            for e in d.findall(ns + "Girder"):
                                temp_AnchorBar = []
                                temp_GirderExt = []
                                temp_Section = []

                                for f in e.findall(ns + "AnchorBar"):
                                    temp_AnchorBar.append(anchorbar.AnchorBar(
                                        GlobalID=f.get("GlobalID"),
                                        Type=f.find(ns + "Type").text if f.find(ns + "Type") is not None else None,
                                        Length=f.find(ns + "Length").text if f.find(
                                            ns + "Length") is not None else None,
                                        Position=f.find(ns + "Position").text if f.find(
                                            ns + "Position") is not None else None,
                                    ))

                                for f in e.findall(ns + "GirderExt"):
                                    temp_GirderExt.append(girderext.GirderExt(
                                        GlobalID=f.get("GlobalID"),
                                        Type=f.find(ns + "Type").text if f.find(ns + "Type") is not None else None,
                                        Position=f.find(ns + "Position").text if f.find(
                                            ns + "Position") is not None else None,
                                        Flags=f.find(ns + "Flags").text if f.find(ns + "Flags") is not None else None,
                                        Val0=f.find(ns + "Val0").text if f.find(ns + "Val0") is not None else None,
                                        Val1=f.find(ns + "Val1").text if f.find(ns + "Val1") is not None else None,
                                        Val2=f.find(ns + "Val2").text if f.find(ns + "Val2") is not None else None,
                                        Val3=f.find(ns + "Val3").text if f.find(ns + "Val3") is not None else None,
                                    ))

                                for f in e.findall(ns + "Section"):
                                    temp_Section.append(section.Section(
                                        GlobalID=f.get("GlobalID"),
                                        L=f.find(ns + "L").text if f.find(ns + "L") is not None else None,
                                        S=f.find(ns + "S").text if f.find(ns + "S") is not None else None,
                                        F=f.find(ns + "F").text if f.find(ns + "F") is not None else None,
                                    ))

                                temp_Girder.append(girder.Girder(GlobalID=e.get("GlobalID"),
                                                                 PieceCount=e.find(ns + "PieceCount").text if e.find(
                                                                     ns + "PieceCount") is not None else None,
                                                                 X=e.find(ns + "X").text if e.find(
                                                                     ns + "X") is not None else None,
                                                                 Y=e.find(ns + "Y").text if e.find(
                                                                     ns + "Y") is not None else None,
                                                                 Z=e.find(ns + "Z").text if e.find(
                                                                     ns + "Z") is not None else None,
                                                                 GirderName=e.find(ns + "GirderName").text if e.find(
                                                                     ns + "GirderName") is not None else None,
                                                                 Length=e.find(ns + "Length").text if e.find(
                                                                     ns + "Length") is not None else None,
                                                                 AngleToX=e.find(ns + "AngleToX").text if e.find(
                                                                     ns + "AngleToX") is not None else None,
                                                                 NoAutoProd=e.find(ns + "NoAutoProd").text if e.find(
                                                                     ns + "NoAutoProd") is not None else None,
                                                                 Height=e.find(ns + "Height").text if e.find(
                                                                     ns + "Height") is not None else None,
                                                                 TopExcess=e.find(ns + "TopExcess").text if e.find(
                                                                     ns + "TopExcess") is not None else None,
                                                                 BottomExcess=e.find(
                                                                     ns + "BottomExcess").text if e.find(
                                                                     ns + "BottomExcess") is not None else None,
                                                                 Weight=e.find(ns + "Weight").text if e.find(
                                                                     ns + "Weight") is not None else None,
                                                                 TopFlangeDiameter=e.find(
                                                                     ns + "TopFlangeDiameter").text if e.find(
                                                                     ns + "TopFlangeDiameter") is not None else None,
                                                                 BottomFlangeDiameter=e.find(
                                                                     ns + "BottomFlangeDiameter").text if e.find(
                                                                     ns + "BottomFlangeDiameter") is not None else None,
                                                                 GirderType=e.find(ns + "GirderType").text if e.find(
                                                                     ns + "GirderType") is not None else None,
                                                                 MountingType=e.find(
                                                                     ns + "MountingType").text if e.find(
                                                                     ns + "MountingType") is not None else None,
                                                                 ArticleNo=e.find(ns + "ArticleNo").text if e.find(
                                                                     ns + "ArticleNo") is not None else None,
                                                                 Machine=e.find(ns + "Machine").text if e.find(
                                                                     ns + "Machine") is not None else None,
                                                                 Period=e.find(ns + "Period").text if e.find(
                                                                     ns + "Period") is not None else None,
                                                                 PeriodOffset=e.find(
                                                                     ns + "PeriodOffset").text if e.find(
                                                                     ns + "PeriodOffset") is not None else None,
                                                                 Width=e.find(ns + "Width").text if e.find(
                                                                     ns + "Width") is not None else None,
                                                                 AnchorBar=temp_AnchorBar,
                                                                 GirderExt=temp_GirderExt,
                                                                 Section=temp_Section
                                                                 ))

                            for e in d.findall(ns + "Alloc"):
                                temp_Region = []
                                for f in e.findall(ns + "Region"):
                                    temp_Region.append(region.Region(
                                        GlobalID=f.get("GlobalID"),
                                        IntervalCount=f.find(ns + "IntervalCount").text if f.find(
                                            ns + "IntervalCount") is not None else None,
                                        Pitch=f.find(ns + "Pitch").text if f.find(ns + "Pitch") is not None else None,
                                        IncludeBegin=f.find(ns + "IncludeBegin").text if f.find(
                                            ns + "IncludeBegin") is not None else None,
                                        IncludeEnd=f.find(ns + "IncludeEnd").text if f.find(
                                            ns + "IncludeEnd") is not None else None,
                                        RefIndex=f.find(ns + "RefIndex").text if f.find(
                                            ns + "RefIndex") is not None else None, ))

                                temp_Alloc.append(alloc.Alloc(
                                    GlobalID=e.get("GlobalID"),
                                    Type=e.find(ns + "Type").text if e.find(ns + "Type") is not None else None,
                                    GuildingBar=e.find(ns + "GuildingBar").text if e.find(
                                        ns + "GuildingBar") is not None else None,
                                    Region=temp_Region

                                ))

                            for e in d.findall(ns + "SteelExt"):
                                temp_SteelExt.append(steelext.SteelExt(
                                    GlobalID=e.get("GlobalID"),
                                    Type=e.find(ns + "Type").text if e.find(ns + "Type") is not None else None,
                                    Info=e.find(ns + "Info").text if e.find(ns + "Info") is not None else None, ))

                            temp_Steel.append(steel.Steel(GlobalID=d.get("GlobalID"),
                                                          Type=d.get("Type"),
                                                          X=d.find(ns + "X").text if d.find(
                                                              ns + "X") is not None else None,
                                                          Y=d.find(ns + "Y").text if d.find(
                                                              ns + "Y") is not None else None,
                                                          Z=d.find(ns + "Z").text if d.find(
                                                              ns + "Z") is not None else None,
                                                          RotX=d.find(ns + "RotX").text if d.find(
                                                              ns + "RotX") is not None else None,
                                                          RotY=d.find(ns + "RotY").text if d.find(
                                                              ns + "RotY") is not None else None,
                                                          RotZ=d.find(ns + "RotZ").text if d.find(
                                                              ns + "RotZ") is not None else None,
                                                          ToTurn=d.find(ns + "ToTurn").text if d.find(
                                                              ns + "ToTurn") is not None else None,
                                                          StopOnTurningSide=d.find(
                                                              ns + "StopOnTurningSide").text if d.find(
                                                              ns + "StopOnTurningSide") is not None else None,
                                                          Name=d.find(ns + "Name").text if d.find(
                                                              ns + "Name") is not None else None,
                                                          GenericInfo01=d.find(ns + "GenericInfo01").text if d.find(
                                                              ns + "GenericInfo01") is not None else None,
                                                          GenericInfo02=d.find(ns + "GenericInfo02").text if d.find(
                                                              ns + "GenericInfo02") is not None else None,
                                                          GenericInfo03=d.find(ns + "GenericInfo03").text if d.find(
                                                              ns + "GenericInfo03") is not None else None,
                                                          GenericInfo04=d.find(ns + "GenericInfo04").text if d.find(
                                                              ns + "GenericInfo04") is not None else None,
                                                          GenericInfo05=d.find(ns + "GenericInfo05").text if d.find(
                                                              ns + "GenericInfo05") is not None else None,
                                                          GenericInfo06=d.find(ns + "GenericInfo06").text if d.find(
                                                              ns + "GenericInfo06") is not None else None,
                                                          MeshType=d.find(ns + "MeshType").text if d.find(
                                                              ns + "MeshType") is not None else None,
                                                          WeldingDensity=d.find(ns + "WeldingDensity").text if d.find(
                                                              ns + "WeldingDensity") is not None else None,
                                                          BorderStrength=d.find(ns + "BorderStrength").text if d.find(
                                                              ns + "BorderStrength") is not None else None,
                                                          ProdX=d.find(ns + "ProdX").text if d.find(
                                                              ns + "ProdX") is not None else None,
                                                          ProdY=d.find(ns + "ProdY").text if d.find(
                                                              ns + "ProdY") is not None else None,
                                                          ProdZ=d.find(ns + "ProdZ").text if d.find(
                                                              ns + "ProdZ") is not None else None,
                                                          ProdRotX=d.find(ns + "ProdRotX").text if d.find(
                                                              ns + "ProdRotX") is not None else None,
                                                          ProdRotY=d.find(ns + "ProdRotY").text if d.find(
                                                              ns + "ProdRotY") is not None else None,
                                                          ProdRotZ=d.find(ns + "ProdRotZ").text if d.find(
                                                              ns + "ProdRotZ") is not None else None,
                                                          Layer=d.find(ns + "Layer").text if d.find(
                                                              ns + "Layer") is not None else None,
                                                          ObjectID=d.find(ns + "ObjectID").text if d.find(
                                                              ns + "ObjectID") is not None else None,
                                                          Bar=temp_Bar,
                                                          Girder=temp_Girder,
                                                          Alloc=temp_Alloc,
                                                          SteelExt=temp_SteelExt

                                                          ))

                        temp_Slab.append(slab.Slab(GlobalID=c.get("GlobalID"),
                                                   SlabNo=c.find(ns + "SlabNo").text if c.find(
                                                       ns + "SlabNo") is not None else None,
                                                   PartType=c.find(ns + "PartType").text if c.find(
                                                       ns + "PartType") is not None else None,
                                                   ProductionAddition=c.find(ns + "ProductionAddition").text if c.find(
                                                       ns + "ProductionAddition") is not None else None,
                                                   ProductionWay=c.find(ns + "ProductionWay").text if c.find(
                                                       ns + "ProductionWay") is not None else None,
                                                   NumberOfMeansOfTransport=c.find(
                                                       ns + "NumberOfMeansOfTransport").text if c.find(
                                                       ns + "NumberOfMeansOfTransport") is not None else None,
                                                   TransportSequence=c.find(ns + "TransportSequence").text if c.find(
                                                       ns + "TransportSequence") is not None else None,
                                                   PileLevel=c.find(ns + "PileLevel").text if c.find(
                                                       ns + "PileLevel") is not None else None,
                                                   TypeOfUnloading=c.find(ns + "TypeOfUnloading").text if c.find(
                                                       ns + "TypeOfUnloading") is not None else None,
                                                   MeanOfTransport=c.find(ns + "MeanOfTransport").text if c.find(
                                                       ns + "MeanOfTransport") is not None else None,
                                                   ExpositionClass=c.find(ns + "ExpositionClass").text if c.find(
                                                       ns + "ExpositionClass") is not None else None,
                                                   SlabArea=c.find(ns + "SlabArea").text if c.find(
                                                       ns + "SlabArea") is not None else None,
                                                   SlabWeight=c.find(ns + "SlabWeight").text if c.find(
                                                       ns + "SlabWeight") is not None else None,
                                                   ProductionThickness=c.find(
                                                       ns + "ProductionThickness").text if c.find(
                                                       ns + "ProductionThickness") is not None else None,
                                                   MaxLength=c.find(ns + "MaxLength").text if c.find(
                                                       ns + "MaxLength") is not None else None,
                                                   MaxWidth=c.find(ns + "MaxWidth").text if c.find(
                                                       ns + "MaxWidth") is not None else None,
                                                   IronProjectionLeft=c.find(ns + "IronProjectionLeft").text if c.find(
                                                       ns + "IronProjectionLeft") is not None else None,
                                                   IronProjectionRight=c.find(
                                                       ns + "IronProjectionRight").text if c.find(
                                                       ns + "IronProjectionRight") is not None else None,
                                                   IronProjectionBottom=c.find(
                                                       ns + "IronProjectionBottom").text if c.find(
                                                       ns + "IronProjectionBottom") is not None else None,
                                                   IronProjectionTop=c.find(ns + "IronProjectionTop").text if c.find(
                                                       ns + "IronProjectionTop") is not None else None,
                                                   X=c.find(ns + "X").text if c.find(ns + "X") is not None else None,
                                                   Y=c.find(ns + "Y").text if c.find(ns + "Y") is not None else None,
                                                   Z=c.find(ns + "Z").text if c.find(ns + "Z") is not None else None,
                                                   RotX=c.find(ns + "RotX").text if c.find(
                                                       ns + "RotX") is not None else None,
                                                   RotY=c.find(ns + "RotY").text if c.find(
                                                       ns + "RotY") is not None else None,
                                                   RotZ=c.find(ns + "RotZ").text if c.find(
                                                       ns + "RotZ") is not None else None,
                                                   ProdX=c.find(ns + "ProdX").text if c.find(
                                                       ns + "ProdX") is not None else None,
                                                   ProdY=c.find(ns + "ProdY").text if c.find(
                                                       ns + "ProdY") is not None else None,
                                                   ProdZ=c.find(ns + "ProdZ").text if c.find(
                                                       ns + "ProdZ") is not None else None,
                                                   ProdRotX=c.find(ns + "ProdRotX").text if c.find(
                                                       ns + "ProdRotX") is not None else None,
                                                   ProdRotY=c.find(ns + "ProdRotY").text if c.find(
                                                       ns + "ProdRotY") is not None else None,
                                                   ProdRotZ=c.find(ns + "ProdRotZ").text if c.find(
                                                       ns + "ProdRotZ") is not None else None,
                                                   OrderPosition=c.find(ns + "OrderPosition").text if c.find(
                                                       ns + "OrderPosition") is not None else None,
                                                   ProductGroup=c.find(ns + "ProductGroup").text if c.find(
                                                       ns + "ProductGroup") is not None else None,
                                                   SlabType=c.find(ns + "SlabType").text if c.find(
                                                       ns + "SlabType") is not None else None,
                                                   ItemDesignation=c.find(ns + "ItemDesignation").text if c.find(
                                                       ns + "ItemDesignation") is not None else None,
                                                   ProjectCoordinates=c.find(ns + "ProjectCoordinates").text if c.find(
                                                       ns + "ProjectCoordinates") is not None else None,
                                                   PositionInPileX=c.find(ns + "PositionInPileX").text if c.find(
                                                       ns + "PositionInPileX") is not None else None,
                                                   PositionInPileY=c.find(ns + "PositionInPileY").text if c.find(
                                                       ns + "PositionInPileY") is not None else None,
                                                   PositionInPileZ=c.find(ns + "PositionInPileZ").text if c.find(
                                                       ns + "PositionInPileZ") is not None else None,
                                                   AngleInPile=c.find(ns + "AngleInPile").text if c.find(
                                                       ns + "AngleInPile") is not None else None,
                                                   GenericInfo01=c.find(ns + "GenericInfo01").text if c.find(
                                                       ns + "GenericInfo01") is not None else None,
                                                   GenericInfo02=c.find(ns + "GenericInfo02").text if c.find(
                                                       ns + "GenericInfo02") is not None else None,
                                                   GenericInfo03=c.find(ns + "GenericInfo03").text if c.find(
                                                       ns + "GenericInfo03") is not None else None,
                                                   GenericInfo04=c.find(ns + "GenericInfo04").text if c.find(
                                                       ns + "GenericInfo04") is not None else None,
                                                   ReforcemInfo=c.find(ns + "ReforcemInfo").text if c.find(
                                                       ns + "ReforcemInfo") is not None else None,
                                                   Outline=temp_Outline,
                                                   Steel=temp_Steel))

                    print("ElementNo: " + b.find(ns + "ElementNo").text if b.find(ns + "ElementNo") is not None else None)
                    temp_Product.append(product.Product(GlobalID=b.get("GlobalID"),
                                                        ElementNo=b.find(
                                                            ns + "ElementNo").text if b.find(
                                                            ns + "ElementNo") is not None else None,
                                                        ProductType=b.find(
                                                            ns + "ProductType").text if b.find(
                                                            ns + "ProductType") is not None else None,
                                                        TotalThickness=b.find(
                                                            ns + "TotalThickness").text if b.find(
                                                            ns + "TotalThickness") is not None else None,
                                                        DoubleWallsGap=b.find(
                                                            ns + "DoubleWallsGap").text if b.find(
                                                            ns + "DoubleWallsGap") is not None else None,
                                                        PieceCount=b.find(
                                                            ns + "PieceCount").text if b.find(
                                                            ns + "PieceCount") is not None else None,
                                                        TurnWidth=b.find(
                                                            ns + "TurnWidth").text if b.find(
                                                            ns + "TurnWidth") is not None else None,
                                                        Comment=b.find(ns + "Comment").text if b.find(
                                                            ns + "Comment") is not None else None,
                                                        RotationPosition=b.find(
                                                            ns + "RotationPosition").text if b.find(
                                                            ns + "RotationPosition") is not None else None,
                                                        StackNo=b.find(ns + "StackNo").text if b.find(
                                                            ns + "StackNo") is not None else None,
                                                        StackID=b.find(ns + "StackID").text if b.find(
                                                            ns + "StackID") is not None else None,
                                                        StackingSequence=b.find(
                                                            ns + "StackingSequence").text if b.find(
                                                            ns + "StackingSequence") is not None else None,
                                                        StackingLevel=b.find(
                                                            ns + "StackingLevel").text if b.find(
                                                            ns + "StackingLevel") is not None else None,
                                                        StackingX=b.find(
                                                            ns + "StackingX").text if b.find(
                                                            ns + "StackingX") is not None else None,
                                                        StackingY=b.find(
                                                            ns + "StackingY").text if b.find(
                                                            ns + "StackingY") is not None else None,
                                                        StackingZ=b.find(
                                                            ns + "StackingZ").text if b.find(
                                                            ns + "StackingZ") is not None else None,
                                                        StackingAngle=b.find(
                                                            ns + "StackingAngle").text if b.find(
                                                            ns + "StackingAngle") is not None else None,
                                                        StackingRotY=b.find(
                                                            ns + "StackingRotY").text if b.find(
                                                            ns + "StackingRotY") is not None else None,
                                                        StackingRotX=b.find(
                                                            ns + "StackingRotX").text if b.find(
                                                            ns + "StackingRotX") is not None else None,
                                                        P1X=b.find(ns + "P1X").text if b.find(
                                                            ns + "P1X") is not None else None,
                                                        P1Y=b.find(ns + "P1Y").text if b.find(
                                                            ns + "P1Y") is not None else None,
                                                        P1Z=b.find(ns + "P1Z").text if b.find(
                                                            ns + "P1Z") is not None else None,
                                                        P2X=b.find(ns + "P2X").text if b.find(
                                                            ns + "P2X") is not None else None,
                                                        P2Y=b.find(ns + "P2Y").text if b.find(
                                                            ns + "P2Y") is not None else None,
                                                        P2Z=b.find(ns + "P2Z").text if b.find(
                                                            ns + "P2Z") is not None else None,
                                                        P3X=b.find(ns + "P3X").text if b.find(
                                                            ns + "P3X") is not None else None,
                                                        P3Y=b.find(ns + "P3Y").text if b.find(
                                                            ns + "P3Y") is not None else None,
                                                        P3Z=b.find(ns + "P3Z").text if b.find(
                                                            ns + "P3Z") is not None else None,
                                                        AdditionInfo=b.find(
                                                            ns + "AdditionInfo").text if b.find(
                                                            ns + "AdditionInfo") is not None else None,
                                                        UnloadingInfo=b.find(
                                                            ns + "UnloadingInfo").text if b.find(
                                                            ns + "UnloadingInfo") is not None else None,
                                                        TransportInfo=b.find(
                                                            ns + "TransportInfo").text if b.find(
                                                            ns + "TransportInfo") is not None else None,
                                                        ItemPosition=b.find(
                                                            ns + "ItemPosition").text if b.find(
                                                            ns + "ItemPosition") is not None else None,
                                                        ElementInfo=temp_ElementInfo,
                                                        Slab=temp_Slab, ))

                self.Order.append(
                    order.Order(GlobalID=GlobalID,
                                OrderNo=(root[ae].find(ns + "OrderNo").text if root[ae].find(
                                    ns + "OrderNo") is not None else None),
                                Structure=(root[ae].find(ns + "Structure").text if root[ae].find(
                                    ns + "Structure") is not None else None),
                                Building=(root[ae].find(ns + "Building").text if root[ae].find(
                                    ns + "Building") is not None else None),
                                Storey=(root[ae].find(ns + "Storey").text if root[ae].find(
                                    ns + "Storey") is not None else None),
                                SubStorey=(root[ae].find(ns + "SubStorey").text if root[ae].find(
                                    ns + "SubStorey") is not None else None),
                                Component=(root[ae].find(ns + "Component").text if root[ae].find(
                                    ns + "Component") is not None else None),
                                DrawingNo=(root[ae].find(ns + "DrawingNo").text if root[ae].find(
                                    ns + "DrawingNo") is not None else None),
                                DrawingDate=(root[ae].find(ns + "DrawingDate").text if root[ae].find(
                                    ns + "DrawingDate") is not None else None),
                                DrawingRevision=(root[ae].find(ns + "DrawingRevision").text if root[ae].find(
                                    ns + "DrawingRevision") is not None else None),
                                DrawingAuthor=(root[ae].find(ns + "DrawingAuthor").text if root[ae].find(
                                    ns + "DrawingAuthor") is not None else None),
                                ErpProjectUnit=(root[ae].find(ns + "ErpProjectUnit").text if root[ae].find(
                                    ns + "ErpProjectUnit") is not None else None),
                                DeliveryDate=(root[ae].find(ns + "DeliveryDate").text if root[ae].find(
                                    ns + "DeliveryDate") is not None else None),
                                GenericOrderInfo01=(root[ae].find(ns + "GenericOrderInfo01").text if root[ae].find(
                                    ns + "GenericOrderInfo01") is not None else None),
                                GenericOrderInfo02=(root[ae].find(ns + "GenericOrderInfo02").text if root[ae].find(
                                    ns + "GenericOrderInfo02") is not None else None),
                                GenericOrderInfo03=(root[ae].find(ns + "GenericOrderInfo03").text if root[ae].find(
                                    ns + "GenericOrderInfo03") is not None else None),
                                GenericOrderInfo04=(root[ae].find(ns + "GenericOrderInfo04").text if root[ae].find(
                                    ns + "GenericOrderInfo04") is not None else None),
                                GenericOrderInfo05=(root[ae].find(ns + "GenericOrderInfo05").text if root[ae].find(
                                    ns + "GenericOrderInfo05") is not None else None),
                                GenericOrderInfo06=(root[ae].find(ns + "GenericOrderInfo06").text if root[ae].find(
                                    ns + "GenericOrderInfo06") is not None else None),
                                GenericOrderInfo07=(root[ae].find(ns + "GenericOrderInfo07").text if root[ae].find(
                                    ns + "GenericOrderInfo07") is not None else None),
                                GenericOrderInfo08=(root[ae].find(ns + "GenericOrderInfo08").text if root[ae].find(
                                    ns + "GenericOrderInfo08") is not None else None),
                                GenericOrderInfo09=(root[ae].find(ns + "GenericOrderInfo09").text if root[ae].find(
                                    ns + "GenericOrderInfo09") is not None else None),
                                GenericOrderInfo10=(root[ae].find(ns + "GenericOrderInfo10").text if root[ae].find(
                                    ns + "GenericOrderInfo10") is not None else None),
                                GenericOrderInfo11=(root[ae].find(ns + "GenericOrderInfo11").text if root[ae].find(
                                    ns + "GenericOrderInfo11") is not None else None),
                                GenericOrderInfo12=(root[ae].find(ns + "GenericOrderInfo12").text if root[ae].find(
                                    ns + "GenericOrderInfo12") is not None else None),
                                GenericOrderInfo13=(root[ae].find(ns + "GenericOrderInfo13").text if root[ae].find(
                                    ns + "GenericOrderInfo13") is not None else None),
                                GenericOrderInfo14=(root[ae].find(ns + "GenericOrderInfo14").text if root[ae].find(
                                    ns + "GenericOrderInfo14") is not None else None),
                                GenericOrderInfo15=(root[ae].find(ns + "GenericOrderInfo15").text if root[ae].find(
                                    ns + "GenericOrderInfo15") is not None else None),
                                GenericOrderInfo16=(root[ae].find(ns + "GenericOrderInfo16").text if root[ae].find(
                                    ns + "GenericOrderInfo16") is not None else None),
                                GenericOrderInfo17=(root[ae].find(ns + "GenericOrderInfo17").text if root[ae].find(
                                    ns + "GenericOrderInfo17") is not None else None),
                                GenericOrderInfo18=(root[ae].find(ns + "GenericOrderInfo18").text if root[ae].find(
                                    ns + "GenericOrderInfo18") is not None else None),
                                GenericOrderInfo19=(root[ae].find(ns + "GenericOrderInfo19").text if root[ae].find(
                                    ns + "GenericOrderInfo19") is not None else None),
                                GenericOrderInfo20=(root[ae].find(ns + "GenericOrderInfo20").text if root[ae].find(
                                    ns + "GenericOrderInfo20") is not None else None),
                                Comment=(root[ae].find(ns + "Comment").text if root[ae].find(
                                    ns + "Comment") is not None else None),
                                OrderArea=(root[ae].find(ns + "OrderArea").text if root[ae].find(
                                    ns + "OrderArea") is not None else None),
                                ImportSource=(root[ae].find(ns + "ImportSource").text if root[ae].find(
                                    ns + "ImportSource") is not None else None),
                                ImportSourceType=(root[ae].find(ns + "ImportSourceType").text if root[ae].find(
                                    ns + "ImportSourceType") is not None else None),
                                ApplicationName=(root[ae].find(ns + "ApplicationName").text if root[ae].find(
                                    ns + "ApplicationName") is not None else None),
                                ApplicationGUID=(root[ae].find(ns + "ApplicationGUID").text if root[ae].find(
                                    ns + "ApplicationGUID") is not None else None),
                                ApplicationVersion=(root[ae].find(ns + "ApplicationVersion").text if root[ae].find(
                                    ns + "ApplicationVersion") is not None else None),
                                OrderInfo=[],
                                Product=temp_Product))

            elif a == "Feedback":
                GlobalID = root[ae].get("GlobalID")
                ItemType = root[ae].get("ItemType")
                temp_description = []
                temp_FbVal = []

                for f in root[ae].findall(ns + "Description"):
                    temp_description.append(description.Description(Culture=f.get("Culture"),
                                                                    Text=f.get("Text")))

                for f in root[ae].findall(ns + "FbVal"):
                    temp_FbVal.append(fbval.FbVal(T=f.get("T"),
                                                V=f.get("V")))

                self.Feedback.append(feedback.Feedback(GlobalID=GlobalID,ItemType=ItemType,
                                                       MessageType=(root[ae].find(ns + "MessageType").text if root[ae].find(
                                                           ns + "MessageType") is not None else None),
                                                       Code=(root[ae].find(ns + "Code").text if root[ae].find(
                                                           ns + "Code") is not None else None),
                                                       InfoValue=(root[ae].find(ns + "InfoValue").text if root[ae].find(
                                                           ns + "InfoValue") is not None else None),
                                                       PieceCount=(root[ae].find(ns + "PieceCount").text if root[ae].find(
                                                           ns + "PieceCount") is not None else None),
                                                       MaterialType=(root[ae].find(ns + "MaterialType").text if root[ae].find(
                                                           ns + "MaterialType") is not None else None),
                                                       MaterialBatch=(root[ae].find(ns + "MaterialBatch").text if root[ae].find(
                                                           ns + "MaterialBatch") is not None else None),
                                                       MaterialWeight=(root[ae].find(ns + "MaterialWeight").text if root[ae].find(
                                                           ns + "MaterialWeight") is not None else None),
                                                       ProdDate=(root[ae].find(ns + "ProdDate").text if root[ae].find(
                                                           ns + "ProdDate") is not None else None),
                                                       Machine=(root[ae].find(ns + "Machine").text if root[ae].find(
                                                           ns + "Machine") is not None else None),
                                                       Description=temp_description, FbVal=temp_FbVal))

        if self.DocInfo is None:
            raise ValueError("No DocInfo found in PXML file. Read https://www.pxml.eu/PXML-Specification-1.3-EN.pdf")

    def __xml__(self):
        def indent(elem, level=0):
            indent_size = "  "
            i = "\n" + level * indent_size
            if len(elem):
                if not elem.text or not elem.text.strip():
                    elem.text = i + indent_size
                if not elem.tail or not elem.tail.strip():
                    elem.tail = i
                for elem in elem:
                    indent(elem, level + 1)
                if not elem.tail or not elem.tail.strip():
                    elem.tail = i
            else:
                if level and (not elem.tail or not elem.tail.strip()):
                    elem.tail = i

        def pretty_print_xml_elementtree(xml_string):
            root = ET.fromstring(xml_string)
            indent(root)
            pretty_xml = ET.tostring(root, encoding="unicode", xml_declaration=True)
            return pretty_xml

        PXML = ET.Element("PXML_Document")
        PXML.set("xmlns", "http://progress-m.com/ProgressXML/Version1")
        PXML.append(self.DocInfo.__xml__())
        for Order in self.Order:
            PXML.append(Order.__xml__())
        for Feedback in self.Feedback:
            PXML.append(Feedback.__xml__())

        xml_str = ET.tostring(PXML)

        return pretty_print_xml_elementtree(xml_str).replace("ns0:", "").replace(":ns0", "")
