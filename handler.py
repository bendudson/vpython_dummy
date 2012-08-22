"""
 Handler for logging of dummy Visual Python module
 
"""

from logging import Handler

class VisualHandler(Handler):
    def __init__(self):
        Handler.__init__(self)
        self.created = {}
        
    ## Functions to handle event types
    def handleCreate(self, record):
        name = record.__dict__['class']
        print("Creating an object of type %s "  % name)
        try:
            c = self.created[name]
        except KeyError:
            c = []
            self.created[name] = c
        try:
            c.append(record.object)
        except:
            pass
        

    def handleSetAttr(self, record):
        pass

    def handleGetAttr(self, record):
        pass

    ## This function called for each event
    def emit(self, record):
        """
        Entry level event handler
        """
        #Decide what to do based on message
        handler = {'create':self.handleCreate,
                   'setattr':self.handleSetAttr,
                   'getattr':self.handleGetAttr}
        
        try:
            return handler[record.msg](record)
        except KeyError:
            print("Unhandled record: " + str(record))
       
    ## Functions to inspect the log
    def getObjectsOfType(self, name):
        """ Returns a list of all objects created with a given class name
        
        """
        try:
            return self.created[name]
        except KeyError:
            return []
        
