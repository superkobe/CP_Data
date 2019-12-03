# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_TimesvcT2SDK', [dirname(__file__)])
        except ImportError:
            import _TimesvcT2SDK
            return _TimesvcT2SDK
        if fp is not None:
            try:
                _mod = imp.load_module('_TimesvcT2SDK', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _TimesvcT2SDK = swig_import_helper()
    del swig_import_helper
else:
    import _TimesvcT2SDK
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
    if (not static):
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



def cdata(*args):
  return _TimesvcT2SDK.cdata(*args)
cdata = _TimesvcT2SDK.cdata

def memmove(*args):
  return _TimesvcT2SDK.memmove(*args)
memmove = _TimesvcT2SDK.memmove

def new_intp():
  return _TimesvcT2SDK.new_intp()
new_intp = _TimesvcT2SDK.new_intp

def copy_intp(*args):
  return _TimesvcT2SDK.copy_intp(*args)
copy_intp = _TimesvcT2SDK.copy_intp

def delete_intp(*args):
  return _TimesvcT2SDK.delete_intp(*args)
delete_intp = _TimesvcT2SDK.delete_intp

def intp_assign(*args):
  return _TimesvcT2SDK.intp_assign(*args)
intp_assign = _TimesvcT2SDK.intp_assign

def intp_value(*args):
  return _TimesvcT2SDK.intp_value(*args)
intp_value = _TimesvcT2SDK.intp_value
class intArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _TimesvcT2SDK.new_intArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TimesvcT2SDK.delete_intArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _TimesvcT2SDK.intArray___getitem__(self, *args)
    def __setitem__(self, *args): return _TimesvcT2SDK.intArray___setitem__(self, *args)
    def cast(self): return _TimesvcT2SDK.intArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _TimesvcT2SDK.intArray_frompointer
    if _newclass:frompointer = staticmethod(_TimesvcT2SDK.intArray_frompointer)
intArray_swigregister = _TimesvcT2SDK.intArray_swigregister
intArray_swigregister(intArray)

def intArray_frompointer(*args):
  return _TimesvcT2SDK.intArray_frompointer(*args)
intArray_frompointer = _TimesvcT2SDK.intArray_frompointer

class TimesvcT2SDK(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TimesvcT2SDK, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TimesvcT2SDK, name)
    __repr__ = _swig_repr
    def InitInterface(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_InitInterface(self, *args)
    def DeInitInterface(self): return _TimesvcT2SDK.TimesvcT2SDK_DeInitInterface(self)
    def GenNewPacker(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_GenNewPacker(self, *args)
    __swig_setmethods__["m_lppack"] = _TimesvcT2SDK.TimesvcT2SDK_m_lppack_set
    __swig_getmethods__["m_lppack"] = _TimesvcT2SDK.TimesvcT2SDK_m_lppack_get
    if _newclass:m_lppack = _swig_property(_TimesvcT2SDK.TimesvcT2SDK_m_lppack_get, _TimesvcT2SDK.TimesvcT2SDK_m_lppack_set)
    def BeginPack(self): return _TimesvcT2SDK.TimesvcT2SDK_BeginPack(self)
    def EndPack(self): return _TimesvcT2SDK.TimesvcT2SDK_EndPack(self)
    def AddField(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_AddField(self, *args)
    def AddStr(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_AddStr(self, *args)
    def AddInt(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_AddInt(self, *args)
    def AddDouble(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_AddDouble(self, *args)
    def AddChar(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_AddChar(self, *args)
    def AddRaw(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_AddRaw(self, *args)
    def SendBiz(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_SendBiz(self, *args)
    def RecvBiz(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_RecvBiz(self, *args)
    __swig_setmethods__["m_lpPoint"] = _TimesvcT2SDK.TimesvcT2SDK_m_lpPoint_set
    __swig_getmethods__["m_lpPoint"] = _TimesvcT2SDK.TimesvcT2SDK_m_lpPoint_get
    if _newclass:m_lpPoint = _swig_property(_TimesvcT2SDK.TimesvcT2SDK_m_lpPoint_get, _TimesvcT2SDK.TimesvcT2SDK_m_lpPoint_set)
    def GetDatasetCount(self): return _TimesvcT2SDK.TimesvcT2SDK_GetDatasetCount(self)
    def GetColCount(self): return _TimesvcT2SDK.TimesvcT2SDK_GetColCount(self)
    def SetCurrentDatasetByIndex(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_SetCurrentDatasetByIndex(self, *args)
    def GetColName(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_GetColName(self, *args)
    def GetRowCount(self): return _TimesvcT2SDK.TimesvcT2SDK_GetRowCount(self)
    def GetColType(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_GetColType(self, *args)
    def GetIntByIndex(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_GetIntByIndex(self, *args)
    def GetCharByIndex(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_GetCharByIndex(self, *args)
    def GetStrByIndex(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_GetStrByIndex(self, *args)
    def GetDoubleByIndex(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_GetDoubleByIndex(self, *args)
    def GetRawByIndex(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_GetRawByIndex(self, *args)
    def Next(self): return _TimesvcT2SDK.TimesvcT2SDK_Next(self)
    def GetErrorMsg(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_GetErrorMsg(self, *args)
    def Connect(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_Connect(self, *args)
    def Close(self): return _TimesvcT2SDK.TimesvcT2SDK_Close(self)
    def testPoint(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_testPoint(self, *args)
    def GetLastExtraErrorMsg(self): return _TimesvcT2SDK.TimesvcT2SDK_GetLastExtraErrorMsg(self)
    def ConvertToken(self, *args): return _TimesvcT2SDK.TimesvcT2SDK_ConvertToken(self, *args)
    def __init__(self): 
        this = _TimesvcT2SDK.new_TimesvcT2SDK()
        try: self.this.append(this)
        except: self.this = this
TimesvcT2SDK_swigregister = _TimesvcT2SDK.TimesvcT2SDK_swigregister
TimesvcT2SDK_swigregister(TimesvcT2SDK)

# This file is compatible with both classic and new-style classes.

