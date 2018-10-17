from flask import Flask, send_file, request, abort
app = Flask(__name__)

@app.route('/config', methods=['GET'])
def get_config():
	return send_file('routes.toml')

@app.route('/config', methods=['PUT'])
def set_config():
	cnf = open('routes.toml', 'wb')
	cnf.write(request.data)
	cnf.close()
	return 'OK', 200


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=7081)
