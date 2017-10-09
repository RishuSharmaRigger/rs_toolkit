import sys
sys.path.append(r'D:\rishu\rs_toolkit')
import rs_toolkit_class
reload(rs_toolkit_class)

win = rs_toolkit_class.testWin()
win.show(dockable=1)