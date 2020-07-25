from com.source.PageObjects.EntryPage import EntryPage

class EntryTest:
    def __init__(self):
        self.entryPage = EntryPage()
    
    def enterToApplication(self):
        self.entryPage.enterText()
        
        