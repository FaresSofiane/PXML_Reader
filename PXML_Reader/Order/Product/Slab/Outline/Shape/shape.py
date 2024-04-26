from .SVertex.svertex import SVertex

class Shape():
    GlobalID = None # STR // 0,1
    Cutout = False # Bool // 0,1
    RefHeight = None # FLOAT // 0,1
    SVertex = [] # SVertex // n,n

    def __init__(self, GlobalID: str = None, Cutout: bool = False, RefHeight: float = None, SVertex: list = []):
        self.GlobalID = GlobalID
        if type(Cutout) is bool:
            self.Cutout = bool(Cutout)
        else:
            if Cutout in ["true","True","TRUE"]:
                self.Cutout = True
            elif Cutout in ["false","False","FALSE"]:
                self.Cutout = False
            elif Cutout is None:
                self.Cutout = None
            else:
                try:
                    self.Cutout = bool(Cutout)
                except:
                    raise ValueError("Cutout must be a boolean")

        if type(RefHeight) is float:
            self.RefHeight = float(RefHeight)
        else:
            if RefHeight is None:
                self.RefHeight = None
            else:
                try:
                    self.RefHeight = float(RefHeight)
                except:
                    raise ValueError("RefHeight must be a float")

        self.SVertex = SVertex

    def get_GlobalID(self):
        return self.GlobalID

    def get_Cutout(self):
        return self.Cutout

    def get_RefHeight(self):
        return self.RefHeight

    def get_SVertex(self):
        return self.SVertex

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_Cutout(self, Cutout: bool):
        self.Cutout = Cutout

    def set_RefHeight(self, RefHeight: float):
        self.RefHeight = RefHeight

    def set_SVertex(self, SVertex: list):
        self.SVertex = SVertex

    def add_SVertex(self, SVertex: SVertex) -> object:
        self.SVertex.append(SVertex)

    def __str__(self):
        return "GlobalID: " + str(self.GlobalID) + ", Cutout: " + str(self.Cutout) + ", RefHeight: " + str(self.RefHeight) + ", SVertex: " + str(self.SVertex)


