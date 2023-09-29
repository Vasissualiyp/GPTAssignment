import os
import openai
import sys
from datetime import datetime

# Initialize the OpenAI API client (as you did before, not included here)
#openai.api_key = "type your api key here (not secure)"
openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "gpt-4"

def generate_homework(folder):
    # Get the current date in the format YYYY-MM-DD
    current_date = datetime.now().strftime("%Y-%m-%d")
    number_of_questions_per_section = 5

    # Read the topic from a file in the $folder/Topics/ directory
    topics_path = os.path.join(folder, "Topics", f"{current_date}.txt")
    try:
        with open(topics_path, 'r') as topic_file:
            topic = topic_file.read().strip()
    except FileNotFoundError:
        print(f"Topic file {topics_path} not found.")
        return

    # Read the LaTeX template
    template_path = os.path.join(folder, "Templates", "homework_template.tex")
    try:
        with open(template_path, 'r') as template_file:
            latex_template = template_file.read()
    except FileNotFoundError:
        print(f"Template file {template_path} not found.")
        return

    # Generate content for the homework (Assuming you have initialized openai before this)
    prompt = [{"role": "user", "content": f"Create a homework assignment about {topic} with {number_of_questions_per_section} problems per section, using the following LaTeX template:\n{latex_template}\n\n---\n\n"}]
    response = openai.ChatCompletion.create(
        model=model_engine,
        max_tokens=6000,
        temperature=1.2,
        messages=prompt
    )

    try:
        generated_content = response['choices'][0]['message']['content'].strip()
    except KeyError as e:
        print(f"KeyError: {e}")
        print("Could not find the required key in the response.")
        return

    # Save generated homework content as a new LaTeX document
    output_path = os.path.join(folder, "Homework_tex", f"{current_date}.tex")
    with open(output_path, 'w') as homework_file:
        homework_file.write(generated_content)

    return output_path

if __name__ == "__main__":
    folder = "/home/vasilii/Documents/Tutoring/Olexandr/Fall 2023/"
    generated_file = generate_homework(folder)
    print(f"Generated homework file: {generated_file}")
