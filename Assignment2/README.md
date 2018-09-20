 
# Project Shell
## Introduction





## Requirements
Shell minimum criteria:

- Using your tokenizer and the system calls fork(), exec(), and wait() create a simple shell that:

- prints a command prompt which is "$ " and waits for the user to enter a command
- parse the command using your tokenizer
- create a child process that uses execve to run the command with its arguments.
- If an absolute path is not specified, your shell should instead find it using the $PATH environment variable.
- the parent process should wait for the child to terminate before printing another command prompt.
- print "command not found" if the command is not found
- if the command fails (with a non-zero exit value N), your shell should print "Program terminated with exit code N."
- empty commands should do nothing
- the "exit" command should cause your shell to terminate.


Don't forget to properly document your source code and how to play the game.
- Most of the code was provided by Dr. Froudental. However I colaborated with Elizardo Baeza on how to field dependencies worked and the os.fork() function. When coding we discuss the understading of the concept to enusure proper understading of the assignment. In addition Sergio Ponce de Leon and Elizardo Baeza and my self got together to discuss how a child process worked. 

$ 

$ 
