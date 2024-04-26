class Section:
    GlobalID = None # STR // 0,1
    L = None # FLOAT // 0,1
    S = None # FLOAT // 0,1
    F = None # FLOAT // 0,1

    def __init__(self, GlobalID: str = None, L: float = None, S: float = None, F: float = None):
        self.GlobalID = GlobalID
        if type(L) is float:
            self.L = float(L)
        else:
            if L is None:
                self.L = None
            else:
                try:
                    self.L = float(L)
                except ValueError:
                    raise ValueError(f'L must be a float')
        if type(S) is float:
            self.S = float(S)
        else:
            if S is None:
                self.S = None
            else:
                try:
                    self.S = float(S)
                except ValueError:
                    raise ValueError(f'S must be a float')
        if type(F) is float:
            self.F = float(F)
        else:
            if F is None:
                self.F = None
            else:
                try:
                    self.F = float(F)
                except ValueError:
                    raise ValueError(f'F must be a float')


    def get_GlobalID(self):
        return self.GlobalID

    def get_L(self):
        return self.L

    def get_S(self):
        return self.S

    def get_F(self):
        return self.F

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_L(self, L: float):
        self.L = L

    def set_S(self, S: float):
        self.S = S

    def set_F(self, F: float):
        self.F = F

    def __str__(self):
        return "GlobalID: " + str(self.GlobalID) + ", L: " + str(self.L) + ", S: " + str(self.S) + ", F: " + str(self.F)

