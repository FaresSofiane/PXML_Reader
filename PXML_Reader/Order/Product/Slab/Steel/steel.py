import xml.etree.ElementTree as ET


class Steel:
    GlobalID = None # STR // 0,1
    Type = None # STR // 0,1
    X = None # FLOAT // 0,1
    Y = None # FLOAT // 0,1
    Z = None # FLOAT // 0,1
    RotX = None # FLOAT // 0,1
    RotY = None # FLOAT // 0,1
    RotZ = None # FLOAT // 0,1
    ToTurn = False # BOOL // 0,1
    StopOnTurningSide = False # BOOL // 0,1
    Name = None # STR // 0,1
    GenericInfo01 = None # STR // 0,1
    GenericInfo02 = None # STR // 0,1
    GenericInfo03 = None # STR // 0,1
    GenericInfo04 = None # STR // 0,1
    GenericInfo05 = None # STR // 0,1
    GenericInfo06 = None # STR // 0,1
    MeshType = None # STR // 0,1
    WeldingDensity = None # INT // 0,1
    BorderStrength = None # INT // 0,1
    ProdX = None # FLOAT // 0,1
    ProdY = None # FLOAT // 0,1
    ProdZ = None # FLOAT // 0,1
    ProdRotX = None # FLOAT // 0,1
    ProdRotY = None # FLOAT // 0,1
    ProdRotZ = None # FLOAT // 0,1
    Layer = None # STR // 0,1
    ObjectID = None # STR // 0,1
    Bar = [] # Bar // n,n
    Girder = [] # Girder // n,n
    Alloc = [] # Alloc // n,n
    SteelExt = [] # SteelExt // n,n

    def __init__(self, GlobalID: str = None, Type: str = None, X: float = None, Y: float = None, Z: float = None, RotX: float = None, RotY: float = None, RotZ: float = None, ToTurn: bool = False, StopOnTurningSide: bool = False, Name: str = None, GenericInfo01: str = None, GenericInfo02: str = None, GenericInfo03: str = None, GenericInfo04: str = None, GenericInfo05: str = None, GenericInfo06: str = None, MeshType: str = None, WeldingDensity: int = None, BorderStrength: int = None, ProdX: float = None, ProdY: float = None, ProdZ: float = None, ProdRotX: float = None, ProdRotY: float = None, ProdRotZ: float = None, Layer: str = None, ObjectID: str = None, Bar: list = [], Girder: list = [], Alloc: list = [], SteelExt: list = []):
        self.GlobalID = GlobalID
        self.Type = Type
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

        if type(ToTurn) is bool:
            self.ToTurn = bool(ToTurn)
        else:
            if ToTurn in ["true","True","TRUE"]:
                self.ToTurn = True
            elif ToTurn in ["false","False","FALSE"]:
                self.ToTurn = False
            elif ToTurn is None:
                self.ToTurn = None
            else:
                try:
                    self.ToTurn = bool(ToTurn)
                except:
                    raise ValueError("ToTurn must be a boolean")
        if type(StopOnTurningSide) is bool:
            self.StopOnTurningSide = bool(StopOnTurningSide)
        else:
            if StopOnTurningSide in ["true","True","TRUE"]:
                self.StopOnTurningSide = True
            elif StopOnTurningSide in ["false","False","FALSE"]:
                self.StopOnTurningSide = False
            elif StopOnTurningSide is None:
                self.StopOnTurningSide = None
            else:
                try:
                    self.StopOnTurningSide = bool(StopOnTurningSide)
                except:
                    raise ValueError("StopOnTurningSide must be a boolean")
        self.Name = Name
        self.GenericInfo01 = GenericInfo01
        self.GenericInfo02 = GenericInfo02
        self.GenericInfo03 = GenericInfo03
        self.GenericInfo04 = GenericInfo04
        self.GenericInfo05 = GenericInfo05
        self.GenericInfo06 = GenericInfo06
        self.MeshType = MeshType
        if type(WeldingDensity) is int:
            self.WeldingDensity = int(WeldingDensity)
        else:
            if WeldingDensity is None:
                self.WeldingDensity = None
            else:
                try:
                    self.WeldingDensity = int(WeldingDensity)
                except ValueError:
                    raise ValueError(f'WeldingDensity must be an int')
        if type(BorderStrength) is int:
            self.BorderStrength = int(BorderStrength)
        else:
            if BorderStrength is None:
                self.BorderStrength = None
            else:
                try:
                    self.BorderStrength = int(BorderStrength)
                except ValueError:
                    raise ValueError(f'BorderStrength must be an int')
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

        self.Layer = Layer
        self.ObjectID = ObjectID
        self.Bar = Bar
        self.Girder = Girder
        self.Alloc = Alloc
        self.SteelExt = SteelExt

    def get_GlobalID(self):
        return self.GlobalID

    def get_Type(self):
        return self.Type

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

    def get_ToTurn(self):
        return self.ToTurn

    def get_StopOnTurningSide(self):
        return self.StopOnTurningSide

    def get_Name(self):
        return self.Name

    def get_GenericInfo01(self):
        return self.GenericInfo01

    def get_GenericInfo02(self):
        return self.GenericInfo02

    def get_GenericInfo03(self):
        return self.GenericInfo03

    def get_GenericInfo04(self):
        return self.GenericInfo04

    def get_GenericInfo05(self):
        return self.GenericInfo05

    def get_GenericInfo06(self):
        return self.GenericInfo06

    def get_MeshType(self):
        return self.MeshType

    def get_WeldingDensity(self):
        return self.WeldingDensity

    def get_BorderStrength(self):
        return self.BorderStrength

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

    def get_Layer(self):
        return self.Layer

    def get_ObjectID(self):
        return self.ObjectID

    def get_Bar(self):
        return self.Bar

    def get_Girder(self):
        return self.Girder

    def get_Alloc(self):
        return self.Alloc

    def get_SteelExt(self):
        return self.SteelExt

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_Type(self, Type: str):
        self.Type = Type

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

    def set_ToTurn(self, ToTurn: bool):
        self.ToTurn = ToTurn

    def set_StopOnTurningSide(self, StopOnTurningSide: bool):
        self.StopOnTurningSide = StopOnTurningSide

    def set_Name(self, Name: str):
        self.Name = Name

    def set_GenericInfo01(self, GenericInfo01: str):
        self.GenericInfo01 = GenericInfo01

    def set_GenericInfo02(self, GenericInfo02: str):
        self.GenericInfo02 = GenericInfo02

    def set_GenericInfo03(self, GenericInfo03: str):
        self.GenericInfo03 = GenericInfo03

    def set_GenericInfo04(self, GenericInfo04: str):
        self.GenericInfo04 = GenericInfo04

    def set_GenericInfo05(self, GenericInfo05: str):
        self.GenericInfo05 = GenericInfo05

    def set_GenericInfo06(self, GenericInfo06: str):
        self.GenericInfo06 = GenericInfo06

    def set_MeshType(self, MeshType: str):
        self.MeshType = MeshType

    def set_WeldingDensity(self, WeldingDensity: int):
        self.WeldingDensity = WeldingDensity

    def set_BorderStrength(self, BorderStrength: int):
        self.BorderStrength = BorderStrength

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

    def set_Layer(self, Layer: str):
        self.Layer = Layer

    def set_ObjectID(self, ObjectID: str):
        self.ObjectID = ObjectID

    def set_Bar(self, Bar: list):
        self.Bar = Bar

    def add_Bar(self, Bar):
        self.Bar.append(Bar)

    def set_Girder(self, Girder: list):
        self.Girder = Girder

    def add_Girder(self, Girder):
        self.Girder.append(Girder)

    def set_Alloc(self, Alloc: list):
        self.Alloc = Alloc

    def add_Alloc(self, Alloc):
        self.Alloc.append(Alloc)

    def set_SteelExt(self, SteelExt: list):
        self.SteelExt = SteelExt

    def add_SteelExt(self, SteelExt):
        self.SteelExt.append(SteelExt)

    def __str__(self):
        return "GlobalID: " + str(self.GlobalID) + ", Type: " + str(self.Type) + ", X: " + str(self.X) + ", Y: " + str(self.Y) + ", Z: " + str(self.Z) + ", RotX: " + str(self.RotX) + ", RotY: " + str(self.RotY) + ", RotZ: " + str(self.RotZ) + ", ToTurn: " + str(self.ToTurn) + ", StopOnTurningSide: " + str(self.StopOnTurningSide) + ", Name: " + str(self.Name) + ", GenericInfo01: " + str(self.GenericInfo01) + ", GenericInfo02: " + str(self.GenericInfo02) + ", GenericInfo03: " + str(self.GenericInfo03) + ", GenericInfo04: " + str(self.GenericInfo04) + ", GenericInfo05: " + str(self.GenericInfo05) + ", GenericInfo06: " + str(self.GenericInfo06) + ", MeshType: " + str(self.MeshType) + ", WeldingDensity: " + str(self.WeldingDensity) + ", BorderStrength: " + str(self.BorderStrength) + ", ProdX: " + str(self.ProdX) + ", ProdY: " + str(self.ProdY) + ", ProdZ: " + str(self.ProdZ) + ", ProdRotX: " + str(self.ProdRotX) + ", ProdRotY: " + str(self.ProdRotY) + ", ProdRotZ: " + str(self.ProdRotZ) + ", Layer: " + str(self.Layer) + ", ObjectID: " + str(self.ObjectID) + ", Bar: " + str(self.Bar) + ", Girder: " + str(self.Girder) + ", Alloc: " + str(self.Alloc) + ", SteelExt: " + str(self.SteelExt)

    def __xml__(self):
        Steel = ET.Element("Steel")
        if self.GlobalID is not None:
            Steel.set("GlobalID",self.GlobalID)
        if self.Type is not None:
            Steel.set("Type",self.Type)
        if self.X is not None:
            X = ET.SubElement(Steel,"X")
            X.text = str(self.X)
        if self.Y is not None:
            Y = ET.SubElement(Steel,"Y")
            Y.text = str(self.Y)
        if self.Z is not None:
            Z = ET.SubElement(Steel,"Z")
            Z.text = str(self.Z)
        if self.RotX is not None:
            RotX = ET.SubElement(Steel,"RotX")
            RotX.text = str(self.RotX)
        if self.RotY is not None:
            RotY = ET.SubElement(Steel,"RotY")
            RotY.text = str(self.RotY)
        if self.RotZ is not None:
            RotZ = ET.SubElement(Steel,"RotZ")
            RotZ.text = str(self.RotZ)
        if self.ToTurn is not None:
            ToTurn = ET.SubElement(Steel,"ToTurn")
            ToTurn.text = str(self.ToTurn)
        if self.StopOnTurningSide is not None:
            StopOnTurningSide = ET.SubElement(Steel,"StopOnTurningSide")
            StopOnTurningSide.text = str(self.StopOnTurningSide)
        if self.Name is not None:
            Name = ET.SubElement(Steel,"Name")
            Name.text = str(self.Name)
        if self.GenericInfo01 is not None:
            GenericInfo01 = ET.SubElement(Steel,"GenericInfo01")
            GenericInfo01.text = str(self.GenericInfo01)
        if self.GenericInfo02 is not None:
            GenericInfo02 = ET.SubElement(Steel,"GenericInfo02")
            GenericInfo02.text = str(self.GenericInfo02)
        if self.GenericInfo03 is not None:
            GenericInfo03 = ET.SubElement(Steel,"GenericInfo03")
            GenericInfo03.text = str(self.GenericInfo03)
        if self.GenericInfo04 is not None:
            GenericInfo04 = ET.SubElement(Steel,"GenericInfo04")
            GenericInfo04.text = str(self.GenericInfo04)
        if self.GenericInfo05 is not None:
            GenericInfo05 = ET.SubElement(Steel,"GenericInfo05")
            GenericInfo05.text = str(self.GenericInfo05)
        if self.GenericInfo06 is not None:
            GenericInfo06 = ET.SubElement(Steel,"GenericInfo06")
            GenericInfo06.text = str(self.GenericInfo06)
        if self.MeshType is not None:
            MeshType = ET.SubElement(Steel,"MeshType")
            MeshType.text = str(self.MeshType)
        if self.WeldingDensity is not None:
            WeldingDensity = ET.SubElement(Steel,"WeldingDensity")
            WeldingDensity.text = str(self.WeldingDensity)
        if self.BorderStrength is not None:
            BorderStrength = ET.SubElement(Steel,"BorderStrength")
            BorderStrength.text = str(self.BorderStrength)
        if self.ProdX is not None:
            ProdX = ET.SubElement(Steel,"ProdX")
            ProdX.text = str(self.ProdX)
        if self.ProdY is not None:
            ProdY = ET.SubElement(Steel,"ProdY")
            ProdY.text = str(self.ProdY)
        if self.ProdZ is not None:
            ProdZ = ET.SubElement(Steel,"ProdZ")
            ProdZ.text = str(self.ProdZ)
        if self.ProdRotX is not None:
            ProdRotX = ET.SubElement(Steel,"ProdRotX")
            ProdRotX.text = str(self.ProdRotX)
        if self.ProdRotY is not None:
            ProdRotY = ET.SubElement(Steel,"ProdRotY")
            ProdRotY.text = str(self.ProdRotY)
        if self.ProdRotZ is not None:
            ProdRotZ = ET.SubElement(Steel,"ProdRotZ")
            ProdRotZ.text = str(self.ProdRotZ)
        if self.Layer is not None:
            Layer = ET.SubElement(Steel,"Layer")
            Layer.text = str(self.Layer)
        if self.ObjectID is not None:
            ObjectID = ET.SubElement(Steel,"ObjectID")
            ObjectID.text = str(self.ObjectID)
        for Bar in self.Bar:
            Steel.append(Bar.__xml__())
        for Girder in self.Girder:
            Steel.append(Girder.__xml__())
        for Alloc in self.Alloc:
            Steel.append(Alloc.__xml__())
        for SteelExt in self.SteelExt:
            Steel.append(SteelExt.__xml__())
        return Steel

