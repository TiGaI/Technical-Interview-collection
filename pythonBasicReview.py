#os
import os, glob

#find all jgp
os.chdir("/USER/asdasd/")
for file in glob.glob('*.jgp'):
	print(file)

#find all file and rename it
print(os.getcwd())
for f in os.listdir():
	print(f) #print all file name
	file_name, file_ext = os.path.splitext(f)
	if file_ext == ".mp3":
		f_title, f_course, f_num = file_name.split('-')
		f_title = f_title.strip()
		f_course = f_course.strip()
		f_num = f_num.strip() #striping space on the left and right of the word
		f_num = f_num.zfile(2) #fill zero infront of one digit number

		new_name = '{}-{}{}'.format(f_title, f_num, file_ext)

		os.rename(f, new_name)


#open and write file
f = open("C:/Python33/README.txt")
f.close()

r = open file for reading
r+ = open file for updating (read and write)
w = open file for writing
x = open a file for exclusive creation. Operation fails if file already exist
a = open file for appendign at the end
t = open in text mode
b = open in binary mode
f.readlines #return a array
f.readline #return line by line of the doc


#Class and inhertances
class A(object): 
    def __init__(self):
        self.a = 'a'
        print(self.a)
class B(A):
    def __init__(self):
        self.b = 'b'
        print(self.b)
        super(B,self).__init__()           
class C(A):
    def __init__(self):
        self.c = 'c'
        print(self.c)
class D(B,C):
    def __init__(self):
        self.d = 'd'
        print(self.d)
        super(D, self).__init__()
d = D()
print(D.mro())
dbc


#advance list compression

#Advance of Generator
The important point is that the list comprehension creates a new list. The generator creates a an iterable object that will "filter" the source material on-the-fly as you consume the bits.
Imagine you have a 2TB log file called "hugefile.txt", and you want the content and length for all the lines that start with the word "ENTRY".
So you try starting out by writing a list comprehension:

logfile = open("hugefile.txt","r")
entry_lines = [(line,len(line)) for line in logfile if line.startswith("ENTRY")]
'''
This slurps up the whole file, processes each line, and stores the matching lines in your array. This array could therefore contain up to 2TB of content. 
That's a lot of RAM, and probably not practical for your purposes.
So instead we can use a generator to apply a "filter" to our content. No data is actually read until we start iterating over the result.
'''
logfile = open("hugefile.txt","r")
entry_lines = ((line,len(line)) for line in logfile if line.startswith("ENTRY"))
'''
Not even a single line has been read from our file yet. In fact, say we want to filter our result even further: long_entries = ((line,length) for (line,length) in entry_lines if length > 80)
Still nothing has been read, but we've specified now two generators that will act on our data as we wishself. Lets write out our filtered lines to another file:
'''
outfile = open("filtered.txt","a")
for entry,length in long_entries:
    outfile.write(entry)
'''    
Now we read the input file. As our for loop continues to request additional lines, the long_entries generator demands lines from the entry_lines generator, 
returning only those whose length is greater than 80 characters. And in turn, the entry_lines generator requests lines (filtered as indicated) from the logfile iterator, which in turn reads the file.
So instead of "pushing" data to your output function in the form of a fully-populated list, you're giving the output function a way to "pull" data only when its needed. This is in our case much more 
efficient, but not quite as flexible. Generators are one way, one pass; the data from the log file we've read gets immediately discarded, so we can't go back to a previous line. On the other hand, 
we don't have to worry about keeping data around once we're done with it.'''

list comprehension will create the entire list in memory first 
Generator expression will create the items on the fly, so you are able to use it for very large (and also infinite!) sequences.


#Using With Method - useful when you have two or more related operation that you like to execture as a pair
class Saved():
    def __init__(self, cr):
        self.cr = cr
    def __enter__(self):
        self.cr.save()
        return self.cr
    def __exit__(self, type, value, traceback):
        self.cr.restore()

cr.translate(68, 68)
for i in xrange(6):
    with Saved(cr):
        cr.rotate(2 * math.pi * i / 6)
        cr.rectangle(-25, -60, 50, 40)
        cr.stroke()

		1. With can use to catches exceptions
#another way to use the with statement		
import cairo
from contextlib import contextmanager

@contextmanager
def saved(cr):
    cr.save()
    try:
        yield cr
    finally:
        cr.restore()

def Tree(angle):
    cr.move_to(0, 0)
    cr.translate(0, -65)
    cr.line_to(0, 0)
    cr.stroke()
    cr.scale(0.72, 0.72)
    if angle > 0.12:
        for a in [-angle, angle]:
            with saved(cr):
                cr.rotate(a)
                Tree(angle * 0.75)

#Ternary Operator
big = x if x > y else y
i=100
a = 1 if i<100 else 2 if i>100 else 0

#regex expression
import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
321-555-4321
123.555.1234
Ha HaHa
MetaCharacters (Need to be erased)
'''

sentence = 'Start a sentence and the nbring it to an end'

* 0 or more					
+ 1 or more
? 0 or 1
^ start of string
$ end of the string
() group
(?:) Non-capturing group

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
r"[A-z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}"
r"(Mr|Mrs|Ms)\.?\s[A-Z]\w*"

matches anything between two words
print(re.sub(r'(?<=\w)([^\w]+)(?=\w)'," ", string))
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

different between split(), sub(), subn()
split() - split string by using a pattern as a seperator into a list
sub() - find a current substring, then it can either be replace it another or be run into a function to return another modified string
subn() - return the samethign as sub() but the number of substitiutions made by re.sub

#Decorator - use to add functionality of your functions. very useful for logging
import logging
logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

logging.info()


#Easy Example on how it works
def decorator_function(original_function):
	def wrapper(*args, **kwargs):
		#....Doing whatever you want
		return original_function(*args, **kwargs)
	return wrapper
@decorator_function
#Use the @wraps(orig_func) in every decorator main function, to stack multiple decorator calls
def anyname():
	print(something)
anyname()

#logger, handler and formatters
import logging
logging.basicConfig(filename="sample.log", level=logging.DEBUG, format='%(asctime)s:%(name)s:%(message)s')

