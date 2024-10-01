import xml.etree.ElementTree as ET


class WeldingPoint():


    def __init__(self, GlobalId: str = None, WeldingOutput: float = None, Position: float = None, WeldingPointType: int = None, WeldingPrgNo: int = None, GroupID: str = None):

        self.GlobalId = None  # STR // 0,1
        self.WeldingOutput = None  # FLOAT // 0,1
        self.Position = None  # FLOAT // 0,1
        self.WeldingPointType = None  # INT // 0,1
        self.WeldingPrgNo = None  # INT // 0,1
        self.GroupID = None  # STR // 0,1
        self.GlobalId = GlobalId
        if type(WeldingOutput) is float:
            self.WeldingOutput = float(WeldingOutput)
        else:
            if WeldingOutput is None:
                self.WeldingOutput = None
            else:
                try:
                    self.WeldingOutput = float(WeldingOutput)
                except ValueError:
                    raise ValueError(f'WeldingOutput must be a float')
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
        if type(WeldingPointType) is int:
            self.WeldingPointType = int(WeldingPointType)
        else:
            if WeldingPointType is None:
                self.WeldingPointType = None
            else:
                try:
                    self.WeldingPointType = int(WeldingPointType)
                except ValueError:
                    raise ValueError(f'WeldingPointType must be a int')
        if type(WeldingPrgNo) is int:
            self.WeldingPrgNo = int(WeldingPrgNo)
        else:
            if WeldingPrgNo is None:
                self.WeldingPrgNo = None
            else:
                try:
                    self.WeldingPrgNo = int(WeldingPrgNo)
                except ValueError:
                    raise ValueError(f'WeldingPrgNo must be a int')
        self.GroupID = GroupID

    def get_GlobalId(self):
        return self.GlobalId

    def get_WeldingOutput(self):
        return self.WeldingOutput

    def get_Position(self):
        return self.Position

    def get_WeldingPointType(self):
        return self.WeldingPointType

    def get_WeldingPrgNo(self):
        return self.WeldingPrgNo

    def get_GroupID(self):
        return self.GroupID

    def set_GlobalId(self, GlobalId: str):
        self.GlobalId = GlobalId

    def set_WeldingOutput(self, WeldingOutput: float):
        self.WeldingOutput = WeldingOutput

    def set_Position(self, Position: float):
        self.Position = Position

    def set_WeldingPointType(self, WeldingPointType: int):
        self.WeldingPointType = WeldingPointType

    def set_WeldingPrgNo(self, WeldingPrgNo: int):
        self.WeldingPrgNo = WeldingPrgNo

    def set_GroupID(self, GroupID: str):
        self.GroupID = GroupID

    def __str__(self):
        return "GlobalId: " + str(self.GlobalId) + ", WeldingOutput: " + str(self.WeldingOutput) + ", Position: " + str(self.Position) + ", WeldingPointType: " + str(self.WeldingPointType) + ", WeldingPrgNo: " + str(self.WeldingPrgNo) + ", GroupID: " + str(self.GroupID)


    def __xml__(self):
        WeldingPoint = ET.Element('WeldingPoint')
        if self.GlobalId is not None:
            WeldingPoint.set('GlobalId', self.GlobalId)
        if self.WeldingOutput is not None:
            WeldingOutput = ET.SubElement(WeldingPoint, 'WeldingOutput')
            WeldingOutput.text = str(float(self.WeldingOutput))
        if self.Position is not None:
            Position = ET.SubElement(WeldingPoint, 'Position')
            Position.text = str(float(self.Position))
        if self.WeldingPointType is not None:
            WeldingPointType = ET.SubElement(WeldingPoint, 'WeldingPointType')
            WeldingPointType.text = str(int(self.WeldingPointType))
        if self.WeldingPrgNo is not None:
            WeldingPrgNo = ET.SubElement(WeldingPoint, 'WeldingPrgNo')
            WeldingPrgNo.text = str(int(self.WeldingPrgNo))
        if self.GroupID is not None:
            GroupID = ET.SubElement(WeldingPoint, 'GroupID')
            GroupID.text = str(self.GroupID)
        return WeldingPoint