import xml.etree.ElementTree as ET

class FbVal:
    T = None # STR // 0,1
    V = None # STR // 0,1

    def __init__(self, T: str = None, V: str = None):
        self.T = T
        self.V = V

    def get_T(self):
        return self.T

    def get_V(self):
        return self.V

    def set_T(self, T: str):
        self.T = T

    def set_V(self, V: str):
        self.V = V

    def __str__(self):
        return "T: " + str(self.T) + ", V: " + str(self.V)

    def __xml__(self):
        FbVal = ET.Element('FbVal')
        if self.T is not None:
            FbVal.set('T', self.T)
        if self.V is not None:
            FbVal.set('V', self.V)
        return FbVal