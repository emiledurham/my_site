server {
    listen 80;
    server_name 167.172.136.115;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/emiledurham/my_site;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}