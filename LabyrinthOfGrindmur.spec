# -*- mode: python ; coding: utf-8 -*-

import os

block_cipher = None
repo_root = SPECPATH
entry_script = os.path.join(repo_root, 'LabyrinthOfGrindmur', 'main.py')

a = Analysis(
    [entry_script],
    pathex=[os.path.join(repo_root, 'LabyrinthOfGrindmur')],
    binaries=[],
    datas=[
        (
            os.path.join(repo_root, 'LabyrinthOfGrindmur', 'rexpaint_cp437_10x10.png'),
            'LabyrinthOfGrindmur',
        ),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='LabyrinthOfGrindmur',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='LabyrinthOfGrindmur',
)