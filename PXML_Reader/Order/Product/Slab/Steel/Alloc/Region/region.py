import xml.etree.ElementTree as ET


class Region:
    GlobalID = None # STR // 0,1
    IntervalCount = None # INT // 0,1
    Pitch = None # FLOAT // 0,1
    IncludeBegin = False # BOOL // 0,1
    IncludeEnd = False # BOOL // 0,1
    RefIndex = None # INT // 0,1

    def __init__(self, GlobalID: str = None, IntervalCount: int = None, Pitch: float = None, IncludeBegin: bool = False, IncludeEnd: bool = False, RefIndex: int = None):
        self.GlobalID = GlobalID
        if type(IntervalCount) is int:
            self.IntervalCount = int(IntervalCount)
        else:
            if IntervalCount is None:
                self.IntervalCount = None
            else:
                try:
                    self.IntervalCount = int(IntervalCount)
                except ValueError:
                    raise ValueError(f'IntervalCount must be a int')
        if type(Pitch) is float:
            self.Pitch = float(Pitch)
        else:
            if Pitch is None:
                self.Pitch = None
            else:
                try:
                    self.Pitch = float(Pitch)
                except ValueError:
                    raise ValueError(f'Pitch must be a float')
        if type(IncludeBegin) is bool:
            self.IncludeBegin = bool(IncludeBegin)
        else:
            if IncludeBegin in ["true", "True", "TRUE"]:
                self.IncludeBegin = True
            elif IncludeBegin in ["false", "False", "FALSE"]:
                self.IncludeBegin = False
            elif IncludeBegin is None:
                self.IncludeBegin = None
            else:
                try:
                    self.IncludeBegin = bool(IncludeBegin)
                except ValueError:
                    raise ValueError(f'IncludeBegin must be a bool')

        if type(IncludeEnd) is bool:
            self.IncludeEnd = bool(IncludeEnd)
        else:
            if IncludeEnd in ["true", "True", "TRUE"]:
                self.IncludeEnd = True
            elif IncludeEnd in ["false", "False", "FALSE"]:
                self.IncludeEnd = False
            elif IncludeEnd is None:
                self.IncludeEnd = None
            else:
                try:
                    self.IncludeEnd = bool(IncludeEnd)
                except ValueError:
                    raise ValueError(f'IncludeEnd must be a bool')

        if type(RefIndex) is int:
            self.RefIndex = int(RefIndex)
        else:
            if RefIndex is None:
                self.RefIndex = None
            else:
                try:
                    self.RefIndex = int(RefIndex)
                except ValueError:
                    raise ValueError(f'RefIndex must be a int')


    def get_GlobalID(self):
        return self.GlobalID

    def get_IntervalCount(self):
        return self.IntervalCount

    def get_Pitch(self):
        return self.Pitch

    def get_IncludeBegin(self):
        return self.IncludeBegin

    def get_IncludeEnd(self):
        return self.IncludeEnd

    def get_RefIndex(self):
        return self.RefIndex

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_IntervalCount(self, IntervalCount: int):
        self.IntervalCount = IntervalCount

    def set_Pitch(self, Pitch: float):
        self.Pitch = Pitch

    def set_IncludeBegin(self, IncludeBegin: bool):
        self.IncludeBegin = IncludeBegin

    def set_IncludeEnd(self, IncludeEnd: bool):
        self.IncludeEnd = IncludeEnd

    def set_RefIndex(self, RefIndex: int):
        self.RefIndex = RefIndex

    def __str__(self):
        return "GlobalID: " + str(self.GlobalID) + ", IntervalCount: " + str(self.IntervalCount) + ", Pitch: " + str(self.Pitch) + ", IncludeBegin: " + str(self.IncludeBegin) + ", IncludeEnd: " + str(self.IncludeEnd) + ", RefIndex: " + str(self.RefIndex)

    def __xml__(self):
        Region = ET.Element("Region")
        if self.GlobalID is not None:
            Region.set("GlobalID",self.GlobalID)
        if self.IntervalCount is not None:
            IntervalCount = ET.SubElement(Region,"IntervalCount")
            IntervalCount.text = str(self.IntervalCount)
        if self.Pitch is not None:
            Pitch = ET.SubElement(Region,"Pitch")
            Pitch.text = str(self.Pitch)
        if self.IncludeBegin is not None:
            IncludeBegin = ET.SubElement(Region,"IncludeBegin")
            IncludeBegin.text = str(self.IncludeBegin)
        if self.IncludeEnd is not None:
            IncludeEnd = ET.SubElement(Region,"IncludeEnd")
            IncludeEnd.text = str(self.IncludeEnd)
        if self.RefIndex is not None:
            RefIndex = ET.SubElement(Region,"RefIndex")
            RefIndex.text = str(self.RefIndex)
        return Region
