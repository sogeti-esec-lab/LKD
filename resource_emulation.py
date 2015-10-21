import ctypes
import itertools
import windows
import windows.hooks
from windows.generated_def.winstructs import *


class Ressource(object):

    def __init__(self, filename, lpName, lpType):
        self.filename = filename
        self.lpName = lpName
        self.lpType = lpType
        self.driver_data = None
        self.loaded_ressource = None

    def match(self, hModule, lpName, lpType):
        x = not hModule and self.lpName == lpName and self.lpType == lpType
        return x

    def get_driver_data(self):
        if self.driver_data is not None:
            return self.driver_data
        self.driver_data = open(self.filename, 'rb').read()
        return self.driver_data

    def load_resource(self):
        driver_data = self.get_driver_data()
        char_p = ctypes.c_char_p(driver_data)
        real_addr = ctypes.cast(char_p, ctypes.c_void_p).value
        return real_addr

    def resource_len(self):
        return len(self.get_driver_data())

resource_list = []
HRSRC_dict = {}
HRSRC_attibution = itertools.count(0x42424242)


@windows.hooks.Callback(PVOID, PVOID, PVOID, PVOID)
def FindResourceWHook(hModule, lpName, lpType, real_function):
    for res in resource_list:
        if res.match(hModule, lpName, lpType):
            HRSRC = next(HRSRC_attibution)
            HRSRC_dict[HRSRC] = res
            return HRSRC
    return real_function()


@windows.hooks.SizeofResourceCallback
def SizeofResourceHook(hModule, hResInfo, real_function):
    if hResInfo in HRSRC_dict:
        return HRSRC_dict[hResInfo].resource_len()
    return real_function()


@windows.hooks.LoadResourceCallback
def LoadResourceHook(hModule, hResInfo, real_function):
    if hResInfo in HRSRC_dict:
        return HRSRC_dict[hResInfo].load_resource()
    return real_function()


@windows.hooks.LockResourceCallback
def LockResourceHook(hResData, real_function):
    x = real_function()
    return x
