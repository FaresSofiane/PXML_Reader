import xml.etree.ElementTree as ET

class Mode():

    def __init__(self,ID, Val=None):
        self.ID = None # STR // Obligatoire 1,1
        self.Val = True # Bool // 0,1

        self.ID = ID
        self.Val = Val

        if self.ID is None:
            raise ValueError("ID in Mode cannot be None. Read https://www.pxml.eu/PXML-Specification-1.3-EN.pdf")

    def get_ID(self):
        return self.ID

    def get_Val(self):
        return self.Val

    def set_ID(self,ID):
        self.ID = ID

    def set_Val(self, Val):
        self.Val = Val

    def __str__(self):
        return "ID: " + str(self.ID) + ", Val: " + str(self.Val)

    def __xml__(self):

        Mode = ET.Element("Mode")
        ID = ET.SubElement(Mode, "ID")
        ID.text = self.ID
        if self.Val is not None:
            Val = ET.SubElement(Mode, "Val")
            Val.text = str(self.Val)

        return Mode

