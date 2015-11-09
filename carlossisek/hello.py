#!/usr/bin/env python
# -*- coding: utf-8 -*-
#####################################################
__author__ = "Carlos Sisek (carlos.sisek@gmail.com)"
__copyright__ = "Copyright (C) 2015 Carlos Sisek"
__license__ = "GPL 3.0"
__version__ = "1"
#####################################################
import locale
import argparse
import os
import gettext
import sys


def print_version(_):
    print _("Copyright (C) Carlos Sisek - carlos.sisek@gmail.com\n\
___________________________________________________\n\
Made for the Diploma in Free Software\n\
Course: Programming II - University of the East\n\
===================================================\n\
License GPLv3+: GNU GPL version 3 \n\
This is free software: you are free to change and redistribute it.\n\
There is NO WARRANTY, to the extent permitted by law.")


def main():
    # Define el idioma (https://docs.python.org/2/library/locale.html)
    locale.setlocale(locale.LC_ALL, '')

    # Implementa la ubicacion de la carpeta de internacionalización
    #(https://docs.python.org/2.7/library/os.path.html)
    traduccion = os.path.abspath(os.path.join(os.path.dirname(__file__), 'locales'))
    print traduccion
    #Las funciones “textdomain” y “bindtextdomain” sirven para decirle a
    #gettext dónde se encuentran las traducciones.
    #http://crysol.org/es/node/203
    gettext.bindtextdomain('hello', traduccion)
    gettext.textdomain('hello')
    _ = gettext.gettext
    #Inicializa el mensaje, para el idioma x defecto
    greeting_msg = _("Hello, world!")

    #Inicializa el uso de ArgParse
    #(https://docs.python.org/2/howto/argparse.html)
    parser = argparse.ArgumentParser()
    #Aquí definimos los argumentos a pasar a la linea de comandos
    parser.add_argument("-s", "--standard",
        help=_("-s, --standard       use standard greeting"),
        action="store_true")
    parser.add_argument("-a", "--alternative",
        help=_("-a, --alternative=TEXT     use TEXT as the other greeting message"),
        action="store")
    parser.add_argument("-v", "--version",
        help=_("-v, --version       display version of script and exit"),
        action="store_true")
    args = parser.parse_args()

    if args.standard:
        #Imprime el mensaje standard
        greeting_msg = _("hello, world!")
    elif args.alternative is not None:
        #Imprime el mensaje alternativo señalado como argumento de -a / --alternative
        greeting_msg = args.alternative
    elif args.version:
        #Imprime la version de la aplicacion
        print_version(_)
        sys.exit()

    #Imprime el mensaje y sale (ejecutado sin argumentos)
    print greeting_msg
    return greeting_msg
    sys.exit()
##############################
if __name__ == "__main__":
    main()
