import xml.etree.ElementTree as ET


class Slab():


    def __init__(self, GlobalID: str = None, SlabNo: str = None, PartType: str = None, ProductionAddition: str = None,
                 ProductionWay: str = None, NumberOfMeansOfTransport: str = None, TransportSequence: str = None,
                 PileLevel: str = None, TypeOfUnloading: str = None, MeanOfTransport: str = None,
                 ExpositionClass: str = None, SlabArea: float = None, SlabWeight: float = None,
                 ProductionThickness: float = None, MaxLength: float = None, MaxWidth: float = None,
                 IronProjectionLeft: float = None, IronProjectionRight: float = None,
                 IronProjectionBottom: float = None, IronProjectionTop: float = None, X: float = None, Y: float = None,
                 Z: float = None, RotX: float = None, RotY: float = None, RotZ: float = None, ProdX: float = None,
                 ProdY: float = None, ProdZ: float = None, ProdRotX: float = None, ProdRotY: float = None,
                 ProdRotZ: float = None, OrderPosition: str = None, ProductGroup: str = None, SlabType: str = None,
                 ItemDesignation: str = None, ProjectCoordinates: str = None, PositionInPileX: float = None,
                 PositionInPileY: float = None, PositionInPileZ: float = None, AngleInPile: float = None,
                 GenericInfo01: str = None, GenericInfo02: str = None, GenericInfo03: str = None,
                 GenericInfo04: str = None, ReforcemInfo: str = None, Outline: list = [], Steel: list = []):
        self.GlobalID = None  # STR // 0,1
        self.SlabNo = None  # STR // 0,1
        self.PartType = None  # STR // 0,1
        self.ProductionAddition = None  # STR // 0,1
        self.ProductionWay = None  # STR // 0,1
        self.NumberOfMeansOfTransport = None  # STR // 0,1
        self.TransportSequence = None  # STR // 0,1
        self.PileLevel = None  # STR // 0,1
        self.TypeOfUnloading = None  # STR // 0,1
        self.MeanOfTransport = None  # STR // 0,1
        self.ExpositionClass = None  # STR // 0,1
        self.SlabArea = None  # FLOAT // 0,1
        self.SlabWeight = None  # FLOAT // 0,1
        self.ProductionThickness = None  # FLOAT // 0,1
        self.MaxLength = None  # FLOAT // 0,1
        self.MaxWidth = None  # FLOAT // 0,1
        self.IronProjectionLeft = None  # FLOAT // 0,1
        self.IronProjectionRight = None  # FLOAT // 0,1
        self.IronProjectionBottom = None  # FLOAT // 0,1
        self.IronProjectionTop = None  # FLOAT // 0,1
        self.X = None  # FLOAT // 0,1
        self.Y = None  # FLOAT // 0,1
        self.Z = None  # FLOAT // 0,1
        self.RotX = None  # FLOAT // 0,1
        self.RotY = None  # FLOAT // 0,1
        self.RotZ = None  # FLOAT // 0,1
        self.ProdX = None  # FLOAT // 0,1
        self.ProdY = None  # FLOAT // 0,1
        self.ProdZ = None  # FLOAT // 0,1
        self.ProdRotX = None  # FLOAT // 0,1
        self.ProdRotY = None  # FLOAT // 0,1
        self.ProdRotZ = None  # FLOAT // 0,1
        self.OrderPosition = None  # STR // 0,1
        self.ProductGroup = None  # STR // 0,1
        self.SlabType = None  # STR // 0,1
        self.ItemDesignation = None  # STR // 0,1
        self.ProjectCoordinates = None  # STR // 0,1
        self.PositionInPileX = None  # FLOAT // 0,1
        self.PositionInPileY = None  # FLOAT // 0,1
        self.PositionInPileZ = None  # FLOAT // 0,1
        self.AngleInPile = None  # FLOAT // 0,1
        self.GenericInfo01 = None  # STR // 0,1
        self.GenericInfo02 = None  # STR // 0,1
        self.GenericInfo03 = None  # STR // 0,1
        self.GenericInfo04 = None  # STR // 0,1
        self.ReforcemInfo = None  # STR // 0,1
        self.Outline = []
        self.Steel = []  # Steel // n,n
        self.GlobalID = GlobalID
        self.SlabNo = SlabNo
        self.PartType = PartType
        self.ProductionAddition = ProductionAddition
        self.ProductionWay = ProductionWay
        self.NumberOfMeansOfTransport = NumberOfMeansOfTransport
        self.TransportSequence = TransportSequence
        self.PileLevel = PileLevel
        self.TypeOfUnloading = TypeOfUnloading
        self.MeanOfTransport = MeanOfTransport
        self.ExpositionClass = ExpositionClass
        if type(SlabArea) is float:
            self.SlabArea = float(SlabArea)
        else:
            if SlabArea is None:
                self.SlabArea = None
            else:
                try:
                    self.SlabArea = float(SlabArea)
                except ValueError:
                    raise ValueError(f'SlabArea must be a float')
        if type(SlabWeight) is float:
            self.SlabWeight = float(SlabWeight)
        else:
            if SlabWeight is None:
                self.SlabWeight = None
            else:
                try:
                    self.SlabWeight = float(SlabWeight)
                except ValueError:
                    raise ValueError(f'SlabWeight must be a float')
        if type(ProductionThickness) is float:
            self.ProductionThickness = ProductionThickness
        else:
            if ProductionThickness is None:
                self.ProductionThickness = None
            else:
                try:
                    self.ProductionThickness = float(ProductionThickness)
                except ValueError:
                    raise ValueError(f'ProductionThickness must be a float')
        if type(MaxLength) is float:
            self.MaxLength = float(MaxLength)
        else:
            if MaxLength is None:
                self.MaxLength = None
            else:
                try:
                    self.MaxLength = float(MaxLength)
                except ValueError:
                    raise ValueError(f'MaxLength must be a float')
        if type(MaxWidth) is float:
            self.MaxWidth = float(MaxWidth)
        else:
            if MaxWidth is None:
                self.MaxWidth = None
            else:
                try:
                    self.MaxWidth = float(MaxWidth)
                except ValueError:
                    raise ValueError(f'MaxWidth must be a float')
        if type(IronProjectionLeft) is float:
            self.IronProjectionLeft = float(IronProjectionLeft)
        else:
            if IronProjectionLeft is None:
                self.IronProjectionLeft = None
            else:
                try:
                    self.IronProjectionLeft = float(IronProjectionLeft)
                except ValueError:
                    raise ValueError(f'IronProjectionLeft must be a float')
        if type(IronProjectionRight) is float:
            self.IronProjectionRight = float(IronProjectionRight)
        else:
            if IronProjectionRight is None:
                self.IronProjectionRight = None
            else:
                try:
                    self.IronProjectionRight = float(IronProjectionRight)
                except ValueError:
                    raise ValueError(f'IronProjectionRight must be a float')
        if type(IronProjectionBottom) is float:
            self.IronProjectionBottom = float(IronProjectionBottom)
        else:
            if IronProjectionBottom is None:
                self.IronProjectionBottom = None
            else:
                try:
                    self.IronProjectionBottom = float(IronProjectionBottom)
                except ValueError:
                    raise ValueError(f'IronProjectionBottom must be a float')
        if type(IronProjectionTop) is float:
            self.IronProjectionTop = float(IronProjectionTop)
        else:
            if IronProjectionTop is None:
                self.IronProjectionTop = None
            else:
                try:
                    self.IronProjectionTop = float(IronProjectionTop)
                except ValueError:
                    raise ValueError(f'IronProjectionTop must be a float')
        if type(X) is float:
            self.X = float(X)
        else:
            if X is None:
                self.X = None
            else:
                try:
                    self.X = float(X)
                except ValueError:
                    raise ValueError(f'X must be a float')
        if type(Y) is float:
            self.Y = float(Y)
        else:
            if Y is None:
                self.Y = None
            else:
                try:
                    self.Y = float(Y)
                except ValueError:
                    raise ValueError(f'Y must be a float')
        if type(Z) is float:
            self.Z = float(Z)
        else:
            if Z is None:
                self.Z = None
            else:
                try:
                    self.Z = float(Z)
                except ValueError:
                    raise ValueError(f'Z must be a float')
        if type(RotX) is float:
            self.RotX = float(RotX)
        else:
            if RotX is None:
                self.RotX = None
            else:
                try:
                    self.RotX = float(RotX)
                except ValueError:
                    raise ValueError(f'RotX must be a float')
        if type(RotY) is float:
            self.RotY = float(RotY)
        else:
            if RotY is None:
                self.RotY = None
            else:
                try:
                    self.RotY = float(RotY)
                except ValueError:
                    raise ValueError(f'RotY must be a float')
        if type(RotZ) is float:
            self.RotZ = float(RotZ)
        else:
            if RotZ is None:
                self.RotZ = None
            else:
                try:
                    self.RotZ = float(RotZ)
                except ValueError:
                    raise ValueError(f'RotZ must be a float')
        if type(ProdX) is float:
            self.ProdX = float(ProdX)
        else:
            if ProdX is None:
                self.ProdX = None
            else:
                try:
                    self.ProdX = float(ProdX)
                except ValueError:
                    raise ValueError(f'ProdX must be a float')
        if type(ProdY) is float:
            self.ProdY = float(ProdY)
        else:
            if ProdY is None:
                self.ProdY = None
            else:
                try:
                    self.ProdY = float(ProdY)
                except ValueError:
                    raise ValueError(f'ProdY must be a float')
        if type(ProdZ) is float:
            self.ProdZ = float(ProdZ)
        else:
            if ProdZ is None:
                self.ProdZ = None
            else:
                try:
                    self.ProdZ = float(ProdZ)
                except ValueError:
                    raise ValueError(f'ProdZ must be a float')
        if type(ProdRotX) is float:
            self.ProdRotX = float(ProdRotX)
        else:
            if ProdRotX is None:
                self.ProdRotX = None
            else:
                try:
                    self.ProdRotX = float(ProdRotX)
                except ValueError:
                    raise ValueError(f'ProdRotX must be a float')
        if type(ProdRotY) is float:
            self.ProdRotY = float(ProdRotY)
        else:
            if ProdRotY is None:
                self.ProdRotY = None
            else:
                try:
                    self.ProdRotY = float(ProdRotY)
                except ValueError:
                    raise ValueError(f'ProdRotY must be a float')
        if type(ProdRotZ) is float:
            self.ProdRotZ = float(ProdRotZ)
        else:
            if ProdRotZ is None:
                self.ProdRotZ = None
            else:
                try:
                    self.ProdRotZ = float(ProdRotZ)
                except ValueError:
                    raise ValueError(f'ProdRotZ must be a float')
        self.OrderPosition = OrderPosition
        self.ProductGroup = ProductGroup
        self.SlabType = SlabType
        self.ItemDesignation = ItemDesignation
        self.ProjectCoordinates = ProjectCoordinates
        if type(PositionInPileX) is float:
            self.PositionInPileX = float(PositionInPileX)
        else:
            if PositionInPileX is None:
                self.PositionInPileX = None
            else:
                try:
                    self.PositionInPileX = float(PositionInPileX)
                except ValueError:
                    raise ValueError(f'PositionInPileX must be a float')
        if type(PositionInPileY) is float:
            self.PositionInPileY = float(PositionInPileY)
        else:
            if PositionInPileY is None:
                self.PositionInPileY = None
            else:
                try:
                    self.PositionInPileY = float(PositionInPileY)
                except ValueError:
                    raise ValueError(f'PositionInPileY must be a float')
        if type(PositionInPileZ) is float:
            self.PositionInPileZ = float(PositionInPileZ)
        else:
            if PositionInPileZ is None:
                self.PositionInPileZ = None
            else:
                try:
                    self.PositionInPileZ = float(PositionInPileZ)
                except ValueError:
                    raise ValueError(f'PositionInPileZ must be a float')
        if type(AngleInPile) is float:
            self.AngleInPile = float(AngleInPile)
        else:
            if AngleInPile is None:
                self.AngleInPile = None
            else:
                try:
                    self.AngleInPile = float(AngleInPile)
                except ValueError:
                    raise ValueError(f'AngleInPile must be a float')
        self.GenericInfo01 = GenericInfo01
        self.GenericInfo02 = GenericInfo02
        self.GenericInfo03 = GenericInfo03
        self.GenericInfo04 = GenericInfo04
        self.ReforcemInfo = ReforcemInfo
        self.Outline = Outline
        self.Steel = Steel

    def get_GlobalID(self):
        return self.GlobalID

    def get_SlabNo(self):
        return self.SlabNo

    def get_PartType(self):
        return self.PartType

    def get_ProductionAddition(self):
        return self.ProductionAddition

    def get_ProductionWay(self):
        return self.ProductionWay

    def get_NumberOfMeansOfTransport(self):
        return self.NumberOfMeansOfTransport

    def get_TransportSequence(self):
        return self.TransportSequence

    def get_PileLevel(self):
        return self.PileLevel

    def get_TypeOfUnloading(self):
        return self.TypeOfUnloading

    def get_MeanOfTransport(self):
        return self.MeanOfTransport

    def get_ExpositionClass(self):
        return self.ExpositionClass

    def get_SlabArea(self):
        return self.SlabArea

    def get_SlabWeight(self):
        return self.SlabWeight

    def get_ProductionThickness(self):
        return self.ProductionThickness

    def get_MaxLength(self):
        return self.MaxLength

    def get_MaxWidth(self):
        return self.MaxWidth

    def get_IronProjectionLeft(self):
        return self.IronProjectionLeft

    def get_IronProjectionRight(self):
        return self.IronProjectionRight

    def get_IronProjectionBottom(self):
        return self.IronProjectionBottom

    def get_IronProjectionTop(self):
        return self.IronProjectionTop

    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y

    def get_Z(self):
        return self.Z

    def get_RotX(self):
        return self.RotX

    def get_RotY(self):
        return self.RotY

    def get_RotZ(self):
        return self.RotZ

    def get_ProdX(self):
        return self.ProdX

    def get_ProdY(self):
        return self.ProdY

    def get_ProdZ(self):
        return self.ProdZ

    def get_ProdRotX(self):
        return self.ProdRotX

    def get_ProdRotY(self):
        return self.ProdRotY

    def get_ProdRotZ(self):
        return self.ProdRotZ

    def get_OrderPosition(self):
        return self.OrderPosition

    def get_ProductGroup(self):
        return self.ProductGroup

    def get_SlabType(self):
        return self.SlabType

    def get_ItemDesignation(self):
        return self.ItemDesignation

    def get_ProjectCoordinates(self):
        return self.ProjectCoordinates

    def get_PositionInPileX(self):
        return self.PositionInPileX

    def get_PositionInPileY(self):
        return self.PositionInPileY

    def get_PositionInPileZ(self):
        return self.PositionInPileZ

    def get_AngleInPile(self):
        return self.AngleInPile

    def get_GenericInfo01(self):
        return self.GenericInfo01

    def get_GenericInfo02(self):
        return self.GenericInfo02

    def get_GenericInfo03(self):
        return self.GenericInfo03

    def get_GenericInfo04(self):
        return self.GenericInfo04

    def get_ReforcemInfo(self):
        return self.ReforcemInfo

    def get_Outline(self):
        return self.Outline

    def get_Steel(self):
        return self.Steel

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_SlabNo(self, SlabNo: str):
        self.SlabNo = SlabNo

    def set_PartType(self, PartType: str):
        self.PartType = PartType

    def set_ProductionAddition(self, ProductionAddition: str):
        self.ProductionAddition = ProductionAddition

    def set_ProductionWay(self, ProductionWay: str):
        self.ProductionWay = ProductionWay

    def set_NumberOfMeansOfTransport(self, NumberOfMeansOfTransport: str):
        self.NumberOfMeansOfTransport = NumberOfMeansOfTransport

    def set_TransportSequence(self, TransportSequence: str):
        self.TransportSequence = TransportSequence

    def set_PileLevel(self, PileLevel: str):
        self.PileLevel = PileLevel

    def set_TypeOfUnloading(self, TypeOfUnloading: str):
        self.TypeOfUnloading = TypeOfUnloading

    def set_MeanOfTransport(self, MeanOfTransport: str):
        self.MeanOfTransport = MeanOfTransport

    def set_ExpositionClass(self, ExpositionClass: str):
        self.ExpositionClass = ExpositionClass

    def set_SlabArea(self, SlabArea: float):
        self.SlabArea = SlabArea

    def set_SlabWeight(self, SlabWeight: float):
        self.SlabWeight = SlabWeight

    def set_ProductionThickness(self, ProductionThickness: float):
        self.ProductionThickness = ProductionThickness

    def set_MaxLength(self, MaxLength: float):
        self.MaxLength = MaxLength

    def set_MaxWidth(self, MaxWidth: float):
        self.MaxWidth = MaxWidth

    def set_IronProjectionLeft(self, IronProjectionLeft: float):
        self.IronProjectionLeft = IronProjectionLeft

    def set_IronProjectionRight(self, IronProjectionRight: float):
        self.IronProjectionRight = IronProjectionRight

    def set_IronProjectionBottom(self, IronProjectionBottom: float):
        self.IronProjectionBottom = IronProjectionBottom

    def set_IronProjectionTop(self, IronProjectionTop: float):
        self.IronProjectionTop = IronProjectionTop

    def set_X(self, X: float):
        self.X = X

    def set_Y(self, Y: float):
        self.Y = Y

    def set_Z(self, Z: float):
        self.Z = Z

    def set_RotX(self, RotX: float):
        self.RotX = RotX

    def set_RotY(self, RotY: float):
        self.RotY = RotY

    def set_RotZ(self, RotZ: float):
        self.RotZ = RotZ

    def set_ProdX(self, ProdX: float):
        self.ProdX = ProdX

    def set_ProdY(self, ProdY: float):
        self.ProdY = ProdY

    def set_ProdZ(self, ProdZ: float):
        self.ProdZ = ProdZ

    def set_ProdRotX(self, ProdRotX: float):
        self.ProdRotX = ProdRotX

    def set_ProdRotY(self, ProdRotY: float):
        self.ProdRotY = ProdRotY

    def set_ProdRotZ(self, ProdRotZ: float):
        self.ProdRotZ = ProdRotZ

    def set_OrderPosition(self, OrderPosition: str):
        self.OrderPosition = OrderPosition

    def set_ProductGroup(self, ProductGroup: str):
        self.ProductGroup = ProductGroup

    def set_SlabType(self, SlabType: str):
        self.SlabType = SlabType

    def set_ItemDesignation(self, ItemDesignation: str):
        self.ItemDesignation = ItemDesignation

    def set_ProjectCoordinates(self, ProjectCoordinates: str):
        self.ProjectCoordinates = ProjectCoordinates

    def set_PositionInPileX(self, PositionInPileX: float):
        self.PositionInPileX = PositionInPileX

    def set_PositionInPileY(self, PositionInPileY: float):
        self.PositionInPileY = PositionInPileY

    def set_PositionInPileZ(self, PositionInPileZ: float):
        self.PositionInPileZ = PositionInPileZ

    def set_AngleInPile(self, AngleInPile: float):
        self.AngleInPile = AngleInPile

    def set_GenericInfo01(self, GenericInfo01: str):
        self.GenericInfo01 = GenericInfo01

    def set_GenericInfo02(self, GenericInfo02: str):
        self.GenericInfo02 = GenericInfo02

    def set_GenericInfo03(self, GenericInfo03: str):
        self.GenericInfo03 = GenericInfo03

    def set_GenericInfo04(self, GenericInfo04: str):
        self.GenericInfo04 = GenericInfo04

    def set_ReforcemInfo(self, ReforcemInfo: str):
        self.ReforcemInfo = ReforcemInfo

    def set_Outline(self, Outline: list):
        self.Outline = Outline

    def set_Steel(self, Steel: list):
        self.Steel = Steel

    def add_Outline(self, Outline):
        self.Outline.append(Outline)

    def add_Steel(self, Steel):
        self.Steel.append(Steel)

    def __str__(self):
        return f'{self.GlobalID} {self.SlabNo} {self.PartType} {self.ProductionAddition} {self.ProductionWay} {self.NumberOfMeansOfTransport} {self.TransportSequence} {self.PileLevel} {self.TypeOfUnloading} {self.MeanOfTransport} {self.ExpositionClass} {self.SlabArea} {self.SlabWeight} {self.ProductionThickness} {self.MaxLength} {self.MaxWidth} {self.IronProjectionLeft} {self.IronProjectionRight} {self.IronProjectionBottom} {self.IronProjectionTop} {self.X} {self.Y} {self.Z} {self.RotX} {self.RotY} {self.RotZ} {self.ProdX} {self.ProdY} {self.ProdZ} {self.ProdRotX} {self.ProdRotY} {self.ProdRotZ} {self.OrderPosition} {self.ProductGroup} {self.SlabType} {self.ItemDesignation} {self.ProjectCoordinates} {self.PositionInPileX} {self.PositionInPileY} {self.PositionInPileZ} {self.AngleInPile} {self.GenericInfo01} {self.GenericInfo02} {self.GenericInfo03} {self.GenericInfo04} {self.ReforcemInfo} {self.Outline} {self.Steel}'

    def __xml__(self):
        Slab = ET.Element('Slab')
        if self.GlobalID is not None:
            Slab.set('GlobalID', self.GlobalID)

        if self.SlabNo is not None:
            SlabNo = ET.SubElement(Slab, "SlabNo")
            SlabNo.text = self.SlabNo
        if self.PartType is not None:
            PartType = ET.SubElement(Slab, "PartType")
            PartType.text = self.PartType

        if self.ProductionAddition is not None:
            ProductionAddition = ET.SubElement(Slab, "ProductionAddition")
            ProductionAddition.text = self.ProductionAddition
        if self.ProductionWay is not None:
            ProductionWay = ET.SubElement(Slab, "ProductionWay")
            ProductionWay.text = self.ProductionWay
        if self.NumberOfMeansOfTransport is not None:
            NumberOfMeansOfTransport = ET.SubElement(Slab, "NumberOfMeansOfTransport")
            NumberOfMeansOfTransport.text = self.NumberOfMeansOfTransport
        if self.TransportSequence is not None:
            TransportSequence = ET.SubElement(Slab, "TransportSequence")
            TransportSequence.text = self.TransportSequence
        if self.PileLevel is not None:
            PileLevel = ET.SubElement(Slab, "PileLevel")
            PileLevel.text = self.PileLevel
        if self.TypeOfUnloading is not None:
            TypeOfUnloading = ET.SubElement(Slab, "TypeOfUnloading")
            TypeOfUnloading.text = self.TypeOfUnloading
        if self.MeanOfTransport is not None:
            MeanOfTransport = ET.SubElement(Slab, "MeanOfTransport")
            MeanOfTransport.text = self.MeanOfTransport
        if self.ExpositionClass is not None:
            ExpositionClass = ET.SubElement(Slab, "ExpositionClass")
            ExpositionClass.text = self.ExpositionClass
        if self.SlabArea is not None:
            SlabArea = ET.SubElement(Slab, "SlabArea")
            SlabArea.text = str(self.SlabArea)
        if self.SlabWeight is not None:
            SlabWeight = ET.SubElement(Slab, "SlabWeight")
            SlabWeight.text = str(self.SlabWeight)
        if self.ProductionThickness is not None:
            ProductionThickness = ET.SubElement(Slab, "ProductionThickness")
            ProductionThickness.text = str(self.ProductionThickness)
        if self.MaxLength is not None:
            MaxLength = ET.SubElement(Slab, "MaxLength")
            MaxLength.text = str(self.MaxLength)
        if self.MaxWidth is not None:
            MaxWidth = ET.SubElement(Slab, "MaxWidth")
            MaxWidth.text = str(self.MaxWidth)
        if self.IronProjectionLeft is not None:
            IronProjectionLeft = ET.SubElement(Slab, "IronProjectionLeft")
            IronProjectionLeft.text = str(self.IronProjectionLeft)
        if self.IronProjectionRight is not None:
            IronProjectionRight = ET.SubElement(Slab, "IronProjectionRight")
            IronProjectionRight.text = str(self.IronProjectionRight)
        if self.IronProjectionBottom is not None:
            IronProjectionBottom = ET.SubElement(Slab, "IronProjectionBottom")
            IronProjectionBottom.text = str(self.IronProjectionBottom)
        if self.IronProjectionTop is not None:
            IronProjectionTop = ET.SubElement(Slab, "IronProjectionTop")
            IronProjectionTop.text = str(self.IronProjectionTop)
        if self.X is not None:
            X = ET.SubElement(Slab, "X")
            X.text = str(self.X)
        if self.Y is not None:
            Y = ET.SubElement(Slab, "Y")
            Y.text = str(self.Y)
        if self.Z is not None:
            Z = ET.SubElement(Slab, "Z")
            Z.text = str(self.Z)
        if self.RotX is not None:
            RotX = ET.SubElement(Slab, "RotX")
            RotX.text = str(self.RotX)
        if self.RotY is not None:
            RotY = ET.SubElement(Slab, "RotY")
            RotY.text = str(self.RotY)
        if self.RotZ is not None:
            RotZ = ET.SubElement(Slab, "RotZ")
            RotZ.text = str(self.RotZ)
        if self.ProdX is not None:
            ProdX = ET.SubElement(Slab, "ProdX")
            ProdX.text = str(self.ProdX)
        if self.ProdY is not None:
            ProdY = ET.SubElement(Slab, "ProdY")
            ProdY.text = str(self.ProdY)
        if self.ProdZ is not None:
            ProdZ = ET.SubElement(Slab, "ProdZ")
            ProdZ.text = str(self.ProdZ)
        if self.ProdRotX is not None:
            ProdRotX = ET.SubElement(Slab, "ProdRotX")
            ProdRotX.text = str(self.ProdRotX)
        if self.ProdRotY is not None:
            ProdRotY = ET.SubElement(Slab, "ProdRotY")
            ProdRotY.text = str(self.ProdRotY)
        if self.ProdRotZ is not None:
            ProdRotZ = ET.SubElement(Slab, "ProdRotZ")
            ProdRotZ.text = str(self.ProdRotZ)
        if self.OrderPosition is not None:
            OrderPosition = ET.SubElement(Slab, "OrderPosition")
            OrderPosition.text = self.OrderPosition
        if self.ProductGroup is not None:
            ProductGroup = ET.SubElement(Slab, "ProductGroup")
            ProductGroup.text = self.ProductGroup
        if self.SlabType is not None:
            SlabType = ET.SubElement(Slab, "SlabType")
            SlabType.text = self.SlabType
        if self.ItemDesignation is not None:
            ItemDesignation = ET.SubElement(Slab, "ItemDesignation")
            ItemDesignation.text = self.ItemDesignation
        if self.ProjectCoordinates is not None:
            ProjectCoordinates = ET.SubElement(Slab, "ProjectCoordinates")
            ProjectCoordinates.text = self.ProjectCoordinates
        if self.PositionInPileX is not None:
            PositionInPileX = ET.SubElement(Slab, "PositionInPileX")
            PositionInPileX.text = str(self.PositionInPileX)
        if self.PositionInPileY is not None:
            PositionInPileY = ET.SubElement(Slab, "PositionInPileY")
            PositionInPileY.text = str(self.PositionInPileY)
        if self.PositionInPileZ is not None:
            PositionInPileZ = ET.SubElement(Slab, "PositionInPileZ")
            PositionInPileZ.text = str(self.PositionInPileZ)
        if self.AngleInPile is not None:
            AngleInPile = ET.SubElement(Slab, "AngleInPile")
            AngleInPile.text = str(self.AngleInPile)
        if self.GenericInfo01 is not None:
            GenericInfo01 = ET.SubElement(Slab, "GenericInfo01")
            GenericInfo01.text = self.GenericInfo01
        if self.GenericInfo02 is not None:
            GenericInfo02 = ET.SubElement(Slab, "GenericInfo02")
            GenericInfo02.text = self.GenericInfo02
        if self.GenericInfo03 is not None:
            GenericInfo03 = ET.SubElement(Slab, "GenericInfo03")
            GenericInfo03.text = self.GenericInfo03
        if self.GenericInfo04 is not None:
            GenericInfo04 = ET.SubElement(Slab, "GenericInfo04")
            GenericInfo04.text = self.GenericInfo04
        if self.ReforcemInfo is not None:
            ReforcemInfo = ET.SubElement(Slab, "ReforcemInfo")
            ReforcemInfo.text = self.ReforcemInfo

        for Outline in self.Outline:
            Slab.append(Outline.__xml__())

        for Steel in self.Steel:
            Slab.append(Steel.__xml__())


        return Slab
