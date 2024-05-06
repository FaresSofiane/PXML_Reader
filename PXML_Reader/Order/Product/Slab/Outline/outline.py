from .Shape.shape import Shape
import xml.etree.ElementTree as ET

class Outline():


    def __init__(self, GlobalID: str = None, Type: str = None, X: float = None, Y: float = None, Z: float = None, RotX: float = None, RotY: float = None, RotZ: float = None, Height: float = None, Name: str = None, GenericInfo01: str = None, GenericInfo02: str = None, MountingInstruction: str = None, MountPartType: str = None, MountPartArticle: str = None, MountPartIronProjection: float = None, MountPartDirection: float = None, MountPartLength: float = None, MountPartWidth: float = None, ConcretingMode: str = None, ConcreteQuality: str = None, UnitWeight: float = None, Volume: float = None, Layer: str = None, ObjectID: str = None, Shape: list = []):
        self.GlobalID = None  # STR // 0,1
        self.Type = None  # STR // 0,1
        self.X = None  # FLOAT // 0,1
        self.Y = None  # FLOAT // 0,1
        self.Z = None  # FLOAT // 0,1
        self.RotX = None  # FLOAT // 0,1
        self.RotY = None  # FLOAT // 0,1
        self.RotZ = None  # FLOAT // 0,1
        self.Height = None  # FLOAT // 0,1
        self.Name = None  # STR // 0,1
        self.GenericInfo01 = None  # STR // 0,1
        self.GenericInfo02 = None  # STR // 0,1
        self.MountingInstruction = None  # STR // 0,1
        self.MountPartType = None  # STR // 0,1
        self.MountPartArticle = None  # STR // 0,1
        self.MountPartIronProjection = None  # FLOAT // 0,1
        self.MountPartDirection = None  # FLOAT // 0,1
        self.MountPartLength = None  # FLOAT // 0,1
        self.MountPartWidth = None  # FLOAT // 0,1
        self.ConcretingMode = None  # STR // 0,1
        self.ConcreteQuality = None  # STR // 0,1
        self.UnitWeight = None  # FLOAT // 0,1
        self.Volume = None  # FLOAT // 0,1
        self.Layer = None  # STR // 0,1
        self.ObjectID = None  # STR // 0,1
        self.Shape = []  # Shape // n,n

        self.GlobalID = GlobalID
        self.Type = Type
        if type(X) is float:
            self.X = float(X)
        else:
            if X is None:
                self.X = None
            else:
                try:
                    self.X = float(X)
                except ValueError:
                    raise ValueError(f'X must be a float')
        if type(Y) is float:
            self.Y = float(Y)
        else:
            if Y is None:
                self.Y = None
            else:
                try:
                    self.Y = float(Y)
                except ValueError:
                    raise ValueError(f'Y must be a float')
        if type(Z) is float:
            self.Z = float(Z)
        else:
            if Z is None:
                self.Z = None
            else:
                try:
                    self.Z = float(Z)
                except ValueError:
                    raise ValueError(f'Z must be a float')
        if type(RotX) is float:
            self.RotX = float(RotX)
        else:
            if RotX is None:
                self.RotX = None
            else:
                try:
                    self.RotX = float(RotX)
                except ValueError:
                    raise ValueError(f'RotX must be a float')
        if type(RotY) is float:
            self.RotY = float(RotY)
        else:
            if RotY is None:
                self.RotY = None
            else:
                try:
                    self.RotY = float(RotY)
                except ValueError:
                    raise ValueError(f'RotY must be a float')
        if type(RotZ) is float:
            self.RotZ = float(RotZ)
        else:
            if RotZ is None:
                self.RotZ = None
            else:
                try:
                    self.RotZ = float(RotZ)
                except ValueError:
                    raise ValueError(f'RotZ must be a float')
        if type(Height) is float:
            self.Height = float(Height)
        else:
            if Height is None:
                self.Height = None
            else:
                try:
                    self.Height = float(Height)
                except ValueError:
                    raise ValueError(f'Height must be a float')
        self.Name = Name
        self.GenericInfo01 = GenericInfo01
        self.GenericInfo02 = GenericInfo02
        self.MountingInstruction = MountingInstruction
        self.MountPartType = MountPartType
        self.MountPartArticle = MountPartArticle
        if type(MountPartIronProjection) is float:
            self.MountPartIronProjection = float(MountPartIronProjection)
        else:
            if MountPartIronProjection is None:
                self.MountPartIronProjection = None
            else:
                try:
                    self.MountPartIronProjection = float(MountPartIronProjection)
                except ValueError:
                    raise ValueError(f'MountPartIronProjection must be a float')
        if type(MountPartDirection) is float:
            self.MountPartDirection = float(MountPartDirection)
        else:
            if MountPartDirection is None:
                self.MountPartDirection = None
            else:
                try:
                    self.MountPartDirection = float(MountPartDirection)
                except ValueError:
                    raise ValueError(f'MountPartDirection must be a float')
        if type(MountPartLength) is float:
            self.MountPartLength = float(MountPartLength)
        else:
            if MountPartLength is None:
                self.MountPartLength = None
            else:
                try:
                    self.MountPartLength = float(MountPartLength)
                except ValueError:
                    raise ValueError(f'MountPartLength must be a float')
        if type(MountPartWidth) is float:
            self.MountPartWidth = float(MountPartWidth)
        else:
            if MountPartWidth is None:
                self.MountPartWidth = None
            else:
                try:
                    self.MountPartWidth = float(MountPartWidth)
                except ValueError:
                    raise ValueError(f'MountPartWidth must be a float')

        self.ConcretingMode = ConcretingMode
        self.ConcreteQuality = ConcreteQuality
        if type(UnitWeight) is float:
            self.UnitWeight = float(UnitWeight)
        else:
            if UnitWeight is None:
                self.UnitWeight = None
            else:
                try:
                    self.UnitWeight = float(UnitWeight)
                except ValueError:
                    raise ValueError(f'UnitWeight must be a float')
        if type(Volume) is float:
            self.Volume = float(Volume)
        else:
            if Volume is None:
                self.Volume = None
            else:
                try:
                    self.Volume = float(Volume)
                except ValueError:
                    raise ValueError(f'Volume must be a float')
        self.Layer = Layer
        self.ObjectID = ObjectID
        self.Shape = Shape


    def get_GlobalID(self):
        return self.GlobalID

    def get_Type(self):
        return self.Type

    def get_X(self):
        return self.X

    def get_Y(self):
        return self.Y

    def get_Z(self):
        return self.Z

    def get_RotX(self):
        return self.RotX

    def get_RotY(self):
        return self.RotY

    def get_RotZ(self):
        return self.RotZ

    def get_Height(self):
        return self.Height

    def get_Name(self):
        return self.Name

    def get_GenericInfo01(self):
        return self.GenericInfo01

    def get_GenericInfo02(self):
        return self.GenericInfo02

    def get_MountingInstruction(self):
        return self.MountingInstruction

    def get_MountPartType(self):
        return self.MountPartType

    def get_MountPartArticle(self):
        return self.MountPartArticle

    def get_MountPartIronProjection(self):
        return self.MountPartIronProjection

    def get_MountPartDirection(self):
        return self.MountPartDirection

    def get_MountPartLength(self):
        return self.MountPartLength

    def get_MountPartWidth(self):
        return self.MountPartWidth

    def get_ConcretingMode(self):
        return self.ConcretingMode

    def get_ConcreteQuality(self):
        return self.ConcreteQuality

    def get_UnitWeight(self):
        return self.UnitWeight

    def get_Volume(self):
        return self.Volume

    def get_Layer(self):
        return self.Layer

    def get_ObjectID(self):
        return self.ObjectID

    def get_Shape(self):
        return self.Shape

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_Type(self, Type: str):
        self.Type = Type

    def set_X(self, X: float):
        self.X = X

    def set_Y(self, Y: float):
        self.Y = Y

    def set_Z(self, Z: float):
        self.Z = Z

    def set_RotX(self, RotX: float):
        self.RotX = RotX

    def set_RotY(self, RotY: float):
        self.RotY = RotY

    def set_RotZ(self, RotZ: float):
        self.RotZ = RotZ

    def set_Height(self, Height: float):
        self.Height = Height

    def set_Name(self, Name: str):
        self.Name = Name

    def set_GenericInfo01(self, GenericInfo01: str):
        self.GenericInfo01 = GenericInfo01

    def set_GenericInfo02(self, GenericInfo02: str):
        self.GenericInfo02 = GenericInfo02

    def set_MountingInstruction(self, MountingInstruction: str):
        self.MountingInstruction = MountingInstruction

    def set_MountPartType(self, MountPartType: str):
        self.MountPartType = MountPartType

    def set_MountPartArticle(self, MountPartArticle: str):
        self.MountPartArticle = MountPartArticle

    def set_MountPartIronProjection(self, MountPartIronProjection: float):
        self.MountPartIronProjection = MountPartIronProjection

    def set_MountPartDirection(self, MountPartDirection: float):
        self.MountPartDirection = MountPartDirection

    def set_MountPartLength(self, MountPartLength: float):
        self.MountPartLength = MountPartLength

    def set_MountPartWidth(self, MountPartWidth: float):
        self.MountPartWidth = MountPartWidth

    def set_ConcretingMode(self, ConcretingMode: str):
        self.ConcretingMode = ConcretingMode

    def set_ConcreteQuality(self, ConcreteQuality: str):
        self.ConcreteQuality = ConcreteQuality

    def set_UnitWeight(self, UnitWeight: float):
        self.UnitWeight = UnitWeight

    def set_Volume(self, Volume: float):
        self.Volume = Volume

    def set_Layer(self, Layer: str):
        self.Layer = Layer

    def set_ObjectID(self, ObjectID: str):
        self.ObjectID = ObjectID

    def set_Shape(self, Shape: list):
        self.Shape = Shape

    def add_Shape(self, Shape: Shape) -> object:
        self.Shape.append(Shape)

    def __str__(self):
        return "GlobalID: " + str(self.GlobalID) + ", Type: " + str(self.Type) + ", X: " + str(self.X) + ", Y: " + str(self.Y) + ", Z: " + str(self.Z) + ", RotX: " + str(self.RotX) + ", RotY: " + str(self.RotY) + ", RotZ: " + str(self.RotZ) + ", Height: " + str(self.Height) + ", Name: " + str(self.Name) + ", GenericInfo01: " + str(self.GenericInfo01) + ", GenericInfo02: " + str(self.GenericInfo02) + ", MountingInstruction: " + str(self.MountingInstruction) + ", MountPartType: " + str(self.MountPartType) + ", MountPartArticle: " + str(self.MountPartArticle) + ", MountPartIronProjection: " + str(self.MountPartIronProjection) + ", MountPartDirection: " + str(self.MountPartDirection) + ", MountPartLength: " + str(self.MountPartLength) + ", MountPartWidth: " + str(self.MountPartWidth) + ", ConcretingMode: " + str(self.ConcretingMode) + ", ConcreteQuality: " + str(self.ConcreteQuality) + ", UnitWeight: " + str(self.UnitWeight) + ", Volume: " + str(self.Volume) + ", Layer: " + str(self.Layer) + ", ObjectID: " + str(self.ObjectID) + ", Shape: " + str(self.Shape)

    def __xml__(self):
        Outline  = ET.Element('Outline')
        if self.GlobalID is not None:
            Outline.set('GlobalID', str(self.GlobalID))
        Outline.set('Type', str(self.Type))
        if self.X is not None:
            X = ET.SubElement(Outline, 'X')
            X.text = str(self.X)
        if self.Y is not None:
            Y = ET.SubElement(Outline, 'Y')
            Y.text = str(self.Y)
        if self.Z is not None:
            Z = ET.SubElement(Outline, 'Z')
            Z.text = str(self.Z)
        if self.RotX is not None:
            RotX = ET.SubElement(Outline, 'RotX')
            RotX.text = str(self.RotX)
        if self.RotY is not None:
            RotY = ET.SubElement(Outline, 'RotY')
            RotY.text = str(self.RotY)
        if self.RotZ is not None:
            RotZ = ET.SubElement(Outline, 'RotZ')
            RotZ.text = str(self.RotZ)
        if self.Height is not None:
            Height = ET.SubElement(Outline, 'Height')
            Height.text = str(self.Height)
        if self.Name is not None:
            Name = ET.SubElement(Outline, 'Name')
            Name.text = str(self.Name)
        if self.GenericInfo01 is not None:
            GenericInfo01 = ET.SubElement(Outline, 'GenericInfo01')
            GenericInfo01.text = str(self.GenericInfo01)
        if self.GenericInfo02 is not None:
            GenericInfo02 = ET.SubElement(Outline, 'GenericInfo02')
            GenericInfo02.text = str(self.GenericInfo02)
        if self.MountingInstruction is not None:
            MountingInstruction = ET.SubElement(Outline, 'MountingInstruction')
            MountingInstruction.text = str(self.MountingInstruction)
        if self.MountPartType is not None:
            MountPartType = ET.SubElement(Outline, 'MountPartType')
            MountPartType.text = str(self.MountPartType)
        if self.MountPartArticle is not None:
            MountPartArticle = ET.SubElement(Outline, 'MountPartArticle')
            MountPartArticle.text = str(self.MountPartArticle)
        if self.MountPartIronProjection is not None:
            MountPartIronProjection = ET.SubElement(Outline, 'MountPartIronProjection')
            MountPartIronProjection.text = str(self.MountPartIronProjection)
        if self.MountPartDirection is not None:
            MountPartDirection = ET.SubElement(Outline, 'MountPartDirection')
            MountPartDirection.text = str(self.MountPartDirection)
        if self.MountPartLength is not None:
            MountPartLength = ET.SubElement(Outline, 'MountPartLength')
            MountPartLength.text = str(self.MountPartLength)
        if self.MountPartWidth is not None:
            MountPartWidth = ET.SubElement(Outline, 'MountPartWidth')
            MountPartWidth.text = str(self.MountPartWidth)
        if self.ConcretingMode is not None:
            ConcretingMode = ET.SubElement(Outline, 'ConcretingMode')
            ConcretingMode.text = str(self.ConcretingMode)
        if self.ConcreteQuality is not None:
            ConcreteQuality = ET.SubElement(Outline, 'ConcreteQuality')
            ConcreteQuality.text = str(self.ConcreteQuality)
        if self.UnitWeight is not None:
            UnitWeight = ET.SubElement(Outline, 'UnitWeight')
            UnitWeight.text = str(self.UnitWeight)
        if self.Volume is not None:
            Volume = ET.SubElement(Outline, 'Volume')
            Volume.text = str(self.Volume)
        if self.Layer is not None:
            Layer = ET.SubElement(Outline, 'Layer')
            Layer.text = str(self.Layer)
        if self.ObjectID is not None:
            ObjectID = ET.SubElement(Outline, 'ObjectID')
            ObjectID.text = str(self.ObjectID)
        if self.Shape is not None:
            for shape in self.Shape:
                Outline.append(shape.__xml__())

        return Outline




