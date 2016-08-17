from flask import Flask, request
import restful
__author__ = 'DGideas'
# For Flask and Python3 only

app = Flask(__name__)

@app.route('/')
def helloWorld():
	requestHandle = restful.request()
	requestHandle.add_param("msg", "Hello, world!")
	return requestHandle.response()

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
