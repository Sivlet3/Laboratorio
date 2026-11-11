#!/bin/sh
set -eu
TARGET_URL="${TARGET_URL:-https://laboratorio-1-y0h7.onrender.com}"
RUTAS="/ /admin /login /backup.zip"
echo "=== MODULO 03: ENUMERACION LIMITADA DE RUTAS ==="
for ruta in $RUTAS; do
  CODE=$(curl -L -sS -o /dev/null --max-time 10 -w "%{http_code}" "$TARGET_URL$ruta" || echo "ERROR")
  echo "[ROUTE_AUDIT] ruta=$ruta codigo_http=$CODE"
done
echo "=== ENUMERACION FINALIZADA ==="
exec python3 /app/status_server.py
