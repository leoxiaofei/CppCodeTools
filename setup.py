from distutils.core import setup
import py2exe

setup(
    zipfile=None,
    windows=[{"script": "CppCodeTools.pyw", "icon_resources": [(1, "res/app.ico")]}],
    options={"py2exe": {"dll_excludes": ["MSVCP90.dll"], "compressed": 1, "optimize": 2, "bundle_files": 1}},
    #data_files=[("res", ["res/app.ico"])]
)
