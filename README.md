# Water Reminder 
 This python script simply has one and only one purpose, remind your loved
 ones to drink water and drink lots of it. 
#How to run?
Running this script is quite easy. The only challenge here is how to leave 
this process running forever on your machine. The technology we need is \
TMUX available in both Linux and Mac based machines.

###Step 1:
ssh into your Raspberry Pi (or any other device you wish to run this script in) 

### Step 2:
Run the command while in root directory
 ```
tmux
```
 you are now in the tmux enviornment  which means that even after hanging up
 on the ssh call, your process will keep on running. 
 
 
 ### Step 3:
 
 while in the tmux enviornment, run the following command:
 ```
python3 waterReminder.py&
```

you will be given a process id for the python script running in the background.


#How to end the script?
### Step 1:

run the command
```
tmux ls
```

to get a list of all ongoing tmux sessions, find the right one and put the command

```
tmux attach-session -t n
```

where n is the session number. 

###Step 2:

While in the tmux enviornment run the command
```
kill(pid)
```

where pid is the process id for our python script which you can find by the 
```
ps
```
command.