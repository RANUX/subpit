## About SubPit 
Simple Django REST API app to collect information about subscribers like emails or phones on your server.


## Dev installation
1.Run `make venv` in project dir

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

## Run example project
First run djangoapp `./manage.py runserver` and then go to example and run `./manage.py runserver 8080`
Open page `http://localhost:8080` and try to send data

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