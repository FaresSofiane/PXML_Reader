import xml.etree.ElementTree as etree

class Order():
    GlobalID = "" # STR // Obligatoire 1,1
    OrderNo = None # INT // 0,1
    Structure = None # STR // 0,1
    Building = None # STR // 0,1
    Storey = None # STR // 0,1
    SubStorey = None # STR // 0,1
    Component = None # STR // 0,1
    DrawingNo = None # STR // 0,1
    DrawingDate = None # STR // 0,1
    DrawingRevision = None # STR // 0,1
    DrawingAuthor = None # STR // 0,1
    ErpProjectUnit = None # STR // 0,1
    DeliveryDate = None # STR // 0,1
    GenericOrderInfo01 = None # STR // 0,1
    GenericOrderInfo02 = None # STR // 0,1
    GenericOrderInfo03 = None # STR // 0,1
    GenericOrderInfo04 = None # STR // 0,1
    GenericOrderInfo05 = None # STR // 0,1
    GenericOrderInfo06 = None # STR // 0,1
    GenericOrderInfo07 = None # STR // 0,1
    GenericOrderInfo08 = None # STR // 0,1
    GenericOrderInfo09 = None # STR // 0,1
    GenericOrderInfo10 = None # STR // 0,1
    GenericOrderInfo11 = None # STR // 0,1
    GenericOrderInfo12 = None # STR // 0,1
    GenericOrderInfo13 = None # STR // 0,1
    GenericOrderInfo14 = None # STR // 0,1
    GenericOrderInfo15 = None # STR // 0,1
    GenericOrderInfo16 = None # STR // 0,1
    GenericOrderInfo17 = None # STR // 0,1
    GenericOrderInfo18 = None # STR // 0,1
    GenericOrderInfo19 = None # STR // 0,1
    GenericOrderInfo20 = None # STR // 0,1
    Comment = None # STR // 0,1
    OrderArea = None # FLOAT // 0,1
    ImportSource = None # STR // 0,1
    ImportSourceType = None # STR // 0,1
    ApplicationName = None # STR // 0,1
    ApplicationGUID = None # STR // 0,1
    ApplicationVersion = None # STR // 0,1
    OrderInfo = []# Object OrderInfo from the module orderinfo. n,n
    Product = []# Object Product from the module product. n,n

    def __init__(self, GlobalID: str, OrderNo: int, Structure: str, Building: str, Storey: str, SubStorey: str, Component: str, DrawingNo: str, DrawingDate: str, DrawingRevision: str, DrawingAuthor: str, ErpProjectUnit: str, DeliveryDate: str, GenericOrderInfo01: str, GenericOrderInfo02: str, GenericOrderInfo03: str, GenericOrderInfo04: str, GenericOrderInfo05: str, GenericOrderInfo06: str, GenericOrderInfo07: str, GenericOrderInfo08: str, GenericOrderInfo09: str, GenericOrderInfo10: str, GenericOrderInfo11: str, GenericOrderInfo12: str, GenericOrderInfo13: str, GenericOrderInfo14: str, GenericOrderInfo15: str, GenericOrderInfo16: str, GenericOrderInfo17: str, GenericOrderInfo18: str, GenericOrderInfo19: str, GenericOrderInfo20: str, Comment: str, OrderArea: float, ImportSource: str, ImportSourceType: str, ApplicationName: str, ApplicationGUID: str, ApplicationVersion: str, OrderInfo: list, Product: list):
        self.GlobalID = GlobalID
        self.OrderNo = OrderNo
        self.Structure = Structure
        self.Building = Building
        self.Storey = Storey
        self.SubStorey = SubStorey
        self.Component = Component
        self.DrawingNo = DrawingNo
        self.DrawingDate = DrawingDate
        self.DrawingRevision = DrawingRevision
        self.DrawingAuthor = DrawingAuthor
        self.ErpProjectUnit = ErpProjectUnit
        self.DeliveryDate = DeliveryDate
        self.GenericOrderInfo01 = GenericOrderInfo01
        self.GenericOrderInfo02 = GenericOrderInfo02
        self.GenericOrderInfo03 = GenericOrderInfo03
        self.GenericOrderInfo04 = GenericOrderInfo04
        self.GenericOrderInfo05 = GenericOrderInfo05
        self.GenericOrderInfo06 = GenericOrderInfo06
        self.GenericOrderInfo07 = GenericOrderInfo07
        self.GenericOrderInfo08 = GenericOrderInfo08
        self.GenericOrderInfo09 = GenericOrderInfo09
        self.GenericOrderInfo10 = GenericOrderInfo10
        self.GenericOrderInfo11 = GenericOrderInfo11
        self.GenericOrderInfo12 = GenericOrderInfo12
        self.GenericOrderInfo13 = GenericOrderInfo13
        self.GenericOrderInfo14 = GenericOrderInfo14
        self.GenericOrderInfo15 = GenericOrderInfo15
        self.GenericOrderInfo16 = GenericOrderInfo16
        self.GenericOrderInfo17 = GenericOrderInfo17
        self.GenericOrderInfo18 = GenericOrderInfo18
        self.GenericOrderInfo19 = GenericOrderInfo19
        self.GenericOrderInfo20 = GenericOrderInfo20
        self.Comment = Comment
        if type(OrderArea) is float:
            self.OrderArea = float(OrderArea)
        else:
            if OrderArea is None:
                self.OrderArea = None
            else:
                try:
                    self.OrderArea = float(OrderArea)
                except ValueError:
                    raise TypeError("OrderArea must be a float")
        self.ImportSource = ImportSource
        self.ImportSourceType = ImportSourceType
        self.ApplicationName = ApplicationName
        self.ApplicationGUID = ApplicationGUID
        self.ApplicationVersion = ApplicationVersion
        self.OrderInfo = OrderInfo
        self.Product = Product

    def get_GlobalID(self):
        return self.GlobalID

    def get_OrderNo(self):
        return self.OrderNo

    def get_Structure(self):
        return self.Structure

    def get_Building(self):
        return self.Building

    def get_Storey(self):
        return self.Storey

    def get_SubStorey(self):
        return self.SubStorey

    def get_Component(self):
        return self.Component

    def get_DrawingNo(self):
        return self.DrawingNo

    def get_DrawingDate(self):
        return self.DrawingDate

    def get_DrawingRevision(self):
        return self.DrawingRevision

    def get_DrawingAuthor(self):
        return self.DrawingAuthor

    def get_ErpProjectUnit(self):
        return self.ErpProjectUnit

    def get_DeliveryDate(self):
        return self.DeliveryDate

    def get_GenericOrderInfo01(self):
        return self.GenericOrderInfo01

    def get_GenericOrderInfo02(self):
        return self.GenericOrderInfo02

    def get_GenericOrderInfo03(self):
        return self.GenericOrderInfo03

    def get_GenericOrderInfo04(self):
        return self.GenericOrderInfo04

    def get_GenericOrderInfo05(self):
        return self.GenericOrderInfo05

    def get_GenericOrderInfo06(self):
        return self.GenericOrderInfo06

    def get_GenericOrderInfo07(self):
        return self.GenericOrderInfo07

    def get_GenericOrderInfo08(self):
        return self.GenericOrderInfo08

    def get_GenericOrderInfo09(self):
        return self.GenericOrderInfo09

    def get_GenericOrderInfo10(self):
        return self.GenericOrderInfo10

    def get_GenericOrderInfo11(self):
        return self.GenericOrderInfo11

    def get_GenericOrderInfo12(self):
        return self.GenericOrderInfo12

    def get_GenericOrderInfo13(self):
        return self.GenericOrderInfo13

    def get_GenericOrderInfo14(self):
        return self.GenericOrderInfo14

    def get_GenericOrderInfo15(self):
        return self.GenericOrderInfo15

    def get_GenericOrderInfo16(self):
        return self.GenericOrderInfo16

    def get_GenericOrderInfo17(self):
        return self.GenericOrderInfo17

    def get_GenericOrderInfo18(self):
        return self.GenericOrderInfo18

    def get_GenericOrderInfo19(self):
        return self.GenericOrderInfo19

    def get_GenericOrderInfo20(self):
        return self.GenericOrderInfo20

    def get_Comment(self):
        return self.Comment

    def get_OrderArea(self):
        return self.OrderArea

    def get_ImportSource(self):
        return self.ImportSource

    def get_ImportSourceType(self):
        return self.ImportSourceType

    def get_ApplicationName(self):
        return self.ApplicationName

    def get_ApplicationGUID(self):
        return self.ApplicationGUID

    def get_ApplicationVersion(self):
        return self.ApplicationVersion

    def get_OrderInfo(self):
        return self.OrderInfo

    def get_Product(self):
        return self.Product

    def set_GlobalID(self, GlobalID: str):
        if type(GlobalID) is str:
            self.GlobalID = GlobalID
        else:
            raise TypeError("GlobalID must be a string")

    def set_OrderNo(self, OrderNo: int):
        if type(OrderNo) is int:
            self.OrderNo = OrderNo
        else:
            raise TypeError("OrderNo must be an integer")

    def set_Structure(self, Structure: str):
        if type(Structure) is str:
            self.Structure = Structure
        else:
            raise TypeError("Structure must be a string")

    def set_Building(self, Building: str):
        if type(Building) is str:
            self.Building = Building
        else:
            raise TypeError("Building must be a string")

    def set_Storey(self, Storey: str):
        if type(Storey) is str:
            self.Storey = Storey
        else:
            raise TypeError("Storey must be a string")

    def set_SubStorey(self, SubStorey: str):
        if type(SubStorey) is str:
            self.SubStorey = SubStorey
        else:
            raise TypeError("SubStorey must be a string")

    def set_Component(self, Component: str):
        if type(Component) is str:
            self.Component = Component
        else:
            raise TypeError("Component must be a string")

    def set_DrawingNo(self, DrawingNo: str):
        if type(DrawingNo) is str:
            self.DrawingNo = DrawingNo
        else:
            raise TypeError("DrawingNo must be a string")

    def set_DrawingDate(self, DrawingDate: str):
        if type(DrawingDate) is str:
            self.DrawingDate = DrawingDate
        else:
            raise TypeError("DrawingDate must be a string")

    def set_DrawingRevision(self, DrawingRevision: str):
        if type(DrawingRevision) is str:
            self.DrawingRevision = DrawingRevision
        else:
            raise TypeError("DrawingRevision must be a string")

    def set_DrawingAuthor(self, DrawingAuthor: str):
        if type(DrawingAuthor) is str:
            self.DrawingAuthor = DrawingAuthor
        else:
            raise TypeError("DrawingAuthor must be a string")

    def set_ErpProjectUnit(self, ErpProjectUnit: str):
        if type(ErpProjectUnit) is str:
            self.ErpProjectUnit = ErpProjectUnit
        else:
            raise TypeError("ErpProjectUnit must be a string")

    def set_DeliveryDate(self, DeliveryDate: str):
        if type(DeliveryDate) is str:
            self.DeliveryDate = DeliveryDate
        else:
            raise TypeError("DeliveryDate must be a string")

    def set_GenericOrderInfo01(self, GenericOrderInfo01: str):
        if type(GenericOrderInfo01) is str:
            self.GenericOrderInfo01 = GenericOrderInfo01
        else:
            raise TypeError("GenericOrderInfo01 must be a string")

    def set_GenericOrderInfo02(self, GenericOrderInfo02: str):
        if type(GenericOrderInfo02) is str:
            self.GenericOrderInfo02 = GenericOrderInfo02
        else:
            raise TypeError("GenericOrderInfo02 must be a string")

    def set_GenericOrderInfo03(self, GenericOrderInfo03: str):
        if type(GenericOrderInfo03) is str:
            self.GenericOrderInfo03 = GenericOrderInfo03
        else:
            raise TypeError("GenericOrderInfo03 must be a string")

    def set_GenericOrderInfo04(self, GenericOrderInfo04: str):
        if type(GenericOrderInfo04) is str:
            self.GenericOrderInfo04 = GenericOrderInfo04
        else:
            raise TypeError("GenericOrderInfo04 must be a string")

    def set_GenericOrderInfo05(self, GenericOrderInfo05: str):
        if type(GenericOrderInfo05) is str:
            self.GenericOrderInfo05 = GenericOrderInfo05
        else:
            raise TypeError("GenericOrderInfo05 must be a string")

    def set_GenericOrderInfo06(self, GenericOrderInfo06: str):
        if type(GenericOrderInfo06) is str:
            self.GenericOrderInfo06 = GenericOrderInfo06
        else:
            raise TypeError("GenericOrderInfo06 must be a string")

    def set_GenericOrderInfo07(self, GenericOrderInfo07: str):
        if type(GenericOrderInfo07) is str:
            self.GenericOrderInfo07 = GenericOrderInfo07
        else:
            raise TypeError("GenericOrderInfo07 must be a string")

    def set_GenericOrderInfo08(self, GenericOrderInfo08: str):
        if type(GenericOrderInfo08) is str:
            self.GenericOrderInfo08 = GenericOrderInfo08
        else:
            raise TypeError("GenericOrderInfo08 must be a string")

    def set_GenericOrderInfo09(self, GenericOrderInfo09: str):
        if type(GenericOrderInfo09) is str:
            self.GenericOrderInfo09 = GenericOrderInfo09
        else:
            raise TypeError("GenericOrderInfo09 must be a string")

    def set_GenericOrderInfo10(self, GenericOrderInfo10: str):
        if type(GenericOrderInfo10) is str:
            self.GenericOrderInfo10 = GenericOrderInfo10
        else:
            raise TypeError("GenericOrderInfo10 must be a string")

    def set_GenericOrderInfo11(self, GenericOrderInfo11: str):
        if type(GenericOrderInfo11) is str:
            self.GenericOrderInfo11 = GenericOrderInfo11
        else:
            raise TypeError("GenericOrderInfo11 must be a string")

    def set_GenericOrderInfo12(self, GenericOrderInfo12: str):
        if type(GenericOrderInfo12) is str:
            self.GenericOrderInfo12 = GenericOrderInfo12
        else:
            raise TypeError("GenericOrderInfo12 must be a string")

    def set_GenericOrderInfo13(self, GenericOrderInfo13: str):
        if type(GenericOrderInfo13) is str:
            self.GenericOrderInfo13 = GenericOrderInfo13
        else:
            raise TypeError("GenericOrderInfo13 must be a string")

    def set_GenericOrderInfo14(self, GenericOrderInfo14: str):
        if type(GenericOrderInfo14) is str:
            self.GenericOrderInfo14 = GenericOrderInfo14
        else:
            raise TypeError("GenericOrderInfo14 must be a string")

    def set_GenericOrderInfo15(self, GenericOrderInfo15: str):
        if type(GenericOrderInfo15) is str:
            self.GenericOrderInfo15 = GenericOrderInfo15
        else:
            raise TypeError("GenericOrderInfo15 must be a string")

    def set_GenericOrderInfo16(self, GenericOrderInfo16: str):
        if type(GenericOrderInfo16) is str:
            self.GenericOrderInfo16 = GenericOrderInfo16
        else:
            raise TypeError("GenericOrderInfo16 must be a string")

    def set_GenericOrderInfo17(self, GenericOrderInfo17: str):
        if type(GenericOrderInfo17) is str:
            self.GenericOrderInfo17 = GenericOrderInfo17
        else:
            raise TypeError("GenericOrderInfo17 must be a string")

    def set_GenericOrderInfo18(self, GenericOrderInfo18: str):
        if type(GenericOrderInfo18) is str:
            self.GenericOrderInfo18 = GenericOrderInfo18
        else:
            raise TypeError("GenericOrderInfo18 must be a string")

    def set_GenericOrderInfo19(self, GenericOrderInfo19: str):
        if type(GenericOrderInfo19) is str:
            self.GenericOrderInfo19 = GenericOrderInfo19
        else:
            raise TypeError("GenericOrderInfo19 must be a string")

    def set_GenericOrderInfo20(self, GenericOrderInfo20: str):
        if type(GenericOrderInfo20) is str:
            self.GenericOrderInfo20 = GenericOrderInfo20
        else:
            raise TypeError("GenericOrderInfo20 must be a string")

    def set_Comment(self, Comment: str):
        if type(Comment) is str:
            self.Comment = Comment
        else:
            raise TypeError("Comment must be a string")

    def set_OrderArea(self, OrderArea: float):
        if type(OrderArea) is float:
            self.OrderArea = OrderArea
        else:
            raise TypeError("OrderArea must be a float")

    def set_ImportSource(self, ImportSource: str):
        if type(ImportSource) is str:
            self.ImportSource = ImportSource
        else:
            raise TypeError("ImportSource must be a string")

    def set_ImportSourceType(self, ImportSourceType: str):
        if type(ImportSourceType) is str:
            self.ImportSourceType = ImportSourceType
        else:
            raise TypeError("ImportSourceType must be a string")

    def set_ApplicationName(self, ApplicationName: str):
        if type(ApplicationName) is str:
            self.ApplicationName = ApplicationName
        else:
            raise TypeError("ApplicationName must be a string")

    def set_ApplicationGUID(self, ApplicationGUID: str):
        if type(ApplicationGUID) is str:
            self.ApplicationGUID = ApplicationGUID
        else:
            raise TypeError("ApplicationGUID must be a string")

    def set_ApplicationVersion(self, ApplicationVersion: str):
        if type(ApplicationVersion) is str:
            self.ApplicationVersion = ApplicationVersion
        else:
            raise TypeError("ApplicationVersion must be a string")

    def set_OrderInfo(self, OrderInfo: list):
        self.OrderInfo = OrderInfo

    def set_Product(self, Product: list):
        self.Product = Product

    def add_OrderInfo(self, OrderInfo: OrderInfo) -> object:
        self.OrderInfo.append(OrderInfo)

    def add_Product(self, Product: Product) -> object:
        self.Product.append(Product)

    def __str__(self):
        return "GlobalID: " + str(self.GlobalID) + ", OrderNo: " + str(self.OrderNo) + ", Structure: " + str(self.Structure) + ", Building: " + str(self.Building) + ", Storey: " + str(self.Storey) + ", SubStorey: " + str(self.SubStorey) + ", Component: " + str(self.Component) + ", DrawingNo: " + str(self.DrawingNo) + ", DrawingDate: " + str(self.DrawingDate) + ", DrawingRevision: " + str(self.DrawingRevision) + ", DrawingAuthor: " + str(self.DrawingAuthor) + ", ErpProjectUnit: " + str(self.ErpProjectUnit) + ", DeliveryDate: " + str(self.DeliveryDate) + ", GenericOrderInfo01: " + str(self.GenericOrderInfo01) + ", GenericOrderInfo02: " + str(self.GenericOrderInfo02) + ", GenericOrderInfo03: " + str(self.GenericOrderInfo03) + ", GenericOrderInfo04: " + str(self.GenericOrderInfo04) + ", GenericOrderInfo05: " + str(self.GenericOrderInfo05) + ", GenericOrderInfo06: " + str(self.GenericOrderInfo06) + ", GenericOrderInfo07: " + str(self.GenericOrderInfo07) + ", GenericOrderInfo08: " + str(self.GenericOrderInfo08) + ", GenericOrderInfo09: " + str(self.GenericOrderInfo09) + ", GenericOrderInfo10: " + str(self.GenericOrderInfo10) + ", GenericOrderInfo11: " + str(self.GenericOrderInfo11) + ", GenericOrderInfo12: " + str(self.GenericOrderInfo12) + ", GenericOrderInfo13: " + str(self.GenericOrderInfo13) + ", GenericOrderInfo14: " + str(self.GenericOrderInfo14) + ", GenericOrderInfo15: " + str(self.GenericOrderInfo15) + ", GenericOrderInfo16: " + str(self.GenericOrderInfo16) + ", GenericOrderInfo17: " + str(self.GenericOrderInfo17) + ", GenericOrderInfo18: " + str(self.GenericOrderInfo18) + ", GenericOrderInfo19: " + str(self.GenericOrderInfo19) + ", GenericOrderInfo20: " + str(self.GenericOrderInfo20) + ", Comment: " + str(self.Comment) + ", OrderArea: " + str(self.OrderArea) + ", ImportSource: " + str(self.ImportSource) + ", ImportSourceType: " + str(self.ImportSourceType) + ", ApplicationName: " + str(self.ApplicationName) + ", ApplicationGUID: " + str(self.ApplicationGUID) + ", ApplicationVersion: " + str(self.ApplicationVersion) + ", OrderInfo: " + str(self.OrderInfo) + ", Product: " + str(self.Product)


    def __xml__(self):
        Order = etree.Element("Order")
        Order.set("GlobalID", self.GlobalID)
        if self.OrderNo is not None:
            OrderNo = etree.SubElement(Order, "OrderNo")
            OrderNo.text = str(self.OrderNo)
        if self.Structure is not None:
            Structure = etree.SubElement(Order, "Structure")
            Structure.text = str(self.Structure)
        if self.Building is not None:
            Building = etree.SubElement(Order, "Building")
            Building.text = str(self.Building)
        if self.Storey is not None:
            Storey = etree.SubElement(Order, "Storey")
            Storey.text = str(self.Storey)
        if self.SubStorey is not None:
            SubStorey = etree.SubElement(Order, "SubStorey")
            SubStorey.text = str(self.SubStorey)
        if self.Component is not None:
            Component = etree.SubElement(Order, "Component")
            Component.text = str(self.Component)
        if self.DrawingNo is not None:
            DrawingNo = etree.SubElement(Order, "DrawingNo")
            DrawingNo.text = str(self.DrawingNo)
        if self.DrawingDate is not None:
            DrawingDate = etree.SubElement(Order, "DrawingDate")
            DrawingDate.text = str(self.DrawingDate)
        if self.DrawingRevision is not None:
            DrawingRevision = etree.SubElement(Order, "DrawingRevision")
            DrawingRevision.text = str(self.DrawingRevision)
        if self.DrawingAuthor is not None:
            DrawingAuthor = etree.SubElement(Order, "DrawingAuthor")
            DrawingAuthor.text = str(self.DrawingAuthor)
        if self.ErpProjectUnit is not None:
            ErpProjectUnit = etree.SubElement(Order, "ErpProjectUnit")
            ErpProjectUnit.text = str(self.ErpProjectUnit)
        if self.DeliveryDate is not None:
            DeliveryDate = etree.SubElement(Order, "DeliveryDate")
            DeliveryDate.text = str(self.DeliveryDate)
        if self.GenericOrderInfo01 is not None:
            GenericOrderInfo01 = etree.SubElement(Order, "GenericOrderInfo01")
            GenericOrderInfo01.text = str(self.GenericOrderInfo01)
        if self.GenericOrderInfo02 is not None:
            GenericOrderInfo02 = etree.SubElement(Order, "GenericOrderInfo02")
            GenericOrderInfo02.text = str(self.GenericOrderInfo02)
        if self.GenericOrderInfo03 is not None:
            GenericOrderInfo03 = etree.SubElement(Order, "GenericOrderInfo03")
            GenericOrderInfo03.text = str(self.GenericOrderInfo03)
        if self.GenericOrderInfo04 is not None:
            GenericOrderInfo04 = etree.SubElement(Order, "GenericOrderInfo04")
            GenericOrderInfo04.text = str(self.GenericOrderInfo04)
        if self.GenericOrderInfo05 is not None:
            GenericOrderInfo05 = etree.SubElement(Order, "GenericOrderInfo05")
            GenericOrderInfo05.text = str(self.GenericOrderInfo05)
        if self.GenericOrderInfo06 is not None:
            GenericOrderInfo06 = etree.SubElement(Order, "GenericOrderInfo06")
            GenericOrderInfo06.text = str(self.GenericOrderInfo06)
        if self.GenericOrderInfo07 is not None:
            GenericOrderInfo07 = etree.SubElement(Order, "GenericOrderInfo07")
            GenericOrderInfo07.text = str(self.GenericOrderInfo07)
        if self.GenericOrderInfo08 is not None:
            GenericOrderInfo08 = etree.SubElement(Order, "GenericOrderInfo08")
            GenericOrderInfo08.text = str(self.GenericOrderInfo08)
        if self.GenericOrderInfo09 is not None:
            GenericOrderInfo09 = etree.SubElement(Order, "GenericOrderInfo09")
            GenericOrderInfo09.text = str(self.GenericOrderInfo09)
        if self.GenericOrderInfo10 is not None:
            GenericOrderInfo10 = etree.SubElement(Order, "GenericOrderInfo10")
            GenericOrderInfo10.text = str(self.GenericOrderInfo10)
        if self.GenericOrderInfo11 is not None:
            GenericOrderInfo11 = etree.SubElement(Order, "GenericOrderInfo11")
            GenericOrderInfo11.text = str(self.GenericOrderInfo11)
        if self.GenericOrderInfo12 is not None:
            GenericOrderInfo12 = etree.SubElement(Order, "GenericOrderInfo12")
            GenericOrderInfo12.text = str(self.GenericOrderInfo12)
        if self.GenericOrderInfo13 is not None:
            GenericOrderInfo13 = etree.SubElement(Order, "GenericOrderInfo13")
            GenericOrderInfo13.text = str(self.GenericOrderInfo13)
        if self.GenericOrderInfo14 is not None:
            GenericOrderInfo14 = etree.SubElement(Order, "GenericOrderInfo14")
            GenericOrderInfo14.text = str(self.GenericOrderInfo14)
        if self.GenericOrderInfo15 is not None:
            GenericOrderInfo15 = etree.SubElement(Order, "GenericOrderInfo15")
            GenericOrderInfo15.text = str(self.GenericOrderInfo15)
        if self.GenericOrderInfo16 is not None:
            GenericOrderInfo16 = etree.SubElement(Order, "GenericOrderInfo16")
            GenericOrderInfo16.text = str(self.GenericOrderInfo16)
        if self.GenericOrderInfo17 is not None:
            GenericOrderInfo17 = etree.SubElement(Order, "GenericOrderInfo17")
            GenericOrderInfo17.text = str(self.GenericOrderInfo17)
        if self.GenericOrderInfo18 is not None:
            GenericOrderInfo18 = etree.SubElement(Order, "GenericOrderInfo18")
            GenericOrderInfo18.text = str(self.GenericOrderInfo18)
        if self.GenericOrderInfo19 is not None:
            GenericOrderInfo19 = etree.SubElement(Order, "GenericOrderInfo19")
            GenericOrderInfo19.text = str(self.GenericOrderInfo19)
        if self.GenericOrderInfo20 is not None:
            GenericOrderInfo20 = etree.SubElement(Order, "GenericOrderInfo20")
            GenericOrderInfo20.text = str(self.GenericOrderInfo20)
        if self.Comment is not None:
            Comment = etree.SubElement(Order, "Comment")
            Comment.text = str(self.Comment)
        if self.OrderArea is not None:
            OrderArea = etree.SubElement(Order, "OrderArea")
            OrderArea.text = str(self.OrderArea)
        if self.ImportSource is not None:
            ImportSource = etree.SubElement(Order, "ImportSource")
            ImportSource.text = str(self.ImportSource)
        if self.ImportSourceType is not None:
            ImportSourceType = etree.SubElement(Order, "ImportSourceType")
            ImportSourceType.text = str(self.ImportSourceType)
        if self.ApplicationName is not None:
            ApplicationName = etree.SubElement(Order, "ApplicationName")
            ApplicationName.text = str(self.ApplicationName)
        if self.ApplicationGUID is not None:
            ApplicationGUID = etree.SubElement(Order, "ApplicationGUID")
            ApplicationGUID.text = str(self.ApplicationGUID)
        if self.ApplicationVersion is not None:
            ApplicationVersion = etree.SubElement(Order, "ApplicationVersion")
            ApplicationVersion.text = str(self.ApplicationVersion)
        for OrderInfo in self.OrderInfo:
            Order.append(OrderInfo.__xml__())
        for Product in self.Product:
            Order.append(Product.__xml__())
        return Order




