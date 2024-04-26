from .Spacer.spacer import Spacer
from .WeldingPoint.weldingpoint import WeldingPoint
from .Segment.segment import Segment

class Bar:
    GlobalID = None # STR // 0,1
    ReinforcementType = None # STR // 0,1
    SteelQuality = None # STR // 0,1
    PieceCount = None # INT // 0,1
    Diameter = None # FLOAT // 0,1
    X = None # FLOAT // 0,1
    Y = None # FLOAT // 0,1
    Z = None # FLOAT // 0,1
    RotZ = None # FLOAT // 0,1
    ArticleNo = None # STR // 0,1
    NoAutoProd = False # BOOL // 0,1
    ExtIronWeight = None # FLOAT // 0,1
    Bin = None # STR // 0,1
    Pos = None # STR // 0,1
    Note = None # STR // 0,1
    Machine = None # STR // 0,1
    BendingDevice = None # STR // 0,1
    Spacer = [] # Spacer // n,n
    WeldingPoint = [] # WeldingPoint // n,n
    Segment = [] # Segment // n,n

    def __init__(self, GlobalID: str = None, ReinforcementType: str = None, SteelQuality: str = None, PieceCount: int = None, Diameter: float = None, X: float = None, Y: float = None, Z: float = None, RotZ: float = None, ArticleNo: str = None, NoAutoProd: bool = False, ExtIronWeight: float = None, Bin: str = None, Pos: str = None, Note: str = None, Machine: str = None, BendingDevice: str = None, Spacer: list = [], WeldingPoint: list = [], Segment: list = []):
        self.GlobalID = GlobalID
        self.ReinforcementType = ReinforcementType
        self.SteelQuality = SteelQuality
        if type(PieceCount) is int:
            self.PieceCount = int(PieceCount)
        else:
            if PieceCount is None:
                self.PieceCount = None
            else:
                try:
                    self.PieceCount = int(PieceCount)
                except ValueError:
                    raise ValueError(f'PieceCount must be a int')
        if type(Diameter) is float:
            self.Diameter = float(Diameter)
        else:
            if Diameter is None:
                self.Diameter = None
            else:
                try:
                    self.Diameter = float(Diameter)
                except ValueError:
                    raise ValueError(f'Diameter must be a float')

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
        self.ArticleNo = ArticleNo
        if type(NoAutoProd) is bool:
            self.NoAutoProd = bool(NoAutoProd)
        else:
            if NoAutoProd is None:
                self.NoAutoProd = None
            elif NoAutoProd in ['true', 'True', 'TRUE']:
                self.NoAutoProd = True
            elif NoAutoProd in ['false', 'False', 'FALSE']:
                self.NoAutoProd = False
            else:
                try:
                    self.NoAutoProd = bool(NoAutoProd)
                except ValueError:
                    raise ValueError(f'NoAutoProd must be a bool')
        if type(ExtIronWeight) is float:
            self.ExtIronWeight = float(ExtIronWeight)
        else:
            if ExtIronWeight is None:
                self.ExtIronWeight = None
            else:
                try:
                    self.ExtIronWeight = float(ExtIronWeight)
                except ValueError:
                    raise ValueError(f'ExtIronWeight must be a float')
        self.Bin = Bin
        self.Pos = Pos
        self.Note = Note
        self.Machine = Machine
        self.BendingDevice = BendingDevice
        self.Spacer = Spacer
        self.WeldingPoint = WeldingPoint
        self.Segment = Segment

    def get_GlobalID(self):
        return self.GlobalID

    def get_ReinforcementType(self):
        return self.ReinforcementType

    def get_SteelQuality(self):
        return self.SteelQuality

    def get_PieceCount(self):
        return self.PieceCount

    def get_Diameter(self):
        return self.Diameter

    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y

    def get_Z(self):
        return self.Z

    def get_RotZ(self):
        return self.RotZ

    def get_ArticleNo(self):
        return self.ArticleNo

    def get_NoAutoProd(self):
        return self.NoAutoProd

    def get_ExtIronWeight(self):
        return self.ExtIronWeight

    def get_Bin(self):
        return self.Bin

    def get_Pos(self):
        return self.Pos

    def get_Note(self):
        return self.Note

    def get_Machine(self):
        return self.Machine

    def get_BendingDevice(self):
        return self.BendingDevice

    def get_Spacer(self):
        return self.Spacer

    def get_WeldingPoint(self):
        return self.WeldingPoint

    def get_Segment(self):
        return self.Segment

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_ReinforcementType(self, ReinforcementType: str):
        self.ReinforcementType = ReinforcementType

    def set_SteelQuality(self, SteelQuality: str):
        self.SteelQuality = SteelQuality

    def set_PieceCount(self, PieceCount: int):
        self.PieceCount = PieceCount

    def set_Diameter(self, Diameter: float):
        self.Diameter = Diameter

    def set_X(self, X: float):
        self.X = X

    def set_Y(self, Y: float):
        self.Y = Y

    def set_Z(self, Z: float):
        self.Z = Z

    def set_RotZ(self, RotZ: float):
        self.RotZ = RotZ

    def set_ArticleNo(self, ArticleNo: str):
        self.ArticleNo = ArticleNo

    def set_NoAutoProd(self, NoAutoProd: bool):
        self.NoAutoProd = NoAutoProd

    def set_ExtIronWeight(self, ExtIronWeight: float):
        self.ExtIronWeight = ExtIronWeight

    def set_Bin(self, Bin: str):
        self.Bin = Bin

    def set_Pos(self, Pos: str):
        self.Pos = Pos

    def set_Note(self, Note: str):
        self.Note = Note

    def set_Machine(self, Machine: str):
        self.Machine = Machine

    def set_BendingDevice(self, BendingDevice: str):
        self.BendingDevice = BendingDevice

    def set_Spacer(self, Spacer: list):
        self.Spacer = Spacer

    def add_Spacer(self, Spacer: Spacer) -> object:
        self.Spacer.append(Spacer)

    def set_WeldingPoint(self, WeldingPoint: list):
        self.WeldingPoint = WeldingPoint

    def add_WeldingPoint(self, WeldingPoint: WeldingPoint) -> object:
        self.WeldingPoint.append(WeldingPoint)

    def set_Segment(self, Segment: list):
        self.Segment = Segment

    def add_Segment(self, Segment: Segment) -> object:
        self.Segment.append(Segment)
