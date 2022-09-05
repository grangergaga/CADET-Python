
import ctypes
import numpy
import addict
import time

#input("Press Enter to continue...")

def log_handler(file, func, line, level, level_name, message):
    log_print('{} ({}:{:d}) {}'.format(level_name.decode('utf-8') , func.decode('utf-8') , line, message.decode('utf-8') ))

c_cadet_result = ctypes.c_int

array_double = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))


point_int = ctypes.POINTER(ctypes.c_int)

def null(*args):
    pass

if 0:
    log_print = print
else:
    log_print = null


class PARAMETERPROVIDER(ctypes.Structure):

    _fields_ = [
        ('userData', ctypes.py_object),

        ('getDouble', ctypes.CFUNCTYPE(c_cadet_result, ctypes.py_object, ctypes.c_char_p, ctypes.POINTER(ctypes.c_double))),
        ('getInt', ctypes.CFUNCTYPE(c_cadet_result, ctypes.py_object, ctypes.c_char_p, point_int)),
        ('getBool', ctypes.CFUNCTYPE(c_cadet_result, ctypes.py_object, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint8))),
        ('getString', ctypes.CFUNCTYPE(c_cadet_result, ctypes.py_object, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p))),

        ('getDoubleArray', ctypes.CFUNCTYPE(c_cadet_result, ctypes.py_object, ctypes.c_char_p, point_int, array_double)),
        ('getIntArray', ctypes.CFUNCTYPE(c_cadet_result, ctypes.py_object, ctypes.c_char_p, point_int, ctypes.POINTER(point_int))),
        ('getBoolArray', ctypes.CFUNCTYPE(c_cadet_result, ctypes.py_object, ctypes.c_char_p, point_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_uint8)))),
        ('getStringArray', ctypes.CFUNCTYPE(c_cadet_result, ctypes.py_object, ctypes.c_char_p, point_int, ctypes.POINTER(ctypes.POINTER(ctypes.c_char_p)))),

        ('getDoubleArrayItem', ctypes.CFUNCTYPE(c_cadet_result, ctypes.py_object, ctypes.c_char_p, ctypes.c_int, ctypes.POINTER(ctypes.c_double))),
        ('getIntArrayItem', ctypes.CFUNCTYPE(c_cadet_result, ctypes.py_object, ctypes.c_char_p, ctypes.c_int, point_int)),
        ('getBoolArrayItem', ctypes.CFUNCTYPE(c_cadet_result, ctypes.py_object, ctypes.c_char_p, ctypes.c_int, ctypes.POINTER(ctypes.c_uint8))),
        ('getStringArrayItem', ctypes.CFUNCTYPE(c_cadet_result, ctypes.py_object, ctypes.c_char_p, ctypes.c_int, ctypes.POINTER(ctypes.c_char_p))),

        ('exists', ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object, ctypes.c_char_p)),
        ('isArray', ctypes.CFUNCTYPE(c_cadet_result, ctypes.py_object, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint8))),
        ('numElements', ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object, ctypes.c_char_p)),
        ('pushScope', ctypes.CFUNCTYPE(c_cadet_result, ctypes.py_object, ctypes.c_char_p)),
        ('popScope', ctypes.CFUNCTYPE(c_cadet_result, ctypes.py_object)),
    ]


class CADETAPIV010000_DATA():
    _data_ = {}
    _data_['createDriver'] = ('drv',)
    _data_['deleteDriver'] = (None, 'drv')
    _data_['runSimulation'] = ('return', 'drv', 'parameterProvider')
    _data_['getNParTypes'] = ('return', 'drv', 'unitOpId', 'nParTypes')
    _data_['getSolutionInlet'] = ('return', 'drv', 'unitOpId', 'time', 'data', 'nTime', 'nPort', 'nComp')
    _data_['getSolutionOutlet'] = ('return', 'drv', 'unitOpId', 'time', 'data', 'nTime', 'nPort', 'nComp')
    _data_['getSolutionBulk'] = ('return', 'drv', 'unitOpId', 'time', 'data', 'nTime', 'nAxialCells', 'nRadialCells', 'nComp')
    _data_['getSolutionParticle'] = ('return', 'drv', 'unitOpId', 'parType', 'time', 'data', 'nTime', 'nParShells', 'nAxialCells', 'nRadialCells', 'nComp')
    _data_['getSolutionSolid'] = ('return', 'drv', 'unitOpId', 'parType', 'time', 'data', 'nTime', 'nParShells', 'nAxialCells', 'nRadialCells', 'nBound')
    _data_['getSolutionFlux'] = ('return', 'drv', 'unitOpId', 'time', 'data', 'nTime', 'nAxialCells', 'nRadialCells', 'nComp')
    _data_['getSolutionVolume'] = ('return', 'drv', 'unitOpId', 'time', 'data', 'nTime')
    _data_['getSolutionDerivativeInlet'] = ('return', 'drv', 'unitOpId', 'time', 'data', 'nTime', 'nPort', 'nComp')
    _data_['getSolutionDerivativeOutlet'] = ('return', 'drv', 'unitOpId', 'time', 'data', 'nTime', 'nPort', 'nComp')
    _data_['getSolutionDerivativeBulk'] = ('return', 'drv', 'unitOpId', 'time', 'data', 'nTime', 'nAxialCells', 'nRadialCells', 'nComp')
    _data_['getSolutionDerivativeParticle'] = ('return', 'drv', 'unitOpId', 'parType', 'time', 'data', 'nTime', 'nParShells', 'nAxialCells', 'nRadialCells', 'nComp')
    _data_['getSolutionDerivativeSolid'] = ('return', 'drv', 'unitOpId', 'parType', 'time', 'data', 'nTime', 'nParShells', 'nAxialCells', 'nRadialCells', 'nBound')
    _data_['getSolutionDerivativeFlux'] = ('return', 'drv', 'unitOpId', 'time', 'data', 'nTime', 'nAxialCells', 'nRadialCells', 'nComp')
    _data_['getSolutionDerivativeVolume'] = ('return', 'drv', 'unitOpId', 'time', 'data', 'nTime')
    _data_['getSensitivityInlet'] = ('return', 'drv', 'unitOpId', 'idx', 'time', 'data', 'nTime', 'nPort', 'nComp')
    _data_['getSensitivityOutlet'] = ('return', 'drv', 'unitOpId', 'idx', 'time', 'data', 'nTime', 'nPort', 'nComp')
    _data_['getSensitivityBulk'] = ('return', 'drv', 'unitOpId', 'idx', 'time', 'data', 'nTime', 'nAxialCells', 'nRadialCells', 'nComp')
    _data_['getSensitivityParticle'] = ('return', 'drv', 'unitOpId', 'idx', 'parType', 'time', 'data', 'nTime', 'nParShells', 'nAxialCells', 'nRadialCells', 'nComp')
    _data_['getSensitivitySolid'] = ('return', 'drv', 'unitOpId', 'idx', 'parType', 'time', 'data', 'nTime', 'nParShells', 'nAxialCells', 'nRadialCells', 'nBound')
    _data_['getSensitivityFlux'] = ('return', 'drv', 'unitOpId', 'idx', 'time', 'data', 'nTime', 'nAxialCells', 'nRadialCells', 'nComp')
    _data_['getSensitivityVolume'] = ('return', 'drv', 'unitOpId', 'idx', 'time', 'data', 'nTime')
    _data_['getSensitivityDerivativeInlet'] = ('return', 'drv', 'unitOpId', 'idx', 'time', 'data', 'nTime', 'nPort', 'nComp')
    _data_['getSensitivityDerivativeOutlet'] = ('return', 'drv', 'unitOpId', 'idx', 'time', 'data', 'nTime', 'nPort', 'nComp')
    _data_['getSensitivityDerivativeBulk'] = ('return', 'drv', 'unitOpId', 'idx', 'time', 'data', 'nTime', 'nAxialCells', 'nRadialCells', 'nComp')
    _data_['getSensitivityDerivativeParticle'] = ('return', 'drv', 'unitOpId', 'idx', 'parType', 'time', 'data', 'nTime', 'nParShells', 'nAxialCells', 'nRadialCells', 'nComp')
    _data_['getSensitivityDerivativeSolid'] = ('return', 'drv', 'unitOpId', 'idx', 'parType', 'time', 'data', 'nTime', 'nParShells', 'nAxialCells', 'nRadialCells', 'nBound')
    _data_['getSensitivityDerivativeFlux'] = ('return', 'drv', 'unitOpId', 'idx', 'time', 'data', 'nTime', 'nAxialCells', 'nRadialCells', 'nComp')
    _data_['getSensitivityDerivativeVolume'] = ('return', 'drv', 'unitOpId', 'idx', 'time', 'data', 'nTime')

    lookup_prototype = {
        'return': c_cadet_result,
        'drv': ctypes.c_void_p,
        'unitOpId': ctypes.c_int,
        'idx': ctypes.c_int,
        'parType': ctypes.c_int,
        'time': array_double,
        'data': array_double,
        'nTime': point_int,
        'nPort': point_int,
        'nAxialCells': point_int,
        'nRadialCells': point_int,
        'nParTypes': point_int,
        'nParShells': point_int,
        'nComp': point_int,
        'nBound': point_int,
        None: None,
        'parameterProvider': ctypes.POINTER(PARAMETERPROVIDER)
    }

    lookup_call = {
        'time': ctypes.POINTER(ctypes.c_double),
        'nTime': ctypes.c_int,
        'data': ctypes.POINTER(ctypes.c_double),
        'nPort': ctypes.c_int,
        'nAxialCells': ctypes.c_int,
        'nRadialCells': ctypes.c_int,
        'nParTypes': ctypes.c_int,
        'nParShells': ctypes.c_int,
        'nComp': ctypes.c_int,
        'nBound': ctypes.c_int,
    }


def setup_api():
    _fields_ = []

    for key, value in CADETAPIV010000_DATA._data_.items():
        args = tuple(CADETAPIV010000_DATA.lookup_prototype[key] for key in value)
        _fields_.append( (key, ctypes.CFUNCTYPE(*args)) )

    return _fields_


class CADETAPIV010000(ctypes.Structure):
    _fields_ = setup_api()


class NestedDictReader:

    def __init__(self, data):
        self.__root = data
        self.__cursor = []
        self.__cursor.append(data)
        self.buffer = None

    def push_scope(self, scope):
        if scope in self.__cursor[-1]:
            log_print('Entering scope {}'.format(scope))
            self.__cursor.append(self.__cursor[-1][scope])
            return True

        return False

    def pop_scope(self):
        self.__cursor.pop()
        log_print('Exiting scope')

    def current(self):
        return self.__cursor[-1]


def param_provider_get_double(reader, name, val):
    n = name.decode('utf-8')
    c = reader.current()

    if n in c:
        o = c[n]
        try:
            float_val = float(o)
        except TypeError:
            float_val = float(o[0])

        val[0] = ctypes.c_double(float_val)

        log_print('GET scalar [double] {}: {}'.format(n, float(val[0])))
        return 0

    return -1


def param_provider_get_int(reader, name, val):
    n = name.decode('utf-8')
    c = reader.current()

    if n in c:
        o = c[n]
        try:
            int_val = int(o)
        except TypeError:
            int_val = int(o[0])

        val[0] = ctypes.c_int(int_val)

        log_print('GET scalar [int] {}: {}'.format(n, int(val[0])))
        return 0

    return -1


def param_provider_get_bool(reader, name, val):
    n = name.decode('utf-8')
    c = reader.current()

    if n in c:
        o = c[n]

        try:
            int_val = int(o)
        except TypeError:
            int_val = int(o[0])

        val[0] = ctypes.c_uint8(int_val)

        log_print('GET scalar [bool] {}: {}'.format(n, bool(val[0])))
        return 0

    return -1


def param_provider_get_string(reader, name, val):
    n = name.decode('utf-8')
    c = reader.current()

    if n in c:
        o = c[n]

        #we have one of array of strings, array of bytestrings, bytestring or string or something convertable to one of these
        if hasattr(o, 'encode'):
            bytes_val = o.encode('utf-8')
        elif hasattr(o, 'decode'):
            bytes_val = o
        elif hasattr(o[0], 'encode'):
            bytes_val = o[0].encode('utf-8')
        elif hasattr(o[0], 'decode'):
            bytes_val = o[0]

        reader.buffer = bytes_val
        val[0] = ctypes.cast(reader.buffer, ctypes.c_char_p)

        return 0

    return -1


def param_provider_get_double_array(reader, name, n_elem, val):
    n = name.decode('utf-8')
    c = reader.current()

    if (n in c):
        o = c[n]
        if isinstance(o, list):
            o = numpy.ascontiguousarray(o)
        if (not isinstance(o, numpy.ndarray)) or (o.dtype != numpy.double) or (not o.flags.c_contiguous):
            return -1

        n_elem[0] = ctypes.c_int(o.size)
        val[0] = o.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
        log_print('GET array [double] {}: {}'.format(n, o))
        return 0

    return -1


def param_provider_get_int_array(reader, name, n_elem, val):
    n = name.decode('utf-8')
    c = reader.current()

    if (n in c):
        o = c[n]
        if isinstance(o, list):
            o = numpy.ascontiguousarray(o)
        if (not isinstance(o, numpy.ndarray)) or (o.dtype != numpy.int) or (not o.flags.c_contiguous):
            return -1

        n_elem[0] = ctypes.c_int(o.size)
        val[0] = o.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
        log_print('GET array [int] {}: {}'.format(n, o))
        return 0

    return -1


def param_provider_get_double_array_item(reader, name, index, val):
    n = name.decode('utf-8')
    c = reader.current()

    if n in c:
        o = c[n]

        try:
            float_val = float(o)
        except TypeError:
            float_val = float(o[index])

        val[0] = ctypes.c_double(float_val)
        log_print('GET array [double] ({}) {}: {}'.format(index, n, val[0]))
        return 0

    return -1


def param_provider_get_int_array_item(reader, name, index, val):
    n = name.decode('utf-8')
    c = reader.current()

    if n in c:
        o = c[n]

        try:
            int_val = int(o)
        except TypeError:
            int_val = int(o[index])

        val[0] = ctypes.c_int(int_val)
        log_print('GET array [int] ({}) {}: {}'.format(index, n, val[0]))
        return 0

    return -1


def param_provider_get_bool_array_item(reader, name, index, val):
    n = name.decode('utf-8')
    c = reader.current()

    if n in c:
        o = c[n]

        try:
            int_val = int(o)
        except TypeError:
            int_val = int(o[index])

        val[0] = ctypes.c_uint8(int_val)
        log_print('GET array [bool] ({}) {}: {}'.format(index, n, bool(val[0])))
        return 0

    return -1


def param_provider_get_string_array_item(reader, name, index, val):
    n = name.decode('utf-8')
    c = reader.current()

    if n in c:
        o = c[n]
        if index == 0:
            if hasattr(o, 'encode'):
                bytes_val = o.encode('utf-8')
            elif hasattr(o, 'decode'):
                bytes_val = o
        else:
            if hasattr(o[index], 'encode'):
                bytes_val = o[index].encode('utf-8')
            elif hasattr(o[index], 'decode'):
                bytes_val = o[index]

        reader.buffer = bytes_val
        val[0] = ctypes.cast(reader.buffer, ctypes.c_char_p)
        log_print('GET array [string] ({}) {}: {}'.format(index, n, reader.buffer.decode('utf-8')))
        return 0

    return -1


def param_provider_exists(reader, name):
    n = name.decode('utf-8')
    c = reader.current()

    log_print('EXISTS {}: {}'.format(n, n in c))

    if n in c:
        return 1

    return 0


def param_provider_is_array(reader, name, res):
    n = name.decode('utf-8')
    c = reader.current()

    if n not in c:
        return -1

    o = c[n]
    res[0] = ctypes.c_uint8(0)
    if isinstance(o, list):
        res[0] = ctypes.c_uint8(1)
    elif isinstance(o, numpy.ndarray):
        res[0] = ctypes.c_uint8(1)

    log_print('ISARRAY {}: {}'.format(n, bool(res[0])))

    return 0


def param_provider_num_elements(reader, name):
    n = name.decode('utf-8')
    c = reader.current()

    if n not in c:
        return -1

    o = c[n]
    if isinstance(o, list):
        log_print('NUMELEMENTS {}: {}'.format(n, len(o)))
        return len(o)
    elif isinstance(o, numpy.ndarray):
        log_print('NUMELEMENTS {}: {}'.format(n, o.size))
        return o.size

    log_print('NUMELEMENTS {}: {}'.format(n, 1))
    return 1


def param_provider_push_scope(reader, name):
    n = name.decode('utf-8')

    if reader.push_scope(n):
        return 0
    else:
        return -1


def param_provider_pop_scope(reader):
    reader.pop_scope()
    return 0


class SimulationResult:

    def __init__(self, api, driver):
        self.__api = api
        self.__driver = driver

    def load_data(self, unit, get_solution, get_solution_str, idx=None, parType=None, own_data=True):
        args = {}
        for key in CADETAPIV010000_DATA._data_[get_solution_str]:
            if key == 'return':
                continue
            elif key == 'drv':
                args['drv'] = self.__driver
            elif key == 'unitOpId':
                args['unitOpId'] = unit
            elif key == 'idx':
                args['idx'] = idx
            elif key == 'parType':
                args['parType'] = parType
            else:
                args[key] = ctypes.byref(CADETAPIV010000_DATA.lookup_call[key]())

        result = get_solution(self.__driver, unit, *tuple(args.values()))

        shape = (args['nTime'].value,)
        for arg in args:
            if arg == 'nPort':
                shape += args['nPort'].value
            elif arg == 'nParShells':
                shape += args['nParShells'].value
            elif 'nAxialCells' in args:
                shape += args['nAxialCells'].value
            elif 'nRadialCells' in args:
                shape += args['nRadialCells'].value
            elif 'nComp' in args:
                shape += args['nComp'].value
            elif 'nBound' in args:
                shape += args['nBound'].value

        data = numpy.ctypeslib.as_array(args['data'], shape=shape)
        time = numpy.ctypeslib.as_array(args['time'], shape=(args['nTime'].value, ))

        if own_data:
            return (time.copy(), data.copy())
        else:
            return (time, data)

    def inlet(self, unit, own_data=True):
        return self.load_data(unit, self.__api.getSolutionInlet, 'getSolutionInlet', own_data=own_data)

    def outlet(self, unit, own_data=True):
        return self.load_data(unit, self.__api.getSolutionOutlet, 'getSolutionOutlet', own_data=own_data)

    def bulk(self, unit, own_data=True):
        return self.load_data(unit, self.__api.getSolutionBulk, 'getSolutionBulk', own_data=own_data)

    def particle(self, unit, parType, own_data=True):
        return self.load_data(unit, self.__api.getSolutionBulk, 'getSolutionBulk', own_data=own_data)

    def solid(self, unit, parType, own_data=True):
        return self.load_data(unit, self.__api.getSolutionSolid, 'getSolutionSolid', own_data=own_data)

    def flux(self, unit, own_data=True):
        return self.load_data(unit, self.__api.getSolutionFlux, 'getSolutionFlux', own_data=own_data)

    def volume(self, unit, own_data=True):
        return self.load_data(unit, self.__api.getSolutionVolume, 'getSolutionVolume', own_data=own_data)

    def derivativeInlet(self, unit, own_data=True):
        return self.load_data(unit, self.__api.getSolutionDerivativeInlet, 'getSolutionDerivativeInlet', own_data=own_data)

    def derivativeOutlet(self, unit, own_data=True):
        return self.load_data(unit, self.__api.getSolutionDerivativeOutlet, 'getSolutionDerivativeOutlet', own_data=own_data)

    def derivativeBulk(self, unit, own_data=True):
        return self.load_data(unit, self.__api.getSolutionDerivativeBulk, 'getSolutionDerivativeBulk', own_data=own_data)

    def derivativeParticle(self, unit, parType, own_data=True):
        return self.load_data(unit, self.__api.getSolutionDerivativeParticle, 'getSolutionDerivativeParticle', own_data=own_data)

    def derivativeSolid(self, unit, parType, own_data=True):
        return self.load_data(unit, self.__api.getSolutionDerivativeSolid, 'getSolutionDerivativeSolid', own_data=own_data)

    def derivativeFlux(self, unit, own_data=True):
        return self.load_data(unit, self.__api.getSolutionDerivativeFlux, 'getSolutionDerivativeFlux', own_data=own_data)

    def derivativeVolume(self, unit, own_data=True):
        return self.load_data(unit, self.__api.getSolutionDerivativeVolume, 'getSolutionDerivativeVolume', own_data=own_data)

    def sensitivityInlet(self, unit, idx, own_data=True):
        return self.load_data(unit, self.__api.getSensitivityInlet, 'getSensitivityInlet', idx=idx, own_data=own_data)

    def sensitivityOutlet(self, unit, idx, own_data=True):
        return self.load_data(unit, self.__api.getSensitivityOutlet, 'getSensitivityOutlet', idx=idx, own_data=own_data)

    def sensitivityBulk(self, unit, idx, own_data=True):
        return self.load_data(unit, self.__api.getSensitivityBulk, 'getSensitivityBulk', idx=idx, own_data=own_data)

    def sensitivityParticle(self, unit, idx, parType, own_data=True):
        return self.load_data(unit, self.__api.getSensitivityParticle, 'getSensitivityParticle', idx=idx, parType=parType, own_data=own_data)

    def sensitivitySolid(self, unit, idx, parType, own_data=True):
        return self.load_data(unit, self.__api.getSensitivitySolid, 'getSensitivitySolid', idx=idx, parType=parType, own_data=own_data)

    def sensitivityFlux(self, unit, idx, own_data=True):
        return self.load_data(unit, self.__api.getSensitivityFlux, 'getSensitivityFlux', idx=idx, own_data=own_data)

    def sensitivityVolume(self, unit, idx, own_data=True):
        return self.load_data(unit, self.__api.getSensitivityVolume, 'getSensitivityVolume', idx=idx, own_data=own_data)

    def sensitivityDerivativeInlet(self, unit, idx, own_data=True):
        return self.load_data(unit, self.__api.getSensitivityDerivativeInlet, 'getSensitivityDerivativeInlet', idx=idx, own_data=own_data)

    def sensitivityDerivativeOutlet(self, unit, idx, own_data=True):
        return self.load_data(unit, self.__api.getSensitivityDerivativeOutlet, 'getSensitivityDerivativeOutlet', idx=idx, own_data=own_data)

    def sensitivityDerivativeBulk(self, unit, idx, own_data=True):
        return self.load_data(unit, self.__api.getSensitivityDerivativeBulk, 'getSensitivityDerivativeBulk', idx=idx, own_data=own_data)

    def sensitivityDerivativeParticle(self, unit, idx, parType, own_data=True):
        return self.load_data(unit, self.__api.getSensitivityDerivativeParticle, 'getSensitivityDerivativeParticle', idx=idx, parType=parType, own_data=own_data)

    def sensitivityDerivativeSolid(self, unit, idx, parType, own_data=True):
        return self.load_data(unit, self.__api.getSensitivityDerivativeSolid, 'getSensitivityDerivativeSolid', idx=idx, parType=parType, own_data=own_data)

    def sensitivityDerivativeFlux(self, unit, idx, own_data=True):
        return self.load_data(unit, self.__api.getSensitivityDerivativeFlux, 'getSensitivityDerivativeFlux', idx=idx, own_data=own_data)

    def sensitivityDerivativeVolume(self, unit, idx, own_data=True):
        return self.load_data(unit, self.__api.getSensitivityDerivativeVolume, 'getSensitivityDerivativeVolume', idx=idx, own_data=own_data)


class CadetDLL:

    def __init__(self, dll_path):
        self.cadet_path = dll_path
        self.__lib = ctypes.cdll.LoadLibrary(dll_path)

        # Query meta information
        cdtGetLibraryVersion = self.__lib.cdtGetLibraryVersion
        cdtGetLibraryVersion.restype = ctypes.c_char_p
        self.cadet_version = cdtGetLibraryVersion().decode('utf-8')

        cdtGetLibraryCommitHash = self.__lib.cdtGetLibraryCommitHash
        cdtGetLibraryCommitHash.restype = ctypes.c_char_p
        self.cadet_commit_hash = cdtGetLibraryCommitHash().decode('utf-8')

        cdtGetLibraryBranchRefspec = self.__lib.cdtGetLibraryBranchRefspec
        cdtGetLibraryBranchRefspec.restype = ctypes.c_char_p
        self.cadet_branch = cdtGetLibraryBranchRefspec().decode('utf-8')

        cdtGetLibraryBuildType = self.__lib.cdtGetLibraryBuildType
        cdtGetLibraryBuildType.restype = ctypes.c_char_p
        self.cadet_build_type = cdtGetLibraryBuildType().decode('utf-8')

        # Enable logging
        LOG_HANDLER_CLBK = ctypes.CFUNCTYPE(
            None,
            ctypes.c_char_p,
            ctypes.c_char_p,
            ctypes.c_uint,
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_char_p
        )
        set_log_handler = self.__lib.cdtSetLogReceiver
        set_log_handler.argtypes = [LOG_HANDLER_CLBK]
        set_log_handler.restype = None
        # Keep reference alive by assigning it to this Python object
        self.__log_handler = LOG_HANDLER_CLBK(log_handler)
        set_log_handler(self.__log_handler)

        self.__set_log_level = self.__lib.cdtSetLogLevel
        self.__set_log_level.argtypes = [ctypes.c_int]
        self.__set_log_level.restype = None
        self.__set_log_level(2)

        # Query API
        cdtGetAPIv010000 = self.__lib.cdtGetAPIv010000
        cdtGetAPIv010000.argtypes = [ctypes.POINTER(CADETAPIV010000)]
        cdtGetAPIv010000.restype = c_cadet_result

        self.__api = CADETAPIV010000()
        cdtGetAPIv010000(ctypes.byref(self.__api))

        self.__driver = self.__api.createDriver()

    def clear(self):
        if hasattr(self, "res"):
            del self.res
        self.__api.deleteDriver(self.__driver)
        self.__driver = self.__api.createDriver()

    def __del__(self):
        log_print('deleteDriver()')
        self.__api.deleteDriver(self.__driver)


    def run(self, filename = None, simulation=None, timeout = None, check=None):
        pp = PARAMETERPROVIDER()

        sim_input = recursively_convert_dict(simulation)

        pp.userData = NestedDictReader(sim_input)

        pp.getDouble = PARAMETERPROVIDER._fields_[1][1](param_provider_get_double)
        pp.getInt = PARAMETERPROVIDER._fields_[2][1](param_provider_get_int)
        pp.getBool = PARAMETERPROVIDER._fields_[3][1](param_provider_get_bool)
        pp.getString = PARAMETERPROVIDER._fields_[4][1](param_provider_get_string)

        pp.getDoubleArray = PARAMETERPROVIDER._fields_[5][1](param_provider_get_double_array)
        pp.getIntArray = PARAMETERPROVIDER._fields_[6][1](param_provider_get_int_array)
        pp.getBoolArray = ctypes.cast(None, PARAMETERPROVIDER._fields_[7][1])
        pp.getStringArray = ctypes.cast(None, PARAMETERPROVIDER._fields_[8][1])

        pp.getDoubleArrayItem = PARAMETERPROVIDER._fields_[9][1](param_provider_get_double_array_item)
        pp.getIntArrayItem = PARAMETERPROVIDER._fields_[10][1](param_provider_get_int_array_item)
        pp.getBoolArrayItem = PARAMETERPROVIDER._fields_[11][1](param_provider_get_bool_array_item)
        pp.getStringArrayItem = PARAMETERPROVIDER._fields_[12][1](param_provider_get_string_array_item)

        pp.exists = PARAMETERPROVIDER._fields_[13][1](param_provider_exists)
        pp.isArray = PARAMETERPROVIDER._fields_[14][1](param_provider_is_array)
        pp.numElements = PARAMETERPROVIDER._fields_[15][1](param_provider_num_elements)
        pp.pushScope = PARAMETERPROVIDER._fields_[16][1](param_provider_push_scope)
        pp.popScope = PARAMETERPROVIDER._fields_[17][1](param_provider_pop_scope)

        self.__api.runSimulation(self.__driver, ctypes.byref(pp))
        self.res = SimulationResult(self.__api, self.__driver)
        return self.res

    def load_solution(self, sim, solution, solution_str):
        # - [ ] Split Components (Should be unified)
        # - [ ] Split Ports (incl `SINGLE_AS_MULTI_PORT`)
        # - [ ] Split Partype (Particle + Solid)
        # - [ ] Coordinates?
        # - [ ] Sensitivities / IDs
        # - [ ] LAST_STATE_Y / LAST_STATE_YDOT
        # - [ ] LAST_STATE_SENSY_XXX / LAST_STATE_SENSYDOT_XXX
        solution = addict.Dict()
        if self.res is not None:
            for key, value in sim.root.input['return'].items():
                if key.startswith('unit'):
                    if value[f'write_{solution_str}']:
                        unit = int(key[-3:])
                        t, out = solution(unit)

                        if not len(solution.solution_times):
                            solution.solution_times = t

                        solution[key][solution_str] = out
        return solution

    def load_solution_io(self, sim, solution, solution_str):
        solution = addict.Dict()
        if self.res is not None:
            for key,value in sim.root.input['return'].items():
                if key.startswith('unit'):
                    if value[f'write_{solution_str}']:
                        unit = int(key[-3:])
                        t, out = self.res.inlet(unit)

                        if not len(solution.solution_times):
                            solution.solution_times = t
                            
                        for comp in range(out.shape[2]):
                            comp_out = numpy.squeeze(out[:,:,comp])
                            solution[key][f'{solution_str}_comp_{comp:03d}'] = comp_out
        return solution

    def load_inlet(self, sim):
        return self.load_solution_io(sim, self.res.inlet, 'solution_inlet')

    def load_outlet(self, sim):
        return self.load_solution_io(sim, self.res.outlet, 'solution_outlet')

    def load_bulk(self, sim):
        return self.load_solution(sim, self.res.bulk, 'solution_bulk')

    def load_particle(self, sim):
        return self.load_solution(sim, self.res.particle, 'solution_particle')

    def load_solid(self, sim):
        return self.load_solution(sim, self.res.solid, 'solution_solid')

    def load_flux(self, sim):
        return self.load_solution(sim, self.res.flux, 'solution_flux')
    
    def load_flux(self, sim):
        return self.load_solution(sim, self.res.flux, 'solution_flux')
    
    def load_volume(self, sim):
        return self.load_solution(sim, self.res.volume, 'solution_volume')
    
    def load_derivative_inlet(self, sim):
        return self.load_solution_io(sim, self.res.soldot_inlet, 'soldot_inlet')
    
    def load_derivative_outlet(self, sim):
        return self.load_solution_io(sim, self.res.soldot_outlet, 'soldot_outlet')
    
    def load_derivative_bulk(self, sim):
        return self.load_solution(sim, self.res.soldot_bulk, 'soldot_bulk')

    def load_derivative_particle(self, sim):
        return self.load_solution(sim, self.res.soldot_particle, 'soldot_particle')

    def load_derivative_solid(self, sim):
        return self.load_solution(sim, self.res.soldot_solid, 'soldot_solid')

    def load_derivative_flux(self, sim):
        return self.load_solution(sim, self.res.soldot_flux, 'soldot_flux')

    def load_derivative_volume(self, sim):
        return self.load_solution(sim, self.res.soldot_volume, 'soldot_volume')

    def load_sensitivity_inlet(self, sim):
        return self.load_solution_io(sim, self.res.sens_inlet, 'sens_inlet')

    def load_sensitivity_outlet(self, sim):
        return self.load_solution_io(sim, self.res.sens_outlet, 'sens_outlet')

    def load_sensitivity_bulk(self, sim):
        return self.load_solution(sim, self.res.sens_bulk, 'sens_bulk')

    def load_sensitivity_particle(self, sim):
        return self.load_solution(sim, self.res.sens_particle, 'sens_particle')

    def load_sensitivity_solid(self, sim):
        return self.load_solution(sim, self.res.sens_solid, 'sens_solid')

    def load_sensitivity_flux(self, sim):
        return self.load_solution(sim, self.res.sens_flux, 'sens_flux')

    def load_sensitivity_volume(self, sim):
        return self.load_solution(sim, self.res.sens_volume, 'sens_volume')

    def load_sensitivity_derivative_inlet(self, sim):
        return self.load_solution_io(sim, self.res.sensdot_inlet, 'sensdot_inlet')

    def load_sensitivity_derivative_outlet(self, sim):
        return self.load_solution_io(sim, self.res.sensdot_outlet, 'sensdot_outlet')

    def load_sensitivity_derivative_bulk(self, sim):
        return self.load_solution(sim, self.res.sensdot_bulk, 'sensdot_bulk')

    def load_sensitivity_derivative_particle(self, sim):
        return self.load_solution(sim, self.res.sensdot_particle, 'sensdot_particle')

    def load_sensitivity_derivative_solid(self, sim):
        return self.load_solution(sim, self.res.sensdot_solid, 'sensdot_solid')

    def load_sensitivity_derivative_flux(self, sim):
        return self.load_solution(sim, self.res.sensdot_flux, 'sensdot_flux')

    def load_sensitivity_derivative_volume(self, sim):
        return self.load_solution(sim, self.res.sensdot_volume, 'sensdot_volume')

    def load_results(self, sim):
        sim.root.output.solution.update(self.load_inlet(sim))
        sim.root.output.solution.update(self.load_outlet(sim))
        sim.root.output.solution.update(self.load_bulk(sim))
        sim.root.output.solution.update(self.load_particle(sim))
        sim.root.output.solution.update(self.load_solid(sim))
        sim.root.output.solution.update(self.load_flux(sim))
        sim.root.output.solution.update(self.load_volume(sim))
        sim.root.output.solution.update(self.load_derivative_inlet(sim))
        sim.root.output.solution.update(self.load_derivative_outlet(sim))
        sim.root.output.solution.update(self.load_derivative_bulk(sim))
        sim.root.output.solution.update(self.load_derivative_particle(sim))
        sim.root.output.solution.update(self.load_derivative_solid(sim))
        sim.root.output.solution.update(self.load_derivative_flux(sim))
        sim.root.output.solution.update(self.load_derivative_volume(sim))
        sim.root.output.solution.update(self.load_sensitivity_inlet(sim))
        sim.root.output.solution.update(self.load_sensitivity_outlet(sim))
        sim.root.output.solution.update(self.load_sensitivity_bulk(sim))
        sim.root.output.solution.update(self.load_sensitivity_particle(sim))
        sim.root.output.solution.update(self.load_sensitivity_solid(sim))
        sim.root.output.solution.update(self.load_sensitivity_flux(sim))
        sim.root.output.solution.update(self.load_sensitivity_volume(sim))
        sim.root.output.solution.update(self.load_sensitivity_derivative_inlet(sim))
        sim.root.output.solution.update(self.load_sensitivity_derivative_outlet(sim))
        sim.root.output.solution.update(self.load_sensitivity_derivative_bulk(sim))
        sim.root.output.solution.update(self.load_sensitivity_derivative_particle(sim))
        sim.root.output.solution.update(self.load_sensitivity_derivative_solid(sim))
        sim.root.output.solution.update(self.load_sensitivity_derivative_flux(sim))
        sim.root.output.solution.update(self.load_sensitivity_derivative_volume(sim))


def recursively_convert_dict(data):
    ans = addict.Dict()
    for key_original, item in data.items():
        if isinstance(item, dict):
            ans[key_original] = recursively_convert_dict(item)
        else:
            key = str.upper(key_original)
            ans[key] = item
    return ans
