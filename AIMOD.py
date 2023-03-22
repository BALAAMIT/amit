import os
import openai

API_KEY='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'
openai.api_key = API_KEY
model= "code-davinci-003"
promot= 'how big is the moon'
response = openai.Completion.acreate(
    promot= 'how big is the moon',
    model=model,
    max_tokens =1000,
    temperature=0.9,
    n=3,
    stop=

)
print(response.usage.total_tokans)