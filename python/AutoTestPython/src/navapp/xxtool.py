# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_xxtool', [dirname(__file__)])
        except ImportError:
            import _xxtool
            return _xxtool
        if fp is not None:
            try:
                _mod = imp.load_module('_xxtool', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _xxtool = swig_import_helper()
    del swig_import_helper
else:
    import _xxtool
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _xxtool.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _xxtool.SwigPyIterator_value(self)
    def incr(self, n = 1): return _xxtool.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _xxtool.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _xxtool.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _xxtool.SwigPyIterator_equal(self, *args)
    def copy(self): return _xxtool.SwigPyIterator_copy(self)
    def next(self): return _xxtool.SwigPyIterator_next(self)
    def __next__(self): return _xxtool.SwigPyIterator___next__(self)
    def previous(self): return _xxtool.SwigPyIterator_previous(self)
    def advance(self, *args): return _xxtool.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _xxtool.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _xxtool.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _xxtool.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _xxtool.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _xxtool.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _xxtool.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _xxtool.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


def CallScript(*args):
  return _xxtool.CallScript(*args)
CallScript = _xxtool.CallScript

def EncodeCoor(*args):
  return _xxtool.EncodeCoor(*args)
EncodeCoor = _xxtool.EncodeCoor

def DecodeCoor(*args):
  return _xxtool.DecodeCoor(*args)
DecodeCoor = _xxtool.DecodeCoor

def PlayNmea(*args):
  return _xxtool.PlayNmea(*args)
PlayNmea = _xxtool.PlayNmea

def StopNmea():
  return _xxtool.StopNmea()
StopNmea = _xxtool.StopNmea

def GetNmeaTime():
  return _xxtool.GetNmeaTime()
GetNmeaTime = _xxtool.GetNmeaTime

def GetNmeaPos():
  return _xxtool.GetNmeaPos()
GetNmeaPos = _xxtool.GetNmeaPos

def Setup(*args):
  return _xxtool.Setup(*args)
Setup = _xxtool.Setup

def TearDown():
  return _xxtool.TearDown()
TearDown = _xxtool.TearDown

def DeleteFilesOnDevice(*args):
  return _xxtool.DeleteFilesOnDevice(*args)
DeleteFilesOnDevice = _xxtool.DeleteFilesOnDevice

def CopyFilesFromDevice(*args):
  return _xxtool.CopyFilesFromDevice(*args)
CopyFilesFromDevice = _xxtool.CopyFilesFromDevice

def CopyFileToDevice(*args):
  return _xxtool.CopyFileToDevice(*args)
CopyFileToDevice = _xxtool.CopyFileToDevice

def StartDevice():
  return _xxtool.StartDevice()
StartDevice = _xxtool.StartDevice

def StopDevice():
  return _xxtool.StopDevice()
StopDevice = _xxtool.StopDevice


