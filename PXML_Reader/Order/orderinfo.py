from .orderinfoval import OrderInfoVal
from xml.etree import ElementTree as ET

class OrderInfo():


    def __init__(self, Type: str, GlobalID: str, Code: str, OrderInfoVal: list):
        self.Type = None  # STR // 0,1
        self.GlobalID = None  # STR // 0,1
        self.Code = None  # STR // 0,1
        self.OrderInfoVal = []  # Object OrderInfoVal from the module orderinfoval. n,n

        self.Type = Type
        self.GlobalID = GlobalID
        self.Code = Code
        self.OrderInfoVal = OrderInfoVal

    def get_Type(self):
        return self.Type

    def get_GlobalID(self):
        return self.GlobalID

    def get_Code(self):
        return self.Code

    def get_OrderInfoVal(self):
        return self.OrderInfoVal

    def set_Type(self, Type: str):
        self.Type = Type

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_Code(self, Code: str):
        self.Code = Code

    def set_OrderInfoVal(self, OrderInfoVal: list):
        self.OrderInfoVal = OrderInfoVal

    def add_OrderInfoVal(self, OrderInfoVal: OrderInfoVal) -> object:
        self.OrderInfoVal.append(OrderInfoVal)

    def __str__(self):
        return "Type: " + str(self.Type) + ", GlobalID: " + str(self.GlobalID) + ", Code: " + str(self.Code) + ", OrderInfoVal: " + str(self.OrderInfoVal)

    def __xml__(self):
        OrderInfo = ET.Element("OrderInfo")
        OrderInfo.set("Type", self.Type)
        OrderInfo.set("GlobalID", self.GlobalID)
        if self.Code is not None:
            Code = ET.SubElement(OrderInfo, "Code")
            Code.text = self.Code

        for OrderInfoVal in self.OrderInfoVal:
            OrderInfo.append(OrderInfoVal.__xml__())

        return OrderInfo

