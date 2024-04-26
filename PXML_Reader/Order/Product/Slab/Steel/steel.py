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

