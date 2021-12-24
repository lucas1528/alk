from cx_Freeze import setup, Executable
import sys
 

base = None
if sys.platform == 'win32':
    base = "Win32GUI"

buildOptions = dict(
    packages = [],
    includes = ['tkinter','functions','time','webbrowser'],
    include_files = ['icone.png','bicos.txt']
)

setup(name='ALK',
    version='2.0',
    description='Tabela Automec com laudo',
    options= dict(build_exe = buildOptions),
    executables = [Executable(
                   script='alk.py',
                   base=base,
                   icon= 'icone.ico'
                   )
                  ]
)