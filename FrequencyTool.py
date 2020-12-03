from os import strerror, scandir

# set initial values to 0
a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=v=w=x=y=z=0 

#set alphabet to count frequency of:
alpDict = {'a': a, 'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i, 'j':j,'k':k,
               'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,
               'x':x,'y':y,'z':z}

# Request path where text files are from user
path = input("Input path to directory with / seperators: ")

# Request name for new folder to save results if wanted (hit Enter if not)
save_name = input("Enter file path/name to save results too or hit enter if you don't want to save results: ")

# Using scandir from os save to list all the file names ending in .txt 
files = [file.name for file in scandir(path) if '.txt' in file.name]

for name in files:
    # iterate through file name list and open the files
    try:
        file = open(f"{path}/{name}", "rt")
        text = file.read()
    except IOError as e:
        print("I/O Error occurred: ", strerror(e.errno))
        exit(e.errno)
        
    for ch in text:
        # iterate through all characters in file and add to frequency dictionary when a matching letter found.
        if ch.isalpha():
            alpDict[ch.lower()] +=1

freqList = []
# Make a list with (value, key) from dictionary,(In this order so the sorted() function can look at the values first)
# Sort the list from highest to lowest frequency of each letter
freqList = sorted([(alpDict[letter], letter) for letter in alpDict if alpDict[letter] >0],reverse=True)

#print each letter and it's frequency in the text files from highests to lowest
for each in freqList:
    print(f"{each[1]} --> {each[0]}")
   
if save_name:
    # If name was given for a results file creat this file in write mode
    try:
        results_file = open(f"{save_name}.txt", "wt")

        for each in freqList:
            #Write to file histogram of results
            line = f"{each[1]} --> {each[0]}\n"
            results_file.write(line)

        # close file when finished
        results_file.close()

    except IOError as e:
        print("Couldn't create file: ", strerror(e.errno))
        exit(e.errno)
