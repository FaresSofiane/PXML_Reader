class AnchorBar():
    GlobalID = None # STR // 0,1
    Type = None # INT // 0,1
    Length = None # FLOAT // 0,1
    Position = None # FLOAT // 0,1

    def __init__(self, GlobalID: str = None, Type: int = None, Length: float = None, Position: float = None):
        self.GlobalID = GlobalID
        if type(Type) is int:
            self.Type = int(Type)
        else:
            if Type is None:
                self.Type = None
            else:
                try:
                    self.Type = int(Type)
                except ValueError:
                    raise ValueError(f'Type must be a int')
        if type(Length) is float:
            self.Length = float(Length)
        else:
            if Length is None:
                self.Length = None
            else:
                try:
                    self.Length = float(Length)
                except ValueError:
                    raise ValueError(f'Length must be a float')
        if type(Position) is float:
            self.Position = float(Position)
        else:
            if Position is None:
                self.Position = None
            else:
                try:
                    self.Position = float(Position)
                except ValueError:
                    raise ValueError(f'Position must be a float')

    def get_GlobalID(self):
        return self.GlobalID

    def get_Type(self):
        return self.Type

    def get_Length(self):
        return self.Length

    def get_Position(self):
        return self.Position

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_Type(self, Type: int):
        self.Type = Type

    def set_Length(self, Length: float):
        self.Length = Length

    def set_Position(self, Position: float):
        self.Position = Position

    def __str__(self):
        return "GlobalID: " + str(self.GlobalID) + ", Type: " + str(self.Type) + ", Length: " + str(self.Length) + ", Position: " + str(self.Position)


