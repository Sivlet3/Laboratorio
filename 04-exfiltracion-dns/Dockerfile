FROM python:3.12-alpine
WORKDIR /app
COPY entrypoint.sh status_server.py ./
RUN chmod +x entrypoint.sh
EXPOSE 10000
CMD ["/app/entrypoint.sh"]
