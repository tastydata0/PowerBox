# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['E:\\Python\\PowerBox\\core.py'],
             pathex=['E:\\Python\\PowerBox'],
             binaries=[],
             datas=[],
             hiddenimports=['pyttsx3.drivers', 'pyttsx3.drivers.dummy', 'pyttsx3.drivers.espeak', 'pyttsx3.drivers.nsss', 'pyttsx3.drivers.sapi5', 'pyttsx3.drivers.*'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='core',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='E:\\Python\\PowerBox\\powerboxBright.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='core')
