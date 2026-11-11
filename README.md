# Etapa 2 - Laboratorio de Ciberseguridad

DMZ autorizada: https://laboratorio-1-y0h7.onrender.com

## Módulos incluidos
- 01: cinco solicitudes HTTP secuenciales (simulación controlada, no DoS real).
- 02: comprobación limitada de cuatro puertos del host DMZ.
- 03: enumeración de cuatro rutas.
- 04: evento DNS ficticio registrado localmente, sin enviar datos.
- 05: detección de un artefacto demostrativo inofensivo.
- 06: eventos de autenticación ficticios, sin probar cuentas reales.
- 07: proxy GET de demostración limitado al host DMZ indicado.

## Render
Para cada carpeta crea un Web Service:
- Runtime: Docker
- Root Directory: nombre de la carpeta
- Branch: main
- Región: la misma de la DMZ, si está disponible
- Plan: Free, si está disponible

Todos los servicios escuchan en 0.0.0.0 y en PORT (por defecto 10000).

Variables opcionales:
- 01 y 03: TARGET_URL=https://laboratorio-1-y0h7.onrender.com
- 02: TARGET_HOST=laboratorio-1-y0h7.onrender.com
- 07: TARGET_DMZ=https://laboratorio-1-y0h7.onrender.com

Después del despliegue, consulta /health en cada servicio.
Los registros de las simulaciones aparecen en Logs durante el arranque.
