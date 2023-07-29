import openai

# Set up your OpenAI API credentials
openai.api_key = ''

def chat_with_gpt3(prompt):
	    response = openai.Completion.create(
	        engine='',
	        prompt=prompt,
	        max_tokens=50,
	        temperature=0.7,
	        n=1,
	        stop=None
	    )
	    return response.choices[0].text.strip()
	# Main program loop
	while True:
	    user_input = input("User: ")
	    if user_input.lower() == 'exit':
.	        break
	    # Add your prompt or conversation history with the AI here
	    # For example, you can start with a simple greeting
	    conversation_history = "You: Hello, how are you?"

	    # Extend the conversation history with the user's input
	    conversation_history += "\nUser: " + user_input

	    conversation_history += "\nUser: " + user_input
	    response = chat_with_gpt3(conversation_history)

	    # Extract and print the AI's response
	    print("AI: " + response)