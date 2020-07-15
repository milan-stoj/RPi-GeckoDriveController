@echo off

echo pyuic5 will convert "guimech.ui" to a "guimech.py"
pause
@echo on
pyuic5 -x guimech.ui -o guimech.py
@echo off

echo pyrcc5 will convert "resources.qrc" to "resources_rc.py"
pause
@echo on
pyrcc5 resources.qrc -o  resources_rc.py
@echo off
pause
