import ollama

response=ollama.chat(model="llama2",messages=[{
    'role':'user',
    'content':'what is AGI in 50 words',
}],)

print(response['message']['content'])