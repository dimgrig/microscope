#pip install pywinauto

import sys, os

#from pywinauto.application import Application



# app = Application(backend="uia").start('notepad.exe')
#
# # Опишем окно, которое хотим найти в процессе Notepad.exe
# dlg_spec = app.UntitledNotepad
# # ждем пока окно реально появится
# actionable_dlg = dlg_spec.wait('visible')

"""
from pywinauto import application
app = application.Application().start('notepad.exe')
app.Notepad.menu_select('Файл->Открыть')
print(0)
# app.[window title].[control name]...
app['Открыть'].Edit.SetText('filename.txt')
app['Открыть'].Open.Click()
 """

from pywinauto import application
from pywinauto import mouse

#app = application.Application().start('Microhardness 5.1.exe')
app = application.Application().start('Microhardness 5.1.exe')




#app['Микротвердость'].wait('visible').menu_select('Файл->Открыть изображение')
wf = app.window(best_match='Микротвердость')
wf.Wait('visible').Maximize()

mouse.click(button='left', coords=(10, 25))
wf.Wait('ready')
mouse.click(button='left', coords=(10, 55))
#wf.menu_select('Файл->Открыть изображение')

# app.[window title].[control name]...
#app['Открыть'].Edit.SetText('filename.txt')
#app['Открыть'].Open.Click()


dlg = app.window(best_match='Открытие')
dlg.Wait('ready')
directory = os.path.dirname(os.path.abspath(__file__))

dlg['Edit'].SetText(os.path.join(directory, 'screen.jpg'))
btn = dlg.ChildWindow(best_match='Открыть').Click()
btn.Click()

wf.Restore()
"""

app = Application(backend="uia").start('Microhardness 5.1.exe')

print(app)

#wf = app.window(best_match='Микротвердость').menu_select("Файл->Открыть изображение")
wf = app['Микротвердость'].menu_select("Файл->Открыть изображение")
print("00")


dlg = app['Открытие']
print("0")

OpenDialog = app.Window(best_match=u'Открытие', class_name='#32770')
print("11")
#wf.print_control_identifiers()

#dlg = app.window(best_match='Открытие')
#actionable_dlg = dlg.wait('visible')

#dlg = app.window(title_re="Открытие", class_name="#32770")
#dlg = app.top_window()
#dlg = app.Dialog.CheckBoxEx32.WindowText()
#dlg['ComboBoxEx32'].set_text("ООРВР")
print("1")
dlg = app['Открытие']
print("2")
dlg.print_control_identifiers()
print("3")
#actionable_dlg.ComboBoxEx32.set_text("ООРВР")

#db = app.window(best_match='Открытие')
"""
