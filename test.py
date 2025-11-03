import openai
from dotenv import dotenv_values
config = dotenv_values('.env')
answer = ()
openai.api_key = config['API_KEY']
def generate_blog(paragraph_topic):
    response = openai.completions.create(
        model = 'gpt-3.5-turbo-instruct', 
        prompt= 'tell me more about' + paragraph_topic, 
        max_tokens = 400, 
        temperature = 0.5, 
    )
    retrieve_blog = response.choices[0].text
    return retrieve_blog
print(generate_blog('test'))
keep_writing = True
while keep_writing:
    answer = str(input('Would you like me to write another paragraph?, Y for yes anything else for no'))
    if answer == 'Y':
        paragraph_topic1 = str(input('What would you like me to talk about?'))
        print(generate_blog(paragraph_topic1))
    else:
     keep_writing = False