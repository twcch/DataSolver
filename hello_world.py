import os
import requests

response = requests.post("https://api.openai.com/v1/chat/completions",
                         headers={"Content-Type": "application/json",
                                  "Authorization": "Bearer " + os.getenv("OPENAI_API_KEY")},
                         json={"model": "gpt-4o-mini",
                               "messages": [
                                   {"role": "system", "content": "你是我的翻譯助手，幫我翻譯成英文"},
                                   {"role": "user", "content": "台灣有幾個縣市"}
                               ]})

data = response.json()
content = data["choices"][0]["message"]["content"]
print(content)
