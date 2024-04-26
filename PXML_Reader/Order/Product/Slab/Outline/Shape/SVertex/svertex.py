class SVertex():
    GlobalID = None # STR // 0,1
    X = None # FLOAT // 0,1
    Y = None # FLOAT // 0,1
    Bulge = None # FLOAT // 0,1
    LineAttribute = None # STR // 0,1
    Profile = None # STR // 0,1
    DX = None # FLOAT // 0,1
    DY = None # FLOAT // 0,1

    def __init__(self, GlobalID: str = None, X: float = None, Y: float = None, Bulge: float = None, LineAttribute: str = None, Profile: str = None, DX: float = None, DY: float = None):
        self.GlobalID = GlobalID
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
        if type(Bulge) is float:
            self.Bulge = float(Bulge)
        else:
            if Bulge is None:
                self.Bulge = None
            else:
                try:
                    self.Bulge = float(Bulge)
                except ValueError:
                    raise ValueError(f'Bulge must be a float')

        self.LineAttribute = LineAttribute
        self.Profile = Profile
        if type(DX) is float:
            self.DX = float(DX)
        else:
            if DX is None:
                self.DX = None
            else:
                try:
                    self.DX = float(DX)
                except ValueError:
                    raise ValueError(f'DX must be a float')
        if type(DY) is float:
            self.DY = float(DY)
        else:
            if DY is None:
                self.DY = None
            else:
                try:
                    self.DY = float(DY)
                except ValueError:
                    raise ValueError(f'DY must be a float')

    def get_GlobalID(self):
        return self.GlobalID

    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y

    def get_Bulge(self):
        return self.Bulge

    def get_LineAttribute(self):
        return self.LineAttribute

    def get_Profile(self):
        return self.Profile

    def get_DX(self):
        return self.DX

    def get_DY(self):
        return self.DY

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_X(self, X: float):
        self.X = X

    def set_Y(self, Y: float):
        self.Y = Y

    def set_Bulge(self, Bulge: float):
        self.Bulge = Bulge

    def set_LineAttribute(self, LineAttribute: str):
        self.LineAttribute = LineAttribute

    def set_Profile(self, Profile: str):
        self.Profile = Profile

    def set_DX(self, DX: float):
        self.DX = DX

    def set_DY(self, DY: float):
        self.DY = DY

    def __str__(self):
        return "GlobalID: " + str(self.GlobalID) + ", X: " + str(self.X) + ", Y: " + str(self.Y) + ", Bulge: " + str(self.Bulge) + ", LineAttribute: " + str(self.LineAttribute) + ", Profile: " + str(self.Profile) + ", DX: " + str(self.DX) + ", DY: " + str(self.DY)