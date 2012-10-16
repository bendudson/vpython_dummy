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

from vector import vector

class arrow(dict, object):
    def __init__(self, **kwargs):
        dict.__init__(self)
        # Set default attributes
        
        self['fixedwidth'] = False
        self['headlength'] = 0.3
        self['headwidth']  = 0.2
        self['length']     = 1.0
        self['shaftwidth'] = 0.1
        self['axis']       = vector(1,0,0, record=False)
        self['color']      = color.white
        self['opacity']    = 1.0
        self['pos']        = vector(0,0,0, record=False)
        self['up']         = vector(0,1,0, record=False)

        for key in kwargs:
            setattr(self, key, kwargs[key])
            
        log.debug("create", extra={'class':'arrow', 'object':self, 'keywords':kwargs})
        
    def __getattribute__(self, name):
        try:
            val = self[name]
            log.debug("getattr", extra={'class':'arrow', 'object':self, 'attr':name, 'value':val})
            return val
        except KeyError:
            log.error("AttributeError: %s", name, extra={'class':'arrow', 'object':self, 'attr':name})
            return None
    
    def __setattr__(self, name, value):
        # Check if a vector quantity
        if name in  ['axis', 'pos', 'up']:
            self[name] = vector(value)  # Ensure it's a vector
        else:
            self[name] = value
        if name == 'pos':
            # change x,y,z
            self['x'] = self['pos'].x
            self['y'] = self['pos'].y
            self['z'] = self['pos'].z
        log.debug("setattr", extra={'class':'arrow', 'object':self, 'attr':name, 'value':value})

class box(dict, object):
    def __init__(self, **kwargs):
        dict.__init__(self)
        # Set default attributes
        
        self['height']  = 1.0
        self['length']  = 1.0
        self['size']    = vector(1,1,1,record=False)
        self['width']   = 1.0
        self['axis']    = vector(1,0,0,record=False)
        self['color']   = color.white
        self['opacity'] = 1.0
        self['pos']     = vector(0,0,0,record=False)
        self['up']      = vector(0,1,0,record=False)
        self['x']       = 0.0
        self['y']       = 0.0
        self['z']       = 0.0

        for key in kwargs:
            setattr(self, key, kwargs[key])

        log.debug("create", extra={'class':'box', 'object':self, 'keywords':kwargs})
        
    def __getattribute__(self, name):
        try:
            val = self[name]
            log.debug("getattr", extra={'class':'box', 'object':self, 'attr':name, 'value':val})
            return val
        except KeyError:
            log.error("AttributeError: %s", name, extra={'class':'box', 'object':self, 'attr':name})
            return None
    
    def __setattr__(self, name, value):
        # Check if a vector quantity
        if name in  ['size', 'axis', 'pos', 'up']:
            self[name] = vector(value)  # Ensure it's a vector
        else:
            self[name] = value
        if name == 'pos':
            # change x,y,z
            self['x'] = self['pos'].x
            self['y'] = self['pos'].y
            self['z'] = self['pos'].z
        log.debug("setattr", extra={'class':'box', 'object':self, 'attr':name, 'value':value})
    

class sphere(dict, object):
    """ Sphere object """
    def __init__(self, **kwargs):
        dict.__init__(self)
        
        # Set the default attributes
        self['radius']  = 1.0
        self['axis']    = vector(1,0,0, record=False) # Don't log the creation of these vectors
        self['color']   = color.white
        self['opacity'] = 1.0
        self['pos']     = vector(0,0,0, record=False)
        self['up']      = vector(0,1,0,record=False)
        self['x']       = 0.0
        self['y']       = 0.0
        self['z']       = 0.0
        
        for key in kwargs:
            setattr(self, key, kwargs[key])
        
        log.debug("create", extra={'class':'sphere', 'object':self, 'keywords':kwargs})

    def __getattribute__(self, name):
        try:
            val = self[name]
            log.debug("getattr", extra={'class':'sphere', 'object':self, 'attr':name, 'value':val})
            return val
        except KeyError:
            log.error("AttributeError: %s", name, extra={'class':'sphere', 'object':self, 'attr':name})
            return None
    
    def __setattr__(self, name, value):
        # Check if a vector quantity
        if name in  ['axis', 'pos', 'up']:
            self[name] = vector(value)  # Ensure it's a vector
        else:
            self[name] = value

        if name == 'pos':
            # change x,y,z
            self['x'] = self['pos'].x
            self['y'] = self['pos'].y
            self['z'] = self['pos'].z
        log.debug("setattr", extra={'class':'sphere', 'object':self, 'attr':name, 'value':value})


# Rate function used in a loop
def rate(fps):
    pass
