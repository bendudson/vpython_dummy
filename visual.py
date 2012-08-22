""" 
Emulates the Visual Python module interface, whilst logging
all calls rather than producing a scene

"""

### Import and set up logging to record events
import logging

log = logging.getLogger('visual')
log.setLevel(logging.DEBUG)

### Colors

import color

### Define each of the Visual Python objects

class vector:
    def __init__(self, *args, **kwargs):
        # Find out whether to record this creation
        try:
            record = kwargs['record']
        except KeyError:
            record = True
        
        if record:
            log.debug("create", extra={'class':'vector', 'object':self})

class arrow:
    def __init__(self, **kwargs):
        log.debug("create", extra={'class':'arrow', 'object':self})

class box:
    def __init__(self, **kwargs):
        log.debug("create", extra={'class':'box', 'object':self})

class sphere(dict,object):
    def __init__(self, **kwargs):
        dict.__init__(self)
        
        # Set the default attributes
        self['radius'] = 1.0
        self['axis']   = vector(1,0,0, record=False) # Don't log the creation of these vectors
        self['color']  = color.white
        self['pos']    = vector(0,0,0, record=False)
        
        for key in kwargs:
            self[key] = kwargs[key]
            
        log.debug("create", extra={'class':'sphere', 'object':self, 'keywords':kwargs})

    def __getattribute__(self, name):
        try:
            val = self[name]
            log.debug("getattr", extra={'class':'sphere', 'object':self, 'attr':name, 'value':val})
        except KeyError:
            log.error("AttributeError: %s", name, extra={'class':'sphere', 'object':self, 'attr':name})
            return None
    
    def __setattr__(self, name, value):
        self[name] = value
        log.debug("setattr", extra={'class':'sphere', 'object':self, 'attr':name, 'value':value})
