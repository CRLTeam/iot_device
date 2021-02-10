# Basic IoT Device

## How to use it

```bash
$ # Get the code
$ git clone git@github.com:CRLTeam/iot_device.git
$ cd iot_device
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$ 
$ # Install modules
$ # SQLIte version
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<YOUR_PORT>
$
$ # Access the web app in browser: http://DEVICE_IP_ADDRESS:YOUR_PORT/
```

