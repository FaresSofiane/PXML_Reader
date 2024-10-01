import xml.etree.ElementTree as ET


class Spacer():


    def __init__(self, GlobalID: str = None, Type: int = None, Position: float = None):
        self.GlobalID = None  # STR // 0,1
        self.Type = None  # INT // 0,1
        self.Position = None  # FLOAT // 0,1

        self.GlobalID = GlobalID
        if type(Type) is int:
            self.Type = int(Type)
        else:
            if Type is None:
                self.Type = None
            else:
                try:
                    self.Type = int(Type)
                except ValueError:
                    raise ValueError(f'Type must be a int')
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

    def get_GlobalID(self):
        return self.GlobalID

    def get_Type(self):
        return self.Type

    def get_Position(self):
        return self.Position

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_Type(self, Type: int):
        self.Type = Type

    def set_Position(self, Position: float):
        self.Position = Position

    def __str__(self):
        return "GlobalID: " + str(self.GlobalID) + ", Type: " + str(self.Type) + ", Position: " + str(self.Position)

    def __xml__(self):
        Spacer = ET.Element('Spacer')
        if self.GlobalID is not None:
            Spacer.set('GlobalID', self.GlobalID)
        if self.Type is not None:
            Type = ET.SubElement(Spacer, 'Type')
            Type.text = str(int(self.Type))
        if self.Position is not None:
            Spacer = ET.SubElement(Spacer, 'Position')
            Spacer.text = str(float(self.Position))
        return Spacer