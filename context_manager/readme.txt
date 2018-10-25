Context managers allow us to properly manage resources so that we can specify exactly what we want to set up and tear down when working with certain objects.
We can tell that we are using context manager becouse of the with statemant.
Context Manager great for files, but it`s useful for so many different resources. So for example we could use this to connect to and close database. 

There are 2 options to work with methods. One of this by usig a class, second one is by using function with decorater.
1)Create Context Manager that opens the file for us.

We`re opening the file using function with decoreater. In our case we`re writing some text. We have to remember to close the file, after we`re done working with it.   
 
form contextlib import context     #We use this context manager decorator to decorate a generator function.

#Code without Context Manager.

    f = open(filename ,'w')                       #Open the file for write
    f.write('simple open and write done!')        #We can just work with this in any way. We write some text into the file
    f.close()


# Code with Context Manager

    with open(filename, 'w') as f:                          #Here we are open file class and pass in the filename, f is a file object. 
       	f.write('write with context manager done!')         #We can just work with this in any way. We write some text into the file.


#2 Same example

@contextmanager
def open_file(file, mode):
    f = open(file, mode) 	
    yield f            		
    f.close()

def check_open_file(filename):
    with open_file(filename, 'w') as f:                   # We can refer to opened file as f due to yield f in context manager.
        f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')
    print(f.closed)

        
