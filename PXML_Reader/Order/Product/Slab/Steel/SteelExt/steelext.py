class SteelExt:
    GlobalID = None # STR // 0,1
    Type = None # STR // 0,1
    Info = None # STR // 0,1

    def __init__(self, GlobalID: str = None, Type: str = None, Info: str = None):
        self.GlobalID = GlobalID
        self.Type = Type
        self.Info = Info

    def get_GlobalID(self):
        return self.GlobalID

    def get_Type(self):
        return self.Type

    def get_Info(self):
        return self.Info

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_Type(self, Type: str):
        self.Type = Type

    def set_Info(self, Info: str):
        self.Info = Info

    def __str__(self):
        return "GlobalID: " + str(self.GlobalID) + ", Type: " + str(self.Type) + ", Info: " + str(self.Info)
