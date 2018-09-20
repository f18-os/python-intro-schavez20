#! /usr/bin/env python3
import os, sys, time, re
reply = " "
pid = os.getpid()
#dir_path = os.path.dirname(os.path.realpath(_file_))
def catWriter(args):
    os.write(1, ("Child: My pid==%d.  Parent's pid=%d\n" % 
                 (os.getpid(), pid)).encode())
    getIndex = args.index(">")
    del arg[getIndex]

    os.close(1)                 # redirect child's stdout
    sys.stdout = open(args[1], "w")
    fd = sys.stdout.fileno() # os.open("p4-output.txt", os.O_CREAT)
    os.set_inheritable(fd, True)
    os.write(2, ("Child: opened fd=%d for writing\n" % fd).encode())

    for dir in re.split(":", os.environ['PATH']): # try each directory in path
        program = "%s/%s" % (dir, args[0])
        try:
            os.execve(program, args, os.environ) # try to exec program
        except FileNotFoundError:             # ...expected-  
            pass                              # ...fail quietly 

    os.write(2, ("Child:    Error: Could not exec %s\n" % args[0]).encode())
    sys.exit(1)                 # terminate with error

def infoCat(args):
    fd = sys.stdout.fileno() 

    for dir in re.split(":", os.environ['PATH']): # try each directory in path
        program = "%s/%s" % (dir, args[0])
        try:
            os.execve(program, args, os.environ) # try to exec program
            os.write(2, ("Child: opened fd=%d for reading\n" % fd).encode())
            sys.stdout = open(args[1], "r")
            os.set_inheritable(1, True)
        except FileNotFoundError:             # ...expected
            pass                              # ...fail quietly 

    os.write(2, ("Child:    Error: Could not exec %s\n" % args[0]).encode())
    sys.exit(1)                 # terminate with error

def help():
	print(" ~$ ls to show directory files \n echo : output")
# need a global empty list for the reply
intake = list() # initial empty list
def my(args):
        for dir in re.split(":", os.environ['PATH']): # try each directory in path
            program = "%s/%s" % (dir, args[0])
            try:
                os.execve(program, args, os.environ) # try to exec program
            except FileNotFoundError:             # ...expected
                pass                              # ...fail quietly 
        sys.exit(1) 

while (reply != "quit"):
    reply = input("\nshell~$ ")
    rc = os.fork()
    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)

    elif rc == 0:                   # child
       # os.write(1, ("Child: My pid==%d.  Parent's pid=%d\n" % 
                # (os.getpid(), pid)).encode())
        # Taking p4 to modify and create the shell
        #args = ["wc", "p3-exec.py"] # hard coded taking values to make it dynamic
        args = reply.split(" ") #parse the command using your tokenizer
        intake = args
        #now we print to see what is going on
       # print(args)
        if len(args) > 2 and ">" in args:
            #print(" prob have a less than value") # checking if there is a more than just 2 thing such as: cat > filename.txt
            theIndex = intake.index(">")
            arguments = [intake[theIndex-1], intake[theIndex+1]]
            print(arguments)
            os.close(1)
         
           
           
            sys.stdout = open(intake[theIndex+1], "w")
            
            fd = sys.stdout.fileno()
            #del arguments[theIndex]
           
            print(arguments)
            os.set_inheritable(fd, True)
            os.write(2, ("Child: opened fd=%d for writing\n" % fd).encode())
            
            for dir in re.split(":", os.environ['PATH']): # try each directory in path
                program = "%s/%s" % (dir, arguments[0])
                try:
                    os.execve(program, arguments, os.environ) # try to exec program
                                       
                    
                except FileNotFoundError:             # ...expected
                    pass                              # ...fail quietly 

            os.write(2, ("Child:    Error: Could not exec %s\n" % arguments[0]).encode())
            sys.exit(1)                 # terminate with error    
        
        elif len(args)==1 and "ls" in args:
            arr = os.listdir()
            for i in arr:
                print(i, end= " ")
                
            sys.exit(1)
       
        elif len(args)==1 and "help" in args:
        	help()
        	sys.exit(1)
        elif len(args)==2 and "cat" in args:
            infoCat(args)
        elif len(args) == 2 and "rm" in args:
            os.remove(args[1])
            sys.exit(1)
        elif "echo" in args[0] and len(args)>1:
            item = args[1:]
            for i in item:
                print(i, end=" ")
            sys.exit(1)
        elif args== " ":
            sys.exit(1)
       
        elif reply != "quit":
            os.write(2,("coomand not found").encode())
            sys.exit(1)

                       
        	
    else:                           # parent (forked ok)
        #os.write(1, ("Parent: Pid %d Child: Pid %d \n" % (pid,rc)).encode())
        childPidCode = os.wait()
        
        #os.write(1,("Forked went fine").encode())
        #os.write(1,("Parent: Child %d termated with exit code %d \n" % childPidCode).encode())
