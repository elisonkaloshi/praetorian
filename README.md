# Praetorian

## Install and setup

`pip3 install -r requirements.txt`

## Run the website

`python3 praetorian.py`

## Test the protection

`Visit http://127.0.0.1:9999, you will be redirected on the welcome page`

`Visit http://127.0.0.1:9999/?username=union, your request will be denied by firewall because of the sql injection attack.`

`Visit http://127.0.0.1:9999/<script>alert(1)</script>, your request will be denied by firewall because of the xss attack.`

`Visit http://127.0.0.1:9999/?id=../../../../test, your request will be denied by firewall because of the path_traversal attack.`