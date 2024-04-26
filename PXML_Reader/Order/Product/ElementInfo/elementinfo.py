import xml.etree.ElementTree as ET

class ElementInfo():
    Type = None # STR // 1,1
    Inventory = False # BOOL // 1,1
    GlobalID = None # STR // 1,1
    Code = None # STR // 1,1
    Description = None # STR // 0,1
    ObjectID = None # STR // 0,1
    PieceCount = None # INT // 0,1
    Val1 = None # FLOAT // 0,1
    Val2 = None # FLOAT // 0,1
    Unit = "m^2" # STR // 0,1
    Details = None # STR // 0,1
    ElementInfoVal = [] # Object ElementInfo from the module elementinfo. n,n

    def __init__(self, Type: str, Inventory: bool, GlobalID: str, Code: str, Description: str, ObjectID: str, PieceCount: int, Val1: float, Val2: float, Unit: str, Details: str, ElementInfoVal: list):
        self.Type = Type
        self.Inventory = Inventory
        self.GlobalID = GlobalID
        self.Code = Code
        self.Description = Description
        self.ObjectID = ObjectID
        if type(PieceCount) is int:
            self.PieceCount = int(PieceCount)
        else:
            if PieceCount is None:
                self.PieceCount = None
            else:
                try:
                    self.PieceCount = int(PieceCount)
                except:
                    raise ValueError("PieceCount must be an integer.")

        if type(Val1) is float:
            self.Val1 = float(Val1)
        else:
            if Val1 is None:
                self.Val1 = None
            else:
                try:
                    self.Val1 = float(Val1)
                except:
                    raise ValueError("Val1 must be a float.")

        if type(Val2) is float:
            self.Val2 = float(Val2)
        else:
            if Val2 is None:
                self.Val2 = None
            else:
                try:
                    self.Val2 = float(Val2)
                except:
                    raise ValueError("Val2 must be a float.")
        self.Unit = Unit
        self.Details = Details
        self.ElementInfoVal = ElementInfoVal

    def get_Type(self):
        return self.Type

    def get_Inventory(self):
        return self.Inventory

    def get_GlobalID(self):
        return self.GlobalID

    def get_Code(self):
        return self.Code

    def get_Description(self):
        return self.Description

    def get_ObjectID(self):
        return self.ObjectID

    def get_PieceCount(self):
        return self.PieceCount

    def get_Val1(self):
        return self.Val1

    def get_Val2(self):
        return self.Val2

    def get_Unit(self):
        return self.Unit

    def get_Details(self):
        return self.Details

    def get_ElementInfoVal(self):
        return self.ElementInfoVal

    def set_Type(self, Type: str):
        self.Type = Type

    def set_Inventory(self, Inventory: bool):
        self.Inventory = Inventory

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_Code(self, Code: str):
        self.Code = Code

    def set_Description(self, Description: str):
        self.Description = Description

    def set_ObjectID(self, ObjectID: str):
        self.ObjectID = ObjectID

    def set_PieceCount(self, PieceCount: int):
        self.PieceCount = PieceCount

    def set_Val1(self, Val1: float):
        self.Val1 = Val1

    def set_Val2(self, Val2: float):
        self.Val2 = Val2

    def set_Unit(self, Unit: str):
        self.Unit = Unit

    def set_Details(self, Details: str):
        self.Details = Details

    def set_ElementInfoVal(self, ElementInfoVal: list):
        self.ElementInfoVal = ElementInfoVal

    def add_ElementInfoVal(self, ElementInfoVal) -> object:
        self.ElementInfoVal.append(ElementInfoVal)

    def __str__(self):
        return "Type: " + str(self.Type) + ", Inventory: " + str(self.Inventory) + ", GlobalID: " + str(self.GlobalID) + ", Code: " + str(self.Code) + ", Description: " + str(self.Description) + ", ObjectID: " + str(self.ObjectID) + ", PieceCount: " + str(self.PieceCount) + ", Val1: " + str(self.Val1) + ", Val2: " + str(self.Val2) + ", Unit: " + str(self.Unit) + ", Details: " + str(self.Details) + ", ElementInfoVal: " + str(self.ElementInfoVal)

    def __xml__(self):
        ElementInfo = ET.Element("ElementInfo")
        ElementInfo.set("Type", self.Type)
        ElementInfo.set("Inventory", str(self.Inventory))
        ElementInfo.set("GlobalID", self.GlobalID)

        if self.Code is not None:
            Code = ET.SubElement(ElementInfo, "Code")
            Code.text = self.Code
        if self.Description is not None:
            Description = ET.SubElement(ElementInfo, "Description")
            Description.text = self.Description
        if self.ObjectID is not None:
            ObjectID = ET.SubElement(ElementInfo, "ObjectID")
            ObjectID.text = self.ObjectID
        if self.PieceCount is not None:
            PieceCount = ET.SubElement(ElementInfo, "PieceCount")
            PieceCount.text = str(self.PieceCount)
        if self.Val1 is not None:
            Val1 = ET.SubElement(ElementInfo, "Val1")
            Val1.text = str(self.Val1)
        if self.Val2 is not None:
            Val2 = ET.SubElement(ElementInfo, "Val2")
            Val2.text = str(self.Val2)
        if self.Unit is not None:
            Unit = ET.SubElement(ElementInfo, "Unit")
            Unit.text = self.Unit
        if self.Details is not None:
            Details = ET.SubElement(ElementInfo, "Details")
            Details.text = self.Details

        for ElementInfoVal in self.ElementInfoVal:
            ElementInfo.append(ElementInfoVal.__xml__())

        return ElementInfo