class ftn(object):
    def __init__( self, l, m, h):
        self.lmh = (l, m, h)
    def __getitem__(self, num):
        if num in [0,1,2]:
            return self.lmh[num]
        else:
            raise IndexError("Triangular Fuzzy Numbers have only three indexs and {0:s} is out of range".format( repr(num)))
    def __setitem__( self, num, val):
        if num in [0,1,2]:
            q = list(self.lmh)
            q[num] = val
            self.lmh = tuple(q)
        else:
            raise IndexError("Triangular Fuzzy Numbers have only three indexs and {0:s} is out of range".format( repr(num)))
    def __repr__(self):
        return "ftn({0:s},{1:s},{2:s})".format( repr( self.lmh[0]), repr(self.lmh[1]),repr(self.lmh[2]))
    def __add__( self, other):
        if type(other) is ftn:
            return ftn( self.lmh[0]+other.lmh[0], self.lmh[1]+other.lmh[1], self.lmh[2]+other.lmh[2])
        else:
            raise TypeError("Addition only supports two ftns not {0:s}".format( repr(type(other))))
    def __mul__(self, other):
        if type(other) is ftn:
            return ftn( self.lmh[0]*other.lmh[0], self.lmh[1]*other.lmh[1], self.lmh[2]*other.lmh[2])
        elif type(other) is int or type(other)is float:
            return ftn( self.lmh[0]*other, self.lmh[1]*other, self.lmh[2]*other)
        else:
            raise TypeError("Multiplication only supports ftns and ints and floats not {0:s}".format( repr(type(other))))
    def __rmul__( self, other):
        if type(other) is ftn:
            return ftn( self.lmh[0]*other.lmh[0], self.lmh[1]*other.lmh[1], self.lmh[2]*other.lmh[2])
        elif type(other) is int or type(other) is float:
            return ftn( self.lmh[0]*other, self.lmh[1]*other, self.lmh[2]*other)
        else:
            raise TypeError("Only supports ints and floats not {0:s}".format( repr(type(other))))
    def __truediv__(self, other):
        if type(other) is ftn:
            return ftn( self.lmh[0]/other.lmh[2], self.lmh[1]/other.lmh[1], self.lmh[2]/other.lmh[0])
        elif type(other) is float or type(other) is int:
            return ftn( self.lmh[0]/other, self.lmh[1]/other, self.lmh[2]/other)
    def __rtruediv__(self, other):
        if type(other) is ftn:
            return ftn( other.lmh[0]/self.lmh[2], other.lmh[1]/self.lmh[1], other.lmh[2]/self.lmh[0])
        elif type(other) is float or type(other) is int:
            return ftn( other/self.lmh[2], other/self.lmh[1], other/self.lmh[0])
        else:
            raise TypeError('Division of ftn with anything other than ftn, int, and floats is undefined')
    def __floordiv__(self, other):
        if type(other) is ftn:
            return ftn( self.lmh[0]//other.lmh[2], self.lmh[1]//other.lmh[1], self.lmh[2]//other.lmh[0])
        elif type(other) is float or type(other) is int:
            return ftn( self.lmh[0]//other, self.lmh[1]//other, self.lmh[2]//other)
        else:
            raise TypeError('Division of ftn with anything other than ftn, int, and floats is undefined')
