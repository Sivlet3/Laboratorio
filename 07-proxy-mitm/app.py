import os
from urllib.parse import urlparse
from flask import Flask, request, Response, jsonify
import requests

app = Flask(__name__)
TARGET_DMZ = os.getenv("TARGET_DMZ", "https://laboratorio-1-y0h7.onrender.com").rstrip("/")
ALLOWED_HOST = "laboratorio-1-y0h7.onrender.com"

@app.get("/health")
def health():
    return jsonify(status="ok", module="07-proxy-mitm", target=TARGET_DMZ)

@app.route("/", defaults={"path": ""}, methods=["GET"])
@app.route("/<path:path>", methods=["GET"])
def proxy(path):
    if urlparse(TARGET_DMZ).hostname != ALLOWED_HOST:
        return jsonify(error="TARGET_DMZ no coincide con el host autorizado"), 403

    url = f"{TARGET_DMZ}/{path}"
    print(f"[MITM_DEMO] solicitud GET interceptada ruta=/{path}", flush=True)
    try:
        upstream = requests.get(
            url,
            headers={"User-Agent": "Laboratorio-MITM-Demo/1.0", "Accept": "text/html"},
            timeout=15
        )
        content = upstream.text
        if "text/html" in upstream.headers.get("Content-Type", ""):
            content += "\n<!-- [MITM DEMO] Respuesta modificada en laboratorio controlado. -->"
        print(f"[MITM_DEMO] respuesta_origen={upstream.status_code} contenido_modificado=SI", flush=True)
        return Response(content, status=upstream.status_code,
                        content_type=upstream.headers.get("Content-Type", "text/plain"))
    except requests.RequestException as exc:
        print(f"[MITM_ERROR] {type(exc).__name__}", flush=True)
        return jsonify(error="No fue posible consultar la DMZ",
                       detail=type(exc).__name__), 502

if __name__ == "__main__":
    port = int(os.getenv("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
