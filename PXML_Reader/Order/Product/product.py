import xml.etree.ElementTree as ET
from lib2to3.pgen2.tokenize import double3prog


class Product():


    def __init__(self, GlobalID: str = None, ElementNo: int = None, ProductType: int = None, TotalThickness: float = None, DoubleWallsGap: float = None, PieceCount: int = None, TurnWidth: float = None, Comment: str = None, RotationPosition: float = None, StackNo: int = None, StackID: int = None, StackingSequence: int = None, StackingLevel: int = None, StackingX: float = None, StackingY: float = None, StackingZ: float = None, StackingAngle: float = None, StackingRotY: float = None, StackingRotX: float = None, P1X: float = None, P1Y: float = None, P1Z: float = None, P2X: float = None, P2Y: float = None, P2Z: float = None, P3X: float = None, P3Y: float = None, P3Z: float = None, AdditionInfo: str = None, UnloadingInfo: str = None, TransportInfo: str = None, ItemPosition: str = None, ElementInfo: list = [], Slab: list = []):
        self.GlobalID = None
        self.ElementNo = None  # INT // 0,1
        self.ProductType = None  # INT // 0,1
        self.TotalThickness = None  # FLOAT // 0,1
        self.DoubleWallsGap = None  # FLOAT // 0,1
        self.PieceCount = None  # INT // 0,1
        self.TurnWidth = None  # FLOAT // 0,1
        self.Comment = None  # STR // 0,1
        self.RotationPosition = None  # FLOAT // 0,1
        self.StackNo = None  # INT // 0,1
        self.StackID = None  # INT // 0,1
        self.StackingSequence = None  # INT // 0,1
        self.StackingLevel = None  # INT // 0,1
        self.StackingX = None  # FLOAT // 0,1
        self.StackingY = None  # FLOAT // 0,1
        self.StackingZ = None  # FLOAT // 0,1
        self.StackingAngle = None  # FLOAT // 0,1
        self.StackingRotY = None  # FLOAT // 0,1
        self.StackingRotX = None  # FLOAT // 0,1
        self.P1X = None  # FLOAT // 0,1
        self.P1Y = None  # FLOAT // 0,1
        self.P1Z = None  # FLOAT // 0,1
        self.P2X = None  # FLOAT // 0,1
        self.P2Y = None  # FLOAT // 0,1
        self.P2Z = None  # FLOAT // 0,1
        self.P3X = None  # FLOAT // 0,1
        self.P3Y = None  # FLOAT // 0,1
        self.P3Z = None  # FLOAT // 0,1
        self.AdditionInfo = None  # STR // 0,1
        self.UnloadingInfo = None  # STR // 0,1
        self.TransportInfo = None  # STR // 0,1
        self.ItemPosition = None  # STR // 0,1
        self.ElementInfo = []  # Object ElementInfo from the module elementinfo. n,n
        self.Slab = []  # Object Slab from the module slab. n,n

        self.GlobalID = GlobalID
        self.ElementNo = ElementNo
        self.ProductType = ProductType
        if type(TotalThickness) is float:
            self.TotalThickness = float(TotalThickness)
        else:
            if TotalThickness is None:
                self.TotalThickness = None
            else:
                try:
                    self.TotalThickness = float(TotalThickness)
                except:
                    raise TypeError("TotalThickness must be a float")
        if type(DoubleWallsGap) is float:
            self.DoubleWallsGap = float(DoubleWallsGap)
        else:
            if DoubleWallsGap is None:
                self.DoubleWallsGap = None
            else:
                try:
                    self.DoubleWallsGap = float(DoubleWallsGap)
                except:

                    raise TypeError(f"DoubleWallsGap must be a float")

        if type(PieceCount) is int:
            self.PieceCount = int(PieceCount)
        else:
            if PieceCount is None:
                self.PieceCount = None
            else:
                try:
                    self.PieceCount = int(PieceCount)
                except:
                    raise TypeError("PieceCount must be an integer")

        if type(TurnWidth) is float:
            self.TurnWidth = float(TurnWidth)
        else:
            if TurnWidth is None:
                self.TurnWidth = None
            else:
                try:
                    self.TurnWidth = float(TurnWidth)
                except:
                    raise TypeError("TurnWidth must be a float")
        self.Comment = Comment
        if type(RotationPosition) is float:
            self.RotationPosition = float(RotationPosition)
        else:
            if RotationPosition is None:
                self.RotationPosition = None
            else:
                try:
                    self.RotationPosition = float(RotationPosition)
                except:
                    raise TypeError("RotationPosition must be a float")

        self.StackNo = StackNo
        self.StackID = StackID
        self.StackingSequence = StackingSequence
        self.StackingLevel = StackingLevel
        if type(StackingX) is float:
            self.StackingX = float(StackingX)
        else:
            if StackingX is None:
                self.StackingX = None
            else:
                try:
                    self.StackingX = float(StackingX)
                except:
                    raise TypeError("StackingX must be a float")

        if type(StackingY) is float:
            self.StackingY = float(StackingY)
        else:
            if StackingY is None:
                self.StackingY = None
            else:
                try:
                    self.StackingY = float(StackingY)
                except:
                    raise TypeError("StackingY must be a float")

        if type(StackingZ) is float:
            self.StackingZ = float(StackingZ)
        else:
            if StackingZ is None:
                self.StackingZ = None
            else:
                try:
                    self.StackingZ = float(StackingZ)
                except:
                    raise TypeError("StackingZ must be a float")

        if type(StackingAngle) is float:
            self.StackingAngle = float(StackingAngle)
        else:
            if StackingAngle is None:
                self.StackingAngle = None
            else:
                try:
                    self.StackingAngle = float(StackingAngle)
                except:
                    raise TypeError("StackingAngle must be a float")

        if type(StackingRotY) is float:
            self.StackingRotY = float(StackingRotY)
        else:
            if StackingRotY is None:
                self.StackingRotY = None
            else:
                try:
                    self.StackingRotY = float(StackingRotY)
                except:
                    raise TypeError("StackingRotY must be a float")

        if type(StackingRotX) is float:
            self.StackingRotX = float(StackingRotX)
        else:
            if StackingRotX is None:
                self.StackingRotX = None
            else:
                try:
                    self.StackingRotX = float(StackingRotX)
                except:
                    raise TypeError("StackingRotX must be a float")

        if type(P1X) is float:
            self.P1X = float(P1X)
        else:
            if P1X is None:
                self.P1X = None
            else:
                try:
                    self.P1X = float(P1X)
                except:
                    raise TypeError("P1X must be a float")

        if type(P1Y) is float:
            self.P1Y = float(P1Y)
        else:
            if P1Y is None:
                self.P1Y = None
            else:
                try:
                    self.P1Y = float(P1Y)
                except:
                    raise TypeError("P1Y must be a float")

        if type(P1Z) is float:
            self.P1Z = float(P1Z)
        else:
            if P1Z is None:
                self.P1Z = None
            else:
                try:
                    self.P1Z = float(P1Z)
                except:
                    raise TypeError("P1Z must be a float")

        if type(P2X) is float:
            self.P2X = float(P2X)
        else:
            if P2X is None:
                self.P2X = None
            else:
                try:
                    self.P2X = float(P2X)
                except:
                    raise TypeError("P2X must be a float")

        if type(P2Y) is float:
            self.P2Y = float(P2Y)
        else:
            if P2Y is None:
                self.P2Y = None
            else:
                try:
                    self.P2Y = float(P2Y)
                except:
                    raise TypeError("P2Y must be a float")

        if type(P2Z) is float:
            self.P2Z = float(P2Z)
        else:
            if P2Z is None:
                self.P2Z = None
            else:
                try:
                    self.P2Z = float(P2Z)
                except:
                    raise TypeError("P2Z must be a float")

        if type(P3X) is float:
            self.P3X = float(P3X)
        else:
            if P3X is None:
                self.P3X = None
            else:
                try:
                    self.P3X = float(P3X)
                except:
                    raise TypeError("P3X must be a float")

        if type(P3Y) is float:
            self.P3Y = float(P3Y)
        else:
            if P3Y is None:
                self.P3Y = None
            else:
                try:
                    self.P3Y = float(P3Y)
                except:
                    raise TypeError("P3Y must be a float")

        if type(P3Z) is float:
            self.P3Z = float(P3Z)
        else:
            if P3Z is None:
                self.P3Z = None
            else:
                try:
                    self.P3Z = float(P3Z)
                except:
                    raise TypeError("P3Z must be a float")

        self.AdditionInfo = AdditionInfo
        self.UnloadingInfo = UnloadingInfo
        self.TransportInfo = TransportInfo
        self.ItemPosition = ItemPosition
        self.ElementInfo = ElementInfo
        self.Slab = Slab

    def get_GlobalID(self):
        return self.GlobalID

    def get_ElementNo(self):
        return self.ElementNo

    def get_ProductType(self):
        return self.ProductType

    def get_TotalThickness(self):
        return self.TotalThickness

    def get_DoubleWallsGap(self):
        return self.DoubleWallsGap

    def get_PieceCount(self):
        return self.PieceCount

    def get_TurnWidth(self):
        return self.TurnWidth

    def get_Comment(self):
        return self.Comment

    def get_RotationPosition(self):
        return self.RotationPosition

    def get_StackNo(self):
        return self.StackNo

    def get_StackID(self):
        return self.StackID

    def get_StackingSequence(self):
        return self.StackingSequence

    def get_StackingLevel(self):
        return self.StackingLevel

    def get_StackingX(self):
        return self.StackingX

    def get_StackingY(self):
        return self.StackingY

    def get_StackingZ(self):
        return self.StackingZ

    def get_StackingAngle(self):
        return self.StackingAngle

    def get_StackingRotY(self):
        return self.StackingRotY

    def get_StackingRotX(self):
        return self.StackingRotX

    def get_P1X(self):
        return self.P1X

    def get_P1Y(self):
        return self.P1Y

    def get_P1Z(self):
        return self.P1Z

    def get_P2X(self):
        return self.P2X

    def get_P2Y(self):
        return self.P2Y

    def get_P2Z(self):
        return self.P2Z

    def get_P3X(self):
        return self.P3X

    def get_P3Y(self):
        return self.P3Y

    def get_P3Z(self):
        return self.P3Z

    def get_AdditionInfo(self):
        return self.AdditionInfo

    def get_UnloadingInfo(self):
        return self.UnloadingInfo

    def get_TransportInfo(self):
        return self.TransportInfo

    def get_ItemPosition(self):
        return self.ItemPosition

    def get_ElementInfo(self):
        return self.ElementInfo

    def get_Slab(self):
        return self.Slab

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_ElementNo(self, ElementNo: int):
        self.ElementNo = ElementNo

    def set_ProductType(self, ProductType: int):
        self.ProductType = ProductType

    def set_TotalThickness(self, TotalThickness: float):
        self.TotalThickness = TotalThickness

    def set_DoubleWallsGap(self, DoubleWallsGap: float):
        self.DoubleWallsGap = DoubleWallsGap

    def set_PieceCount(self, PieceCount: int):
        self.PieceCount = PieceCount

    def set_TurnWidth(self, TurnWidth: float):
        self.TurnWidth = TurnWidth

    def set_Comment(self, Comment: str):
        self.Comment = Comment

    def set_RotationPosition(self, RotationPosition: float):
        self.RotationPosition = RotationPosition

    def set_StackNo(self, StackNo: int):
        self.StackNo = StackNo

    def set_StackID(self, StackID: int):
        self.StackID = StackID

    def set_StackingSequence(self, StackingSequence: int):
        self.StackingSequence = StackingSequence

    def set_StackingLevel(self, StackingLevel: int):
        self.StackingLevel = StackingLevel

    def set_StackingX(self, StackingX: float):
        self.StackingX = StackingX

    def set_StackingY(self, StackingY: float):
        self.StackingY = StackingY

    def set_StackingZ(self, StackingZ: float):
        self.StackingZ = StackingZ

    def set_StackingAngle(self, StackingAngle: float):
        self.StackingAngle = StackingAngle

    def set_StackingRotY(self, StackingRotY: float):
        self.StackingRotY = StackingRotY

    def set_StackingRotX(self, StackingRotX: float):
        self.StackingRotX = StackingRotX

    def set_P1X(self, P1X: float):
        self.P1X = P1X

    def set_P1Y(self, P1Y: float):
        self.P1Y = P1Y

    def set_P1Z(self, P1Z: float):
        self.P1Z = P1Z

    def set_P2X(self, P2X: float):
        self.P2X = P2X

    def set_P2Y(self, P2Y: float):
        self.P2Y = P2Y

    def set_P2Z(self, P2Z: float):
        self.P2Z = P2Z

    def set_P3X(self, P3X: float):
        self.P3X = P3X

    def set_P3Y(self, P3Y: float):
        self.P3Y = P3Y

    def set_P3Z(self, P3Z: float):
        self.P3Z = P3Z

    def set_AdditionInfo(self, AdditionInfo: str):
        self.AdditionInfo = AdditionInfo

    def set_UnloadingInfo(self, UnloadingInfo: str):
        self.UnloadingInfo = UnloadingInfo

    def set_TransportInfo(self, TransportInfo: str):
        self.TransportInfo = TransportInfo

    def set_ItemPosition(self, ItemPosition: str):
        self.ItemPosition = ItemPosition

    def set_ElementInfo(self, ElementInfo: list):
        self.ElementInfo = ElementInfo

    def set_Slab(self, Slab: list):
        self.Slab = Slab

    def add_ElementInfo(self, ElementInfo):
        self.ElementInfo.append(ElementInfo)

    def add_Slab(self, Slab):
        self.Slab.append(Slab)

    def __str__(self):
        return str({
            "GlobalID": self.GlobalID,
            "ElementNo": self.ElementNo,
            "ProductType": self.ProductType,
            "TotalThickness": self.TotalThickness,
            "DoubleWallsGap": self.DoubleWallsGap,
            "PieceCount": self.PieceCount,
            "TurnWidth": self.TurnWidth,
            "Comment": self.Comment,
            "RotationPosition": self.RotationPosition,
            "StackNo": self.StackNo,
            "StackID": self.StackID,
            "StackingSequence": self.StackingSequence,
            "StackingLevel": self.StackingLevel,
            "StackingX": self.StackingX,
            "StackingY": self.StackingY,
            "StackingZ": self.StackingZ,
            "StackingAngle": self.StackingAngle,
            "StackingRotY": self.StackingRotY,
            "StackingRotX": self.StackingRotX,
            "P1X": self.P1X,
            "P1Y": self.P1Y,
            "P1Z": self.P1Z,
            "P2X": self.P2X,
            "P2Y": self.P2Y,
            "P2Z": self.P2Z,
            "P3X": self.P3X,
            "P3Y": self.P3Y,
            "P3Z": self.P3Z,
            "AdditionInfo": self.AdditionInfo,
            "UnloadingInfo": self.UnloadingInfo,
            "TransportInfo": self.TransportInfo,
            "ItemPosition": self.ItemPosition,
            "ElementInfo": self.ElementInfo,
            "Slab": self.Slab
        })

    def __xml__(self):
        Product = ET.Element("Product")
        Product.set("GlobalID", self.GlobalID)
        if self.ElementNo is not None:
            ElementNo = ET.SubElement(Product, "ElementNo")
            ElementNo.text = str(self.ElementNo)
        if self.ProductType is not None:
            ProductType = ET.SubElement(Product, "ProductType")
            ProductType.text = str(self.ProductType)
        if self.TotalThickness is not None:
            TotalThickness = ET.SubElement(Product, "TotalThickness")
            TotalThickness.text = str(float(self.TotalThickness))
        if self.DoubleWallsGap is not None:
            DoubleWallsGap = ET.SubElement(Product, "DoubleWallsGap")
            DoubleWallsGap.text = str(float(self.DoubleWallsGap))
        if self.PieceCount is not None:
            PieceCount = ET.SubElement(Product, "PieceCount")
            PieceCount.text = str(int(self.PieceCount))
        if self.TurnWidth is not None:
            TurnWidth = ET.SubElement(Product, "TurnWidth")
            TurnWidth.text = str(float(self.TurnWidth))
        if self.Comment is not None:
            Comment = ET.SubElement(Product, "Comment")
            Comment.text = self.Comment
        if self.RotationPosition is not None:
            RotationPosition = ET.SubElement(Product, "RotationPosition")
            RotationPosition.text = str(float(self.RotationPosition))
        if self.StackNo is not None:
            StackNo = ET.SubElement(Product, "StackNo")
            StackNo.text = str(self.StackNo)
        if self.StackID is not None:
            StackID = ET.SubElement(Product, "StackID")
            StackID.text = str(self.StackID)
        if self.StackingSequence is not None:
            StackingSequence = ET.SubElement(Product, "StackingSequence")
            StackingSequence.text = str(self.StackingSequence)
        if self.StackingLevel is not None:
            StackingLevel = ET.SubElement(Product, "StackingLevel")
            StackingLevel.text = str(self.StackingLevel)
        if self.StackingX is not None:
            StackingX = ET.SubElement(Product, "StackingX")
            StackingX.text = str(float(self.StackingX))
        if self.StackingY is not None:
            StackingY = ET.SubElement(Product, "StackingY")
            StackingY.text = str(float(self.StackingY))
        if self.StackingZ is not None:
            StackingZ = ET.SubElement(Product, "StackingZ")
            StackingZ.text = str(float(self.StackingZ))
        if self.StackingAngle is not None:
            StackingAngle = ET.SubElement(Product, "StackingAngle")
            StackingAngle.text = str(float(self.StackingAngle))
        if self.StackingRotY is not None:
            StackingRotY = ET.SubElement(Product, "StackingRotY")
            StackingRotY.text = str(float(self.StackingRotY))
        if self.StackingRotX is not None:
            StackingRotX = ET.SubElement(Product, "StackingRotX")
            StackingRotX.text = str(float(self.StackingRotX))
        if self.P1X is not None:
            P1X = ET.SubElement(Product, "P1X")
            P1X.text = str(float(self.P1X))
        if self.P1Y is not None:
            P1Y = ET.SubElement(Product, "P1Y")
            P1Y.text = str(float(self.P1Y))
        if self.P1Z is not None:
            P1Z = ET.SubElement(Product, "P1Z")
            P1Z.text = str(float(self.P1Z))
        if self.P2X is not None:
            P2X = ET.SubElement(Product, "P2X")
            P2X.text = str(float(self.P2X))
        if self.P2Y is not None:
            P2Y = ET.SubElement(Product, "P2Y")
            P2Y.text = str(float(self.P2Y))
        if self.P2Z is not None:
            P2Z = ET.SubElement(Product, "P2Z")
            P2Z.text = str(float(self.P2Z))
        if self.P3X is not None:
            P3X = ET.SubElement(Product, "P3X")
            P3X.text = str(float(self.P3X))
        if self.P3Y is not None:
            P3Y = ET.SubElement(Product, "P3Y")
            P3Y.text = str(float(self.P3Y))
        if self.P3Z is not None:
            P3Z = ET.SubElement(Product, "P3Z")
            P3Z.text = str(float(self.P3Z))
        if self.AdditionInfo is not None:
            AdditionInfo = ET.SubElement(Product, "AdditionInfo")
            AdditionInfo.text = self.AdditionInfo
        if self.UnloadingInfo is not None:
            UnloadingInfo = ET.SubElement(Product, "UnloadingInfo")
            UnloadingInfo.text = self.UnloadingInfo
        if self.TransportInfo is not None:
            TransportInfo = ET.SubElement(Product, "TransportInfo")
            TransportInfo.text = self.TransportInfo
        if self.ItemPosition is not None:
            ItemPosition = ET.SubElement(Product, "ItemPosition")
            ItemPosition.text = self.ItemPosition
        for ElementInfo in self.ElementInfo:
            Product.append(ElementInfo.__xml__())
        for Slab in self.Slab:
            Product.append(Slab.__xml__())
        return Product





