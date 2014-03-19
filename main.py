#!/usr/bin/python

import os, sys
import BaseHTTPServer
import serial 
import time

try:
    from serial.tools.list_ports import comports
except ImportError:
    print "comports not present, check serial library"
    comports = None


PORT = 8000     


class myHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """
        Clase heredada de BaseHTTPRequestHandler, para gestionar las acciones en cada request.
    """



    def do_GET(self):
        print "Acaba de entrar una peticion"
        #envia un codigo 200 como respuesta http, es decir OK
        self.send_response(200)

        #envia los headers de respuesta 
        self.protocol_version='HTTP/1.1'
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # envia el html en el body de la respuesta
        #TODO servir un archivo del directorio raiz o custom dir
        self.wfile.write(bytes("<html> <head><title> Kill Me </title> </head> <body> <h1> Hola Mundo </h1><body></html>"))


        #Abre puerto serial, espera 3 secs, escribe la data y cierra puerto
        #TODO implementar callbacks y threading
        micro = serial.Serial("/dev/tty.usbmodem621", 115200)
        time.sleep(2)
        micro.write('a')
        micro.close()


if __name__ == '__main__':

    httpd_class = BaseHTTPServer.HTTPServer 
    httpd = httpd_class(("192.168.1.29", 8000), myHandler)

    # gestion de escepciones y errores con try - except
    try:
        print "Starting Server"
        httpd.serve_forever()

    except KeyboardInterrupt:
        print "Stoping Server"
        httpd.server_close()
