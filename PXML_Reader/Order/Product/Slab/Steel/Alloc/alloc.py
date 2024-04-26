from .Region.region import Region
import xml.etree.ElementTree as ET

class Alloc:
    GlobalID = None # STR // 0,1
    Type = None # STR // 0,1
    GuildingBar = None # INT // 0,1
    Region = []

    def __init__(self, GlobalID: str = None, Type: str = None, GuildingBar: int = None, Region = []):
        self.GlobalID = GlobalID
        self.Type = Type
        if type(GuildingBar) is int:
            self.GuildingBar = int(GuildingBar)
        else:
            if GuildingBar is None:
                self.GuildingBar = None
            else:
                try:
                    self.GuildingBar = int(GuildingBar)
                except ValueError:
                    raise ValueError(f'GuildingBar must be a int')
        self.Region = Region

    def get_GlobalID(self):
        return self.GlobalID

    def get_Type(self):
        return self.Type

    def get_GuildingBar(self):
        return self.GuildingBar

    def get_Region(self):
        return self.Region

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_Type(self, Type: str):
        self.Type = Type

    def set_GuildingBar(self, GuildingBar: int):
        self.GuildingBar = GuildingBar

    def set_Region(self, Region):
        self.Region = Region

    def add_Region(self, Region):
        self.Region.append(Region)

    def __str__(self):
        return "GlobalID: " + str(self.GlobalID) + ", Type: " + str(self.Type) + ", GuildingBar: " + str(self.GuildingBar) + ", Region: " + str(self.Region)

    def __xml__(self):
        Alloc = ET.Element('Alloc')
        if self.GlobalID is not None:
            Alloc.set('GlobalID', self.GlobalID)
        if self.Type is not None:
            Alloc.set('Type', self.Type)
        if self.GuildingBar is not None:
            GuildingBar = ET.SubElement(Alloc, 'GuildingBar')
            GuildingBar.text = str(self.GuildingBar)
        for Region in self.Region:
            Alloc.append(Region.__xml__())
        return Alloc

