import openai
import os
import sys

# Initialize the OpenAI API client
openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "gpt-3.5-turbo"

def generate_homework(topic, template_path):
    with open(template_path, 'r') as template_file:
        latex_template = template_file.read()

    # Generate content for the homework using ChatGPT
    response = openai.Completion.create(
        model=model_engine,
        prompt=f"Create a homework assignment about {topic} using the following LaTeX template:\n{latex_template}\n\n---\n\n",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )

    generated_content = response.choices[0].text.strip()

    # Save generated homework content as a new LaTeX document
    with open(f'homework_{topic.replace(" ", "_")}.tex', 'w') as homework_file:
        homework_file.write(generated_content)

    return f'homework_{topic.replace(" ", "_")}.tex'


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_homework.py 'Topic' 'template_path.tex'")
    else:
        topic = sys.argv[1]
        template_path = sys.argv[2]
        generated_file = generate_homework(topic, template_path)
        print(f"Generated homework file: {generated_file}")
