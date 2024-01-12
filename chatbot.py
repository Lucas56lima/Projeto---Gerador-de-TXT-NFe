import openai




openai.api_key = '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'
openai.organization = 'org-HRrNupmck6W40skTFpETBSDb'


response = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

response['choices'][0]['message']['content']