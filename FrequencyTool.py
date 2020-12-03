from os import strerror, scandir

a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=v=w=x=y=z=0
alpDict = {'a': a, 'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i, 'j':j,'k':k,
               'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,
               'x':x,'y':y,'z':z}
path = input("Input path to directory with / seperators: ")
files = [file.name for file in scandir(path) if '.txt' in file.name]

for name in files:
    try:
        file = open(f"{path}/{name}", "rt")
        text = file.read()
    except IOError as e:
        print("I/O Error occurred: ", strerror(e.errno))
        exit(e.errno)
        
    for ch in text:
        if ch.isalpha():
            alpDict[ch.lower()] +=1

freqList = []

freqList = sorted([(alpDict[letter], letter) for letter in alpDict if alpDict[letter] >0],reverse=True)

for each in freqList:
    print(f"{each[1]} --> {each[0]}")
