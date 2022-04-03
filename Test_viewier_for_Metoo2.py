from pywinauto.application import Application

app = Application().Start(cmd_line=u'"C:\\Program Files (x86)\\SASM\\sasm.exe" ')
qtqwindowicon = app.SASM
qtqwindowicon.Wait('ready')

app = Application().Start(cmd_line=u'"C:\\Program Files (x86)\\SASM\\sasm.exe" ')
qtqwindowicon = app.SASM
qtqwindowicon.Wait('ready')

app2 = Application().Connect(title=u'SASM', class_name='Qt5QWindowIcon')
qtqwindowicon2 = app2.SASM