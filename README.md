

## Dev installation
1.Run `make` in project dir

2.Activate virtual environment and apply migrations:
```
. venv/bin/activate
cd djangoapp
./manage.py migrate
```
3.Create super user
```
./manage.py createsuperuser
```
4.run dev server:
```
./manage.py runserver
```


### Gunicorn tips
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