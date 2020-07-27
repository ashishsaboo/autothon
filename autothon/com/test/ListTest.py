from com.source.PageObjects.ListPage import ListPage
class ListTest:
    def __init__(self):
        self.listPage = ListPage()
        
    def printListValues(self, listValues):
        self.listPage.printListContent(listValues)