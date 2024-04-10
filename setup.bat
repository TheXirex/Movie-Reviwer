docker-compose up -d
timeout /t 3
start "" "http://127.0.0.1:7700/"
start "" "http://127.0.0.1:7070/"