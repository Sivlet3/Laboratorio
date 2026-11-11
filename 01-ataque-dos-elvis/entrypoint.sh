#!/bin/sh
set -eu
TARGET_URL="${TARGET_URL:-https://laboratorio-1-y0h7.onrender.com}"
echo "=== MODULO 01: RAFAGA HTTP CONTROLADA ==="
echo "Objetivo autorizado: $TARGET_URL"
echo "Solo 5 solicitudes secuenciales; no es un ataque DoS real."
i=1
while [ "$i" -le 5 ]; do
  RESULT=$(curl -L -sS -o /dev/null --max-time 10 -w 'HTTP %{http_code} | tiempo %{time_total}s' "$TARGET_URL/" || true)
  echo "[HTTP_SIMULATION] solicitud=$i resultado=$RESULT"
  i=$((i + 1))
done
echo "=== SIMULACION FINALIZADA ==="
exec python3 /app/status_server.py
