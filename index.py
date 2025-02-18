import ollama

def generate_story_with_llama(girl_name, boy_name, romance_level):
    prompt = f"Create a {romance_level} romantic story where the main characters are {girl_name} and {boy_name}. The story should focus on their intense attraction, chemistry, and growing desire. It should include moments of deep connection, longing gazes, and the electric tension between them during their first meeting."
    response = ollama.chat(model="llama3.2:1b", messages=[{"role": "user", "content": prompt}])
    story = response.get('message', {}).get('content', 'No content available')
    return story

girl_name = input("Enter the girl's name: ")
boy_name = input("Enter the boy's name: ")
romance_level = input("Enter the romance level (Low, Medium, High): ")

story = generate_story_with_llama(girl_name, boy_name, romance_level)
print("\nHere is your generated story:\n")
print(story)