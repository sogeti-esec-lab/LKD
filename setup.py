from setuptools import setup
# -*- coding: utf-8 -*-

PKG_NAME = "LKD"
VERSION  = "1.0"

SETUP_DATA_FILES = []
SETUP_DATA_FILES_32 = []
SETUP_DATA_FILES_64 = []

SETUP_DATA_FILES_32.append("bin/DBGDLL/dbgeng.dll")
SETUP_DATA_FILES_32.append("bin/DBGDLL/dbghelp.dll")
SETUP_DATA_FILES_32.append("bin/DBGDLL/symsrv.dll")
SETUP_DATA_FILES_32.append("bin/DBGDLL/symsrv.yes")
SETUP_DATA_FILES_64.append("bin/DBGDLL64/dbgeng.dll")
SETUP_DATA_FILES_64.append("bin/DBGDLL64/dbghelp.dll")
SETUP_DATA_FILES_64.append("bin/DBGDLL64/symsrv.dll")
SETUP_DATA_FILES_64.append("bin/DBGDLL64/symsrv.yes")
SETUP_DATA_FILES.append("bin/windbg_driver_x64.sys")
SETUP_DATA_FILES.append("bin/windbg_driver_x86.sys")

setup(
    name = PKG_NAME,
    version = VERSION,
    author = 'Samuel Chevet, Clément Rouault',
    author_email = 'none',
    description = ' python wrapper around dbgengine.dll',
    license = 'BSD',
    keywords = 'dbgengine python',
    url = 'https://github.com/sogeti-esec-lab/LKD',
    py_modules= ['dbginterface', 'dbgdef', 'driver_upgrade', 'resource_emulation', 'simple_com'],
    packages = ['windows', 'windows/generated_def', 'windows/native_exec', 'windows/utils'],
    data_files=[('bin', SETUP_DATA_FILES), ('bin/DBGDLL', SETUP_DATA_FILES_32), 
        ('bin/DBGDLL64',SETUP_DATA_FILES_64)],
)