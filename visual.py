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

from math import sqrt

class vector(dict, object):
    def __init__(self, *args, **kwargs):
        dict.__init__(self)
        # Set default attributes
        
        self['mag']  = 0.0
        self['mag2'] = 0.0
        self['x']    = 0.0
        self['y']    = 0.0
        self['z']    = 0.0
        
        # Find out whether to record this creation
        try:
            record = kwargs['record']
        except KeyError:
            record = True
        
        if record:
            log.debug("create", extra={'class':'vector', 'object':self})

    def __getattribute__(self, name):
        try:
            val = self[name]
            log.debug("getattr", extra={'class':'vector', 'object':self, 'attr':name, 'value':val})
        except KeyError:
            log.error("AttributeError: %s", name, extra={'class':'vector', 'object':self, 'attr':name})
            return None
    
    def __setattr__(self, name, value):
        if (name == 'mag') or (name == 'mag2'):
            # Setting these has no effect
            log.warning("setattr ignored", extra={'class':'vector', 'object':self, 'attr':name})
            return
        self[name] = value
        # re-calculate mag, mag2
        self['mag2'] = self['x']**2 + self['y']**2 + self['z']**2
        self['mag'] = sqrt(self['mag2'])
        log.debug("setattr", extra={'class':'vector', 'object':self, 'attr':name, 'value':value})


    def astuple(self):
        """ Convert this vector to a tuple. """
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'astuple'})
        return (self['x'], self['y'], self['z'])
    
    def clear(self):
        """ Zero the state of this vector. """
        self['x'] = 0.
        self['y'] = 0.
        self['z'] = 0.
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'clear'})

    def comp(self, other):
        """ The scalar projection of this vector onto another. """
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'comp'})
        pass
    
    def cross(self, other):
        """ The cross product of this vector and another. """
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'cross'})
        pass
    
    def diff_angle(self, other):
        """ The angle between this vector and another, in radians. """
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'diff_angle'})
        pass
    
    def dot(self, other):
        """ The dot product of this vector and another. """
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'dot'})
        pass

    def norm(self):
        """ The unit vector of this vector. """
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'norm'})
        pass

    def proj(self, other):
        """ The vector projection of this vector onto another. """
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'proj'})
        pass

    def rotate(self, angle, axis=None):
        """ Rotate this vector about the specified axis through the specified angle, in radians """
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'rotate'})
        

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
            self[key] = kwargs[key]
            
        log.debug("create", extra={'class':'arrow', 'object':self, 'keywords':kwargs})
        
    def __getattribute__(self, name):
        try:
            val = self[name]
            log.debug("getattr", extra={'class':'arrow', 'object':self, 'attr':name, 'value':val})
        except KeyError:
            log.error("AttributeError: %s", name, extra={'class':'arrow', 'object':self, 'attr':name})
            return None
    
    def __setattr__(self, name, value):
        self[name] = value
        if name == 'pos':
            # change x,y,z
            pass
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
            self[key] = kwargs[key]
        
        log.debug("create", extra={'class':'box', 'object':self, 'keywords':kwargs})
        
    def __getattribute__(self, name):
        try:
            val = self[name]
            log.debug("getattr", extra={'class':'box', 'object':self, 'attr':name, 'value':val})
        except KeyError:
            log.error("AttributeError: %s", name, extra={'class':'box', 'object':self, 'attr':name})
            return None
    
    def __setattr__(self, name, value):
        self[name] = value
        if name == 'pos':
            # change x,y,z
            pass
        log.debug("setattr", extra={'class':'box', 'object':self, 'attr':name, 'value':value})
    

class sphere(dict, object):
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
        if name == 'pos':
            # change x,y,z
            pass
        log.debug("setattr", extra={'class':'sphere', 'object':self, 'attr':name, 'value':value})


# Rate function used in a loop
def rate(fps):
    pass
