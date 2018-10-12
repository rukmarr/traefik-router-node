from flask import Flask, send_file, request, abort
app = Flask(__name__)

@app.route('/config', methods=['GET'])
def get_config():
	return send_file('/etc/traefik/routes.toml')

@app.route('/config', methods=['PUT'])
def set_config():
	cnf = open('/etc/traefik/routes.toml', 'wb')
	cnf.write(request.data)
	cnf.close()
	return 'OK', 200
