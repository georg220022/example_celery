"""  nginx:
    container_name: nginx
    image: nginx:latest
    restart: always
    ports:
      - "8000:8000"
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - web"""