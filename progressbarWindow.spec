# -*- mode: python -*-

block_cipher = None


a = Analysis(['progressbarWindow.py'],
             pathex=['F:\\MyProject\\Ulord\\uwallet-client-pro'],
             binaries=[],
             datas=[],
             hiddenimports=['queue'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='progressbarWindow',
          debug=False,
          strip=False,
          upx=True,
          console=False , version='version', icon='uwallet.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='progressbarWindow')
