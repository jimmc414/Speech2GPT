ChatGPT Voice Assistant
This is a simple voice assistant script that uses OpenAI's GPT-4 to generate text responses based on user input. It listens to the user's speech, converts it to text using the Google Speech Recognition API, and generates a response using OpenAI's GPT-4. The response is then spoken back to the user using a text-to-speech engine.
It uses davinci-002 and 1000 token limit but these both can be changed according to OpenAI documentation
Requirements
Python 3.6 or higher
An OpenAI API key
Installation
Clone the repository:
bash
```
git clone https://github.com/yourusername/ChatGPT-Voice-Assistant.git
```
Change the working directory:
bash
```
cd ChatGPT-Voice-Assistant
```
Install the required packages:
bash
```
pip install -r requirements.txt
```
Usage
Set the OPENAI_API_KEY environment variable with your OpenAI API key:
For Windows:

bash
```
setx OPENAI_API_KEY=your_api_key
```
For Linux/macOS:

bash
```
export OPENAI_API_KEY=your_api_key
```
Run the script:
bash
```
python chatgpt_voice_assistant.py
```
The voice assistant will start listening for your input and respond using text-to-speech.

Additional Files
requirements.txt: A list of required Python packages to be installed.
.gitignore: A file specifying files and directories that should not be tracked by Git.
Troubleshooting
If you encounter any issues, please ensure that you have set the OPENAI_API_KEY environment variable correctly and have installed all required packages. If the problem persists, please open an issue on the repository's GitHub page.

License
This project is released under the MIT License."# Speech2GPT" 
