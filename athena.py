#!/usr/bin/env python3
import PySimpleGUIQt as gui
import webbrowser, os
from configparser import ConfigParser

def writeconfig():
    config = ConfigParser()
    config['DEFAULT'] = {
        'theme': ''
    }
    with open('config.cfg', 'w') as f:
        config.write(f)

def checkconfig():
    if os.path.exists('config.cfg') == True:
        pass
    elif os.path.exists('config.cfg') == False:
        writeconfig()
        checkconfig()

checkconfig()
def themewindow():
    config = ConfigParser()
    config.read('config.cfg')
    layout = [
        [gui.T('Choose Theme')],
        [gui.Radio('Light', 'RADIO1'), gui.Radio('Dark', 'RADIO01', key='_THEME_')],
        [gui.Button('Exit'), gui.Button('Enter')]
    ]
    window = gui.Window('Theme Picker', no_titlebar=True, keep_on_top=True, grab_anywhere=True).Layout(layout)
    while True:
        event, values = window.Read()
        if event == 'Exit':
            break
        elif event == 'Enter':
            if values['_THEME_'] == True:
                config['DEFAULT']['theme'] = 'dark'
                with open('config.cfg', 'w') as f:
                    config.write(f)
                break
            elif values['_THEME_'] == False:
                config['DEFAULT']['theme'] = 'light'
                with open('config.cfg', 'w') as f:
                    config.write(f)
                break
    config.read('config.cfg')
    theme = config['DEFAULT']['theme']
    window.Close()
    return theme

theme = themewindow()
if theme == 'light':
    bgcolor = None
    tebgcolor = None
    iebgcolor = None
    bcolor = ('black', '#49b6ff')
    itcolor = 'black'
    tcolor = 'black'
elif theme == 'dark':
    bgcolor = '#0a0a0a'
    tebgcolor = '#0a0a0a'
    iebgcolor = '#0f0f0f'
    bcolor = ('white', '#0f0f0f')
    itcolor = 'white'
    tcolor = 'white'

gui.SetOptions(background_color=bgcolor, text_element_background_color=tebgcolor, input_elements_background_color=iebgcolor, button_color=bcolor, border_width=0, input_text_color=itcolor, text_color=tcolor)
def main():
    layout = [
        [gui.T('Have You Installed Theos Before? ', font=('Arial', 10), justification='center')],
        [gui.Radio('No', 'RADIO1', default=True), gui.Radio('Yes', 'RADIO1', key='_RADIOYES_', default=True)],
        [gui.Button('Exit'), gui.Button('Enter')]
    ]
    window = gui.Window('Check Theos Install', no_titlebar=True, keep_on_top=True, grab_anywhere=True).Layout(layout)
    while True:
        event, values = window.Read()
        if event == 'Exit':
            exit()
            break
        if event == 'Enter':
            if values['_RADIOYES_'] == True:
                window.Close()
                break
            elif values['_RADIOYES_'] == False:
                while True:
                    window2 = gui.Window('Open Tutorial', no_titlebar=True, keep_on_top=True, grab_anywhere=True).Layout([[gui.Text('Please Install Theos First ', justification='center')], [gui.Button('Exit'), gui.Button('Open Link')]])
                    event, values = window2.Read()
                    if event == 'Exit':
                        window2.Close()
                        break
                    elif event == 'Open Link':
                        webbrowser.open_new_tab('https://github.com/theos/theos')
                        window2.Close()
                        break
                        
    theosgui()

def theosgui():
    nic_layout = [
        [gui.Text('Athena | Theos GUI', font=('Arial', 13, 'bold'), text_color=tcolor, justification='center')],
        [gui.Text('Developed by @maxbridgland', font=('Arial', 10, 'italic'), text_color=tcolor, justification='center')],
        [gui.T('New Tweak Creator', font=('Arial', 13, 'bold'), justification='center')],
        [gui.T('Project Name:', justification='left'), gui.InputText('ExampleTweak', text_color=itcolor, size=(20,1), key='_PROJNAME_', justification='right')],
        [gui.T('Package Name:', justification='left'), gui.InputText('com.Athena.exampletweak', text_color=itcolor, size=(20,1), key='_PACKNAME_', justification='right')],
        [gui.T('Author Name:', justification='left'), gui.InputText('AthenaTeam', text_color=itcolor, size=(20,1), key='_AUTHNAME_', justification='right')],
        [gui.Button('Create New Package')],
        [gui.Text('')],
        [gui.Text('_' * 100)],
        [gui.Text('')],
        [gui.T('Tweak Compiler', font=('Arial', 13, 'bold'), justification='center')],
        [gui.T('Project Directory:', justification='left'), gui.InputText('C:\\Example\\Tweak\\Path', text_color=itcolor, size=(50,1), key='_TWEAKPATH_', justification='right'), gui.FolderBrowse()],
        [gui.Checkbox('Install To Device (Required .bashrc setup)  ', text_color=itcolor, key='_INSTALL_', default=False), gui.Checkbox('Clean Directory/Theos Cache', text_color=itcolor, key='_CLEAN_', default=True), gui.Checkbox('Final Package Flag', text_color=itcolor, key='_FINAL_', default=True)],
        [gui.T('Theos Device IP (Enter Only If Using Install To Device): ', justification='left'), gui.InputText('', text_color=itcolor, size=(20,1), justification='center', key='_DEVIP_')],
        [gui.Button('Build')],
        [gui.Button('Exit'), gui.Button('Donate')]
    ]
    window = gui.Window('Athena', no_titlebar=True, keep_on_top=True, grab_anywhere=True).Layout(nic_layout)
    count = 0
    while True:
        event, values = window.Read()
        if event == 'Exit':
            window.Close()
            break
        elif event == 'Create New Package':
            if len(values['_PROJNAME_']) == 0:
                count += 1
            if len(values['_PACKNAME_']) == 0:
                count += 1
            if len(values['_AUTHNAME_']) == 0:
                count += 1
            if count >= 1:
                gui.Window('Error', no_titlebar=True, keep_on_top=True, auto_close=True, auto_close_duration=1).Layout([[gui.T('Error: Missing Value! ', justification='center')]]).Read()
            createnewpkg(values['_PROJNAME_'], values['_PACKNAME_'], values['_AUTHNAME_'])
        elif event == 'Build':
            if values['_TWEAKPATH_'] == '':
                gui.Window('Error', no_titlebar=True, keep_on_top=True, auto_close=True, auto_close_duration=1).Layout([[gui.T('Error: Missing Tweak Path! ', justification='center')]]).Read()
            elif values['_TWEAKPATH_'] != '':
                path = values['_TWEAKPATH_']
            if values['_INSTALL_'] == True:
                install = 'install'
            elif values['_INSTALL_'] == False:
                install = ''
            if values['_CLEAN_'] == True:
                clean = 'clean'
            elif values['_CLEAN_'] == False:
                clean = ''
            if values['_FINAL_'] == True:
                final = 'FINALPACKAGE=1'
            elif values['_FINAL_'] == False:
                final = ''
            query = "make %s package %s -C %s %s" % (clean, install, path, final)
            buildwindow(path, query)
        elif event == 'Donate':
            webbrowser.open_new_tab('https://paypal.me/AuxilumDevelopment')

def buildwindow(path, query):
    os.system(query)
    layout = [
        [gui.Text('Info: It make take a few moments to run and build the program. Refer to your console if there are any errors they will show there.')],
        [gui.Button('Open Package Directory', key='_OPEN_'), gui.Button('Close')]
    ]
    window = gui.Window('Build', no_titlebar=True, keep_on_top=True, grab_anywhere=True).Layout(layout)
    while True:
        event, values = window.Read()
        if event == 'Open Package Directory':
            path = os.path.realpath(path)
            os.startfile(path)
            break
        if event == 'Close':
            break
    window.Close()

def createnewpkg(projectname, packagename, authname):
    layout = [
        [gui.Text('New Package Creator')],
        [gui.Text('Package Name: %s' % packagename, justification='center')],
        [gui.Text('Project Name: %s' % projectname, justification='center')],
        [gui.Text('Author Name: %s' % authname, justification='center')],
        [gui.Text('Maintainer: ', justification='center'), gui.InputText('', size=(30,1), key='_MAINTAINER_', justification='center')],
        [gui.Text('Description: ', justification='center'), gui.InputText('', size=(30, 1), key='_DESCRIPTION_', justification='center')],
        [gui.Text('Version: ', justification='center'), gui.InputText('1.0.0', size=(10, 1), key='_VERSION_', justification='center')],
        [gui.Text('Dependencies: ', justification='center')],
        [gui.InputText('mobilesubstrate, libcolorpicker', size=(100, 1), justification='center', key='_DEPENDENCIES_')],
        [gui.Text('Filter: ', justification='center'), gui.InputText('com.apple.SpringBoard', size=(30, 1), key='_FILTER_', justification='center')],
        [gui.Text('Kill Process On Install: ', justification='center'), gui.InputText('SpringBoard', size=(30, 1), key='_KILLPROC_', justification='center')],
        [gui.Text('Folder To Build To', font=('Arial', 13, 'bold'), justification='center')],
        [gui.InputText('', size=(70, 1), justification='left', key='_BUILDPATH_'), gui.FolderBrowse()],
        [gui.Button('Cancel'), gui.Button('Create')]
    ]
    window = gui.Window('Create Menu', no_titlebar=True, keep_on_top=True, grab_anywhere=True).Layout(layout)
    count = 0
    while True:
        event, values = window.Read()
        if event == 'Cancel':
            break
        if event == 'Create':
            if values['_FILTER_'] == '':
                count = 1
            elif values['_FILTER_'] != '':
                appfilter = values['_FILTER_']
                count = 0
            if values['_KILLPROC_'] == '':
                count = 2
            elif values['_KILLPROC_'] != '':
                killproc = values['_KILLPROC_']
            if values['_BUILDPATH_'] == '':
                count = 3
            elif values['_BUILDPATH_'] != '':
                buildpath = values['_BUILDPATH_']
            if values['_DEPENDENCIES_'] == 'Ex: mobilesubstrate, libcolorpicker':
                count = 4
            elif values['_DEPENDENCIES_'] != 'Ex: mobilesubstrate, libcolorpicker':
                dependencies = values['_DEPENDENCIES_']
            description = values['_DESCRIPTION_']
            maintainer = values['_MAINTAINER_']
            version = values['_MAINTAINER_']
            controltemp = """Package: %s
Name: %s
Depends: %s
Version: %s
Architecture: iphoneos-arm
Description: %s
Maintainer: %s
Author: %s
Section: Tweaks""" % (packagename, projectname, dependencies, version, description, maintainer, authname)
            plisttemp = """{ Filter = { Bundles = ( "%s" ); }; }""" % appfilter
            makefiletemp = """ARCHS = arm64
include $(THEOS)/makefiles/common.mk
TWEAK_NAME = %s
%s_FILES = Tweak.xm

include $(THEOS_MAKE_PATH)/tweak.mk

after-install::
        install.exec "killall -9 %s" """ % (projectname, projectname, killproc)
            plistname = buildpath + "/%s.plist" % projectname
            with open(plistname, 'w') as f:
                f.write(plisttemp)
                f.close()
            with open(buildpath+'/control', 'w') as f:
                f.write(controltemp)
                f.close()
            with open(buildpath+'/Makefile', 'w') as f:
                f.write(makefiletemp)
                f.close()
            with open(buildpath+"/Tweak.xm", "w") as f:
                f.write("Write your code here boi")
                f.close()
        if count == 1:
            gui.Window('Error', no_titlebar=True, keep_on_top=True, auto_close=True, auto_close_duration=1).Layout([[gui.T('Error: Missing Filter! ', justification='center')]]).Read()
            count = 0
        elif count == 2:
            gui.Window('Error', no_titlebar=True, keep_on_top=True, auto_close=True, auto_close_duration=1).Layout([[gui.T('Error: Missing Kill Process! ', justification='center')]]).Read()
            count = 0
        elif count == 3:
            gui.Window('Error', no_titlebar=True, keep_on_top=True, auto_close=True, auto_close_duration=1).Layout([[gui.T('Error: Missing Build Path! ', justification='center')]]).Read()
            count = 0

    window.Close()
main()
