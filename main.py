from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Helllloooo Woorrrllldd!'



@app.route('/name')
def returnName():
  return 'Lalith'

@app.route("/address")
def returnAddress():
  return '4405 Valley Avenue, Pleasanton, California'

@app.route('/query_example')
def query_example():
  language = request.args.get('language')
  framework = request.args['framework']
  website = request.args.get('website')
  return '''<h1>The language is : {}</h1>
  <h1>The framework is {} </h1> 
  <h1>The website is {}</h1>'''.format(language, framework, website)

@app.route('/json_example',methods=['POST'])
def json_example():
  req_data = request.get_json()

  language = req_data['language']
  framework = req_data['framework']
  python_version = req_data['version_info']['python']
  example = req_data['examples'][0]
  boolean_test = req_data['boolean_test']

  return '''<h1>
    The language value is {}.
    The framework value is {}.
    The python version is {}.
    The example at 0 index is {}.
    The boolean value is {}.
    </h1>'''.format(language, framework, python_version, example, boolean_test)


@app.route('/emails',methods=['POST'])
def emails():
  req_data = request.get_json()
  to = req_data['to']
  subject = req_data['subject']
  body = req_data['body']

  return '''
  The to value is {}.
  The subject value is {}.
  The body is {}.
  
  '''.format(to,subject,body)

if __name__ == "__main__":
  app.run()

