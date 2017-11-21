#pip install pywinauto
import cv2
import os
from pywinauto import application
from pywinauto import mouse


def open_Microhardness():
    """
    from pywinauto import application
    app = application.Application().start('notepad.exe')
    app.Notepad.menu_select('Файл->Открыть')
    print(0)
    # app.[window title].[control name]...
    app['Открыть'].Edit.SetText('filename.txt')
    app['Открыть'].Open.Click()
     """

    app = application.Application().start('Microhardness 5.1.exe')
    wf = app.window(best_match='Микротвердость')
    wf.Wait('visible').Maximize()
    mouse.click(button='left', coords=(10, 25))
    wf.Wait('ready')
    mouse.click(button='left', coords=(10, 55))

    dlg = app.window(best_match='Открытие')
    dlg.Wait('ready')
    directory = os.path.dirname(os.path.abspath(__file__))
    dlg['Edit'].SetText(os.path.join(directory, 'screen.jpg'))
    btn = dlg.ChildWindow(best_match='Открыть').Click()
    btn.Click()

    wf.Restore()


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
open = 0
while(True):

    # Capture frame-by-frameq
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLORMAP_AUTUMN)

    # Display the resulting frame
    cv2.imshow('frame',gray)

    if cv2.waitKey(10) & 0xFF == ord('s'):
        cv2.imwrite('screen.jpg',frame)
        open = 1
        break
    else:
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
if (open == 1):
    open_Microhardness()
