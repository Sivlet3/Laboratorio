#!/bin/sh
set -eu
TARGET_HOST="${TARGET_HOST:-laboratorio-1-y0h7.onrender.com}"
PORTS="80 443 22 3306"
echo "=== MODULO 02: COMPROBACION LIMITADA DE PUERTOS ==="
echo "Host autorizado: $TARGET_HOST"
for port in $PORTS; do
  if nc -z -w 2 "$TARGET_HOST" "$port" >/dev/null 2>&1; then
    echo "[PORT_CHECK] puerto=$port estado=ABIERTO_O_ACCESIBLE"
  else
    echo "[PORT_CHECK] puerto=$port estado=CERRADO_O_FILTRADO"
  fi
done
echo "=== COMPROBACION FINALIZADA ==="
exec python3 /app/status_server.py
