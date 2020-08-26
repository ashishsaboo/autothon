
'''creating user defined exception'''
class AutomationError(RuntimeError):
    def __init__(self, args):
        self.args = args
        
