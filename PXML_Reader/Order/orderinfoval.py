from xml.etree import ElementTree as ET

class OrderInfoVal():


    def __init__(self, Type: str, V: str, U: str, Culture: str):
        self.Type = None  # STR // 0,1
        self.V = None  # STR // 0,1
        self.U = None  # STR // 0,1
        self.Culture = "en"  # STR // 0,1
        self.Type = Type
        self.V = V
        self.U = U
        self.Culture = Culture

    def get_Type(self):
        return self.Type

    def get_V(self):
        return self.V

    def get_U(self):
        return self.U

    def get_Culture(self):
        return self.Culture

    def set_Type(self, Type: str):
        self.Type = Type

    def set_V(self, V: str):
        self.V = V

    def set_U(self, U: str):
        self.U = U

    def set_Culture(self, Culture: str):
        self.Culture = Culture

    def __str__(self):
        return "Type: " + str(self.Type) + ", V: " + str(self.V) + ", U: " + str(self.U) + ", Culture: " + str(self.Culture)

    def __xml__(self):
        OrderInfoVal = ET.Element("OrderInfoVal")
        OrderInfoVal.set("Type", self.Type)
        OrderInfoVal.set("V", self.V)
        OrderInfoVal.set("U", self.U)
        OrderInfoVal.set("Culture", self.Culture)

        return OrderInfoVal