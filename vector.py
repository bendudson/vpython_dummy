
from numpy import ndarray, arccos, sqrt

import logging
log = logging.getLogger('visual')

class vector(ndarray):
    def __new__(self, *args, **kwargs):
        return ndarray.__new__(self, 3)
        
    def __init__(self, *args, **kwargs):
        self[0] = 0.
        self[1] = 0.
        self[2] = 0.
        
        narg = len(args)
        if narg > 0:
            self[0] = args[0]
            if narg > 1:
                self[1] = args[1]
                if narg > 2:
                    self[2] = args[2]
        
        # Find out whether to record this creation
        try:
            record = kwargs['record']
        except KeyError:
            record = True
        
        if record:
            log.debug("create", extra={'class':'vector', 'object':self})
    
    def __getattribute__(self, name):
        if name == "x":
            val = self[0]
        elif name == "y":
            val = self[1]
        elif name == "z":
            val = self[2]
        elif name == "mag":
            val = sqrt(self[0]**2 + self[1]**2 + self[2]**2)
        elif name == "mag2":
            val = self[0]**2 + self[1]**2 + self[2]**2
        else:
            return ndarray.__getattribute__(self, name)
        
        log.debug("getattr", extra={'class':'vector', 'object':self, 'attr':name, 'value':val})
        return val

    def __setattr__(self, name, value):
        if name == "x":
            self[0] = value
        elif name == "y":
            self[1] = value
        elif name == "z":
            self[1] = value
        else:
            log.warning("setattr ignored", extra={'class':'vector', 'object':self, 'attr':name})
            return
        log.debug("setattr", extra={'class':'vector', 'object':self, 'attr':name, 'value':value})
        
    def astuple(self):
        """ Convert this vector to a tuple. """
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'astuple'})
        return (self[0], self[1], self[2])
    
    def clear(self):
        """ Zero the state of this vector. """
        self[0] = 0.
        self[1] = 0.
        self[2] = 0.
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'clear'})

    def comp(self, other):
        """ The scalar projection of this vector onto another. """
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'comp'})
        return NotImplemented
    
    def cross(self, other):
        """ The cross product of this vector and another. """
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'cross'})
        return NotImplemented
    
    def diff_angle(self, other):
        """ The angle between this vector and another, in radians. """
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'diff_angle'})
        vDot = self.dot(other) / (self.mag * other.mag)
        if vDot < -1.0 : vDot = -1.0
        if vDot > 1.0 : vDot = 1.0
        return float(acos(vDot))
    
    def dot(self, other):
        """ The dot product of this vector and another. """
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'dot'})
        return NotImplemented

    def norm(self):
        """ The unit vector of this vector. """
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'norm'})
        mag = self.mag
        return vector(self[0]/mag, self[1]/mag, self[2]/mag)

    def proj(self, other):
        """ The vector projection of this vector onto another. """
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'proj'})
        return NotImplemented

    def rotate(self, angle, axis=None):
        """ Rotate this vector about the specified axis through the specified angle, in radians """
        log.debug("method", extra={'class':'vector', 'object':self, 'method':'rotate'})
        return NotImplemented
