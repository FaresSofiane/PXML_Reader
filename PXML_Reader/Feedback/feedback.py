import xml.etree.ElementTree as ET
from .Description.description import Description
from .FbVal.fbval import FbVal

class Feedback:


    def __init__(self, GlobalID: str = None, ItemType: str = None, MessageType: str = None, Code: str = None, InfoValue: str = None, PieceCount: int = None, MaterialType: str = None, MaterialBatch: str = None, MaterialWeight: float = None, ProdDate: str = None, Machine: str = None, Description: list = [], FbVal: list = []):
        self.GlobalID = None  # STR // 0,1
        self.ItemType = None  # STR // 0,1
        self.MessageType = None  # STR // 0,1
        self.Code = None  # STR // 0,1
        self.InfoValue = None  # STR // 0,1
        self.PieceCount = None  # INT // 0,1
        self.MaterialType = None  # STR // 0,1
        self.MaterialBatch = None  # STR // 0,1
        self.MaterialWeight = None  # FLOAT // 0,1
        self.ProdDate = None  # STR // 0,1
        self.Machine = None  # STR // 0,1
        self.Description = []  # Description // n,n
        self.FbVal = []  # FbVal // n,n

        self.GlobalID = GlobalID
        self.ItemType = ItemType
        self.MessageType = MessageType
        self.Code = Code
        self.InfoValue = InfoValue
        if type(PieceCount) is int:
            self.PieceCount = PieceCount
        else:
            if PieceCount is None:
                self.PieceCount = None
            else:
                try:
                    self.PieceCount = int(PieceCount)
                except ValueError:
                    raise ValueError(f'PieceCount must be a int')

        self.MaterialType = MaterialType
        self.MaterialBatch = MaterialBatch
        if type(MaterialWeight) is float:
            self.MaterialWeight = float(MaterialWeight)
        else:
            if MaterialWeight is None:
                self.MaterialWeight = None
            else:
                try:
                    self.MaterialWeight = float(MaterialWeight)
                except ValueError:
                    raise ValueError(f'MaterialWeight must be a float')
        self.ProdDate = ProdDate
        self.Machine = Machine
        self.Description = Description
        self.FbVal = FbVal

    def get_GlobalID(self):
        return self.GlobalID

    def get_ItemType(self):
        return self.ItemType

    def get_MessageType(self):
        return self.MessageType

    def get_Code(self):
        return self.Code

    def get_InfoValue(self):
        return self.InfoValue

    def get_PieceCount(self):
        return self.PieceCount

    def get_MaterialType(self):
        return self.MaterialType

    def get_MaterialBatch(self):
        return self.MaterialBatch

    def get_MaterialWeight(self):
        return self.MaterialWeight

    def get_ProdDate(self):
        return self.ProdDate

    def get_Machine(self):
        return self.Machine

    def get_Description(self):
        return self.Description

    def get_FbVal(self):
        return self.FbVal

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_ItemType(self, ItemType: str):
        self.ItemType = ItemType

    def set_MessageType(self, MessageType: str):
        self.MessageType = MessageType

    def set_Code(self, Code: str):
        self.Code = Code

    def set_InfoValue(self, InfoValue: str):
        self.InfoValue = InfoValue

    def set_PieceCount(self, PieceCount: int):
        if type(PieceCount) is int:
            self.PieceCount = PieceCount
        else:
            raise TypeError("PieceCount must be an integer")

    def set_MaterialType(self, MaterialType: str):
        self.MaterialType = MaterialType

    def set_MaterialBatch(self, MaterialBatch: str):
        self.MaterialBatch = MaterialBatch

    def set_MaterialWeight(self, MaterialWeight: float):
        if type(MaterialWeight) is float:
            self.MaterialWeight = MaterialWeight
        else:
            raise TypeError("MaterialWeight must be a float")

    def set_ProdDate(self, ProdDate: str):
        self.ProdDate = ProdDate

    def set_Machine(self, Machine: str):
        self.Machine = Machine

    def set_Description(self, Description: list):
        self.Description = Description

    def set_FbVal(self, FbVal: list):
        self.FbVal = FbVal

    def add_Description(self, Description: Description) -> object:
        self.Description.append(Description)

    def add_FbVal(self, FbVal: FbVal) -> object:
        self.FbVal.append(FbVal)

    def __str__(self):
        return "GlobalID: " + str(self.GlobalID) + ", ItemType: " + str(self.ItemType) + ", MessageType: " + str(self.MessageType) + ", Code: " + str(self.Code) + ", InfoValue: " + str(self.InfoValue) + ", PieceCount: " + str(self.PieceCount) + ", MaterialType: " + str(self.MaterialType) + ", MaterialBatch: " + str(self.MaterialBatch) + ", MaterialWeight: " + str(self.MaterialWeight) + ", ProdDate: " + str(self.ProdDate) + ", Machine: " + str(self.Machine) + ", Description: " + str(self.Description) + ", FbVal: " + str(self.FbVal)

    def __xml__(self):
        Feedback = ET.Element('Feedback')
        if self.GlobalID is not None:
            Feedback.set('GlobalID', self.GlobalID)
        if self.ItemType is not None:
            Feedback.set('ItemType', self.ItemType)
        if self.MessageType is not None:
            MessageType = ET.SubElement(Feedback, 'MessageType')
            MessageType.text = self.MessageType
        if self.Code is not None:
            Code = ET.SubElement(Feedback, 'Code')
            Code.text = self.Code
        if self.InfoValue is not None:
            InfoValue = ET.SubElement(Feedback, 'InfoValue')
            InfoValue.text = self.InfoValue
        if self.PieceCount is not None:
            PieceCount = ET.SubElement(Feedback, 'PieceCount')
            PieceCount.text = str(self.PieceCount)
        if self.MaterialType is not None:
            MaterialType = ET.SubElement(Feedback, 'MaterialType')
            MaterialType.text = self.MaterialType
        if self.MaterialBatch is not None:
            MaterialBatch = ET.SubElement(Feedback, 'MaterialBatch')
            MaterialBatch.text = self.MaterialBatch
        if self.MaterialWeight is not None:
            MaterialWeight = ET.SubElement(Feedback, 'MaterialWeight')
            MaterialWeight.text = str(self.MaterialWeight)
        if self.ProdDate is not None:
            ProdDate = ET.SubElement(Feedback, 'ProdDate')
            ProdDate.text = self.ProdDate
        if self.Machine is not None:
            Machine = ET.SubElement(Feedback, 'Machine')
            Machine.text = self.Machine
        for Description in self.Description:
            Feedback.append(Description.__xml__())
        for FbVal in self.FbVal:
            Feedback.append(FbVal.__xml__())

        return Feedback