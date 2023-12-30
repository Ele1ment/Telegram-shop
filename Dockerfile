FROM python:3.10-slim-buster
USER root

WORKDIR /app
COPY . .

RUN python3 -m pip install -r requirements.txt

# Установка переменных окружения
ENV TELEGRAM_TOKEN=6866566554:AAHSShKT8hblHkX2tq8iD4hHgnMpCRDYvNo
ENV MAIN_ADMIN_ID=6522054669

CMD python3 installer.py --nointeract && python3 src/main.py
