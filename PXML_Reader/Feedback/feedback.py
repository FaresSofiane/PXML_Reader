class Feedback:
    GlobalID = None # STR // 0,1
    ItemType= None # STR // 0,1
    MessageType = None # STR // 0,1
    Code = None # STR // 0,1
    InfoValue = None # STR // 0,1
    PieceCount = None # INT // 0,1
    MaterialType = None # STR // 0,1
    MaterialBatch = None # STR // 0,1
    MaterialWeight = None # FLOAT // 0,1
    ProdDate = None # STR // 0,1
    Machine = None # STR // 0,1
    Description = [] # Description // n,n
    FbValue = [] # FbValue // n,n

    def __init__(self, GlobalID: str = None, ItemType: str = None, MessageType: str = None, Code: str = None, InfoValue: str = None, PieceCount: int = None, MaterialType: str = None, MaterialBatch: str = None, MaterialWeight: float = None, ProdDate: str = None, Machine: str = None, Description: list = [], FbValue: list = []):
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
        self.FbValue = FbValue

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

    def get_FbValue(self):
        return self.FbValue

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

    def set_FbValue(self, FbValue: list):
        self.FbValue = FbValue

    def add_Description(self, Description: Description) -> object:
        self.Description.append(Description)

    def add_FbValue(self, FbValue: FbValue) -> object:
        self.FbValue.append(FbValue)

    def __str__(self):
        return "GlobalID: " + str(self.GlobalID) + ", ItemType: " + str(self.ItemType) + ", MessageType: " + str(self.MessageType) + ", Code: " + str(self.Code) + ", InfoValue: " + str(self.InfoValue) + ", PieceCount: " + str(self.PieceCount) + ", MaterialType: " + str(self.MaterialType) + ", MaterialBatch: " + str(self.MaterialBatch) + ", MaterialWeight: " + str(self.MaterialWeight) + ", ProdDate: " + str(self.ProdDate) + ", Machine: " + str(self.Machine) + ", Description: " + str(self.Description) + ", FbValue: " + str(self.FbValue)

