class Girder:
    GlobalID = None # STR // 0,1
    PieceCount = None # INT // 0,1
    X = None # FLOAT // 0,1
    Y = None # FLOAT // 0,1
    Z = None # FLOAT // 0,1
    GirderName = None # STR // 0,1
    Length = None # FLOAT // 0,1
    AngleToX = None # FLOAT // 0,1
    NoAutoProd = False # BOOL // 0,1
    Height = None # FLOAT // 0,1
    TopExcess = None # FLOAT // 0,1
    BottomExcess = None # FLOAT // 0,1
    Weight = None # FLOAT // 0,1
    TopFlangeDiameter = None # FLOAT // 0,1
    BottomFlangeDiameter = None # FLOAT // 0,1
    GirderType = None # INT // 0,1
    MountingType = None # INT // 0,1
    ArticleNo = None # STR // 0,1
    Machine = None # STR // 0,1
    Period = None # FLOAT // 0,1
    PeriodOffset = None # FLOAT // 0,1
    Width = None # FLOAT // 0,1
    AnchorBar = [] # AnchorBar // n,n
    GirderExt = [] # GirderExt // n,n
    Section = [] # Section // n,n

    def __init__(self, GlobalID: str = None, PieceCount: int = None, X: float = None, Y: float = None, Z: float = None, GirderName: str = None, Length: float = None, AngleToX: float = None, NoAutoProd: bool = False, Height: float = None, TopExcess: float = None, BottomExcess: float = None, Weight: float = None, TopFlangeDiameter: float = None, BottomFlangeDiameter: float = None, GirderType: int = None, MountingType: int = None, ArticleNo: str = None, Machine: str = None, Period: float = None, PeriodOffset: float = None, Width: float = None, AnchorBar: list = [], GirderExt: list = [], Section: list = []):
        self.GlobalID = GlobalID
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

        self.GirderName = GirderName
        if type(Length) is float:
            self.Length = float(Length)
        else:
            if Length is None:
                self.Length = None
            else:
                try:
                    self.Length = float(Length)
                except ValueError:
                    raise ValueError(f'Length must be a float')

        if type(AngleToX) is float:
            self.AngleToX = float(AngleToX)
        else:
            if AngleToX is None:
                self.AngleToX = None
            else:
                try:
                    self.AngleToX = float(AngleToX)
                except ValueError:
                    raise ValueError(f'AngleToX must be a float')

        if type(NoAutoProd) is bool:
            self.NoAutoProd = bool(NoAutoProd)
        else:
            if NoAutoProd in ['true', 'True', 'TRUE']:
                self.NoAutoProd = True
            elif NoAutoProd in ['false', 'False', 'FALSE']:
                self.NoAutoProd = False
            elif NoAutoProd is None:
                self.NoAutoProd = None
            else:
                try:
                    self.NoAutoProd = bool(NoAutoProd)
                except ValueError:
                    raise ValueError(f'NoAutoProd must be a bool')
        if type(Height) is float:
            self.Height = float(Height)
        else:
            if Height is None:
                self.Height = None
            else:
                try:
                    self.Height = float(Height)
                except ValueError:
                    raise ValueError(f'Height must be a float')
        if type(TopExcess) is float:
            self.TopExcess = float(TopExcess)
        else:
            if TopExcess is None:
                self.TopExcess = None
            else:
                try:
                    self.TopExcess = float(TopExcess)
                except ValueError:
                    raise ValueError(f'TopExcess must be a float')
        if type(BottomExcess) is float:
            self.BottomExcess = float(BottomExcess)
        else:
            if BottomExcess is None:
                self.BottomExcess = None
            else:
                try:
                    self.BottomExcess = float(BottomExcess)
                except ValueError:
                    raise ValueError(f'BottomExcess must be a float')
        if type(Weight) is float:
            self.Weight = float(Weight)
        else:
            if Weight is None:
                self.Weight = None
            else:
                try:
                    self.Weight = float(Weight)
                except ValueError:
                    raise ValueError(f'Weight must be a float')

        if type(TopFlangeDiameter) is float:
            self.TopFlangeDiameter = float(TopFlangeDiameter)
        else:
            if TopFlangeDiameter is None:
                self.TopFlangeDiameter = None
            else:
                try:
                    self.TopFlangeDiameter = float(TopFlangeDiameter)
                except ValueError:
                    raise ValueError(f'TopFlangeDiameter must be a float')

        if type(BottomFlangeDiameter) is float:
            self.BottomFlangeDiameter = float(BottomFlangeDiameter)
        else:
            if BottomFlangeDiameter is None:
                self.BottomFlangeDiameter = None
            else:
                try:
                    self.BottomFlangeDiameter = float(BottomFlangeDiameter)
                except ValueError:
                    raise ValueError(f'BottomFlangeDiameter must be a float')

        if type(GirderType) is int:
            self.GirderType = int(GirderType)
        else:
            if GirderType is None:
                self.GirderType = None
            else:
                try:
                    self.GirderType = int(GirderType)
                except ValueError:
                    raise ValueError(f'GirderType must be a int')
        if type(MountingType) is int:
            self.MountingType = int(MountingType)
        else:
            if MountingType is None:
                self.MountingType = None
            else:
                try:
                    self.MountingType = int(MountingType)
                except ValueError:
                    raise ValueError(f'MountingType must be a int')
        self.ArticleNo = ArticleNo
        self.Machine = Machine
        if type(Period) is float:
            self.Period = float(Period)
        else:
            if Period is None:
                self.Period = None
            else:
                try:
                    self.Period = float(Period)
                except ValueError:
                    raise ValueError(f'Period must be a float')

        if type(PeriodOffset) is float:
            self.PeriodOffset = float(PeriodOffset)
        else:
            if PeriodOffset is None:
                self.PeriodOffset = None
            else:
                try:
                    self.PeriodOffset = float(PeriodOffset)
                except ValueError:
                    raise ValueError(f'PeriodOffset must be a float')
        if type(Width) is float:
            self.Width = float(Width)
        else:
            if Width is None:
                self.Width = None
            else:
                try:
                    self.Width = float(Width)
                except ValueError:
                    raise ValueError(f'Width must be a float')

        self.AnchorBar = AnchorBar
        self.GirderExt = GirderExt
        self.Section = Section

    def get_GlobalID(self):
        return self.GlobalID

    def get_PieceCount(self):
        return self.PieceCount

    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y

    def get_Z(self):
        return self.Z

    def get_GirderName(self):
        return self.GirderName

    def get_Length(self):
        return self.Length

    def get_AngleToX(self):
        return self.AngleToX

    def get_NoAutoProd(self):
        return self.NoAutoProd

    def get_Height(self):
        return self.Height

    def get_TopExcess(self):
        return self.TopExcess

    def get_BottomExcess(self):
        return self.BottomExcess

    def get_Weight(self):
        return self.Weight

    def get_TopFlangeDiameter(self):
        return self.TopFlangeDiameter

    def get_BottomFlangeDiameter(self):
        return self.BottomFlangeDiameter

    def get_GirderType(self):
        return self.GirderType

    def get_MountingType(self):
        return self.MountingType

    def get_ArticleNo(self):
        return self.ArticleNo

    def get_Machine(self):
        return self.Machine

    def get_Period(self):
        return self.Period

    def get_PeriodOffset(self):
        return self.PeriodOffset

    def get_Width(self):
        return self.Width

    def get_AnchorBar(self):
        return self.AnchorBar

    def get_GirderExt(self):
        return self.GirderExt

    def get_Section(self):
        return self.Section

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_PieceCount(self, PieceCount: int):
        self.PieceCount = PieceCount

    def set_X(self, X: float):
        self.X = X

    def set_Y(self, Y: float):
        self.Y = Y

    def set_Z(self, Z: float):
        self.Z = Z

    def set_GirderName(self, GirderName: str):
        self.GirderName = GirderName

    def set_Length(self, Length: float):
        self.Length = Length

    def set_AngleToX(self, AngleToX: float):
        self.AngleToX = AngleToX

    def set_NoAutoProd(self, NoAutoProd: bool):
        self.NoAutoProd = NoAutoProd

    def set_Height(self, Height: float):
        self.Height = Height

    def set_TopExcess(self, TopExcess: float):
        self.TopExcess = TopExcess

    def set_BottomExcess(self, BottomExcess: float):
        self.BottomExcess = BottomExcess

    def set_Weight(self, Weight: float):
        self.Weight = Weight

    def set_TopFlangeDiameter(self, TopFlangeDiameter: float):
        self.TopFlangeDiameter = TopFlangeDiameter

    def set_BottomFlangeDiameter(self, BottomFlangeDiameter: float):
        self.BottomFlangeDiameter = BottomFlangeDiameter

    def set_GirderType(self, GirderType: int):
        self.GirderType = GirderType

    def set_MountingType(self, MountingType: int):
        self.MountingType = MountingType

    def set_ArticleNo(self, ArticleNo: str):
        self.ArticleNo = ArticleNo

    def set_Machine(self, Machine: str):
        self.Machine = Machine

    def set_Period(self, Period: float):
        self.Period = Period

    def set_PeriodOffset(self, PeriodOffset: float):
        self.PeriodOffset = PeriodOffset

    def set_Width(self, Width: float):
        self.Width = Width

    def set_AnchorBar(self, AnchorBar: list):
        self.AnchorBar = AnchorBar

    def add_AnchorBar(self, AnchorBar):
        self.AnchorBar.append(AnchorBar)

    def set_GirderExt(self, GirderExt: list):
        self.GirderExt = GirderExt

    def add_GirderExt(self, GirderExt):
        self.GirderExt.append(GirderExt)

    def set_Section(self, Section: list):
        self.Section = Section

    def add_Section(self, Section):
        self.Section.append(Section)

    def __str__(self):
        return "GlobalID: " + str(self.GlobalID) + ", PieceCount: " + str(self.PieceCount) + ", X: " + str(self.X) + ", Y: " + str(self.Y) + ", Z: " + str(self.Z) + ", GirderName: " + str(self.GirderName) + ", Length: " + str(self.Length) + ", AngleToX: " + str(self.AngleToX) + ", NoAutoProd: " + str(self.NoAutoProd) + ", Height: " + str(self.Height) + ", TopExcess: " + str(self.TopExcess) + ", BottomExcess: " + str(self.BottomExcess) + ", Weight: " + str(self.Weight) + ", TopFlangeDiameter: " + str(self.TopFlangeDiameter) + ", BottomFlangeDiameter: " + str(self.BottomFlangeDiameter) + ", GirderType: " + str(self.GirderType) + ", MountingType: " + str(self.MountingType) + ", ArticleNo: " + str(self.ArticleNo) + ", Machine: " + str(self.Machine) + ", Period: " + str(self.Period) + ", PeriodOffset: " + str(self.PeriodOffset) + ", Width: " + str(self.Width) + ", AnchorBar: " + str(self.AnchorBar) + ", GirderExt: " + str(self.GirderExt) + ", Section: " + str(self.Section)

