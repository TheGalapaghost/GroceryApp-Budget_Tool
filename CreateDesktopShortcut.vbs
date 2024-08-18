Set WshShell = CreateObject("Wscript.Shell")

Set fso = CreateObject("Scripting.FileSystemObject")

CurrentDirectory = fso.GetAbsolutePathName(".")

Desktop = WshShell.SpecialFolders("Desktop")

WorkingDirectory = Desktop + "\Shopping Calculator.lnk"

TargetDirectory = CurrentDirectory + "\Main\Shopping Calculator.html"

IcoDirectory = CurrentDirectory + "\Main\Shopping_DESK_ICO.ico"

Set Shortcut = WshShell.CreateShortcut(WorkingDirectory)

Shortcut.TargetPath = TargetDirectory

Shortcut.IconLocation = IcoDirectory

Shortcut.save
