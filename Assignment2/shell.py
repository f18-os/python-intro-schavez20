#! /usr/bin/env python3
import os, sys, time, re
reply = " "
pid = os.getpid()
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
    reply = input(" shell/>")
    rc = os.fork()
    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)

    elif rc == 0:                   # child
        os.write(1, ("Child: My pid==%d.  Parent's pid=%d\n" % 
                 (os.getpid(), pid)).encode())
        # Taking p4 to modify and create the shell
        #args = ["wc", "p3-exec.py"] # hard coded taking values to make it dynamic
        args = reply.split(" ")
        intake = args
        #now we print to see what is going on
       # print(args)
        if len(args) > 2 and ">" in args:
            #print(" prob have a less than value") # checking if there is a more than just 2 thing such as: cat > filename.txt
            #print(intake)
        
            for indx,val in enumerate(intake):
                print(indx,val)
                if(intake[indx] ==">"):
                    print(intake[indx +1])
                    os.close(1)
                    #print(intake[indx+1])
                    sys.stdout = open(intake[indx+1], "w")
                    fd = sys.stdout.fileno() # os.open("p4-output.txt", os.O_CREAT)
                    os.set_inheritable(fd, True)
                   # os.write(2, ("Child: opened fd=%d for writing\n" % fd).encode())

                    for dir in re.split(":", os.environ['PATH']): # try each directory in path
                        program = "%s/%s" % (dir, args[0])
                        print(program)
                        try:
                            os.execve(program, args, os.environ) # try to exec program
                        except FileNotFoundError:             # ...expected
                            pass                              # ...fail quietly 

                    os.write(2, ("Child:    Error: Could not exec %s\n" % args[0]).encode())
                    sys.exit(1)                 # terminate with error
          
        elif len(args)==1 and "ls" in args:
            print("dird")
            sys.exit(1)
            """os.close(1)                 # redirect child's stdout
            sys.stdout = open("p4-output.txt", "w")
            fd = sys.stdout.fileno() # os.open("p4-output.txt", os.O_CREAT)
            os.set_inheritable(fd, True)
            os.write(2, ("Child: opened fd=%d for writing\n" % fd).encode())

            for dir in re.split(":", os.environ['PATH']): # try each directory in path
                program = "%s/%s" % (dir, args[0])
                try:
                    os.execve(program, args, os.environ) # try to exec program
                except FileNotFoundError:             # ...expected
                    pass                              # ...fail quietly 

            os.write(2, ("Child:    Error: Could not exec %s\n" % args[0]).encode())
            sys.exit(1)                 # terminate with error """
        
    else:                           # parent (forked ok)
          os.write(1, ("Parent: Pid %d Child: Pid %d \n" % (pid,rc)).encode())
          childPidCode = os.wait()
          os.write(1,("Parent: Child %d termated with exit code %d \n" % childPidCode).encode())
     
