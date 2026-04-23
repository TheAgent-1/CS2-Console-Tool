FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY /templates ./templates
COPY app.py .

# Set environment variables
ENV RCON_HOST=127.0.0.1
ENV RCON_PORT=27015
ENV RCON_PASSWORD=
ENV CS2_CONTAINER=cs2
ENV WEB_PORT=4596

# Dont bother setting user passwords, it can be done at runtime if needed

CMD python -m waitress --host=0.0.0.0 --port=$WEB_PORT app:app
