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
| URL                      | Type | Desc                                           | Example Params                                               | 
| ------------------------ | ---- | ---------------------------------------------- | ------------------------------------------------------------ | 
| /device/command          | POST | Send a command for device to execute           | { "command": "open", "length": 5}                            | 
| /device/status           | GET  | Get current device status                      |                                                              | 
| /device/settings         | GET  | Get current device settings                    |                                                              | 
| /device/settings         | POST | Set device settings                            | {"default": "close", "monitor": "passive"}                   | 
| /device/monitor          | GET  | Get log last hour                              |                                                              | 
| /device/monitor          | POST | Get log from time range                        | {"start": "2021-02-03T00:00:00.000Z", "end": "2021-02-04T00:00:0.000Z"} |
| /device/simulation       | POST | Set the simulation script                      | {"script": [{"command": "open", "length": 3, "wait": "none"}, {"command": "close", "length": 3, "wait": "rand1"}], "repeat": 20} | 
| /device/simulation/start | GET  | Start the simulation script from the beginning | | 
| /device/simulation/start | GET  | Stop the simulation script                     |                                                              |

​		
