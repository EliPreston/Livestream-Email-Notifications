# NOT COMPLETE
- Need to add instructions for using smtp with outlook
- Need to add instructions for getting a twitch client/secret
- Need to indicate you need an .env file


# Personalized Twitch Stream Notifcation by Email
I built this becuase I didn't want to download twitch on my phone (running low on storage) and I was setting up a home server on an old laptop, so I thought "why not run a script that sends me emails when certain streamers are live in a docker container".



## Setting up Virtual Environment to Run Program

### In the directory of your choice create a virtual enviornment: `python3 -m venv .venv` on Linux/Mac (Unix based) or `py -m venv .venv` on Windows where the second argument is the location of the venv folder
#### For example on a Linux or Mac computer:
>$ cd ~/Programming/twitch-live-notifications \
>\$ python3 -m venv .venv


### To activate and enter the virtual environment that was just created: `source path-to-venv-folder/bin/activate` on Linux/Mac or `.venv\Scripts\activate` on Windows
#### Continuing the example on Linux/Mac:
> \$ source .venv/bin/activate \
>(twitch-live-notifications)$

- You should now see the name of the folder containing the .venv folder in brackets at the start of your terminal prompt


### Then finally you can install the required packages with pip inside the active virtual environment:
#### Continuing the example on Linux/Mac:
> (twitch-live-notifications)$ pip3 install requests python-dotenv

### Now to run the script:
> (twitch-live-notifications)$ python3 src/main.py

### And finally you can press `ctrl-c` to stop the script followed by typing `deactivate` (Linux/Mac and Windows) in the terminal prompt to exit the virtual environment
#### Ex:
> script runnning... \
> ... \
> ... \
> ^C \
> (twitch-live-notifications)$ deactivate \
> \$


#### For myself, I have a folder where I keep virtual environments separate from the actual project folder, and do each of the above steps for activating, running the script, and exiting the venv (after ctrl-c) in one line: 
`source ~/Programming/.venv/check-livestream/bin/activate && python3 src/main.py && deactivate`
