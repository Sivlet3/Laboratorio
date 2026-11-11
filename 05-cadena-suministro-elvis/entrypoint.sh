#!/bin/sh
set -eu
echo "=== MODULO 05: INTEGRIDAD DE CADENA DE SUMINISTRO ==="
if [ -f /app/dependency_manifest.txt ]; then
  echo "[SUPPLY_CHAIN] manifiesto_presente=SI"
  sha256sum /app/dependency_manifest.txt
else
  echo "[SUPPLY_CHAIN] manifiesto_presente=NO"
fi
if [ -f /app/demo_dependency_notice.sh ]; then
  echo "[ALERTA_CONTROLADA] artefacto de demostracion detectado."
  sh /app/demo_dependency_notice.sh
else
  echo "[OK] No se encontro el artefacto de demostracion."
fi
echo "=== REVISION FINALIZADA ==="
exec python3 /app/status_server.py
