#!/bin/sh
set -eu
FAKE_DATA="dato_demo_sin_valor"
ENCODED=$(printf "%s" "$FAKE_DATA" | base64 | tr -d '=\n')
DEMO_DOMAIN="${DEMO_DOMAIN:-example.invalid}"
echo "=== MODULO 04: SIMULACION DE EVENTO DNS ==="
echo "[DNS_SIMULATION] dato_ficticio=$FAKE_DATA"
echo "[DNS_SIMULATION] etiqueta_codificada=$ENCODED"
echo "[DNS_SIMULATION] nombre_de_consulta=${ENCODED}.${DEMO_DOMAIN}"
echo "[DNS_SIMULATION] consulta no enviada; evidencia registrada localmente."
echo "=== SIMULACION DNS FINALIZADA ==="
exec python3 /app/status_server.py
