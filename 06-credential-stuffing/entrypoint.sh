#!/bin/sh
set -eu
USUARIOS="admin usuario_demo docente_demo"
echo "=== MODULO 06: SIMULACION DE CREDENCIALES FICTICIAS ==="
echo "No se realizan inicios de sesion ni se prueban cuentas reales."
for user in $USUARIOS; do
  echo "[AUTH_SIMULATION] usuario=$user clave=[REDACTADA_DEMO] resultado=RECHAZADO_SIMULADO"
done
echo "=== SIMULACION FINALIZADA ==="
exec python3 /app/status_server.py
