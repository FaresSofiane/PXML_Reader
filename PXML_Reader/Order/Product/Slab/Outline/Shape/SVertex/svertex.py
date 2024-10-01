import xml.etree.ElementTree as ET
from lib2to3.pgen2.tokenize import double3prog


class SVertex():


    def __init__(self, GlobalID: str = None, X: float = None, Y: float = None, Bulge: float = None, LineAttribute: str = None, Profile: str = None, DX: float = None, DY: float = None):
        self.GlobalID = None  # STR // 0,1
        self.X = None  # FLOAT // 0,1
        self.Y = None  # FLOAT // 0,1
        self.Bulge = None  # FLOAT // 0,1
        self.LineAttribute = None  # STR // 0,1
        self.Profile = None  # STR // 0,1
        self.DX = None  # FLOAT // 0,1
        self.DY = None  # FLOAT // 0,1

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

    def __xml__(self):
        SVertex = ET.Element("SVertex")
        if self.GlobalID is not None:
            SVertex.set("GlobalID",self.GlobalID)
        if self.X is not None:
            X = ET.SubElement(SVertex,"X")
            X.text = str(float(self.X))
        if self.Y is not None:
            Y = ET.SubElement(SVertex,"Y")
            Y.text = str(float(self.Y))
        if self.Bulge is not None:
            Bulge = ET.SubElement(SVertex,"Bulge")
            Bulge.text = str(float(self.Bulge))
        if self.LineAttribute is not None:
            LineAttribute = ET.SubElement(SVertex,"LineAttribute")
            LineAttribute.text = str(self.LineAttribute)
        if self.Profile is not None:
            Profile = ET.SubElement(SVertex,"Profile")
            Profile.text = str(self.Profile)
        if self.DX is not None:
            DX = ET.SubElement(SVertex,"DX")
            DX.text = str(float(self.DX))
        if self.DY is not None:
            DY = ET.SubElement(SVertex,"DY")
            DY.text = str(float(self.DY))
        return SVertex