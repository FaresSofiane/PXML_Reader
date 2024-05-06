import xml.etree.ElementTree as ET

class Description:


    def __init__(self, Culture: str = None, Text: str = None):
        self.Culture = None # STR // 0,1
        self.Text = None # STR // 0,1
        self.Culture = Culture
        self.Text = Text

    def get_Culture(self):
        return self.Culture

    def get_Text(self):
        return self.Text

    def set_Culture(self, Culture: str):
        self.Culture = Culture

    def set_Text(self, Text: str):
        self.Text = Text

    def __str__(self):
        return "Culture: " + str(self.Culture) + ", Text: " + str(self.Text)

    def __xml__(self):
        Description = ET.Element('Description')
        if self.Culture is not None:
            Description.set('Culture', self.Culture)
        if self.Text is not None:
            Description.set('Text', self.Text)
        return Description