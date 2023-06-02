from flask import Flask, request, send_file, abort, jsonify
from gpt4allj import Model
import sys

#model = Model("/mnt/models/gpt4all-ui/models/gpt_4all/ggml-gpt4all-j-v1.3-groovy.bin")
model = Model("models/gpt_4all/ggml-gpt4all-j-v1.3-groovy.bin")

if __name__ == "__main__":
  
  app = Flask(__name__)
  
  @app.route('/',methods=['POST'])
  def get_prompt(): 
    content = request.json
    result = model.generate(content['prompt'])
    print(result)
    return jsonify({'reply': result})

    
  cli = sys.modules['flask.cli']
  cli.show_server_banner = lambda *x: None
  app.run(host="0.0.0.0", port=5004)
