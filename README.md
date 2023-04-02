# ChatGPT Homework Generator

This Python script generates homework assignments based on a given LaTeX template and topic using OpenAI's ChatGPT API. The script reads the LaTeX template, sends it along with the topic to ChatGPT, and writes the generated content to a new LaTeX file.

## Prerequisites

- Python 3.6 or later
- OpenAI Python API client library
- LaTeX distribution (e.g., TeX Live)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Vasissualiyp/GPTAssignment.git
cd GPTAssignment
```


2. (Optional) If you haven't already, you can sign up for a free OpenAI API key at https://beta.openai.com/signup/.

3. Make sure to replace `your_openai_api_key_here` with your actual OpenAI API key in the `setup.sh` file.

4. Run the setup script to install the required dependencies and set up environment variables:

```bash
chmod +x setup.sh
./setup.sh
```

## Usage

To generate a homework assignment based on a given topic and LaTeX template, run the following command:

```bash
python generate_homework.py 'Topic' 'path_to_your_template.tex'
```

Replace `'Topic'` with your desired topic (e.g., `'Kinematics of translational motion'`) and `'path_to_your_template.tex'` with the path to your LaTeX template file.

Example:

```bash
python generate_homework.py 'Kinematics of translational motion' 'template.tex'
```

This will generate a new `.tex` file with the generated content. To compile the generated LaTeX file into a PDF, use `pdflatex`:

```bash
pdflatex homework_Kinematics_of_translational_motion.tex
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](https://choosealicense.com/licenses/mit/)

This README provides an overview of the project, prerequisites, installation instructions, usage information, and contributing guidelines. You can customize it according to your needs and preferences.
