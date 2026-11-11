from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json, os
from datetime import datetime, timezone

MODULE = os.getenv("MODULE_NAME", "Modulo de laboratorio")
PORT = int(os.getenv("PORT", "10000"))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event": "MODULE_HEALTH_REQUEST",
            "module": MODULE,
            "path": self.path,
            "method": "GET"
        }
        print(json.dumps(event, ensure_ascii=False), flush=True)
        if self.path == "/health":
            status, content_type = 200, "application/json; charset=utf-8"
            payload = json.dumps({"status": "ok", "module": MODULE})
        else:
            status, content_type = 200, "text/html; charset=utf-8"
            payload = f"<h1>{MODULE}</h1><p>Servicio activo en Render.</p><p>Consulta /health para verificar el estado.</p>"
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(payload.encode("utf-8"))

    def log_message(self, fmt, *args):
        pass

server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
print(f"[STARTUP] {MODULE} escuchando en 0.0.0.0:{PORT}", flush=True)
server.serve_forever()
