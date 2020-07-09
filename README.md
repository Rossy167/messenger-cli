## messenger-cli
Terminal application to use Facebook Messenger the command line! Pretend you're working when really you're shitposting!

### Usage
Honestly, there's no valid reason to use this, I thought it would just be a fun project. There is an image that kind of describes the flow of the program: effectively you login, then it queries FB for all your latest chats, then you can read the threads and send messages to them. The closest thing I have to a reason is that I hate using Facebook and yet all my friends insist on it being our main form of communication... but it's not like I'm going to switch to a terminal application for that. So... this exists

### Setup
You will need to generate a venv, some setup scripts are provided to get this going.

Mac/Linux:
* cd into root directory for (should be messenger-cli or messenger-cli-master)
* run `bash setup/setup.sh (chmod to x if on Linux)`

Windows:
* Use Powershell, I have no intention of making this work for cmd.exe
* cd into root directory for (should be messenger-cli or messenger-cli-master) 
* run `.\setup\setup.ps1`

You may delete setup folder, though I would recommend the python package works first (this is why I don't delete it programmatically). You can, of course, create and manage own venv you will at the bare minimum need `fbchat switchcase`.  

### Using
Mac/Linux: cd into root directory and run `bash start.sh`

Windows: using Powershell, cd into root directory and run `.\start.ps1`

You can also manually run the script, activate the venv at messenger-cli/messenger_environment/ and then run python messenger-cli from root. It's just like... why not use mine right?

### Resources Used
* https://fbchat.readthedocs.io/en/stable/
