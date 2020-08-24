from com.source.PageObjects.EntryPage import EntryPage

class EntryTest:
    def __init__(self):
        self.entryPage = EntryPage()
    
    def enterToApplication(self, url):
        print("enter to application")
        print("enter to application")
        print("enter to application")
        self.entryPage.enterText(url)
        
        