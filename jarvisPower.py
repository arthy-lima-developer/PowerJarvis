import openai
import subprocess
import os

class PowershellAssistant:
    """A class representing an assistant that translates natural language into PowerShell commands."""
    
    OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'  # Set your OpenAI API key here

    def __init__(self):
        openai.api_key = self.OPENAI_API_KEY

    def get_command_from_gpt(self, input):
        """Generates a PowerShell command using GPT-3."""
        path = os.path.abspath(__file__)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", #The model is set to GPT-3.5-turbo by default for its balance between speed and accuracy. If you have access to GPT-4 and prefer more accurate results over speed, feel free to switch, but be aware that it will increase processing time and costs.
            messages=[
                {
                    "role": "system", 
                      "content": "You are a PowerShell assistant that translates natural language commands into Windows PowerShell commands without providing any additional explanations or instructions. For instance, if the user says 'create a directory named dog', you should respond with 'New-Item -ItemType Directory -Force -Path dog'. If the user says 'open firefox', you should respond with 'Start-Process firefox'.Ensure you do not provide any additional explanations or instructions. If the user asks for a multi-step command, do not explain it in natural language. Instead, provide the command that will carry out the steps, such as opening a folder and creating a notepad.Your output needs to be compatible with PowerShell. Also, remember to reference the paths of the files and folders correctly. For instance, if a user says 'create a folder named dog and inside the folder, create an index.html', then asks to open it with Chrome, you should reference the paths of the files and folders correctly.Bear in mind the directory from which the user is running these commands. Don't use bullet points or explanations, and ensure that all the code can be run in PowerShell. Only display the PowerShell instruction.If the user asks you to create some kind of document or code, you can use your knowledge to fulfill this task, but your answer must always be a PowerShell command. For instance, if a user asks to create a .txt file with a summary of Independence Day, you can use your knowledge to create such a .txt file and then respond with the corresponding PowerShell command.Remember, in PowerShell, the '@"' and '"@' delimiters of a Here-String must be at the beginning of the line with no leading or trailing whitespace. Start with ```powershell and end with ```."
            },
                {"role": "user", "content": f"Context where command is running:{path} Command:{input}"}
            ]
        )
        return response['choices'][0]['message']['content']

    @staticmethod
    def execute_command(command):
        """Executes a given PowerShell command."""
        try:
            process = subprocess.Popen(["powershell", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()

            if error:
                print(f"Error: {error.decode('utf-8', 'ignore')}")
            else:
                print(output.decode('utf-8', 'ignore'))
        except Exception as e:
            print(f"An error occurred while executing the command: {str(e)}")

    @staticmethod
    def get_command_powershell(command):
        """Extracts the PowerShell command from the input string."""
        if '```powershell' in command:
            command = command.split('```powershell')[1]
            command = command.split('```')[0]
        elif '```' in command:
            command = command.split('```')[1]
            command = command.split('```')[0]
        return command

def main():
    assistant = PowershellAssistant()

    while True:
        try:
            user_input = input("Enter your command: ")
            if user_input.lower() == "exit":
                break

            ai_command = assistant.get_command_powershell(assistant.get_command_from_gpt(user_input))
            print(f"AI Command: {ai_command}")

            assistant.execute_command(ai_command)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
