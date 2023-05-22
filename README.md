# PowerJarvis
# Description
The PowerShell Assistant: "PowerJarvis" is an AI-powered tool that allows users to interact with Windows PowerShell via natural language commands. Rather than memorizing intricate commands and syntax, users can simply tell the PowerShell Assistant what they want to do and the AI will translate that into the corresponding PowerShell command.

This project uses OpenAI's GPT-3.5-turbo model by default, which is capable of understanding complex instructions and generating accurate responses. If you have access, you can opt to use GPT-4 for improved accuracy, albeit with slower processing times.

The PowerShell Assistant encapsulates the communication with the AI model and handles executing the generated commands on PowerShell, making it ideal for both novice and experienced PowerShell users seeking an intuitive and efficient way to perform tasks.

# Features
Natural Language Processing: Understands commands given in simple, natural language.
PowerShell Command Execution: Executes translated commands directly on PowerShell.
Error Handling: Handles and reports errors during command execution.
Continuous Interaction: Provides a seamless user experience by allowing continuous command input.
How to Use
Ensure your environment is set up with OpenAI's Python library.
Clone this repository.
Run powershell_assistant.py in a PowerShell window.
Enter a command in natural language (e.g., "create a directory named dog").
The PowerShell Assistant will translate this command into a PowerShell command, display it, and then execute it.
The output (or any error) will be shown in the same PowerShell window.
To stop the assistant, simply type exit.
# Examples
User Input: "create a directory named dog"
AI Output: 
```powershell
New-Item -ItemType Directory -Force -Path dog
```

User Input: "open firefox"
AI Output: 
```powershell
Start-Process firefox
```

User Input: "create a .txt file with a summary of Independence Day"
AI Output:

```powershell
@"
Independence Day is annually celebrated on July 4 and is often known as 'the Fourth of July'. It is the anniversary of the publication of the declaration of independence from Great Britain in 1776.
"@ | Out-File -FilePath 'summary_of_independence_day.txt'
```
# License
This project is licensed under the terms of the MIT license.

# Disclaimer
This tool should be used responsibly. It is not recommended to use this tool for commands that can alter system files or perform administrative tasks without proper understanding of the underlying operations. Always review the generated PowerShell command before execution. The creators of this tool will not be responsible for any misuse or any damage caused.
