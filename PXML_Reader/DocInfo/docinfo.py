from .mode import Mode
import xml.etree.ElementTree as ET


class DocInfo():  # The DocInfo block must be there precisely once per document.

    def __init__(self, GlobalID: str, MajorVersion: int, MinorVersion: int, Comment: str, ConvertConventions: str,
                 Mode: list):

        self.GlobalID = ""
        self.MajorVersion = None  # INT // Obligatoire 1,1
        self.MinorVersion = None  # INT // Obligatoire 1,1
        self.Comment = ""  # STR // 0,1
        self.ConvertConventions = ""  # STR // 0,1
        self.Mode = []  # Object Mode from the module mode. n,n

        self.GlobalID = GlobalID
        if type(MajorVersion) is int and type(MinorVersion) is int:
            self.MajorVersion = int(MajorVersion)
            self.MinorVersion = int(MinorVersion)
        else:
            raise TypeError("MajorVersion and MinorVersion must be integers")

        self.Comment = Comment
        self.ConvertConventions = ConvertConventions
        self.Mode = Mode

    def get_GlobalID(self):
        return self.GlobalID

    def get_MajorVersion(self):
        return self.MajorVersion

    def get_MinorVersion(self):
        return self.MinorVersion

    def get_Comment(self):
        return self.Comment

    def get_ConvertConventions(self):
        return self.ConvertConventions

    def get_Mode(self):
        return self.Mode

    def set_GlobalID(self, GlobalID: str):
        self.GlobalID = GlobalID

    def set_MajorVersion(self, MajorVersion: int):
        if type(MajorVersion) is int:
            self.MajorVersion = MajorVersion
        else:
            raise TypeError("MajorVersion must be an integer")

    def set_MinorVersion(self, MinorVersion: int):
        if type(MinorVersion) is int:
            self.MinorVersion = MinorVersion
        else:
            raise TypeError("MinorVersion must be an integer")

    def set_Comment(self, Comment: str):
        self.Comment = Comment

    def set_ConvertConventions(self, ConvertConventions: str):
        self.ConvertConventions = ConvertConventions

    def set_Mode(self, Mode: list):
        self.Mode = Mode

    def add_Mode(self, Mode: Mode) -> object:
        self.Mode.append(Mode)

    def __str__(self):
        return f"GlobalID: {self.GlobalID}\nMajorVersion: {self.MajorVersion}\nMinorVersion: {self.MinorVersion}\nComment: {self.Comment}\nConvertConventions: {self.ConvertConventions}\nMode: {self.Mode}"

    def __xml__(self):
        docinfo = ET.Element('DocInfo')
        MajorVersion = ET.SubElement(docinfo, 'MajorVersion')
        MajorVersion.text = str(int(self.MajorVersion))
        MinorVersion = ET.SubElement(docinfo, 'MinorVersion')
        MinorVersion.text = str(int(self.MinorVersion))
        if self.Comment is not None:
            Comment = ET.SubElement(docinfo, 'Comment')
            Comment.text = self.Comment

        if self.ConvertConventions is not None:
            ConvertConventions = ET.SubElement(docinfo, 'ConvertConventions')
            ConvertConventions.text = self.ConvertConventions

        for mode in self.Mode:
            docinfo.append(mode.__xml__())

        return docinfo
