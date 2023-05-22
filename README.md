# PowerJarvis
# Description
The PowerShell Assistant: "PowerJarvis" is an AI-powered tool that allows users to interact with Windows PowerShell via natural language commands. Rather than memorizing intricate commands and syntax, users can simply tell the PowerShell Assistant what they want to do and the AI will translate that into the corresponding PowerShell command.

This project uses OpenAI's GPT-3.5-turbo model by default, which is capable of understanding complex instructions and generating accurate responses. If you have access, you can opt to use GPT-4 for improved accuracy, albeit with slower processing times.

The PowerShell Assistant encapsulates the communication with the AI model and handles executing the generated commands on PowerShell, making it ideal for both novice and experienced PowerShell users seeking an intuitive and efficient way to perform tasks.

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

User Input: "create content for summary for independence day and write it to a file called summary_of_independence_day.txt on my desktop then open it"
AI Output:

```powershell
@"
New-Item -ItemType Directory -Force $Env:USERPROFILE\Desktop\summary
Set-Content -Path $Env:USERPROFILE\Desktop\summary\summary_of_independence_day.txt -Value "On July 4, 1776, the thirteen colonies claimed their independence from England, an event which eventually led to the 
formation of the United States."
Start-Process $Env:USERPROFILE\Desktop\summary\summary_of_independence_day.txt
"@
```
# License
This project is licensed under the terms of the MIT license.

# Disclaimer
This tool should be used responsibly. It is not recommended to use this tool for commands that can alter system files or perform administrative tasks without proper understanding of the underlying operations. Always review the generated PowerShell command before execution. The creators of this tool will not be responsible for any misuse or any damage caused.
