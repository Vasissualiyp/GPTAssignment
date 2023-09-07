import openai
import os
import sys

# Initialize the OpenAI API client
openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "gpt-4"
homework_no = 42
number_of_questions_per_section = 5

def generate_homework(topic, template_path):
    with open(template_path, 'r') as template_file:
        latex_template = template_file.read()

    # Generate content for the homework using ChatGPT

    prompt=[{"role": "user", "content": f"Create a homework assignment about {topic} with {number_of_questions_per_section} problems per section, using the following LaTeX template:\n{latex_template}\n\n---\n\n"}]

    response = openai.ChatCompletion.create(
        model=model_engine,
        max_tokens=6000,
        temperature=1.2,
        messages = prompt
    )
    #print(response.__dict__)

    # Accessing the generated content from the correct attribute
    try:
        generated_content = response['choices'][0]['message']['content'].strip()
    except KeyError as e:
        print(f"KeyError: {e}")
        print("Could not find the required key in the response.")
    
    # Save generated homework content as a new LaTeX document
    with open(f'homework_{homework_no}.tex', 'w') as homework_file:
        homework_file.write(generated_content)

    return f'homework_{homework_no}.tex'




if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_homework.py 'Topic' 'template_path.tex'")
    else:
        topic = sys.argv[1]
        template_path = sys.argv[2]
        generated_file = generate_homework(topic, template_path)
        print(f"Generated homework file: {generated_file}")

