import math

try:
    import numpy as np
except:
    np = False

def add_angle(angle, angle2):
    angle += angle2
    if angle < 0:
        angle += 360
    elif angle > 360:
        angle -= 360
    
    return
    
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

class Vector(object):
    
    @staticmethod
    def fromLA(length, angle):
        x = length * math.cos(angle * math.pi / 180)
        y = length * math.sin(angle * math.pi / 180)
        return Vector(x, y)
        
    polar = fromLA
    
    def __init__(self, *args):
        # first arg may be an iterable (list, tuple, etc...)
        if len(args) == 1 and hasattr(args[0], "__iter__"):
            self.coords = list(args[0])
        else:
            # convert `args` tuple to list 
            self.coords = list(args)

        if len(self.coords) > 0:
            self.x = self.coords[0]
        if len(self.coords) > 1:
            self.y = self.coords[1]
        if len(self.coords) > 2:
            self.z = self.coords[2]
        
    def __iter__(self):
        return iter(self.coords)

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, index):
        return self.coords[index]

    def __setitem__(self, index, value):
        self.coords[index] = value
        
    def __eq__(self, other):
        return all(isclose(a,b) for a,b in zip(self, other))

    def __neg__(self):
        return self * -1

    def __add__(self, other):
        return Vector(a + b for a, b in zip(self, other))
        
    def __radd__(self, other):
        return self.__add__(self, other)
        
    def __sub__(self, other):
        # add the negative of `other`
        return self + (-other)
        
    #def __rsub__(self, other):
    #    # SomeNotVector - Vector IS NOT POSSIBLE
    #    return NotImplemented
        
    def __mul__(self, other):
        
        # vector * scalar
        if isinstance(other, (int, float)):
            return Vector(a * other for a in self)
        
        # vector * vector
        elif isinstance(other, self.__class__):
            return Vector(a * b for a, b in zip(self, other))
            
        # vector * iterable (not vector)
        elif hasattr(other, "__iter__"):
            return self * Vector(other)
            
        else:
            return NotImplemented
        
    def __rmul__(self, other):
        return self.__mul__(other)
        
    def __truediv__(self, other):
    
        # vector / scalar
        if isinstance(other, (int, float)):
            return Vector(a / float(other) for a in self)
        
        # vector / vector
        elif isinstance(other, self.__class__):
            return Vector(a / b for a, b in zip(self, other))
            
        # vector / iterable (not vector)
        elif hasattr(other, "__iter__"):
            return self / Vector(other)
            
        else:
            return NotImplemented
        
    def __rtruediv__(self, other):
        # scalar / vector
        if isinstance(other, (int, float)):
            return Vector(float(other) / a for a in self)
        
        # vector / vector case is always handled by __truediv__
            
        # iterable (not vector) / vector
        elif hasattr(other, "__iter__"):
            return Vector(other) / self
            
        else:
            return NotImplemented
        
    __div__ = __truediv__
    
    def __pow__(self, power):
        return Vector(a ** power for a in self)
    
#   #####################################
#   THESE ALREADY WORK AND ARE NOT NEEDED
#   #####################################
    
#    def __list__(self):
#        pass
#        
#    def __tuple__(self):
#        pass
        
    @property    
    def nparray(self):
        return np.array(self.coords) if np else NotImplemented
    
    @property    
    def length(self):
        length = 0
        for c in self.coords:
            length += c**2
        return math.sqrt(length)
        
    @property
    def angle(self, allow_negative=True, quadrants=True):
        if len(self.coords) == 2:
            angle = math.atan(float(self.y) / self.x) * 180 / math.pi
            
            if not allow_negative:
                if angle < 0:
                    angle += 360
#            if quadrants:
#                if self.x < 0:
#                    if self.y < 0: # Quadrant III
#                        if angle < 0 or angle > 180:
#                            add_angle(angle, 180)
#                    else: # Quadrant II
#                        if angle < 0 or angle > 180:
#                            add_angle(angle, 180)
#                else:
#                    if self.y < 0: # Quadrant IV
#                        if angle 
#                    else: # Quadrant I
                        
            return angle
#        else:
#            if angle < 0:
#                if self.x < 0 and self.y > 0:
                    
            
    @property
    def normal(self):
        return self / self.length
        
    # String representation    
        
    def _repr_la(self):
        return "{0:.3f} @ {1:.3f} degrees".format(self.length, self.angle)
        
    def _repr_cmp(self):
        return "Vector[{0}]".format(",".join("{0:.3f}".format(c) for c in self))
        
    def __repr__(self):
        return self._repr_cmp()
        
def dot(v1, v2):
    return sum(v1*v2)
    
def angle(v1, v2):
    return math.acos(dot(v1,v2) / (v1.length * v2.length)) * 180 / math.pi
