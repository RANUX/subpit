


Gunicorn setting file
```
vim /etc/systemd/system/yourservice-gunicorn.service
```
After editings run:
```
systemctl daemon-reload
systemctl restart yourservice-gunicorn.service

# if errors see journal
journalctl -u yourservice-gunicorn
```