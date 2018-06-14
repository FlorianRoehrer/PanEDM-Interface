#!/bin/sh
pyuic5 -x ./GUI/Interface_Main_Window.ui -o ./GUI/PanEDMInterface_Main_Window_GUI.py
pyuic5 -x ./GUI/Infowindow.ui -o ./GUI/InfowindowGUI.py
pyuic5 -x ./GUI/Login.ui -o ./GUI/LoginGUI.py
pyuic5 -x ./GUI/Settings.ui -o ./GUI/SettingsGUI.py
