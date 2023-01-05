

RHOST=8.8.8.8  
IP=$(ip route get $RHOST | awk '{ print $7; exit }')
export FLASK_APP=app
export FLASK_DEBUG=1
export FLASK_RUN_PORT=8000
flask run --host=$IP
$SHELL