import xml.etree.ElementTree as ET


class GirderExt:
    GlobalID = None # STR // 0,1
    Type = None # STR // 0,1
    Position = None # FLOAT // 0,1
    Flags = None # INT // 0,1
    Val0 = None # FLOAT // 0,1
    Val1 = None # FLOAT // 0,1
    Val2 = None # FLOAT // 0,1
    Val3 = None # FLOAT // 0,1

    def __init__(self, GlobalID: str = None, Type: str = None, Position: float = None, Flags: int = None, Val0: float = None, Val1: float = None, Val2: float = None, Val3: float = None):
        self.GlobalID = GlobalID
        self.Type = Type
        if type(Flags) is int:
            self.Flags = int(Flags)
        else:
            if Flags is None:
                self.Flags = None
            else:
                try:
                    self.Flags = int(Flags)
                except ValueError:
                    raise ValueError(f'Flags must be a int')

        if type(Position) is float:
            self.Position = float(Position)
        else:
            if Position is None:
                self.Position = None
            else:
                try:
                    self.Position = float(Position)
                except ValueError:
                    raise ValueError(f'Position must be a float')

        if type(Val3) is float:
            self.Val3 = float(Val3)
        else:
            if Val3 is None:
                self.Val3 = None
            else:
                try:
                    self.Val3 = float(Val3)
                except ValueError:
                    raise ValueError(f'Val3 must be a float')

        if type(Val2) is float:
            self.Val2 = float(Val2)
        else:
            if Val2 is None:
                self.Val2 = None
            else:
                try:
                    self.Val2 = float(Val2)
                except ValueError:
                    raise ValueError(f'Val2 must be a float')

        if type(Val1) is float:
            self.Val1 = float(Val1)
        else:
            if Val1 is None:
                self.Val1 = None
            else:
                try:
                    self.Val1 = float(Val1)
                except ValueError:
                    raise ValueError(f'Val1 must be a float')

        if type(Val0) is float:
            self.Val0 = float(Val0)
        else:
            if Val0 is None:
                self.Val0 = None
            else:
                try:
                    self.Val0 = float(Val0)
                except ValueError:
                    raise ValueError(f'Val0 must be a float')


    def get_GlobalID(self):
        return self.GlobalID

    def get_Type(self):
        return self.Type

    def get_Position(self):
        return self.Position

    def get_Flags(self):
        return self.Flags

    def get_Val0(self):
        return self.Val0

    def get_Val1(self):
        return self.Val1

    def get_Val2(self):
        return self.Val2

    def get_Val3(self):
        return self.Val3

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_Type(self, Type: str):
        self.Type = Type

    def set_Position(self, Position: float):
        self.Position = Position

    def set_Flags(self, Flags: int):
        self.Flags = Flags

    def set_Val0(self, Val0: float):
        self.Val0 = Val0

    def set_Val1(self, Val1: float):
        self.Val1 = Val1

    def set_Val2(self, Val2: float):
        self.Val2 = Val2

    def set_Val3(self, Val3: float):
        self.Val3 = Val3

    def __str__(self):
        return "GlobalID: " + str(self.GlobalID) + ", Type: " + str(self.Type) + ", Position: " + str(self.Position) + ", Flags: " + str(self.Flags) + ", Val0: " + str(self.Val0) + ", Val1: " + str(self.Val1) + ", Val2: " + str(self.Val2) + ", Val3: " + str(self.Val3)

    def __xml__(self):
        GirderExt = ET.Element('GirderExt')
        if self.GlobalID is not None:
            GirderExt.set('GlobalID', self.GlobalID)
        if self.Type is not None:
            GirderExt.set('Type', self.Type)
        if self.Position is not None:
            Position = ET.SubElement(GirderExt, 'Position')
            Position.text = str(self.Position)
        if self.Flags is not None:
            Flags = ET.SubElement(GirderExt, 'Flags')
            Flags.text = str(self.Flags)
        if self.Val0 is not None:
            Val0 = ET.SubElement(GirderExt, 'Val0')
            Val0.text = str(self.Val0)
        if self.Val1 is not None:
            Val1 = ET.SubElement(GirderExt, 'Val1')
            Val1.text = str(self.Val1)
        if self.Val2 is not None:
            Val2 = ET.SubElement(GirderExt, 'Val2')
            Val2.text = str(self.Val2)
        if self.Val3 is not None:
            Val3 = ET.SubElement(GirderExt, 'Val3')
            Val3.text = str(self.Val3)
        return GirderExt