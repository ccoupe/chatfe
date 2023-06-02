'''
# Mac mini - 
from gpt4all import GPT4All
gptj = GPT4All(model_path="/Volumes/SSD/GPT4All", 
		model_name="ggml-gpt4all-j.bin",
		model_type='gptj')
messages = [{"role": "user", "content": "I will call you GLaDOS"}]

result = gptj.chat_completion(messages)
print(type(result))
print(result)
'''
from gpt4allj import Model

model = Model("/mnt/models/gpt4all-ui/models/gpt_4all/ggml-gpt4all-j-v1.3-groovy.bin")

result = model.generate('Tell me about CO2 lasers')
print(type(result))
print(result)
