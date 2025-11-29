# UTF-8
#
# Version information for SunoApiDownloader.exe
# This helps reduce false positives from antivirus software

from PyInstaller.utils.win32.versioninfo import (
    VSVersionInfo, VarFileInfo, VarStruct, StringFileInfo, 
    StringTable, StringStruct, FixedFileInfo
)

version_info = VSVersionInfo(
    ffi=FixedFileInfo(
        filevers=(1, 0, 0, 0),
        prodvers=(1, 0, 0, 0),
        mask=0x3f,
        flags=0x0,
        OS=0x40004,
        fileType=0x1,
        subtype=0x0,
        date=(0, 0)
    ),
    kids=[
        StringFileInfo([
            StringTable(
                u'040904B0',
                [
                    StringStruct(u'CompanyName', u'SunoSync'),
                    StringStruct(u'FileDescription', u'Suno Music Downloader'),
                    StringStruct(u'FileVersion', u'1.0.0.0'),
                    StringStruct(u'InternalName', u'SunoApiDownloader'),
                    StringStruct(u'LegalCopyright', u'Copyright (C) 2024'),
                    StringStruct(u'OriginalFilename', u'SunoApiDownloader.exe'),
                    StringStruct(u'ProductName', u'SunoSync'),
                    StringStruct(u'ProductVersion', u'1.0.0.0')
                ]
            )
        ]),
        VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
    ]
)

