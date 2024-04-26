from xml.etree import ElementTree as ET

class ElemInfoVal():
    Type = None # STR // 0,1
    V = None # STR // 0,1

    def __init__(self, Type: str, V: str):
        self.Type = Type
        self.V = V

    def get_Type(self):
        return self.Type

    def get_V(self):
        return self.V

    def set_Type(self, Type: str):
        self.Type = Type

    def set_V(self, V: str):
        self.V = V

    def __str__(self):
        return "Type: " + str(self.Type) + ", V: " + str(self.V)

    def __xml__(self):
        ElemInfoVal = ET.Element("ElemInfoVal")
        ElemInfoVal.set("Type", self.Type)
        ElemInfoVal.set("V", self.V)

        return ElemInfoVal