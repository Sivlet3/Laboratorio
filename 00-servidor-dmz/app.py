
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import os
import json
from datetime import datetime, timezone

ESTUDIANTE = os.getenv(
    "ESTUDIANTE_NOMBRE",
    "Elvis"
)

PORT = int(os.getenv("PORT", "10000"))


class DMZHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        evento = {
            "fecha": datetime.now(timezone.utc).isoformat(),
            "tipo": "HTTP_REQUEST",
            "metodo": "GET",
            "ruta": self.path,
            "ip": self.client_address[0]
        }

        print(json.dumps(evento, ensure_ascii=False), flush=True)

        if self.path in ["/", "/index.html"]:
            codigo = 200

            contenido = f"""
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <title>Servidor DMZ</title>
                <style>
                    body {{
                        font-family: Arial;
                        background: #eef2f7;
                        margin: 40px;
                    }}
                    .container {{
                        background: white;
                        padding: 30px;
                        border-radius: 12px;
                    }}
                    h1 {{ color: #263c58; }}
                    .status {{ color: green; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Servidor DMZ Activo</h1>
                    <h2>Laboratorio de {ESTUDIANTE}</h2>
                    <p class="status">Estado: ONLINE</p>
                    <p>Servidor desplegado correctamente en Render.</p>
                    <p>Infraestructura de laboratorio de ciberseguridad.</p>
                </div>
            </body>
            </html>
            """

        else:
            codigo = 404
            contenido = "<h1>404 - Ruta no encontrada</h1>"

        self.send_response(codigo)
        self.send_header(
            "Content-Type",
            "text/html; charset=utf-8"
        )
        self.end_headers()

        self.wfile.write(contenido.encode("utf-8"))

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":

    servidor = ThreadingHTTPServer(
        ("0.0.0.0", PORT),
        DMZHandler
    )

    print(
        f"Servidor DMZ activo en el puerto {PORT}",
        flush=True
    )

    servidor.serve_forever()
