import xml.etree.ElementTree as ET


class Segment():


    def __init__(self, GlobalID: str = None, Type: str = None, RotX: float = None, BendY: float = None, L: float = None, R: float = None):
        self.GlobalID = None  # STR // 0,1
        self.Type = None  # STR // 0,1
        self.RotX = None  # FLOAT // 0,1
        self.BendY = None  # FLOAT // 0,1
        self.L = None  # FLOAT 0,1
        self.R = None  # FLOAT 0,1

        self.GlobalID = GlobalID
        self.Type = Type
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
        if type(BendY) is float:
            self.BendY = float(BendY)
        else:
            if BendY is None:
                self.BendY = None
            else:
                try:
                    self.BendY = float(BendY)
                except ValueError:
                    raise ValueError(f'BendY must be a float')
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
        if type(R) is float:
            self.R = float(R)
        else:
            if R is None:
                self.R = None
            else:
                try:
                    self.R = float(R)
                except ValueError:
                    raise ValueError(f'R must be a float')

    def get_GlobalID(self):
        return self.GlobalID

    def get_Type(self):
        return self.Type

    def get_RotX(self):
        return self.RotX

    def get_BendY(self):
        return self.BendY

    def get_L(self):
        return self.L

    def get_R(self):
        return self.R

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_Type(self, Type: str):
        self.Type = Type

    def set_RotX(self, RotX: float):
        self.RotX = RotX

    def set_BendY(self, BendY: float):
        self.BendY = BendY

    def set_L(self, L: float):
        self.L = L

    def set_R(self, R: float):
        self.R = R

    def __str__(self):
        return "GlobalID: " + str(self.GlobalID) + ", Type: " + str(self.Type) + ", RotX: " + str(self.RotX) + ", BendY: " + str(self.BendY) + ", L: " + str(self.L) + ", R: " + str(self.R)

    def __xml__(self):
        Segment = ET.Element('Segment')
        if self.GlobalID is not None:
            Segment.set('GlobalID', self.GlobalID)
        if self.Type is not None:
            Segment.set('Type', self.Type)
        if self.RotX is not None:
            RotX = ET.SubElement(Segment, 'RotX')
            RotX.text = str(self.RotX)
        if self.BendY is not None:
            BendY = ET.SubElement(Segment, 'BendY')
            BendY.text = str(self.BendY)
        if self.L is not None:
            L = ET.SubElement(Segment, 'L')
            L.text = str(self.L)
        if self.R is not None:
            R = ET.SubElement(Segment, 'R')
            R.text = str(self.R)
        return Segment