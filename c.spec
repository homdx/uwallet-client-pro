# -*- mode: python -*-

block_cipher = None


a = Analysis(['c', 'uwallet'],
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
          name='c',
          debug=True,
          strip=False,
          upx=False,
          console=True , icon='Uwallet.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='c')
