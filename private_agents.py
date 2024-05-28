import ollama
import sys
with open('hello.txt','r') as file:
    data=file.read()
print()

if data:
    print("data loaded successfully")
else:
    print('unable to read file.')
    sys.exit(1)

prompt1=f"from the provided data below. tell me three intresting facts about AGI. <data> {data} </data>."
print('prompt loaded')
print('generating response...')



response1=ollama.chat(model="llama2",messages=[{
    'role':'user',
    'content':prompt1
}])

resp=response1['message']['content']

prompt2=f"""<response> {resp} </response> \n\n\n explain the above response to the user in a funny manner."""

response2=ollama.chat(model="llama2",messages=[{
    'role':'user',
    'content':prompt2
}])

print(response2['message']['content'])