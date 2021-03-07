from cx_Freeze import setup, Executable

base = "Win32GUI"

executables = [
    Executable('core.py', base=base)
]

setup(name='PowerBox',
      version='0.9',
      description="Human's work optimization",
      executables=executables)
