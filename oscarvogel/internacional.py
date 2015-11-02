# coding: utf-8
import os
import gettext
import locale

# primero, establecer que configuración de internacionalización se utiliza:

print locale.setlocale(locale.LC_ALL, "");

# luego, ubicar la carpeta de localizaciones (con la estructura correcta):

localedir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'locales'))
print "localedir", localedir

gettext.bindtextdomain('internacional', localedir)
gettext.textdomain('internacional')

_ = gettext.gettext

print gettext.find('internacional', localedir, None, True)

# el mensaje a traducir debe ser escrito tal cual 
print _('Hello, world!')     
