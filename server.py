"""
server.py
=========
Servidor local ligero para ejecutar la aplicación del Generador Dimensional.
Abre automáticamente el navegador en http://localhost:8000.
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/index.html"
        print(f"============================================================")
        print(f"  GENERADOR DE ANÁLISIS DIMENSIONAL CONFORMADO")
        print(f"  Servidor activo en: {url}")
        print(f"  Presiona Ctrl+C en esta terminal para detener.")
        print(f"============================================================")
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor detenido.")
            sys.exit(0)

if __name__ == "__main__":
    run()
