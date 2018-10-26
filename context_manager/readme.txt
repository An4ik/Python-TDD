Context managers allow us to properly manage resources, so that we can specify exactly what we want to set up and tear down, when working with certain objects. We can understand that is the Context Manager by keyword-'with'. Context Manager great for files, but it`s useful also for so many different resources. For example, we could use this, to connect and close database. 

There are 2 options to work with methods. One of this by usig a class, second one is by using function with decorater.
1)Create Context Manager that opens the file for us.

We`re opening the file using function with decorater. In our case we`re writing some text. We have to remember to close the file, after we`re done working with it.   
 
from contextlib import context     #We use this context manager decorator to decorate a generator function.

#Code without Context Manager

    f = open(filename ,'w')                       #Open the file for write
    f.write('simple open and write done!')        #We can just work with this in any way. We write some text into the file
    f.close()


# Code with Context Manager

    with open(filename, 'w') as f:                      #Here we are open the file and pass in the filename, f is a file object. 
       	f.write('write with context manager done!')     #We can just work with this in any way. We decide to write some text into the file


#2 Same example

@contextmanager                #decorater
def open_file(file, mode):
    f = open(file, mode)
    yield f                                               
    f.close()

def check_open_file(filename):
    with open_file(filename, 'w') as f:      # We can refer to opened file as f due to yield f in context manager.
        f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
    print(f.closed)


2)So let's say that we are using Python to do some work in a lot of different directories. We're seeding into those directories doing some work and then seeding back to, where we started. For that, we initially  import os  and from contextlib import contextmanager   
     
cwd = os.getcwd()         #then we are setting CWD variable to our current working directory
os.chdir(filename).       #  Now we are changing to the directory where we want to do some work 
print(os.listdir())       #  Then we are listing out everything in that directory and just print it
os.chdir(cwd)             # we're changing directory back to our original current working(cwd) by chdir method
 
We're doing this multiple times whenever we want to do this again.So, if we run the code we can see, that this works fine, it displays all files that are located in the directory. But this is a little inconvenient to save our current directory, switch directories and then switch back to the original after we're done doing what we need to do. So these are things that we don't want to have to remember to do each time. So let's create context manager with a generator function that does this. First:
 
@contextmanager.                  #We use the context manager decorator

We are getting our current working directory, and then we want to change directory to this destination, so we create this function that takes destination as a parameter 

def change_directory(destination)
In order to catch errors we put our setup in a try and a our tear down in a finally.  
cwd = os.getcwd().                   #With setup we will save the current directory that we are in into that CWD variable
os.chdir(destination).               #Now we change directory to our destination
yield                                #We are done with our setup, so now we can just yield.   

In the finally block we just change directory back  to the original:
finally:
   os.chdir(cwd)
)
And now we just call function and print out. We can do it multiple times with directories that we want.
with change_directory(filename):    
    print(os.listdir()
