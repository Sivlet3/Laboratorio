FROM python:3.12-alpine
WORKDIR /app
RUN printf 'dependency=demo-package\nversion=1.0-demo\n' > /app/dependency_manifest.txt \
 && printf '#!/bin/sh\necho "[PAYLOAD_SIMULADO] Artefacto de demostracion detectado; sin acciones adicionales."\n' > /app/demo_dependency_notice.sh \
 && chmod +x /app/demo_dependency_notice.sh
COPY entrypoint.sh status_server.py ./
RUN chmod +x entrypoint.sh
EXPOSE 10000
CMD ["/app/entrypoint.sh"]
