import csv
from rich.console import Console
from rich.table import Table
from rich.text import Text
heading = ['day', '9-10', '10-11', '11-11:30', '11:30-12:30', '12:30-1:30', '1:30-2:10', '2:10-3:10', '3:10-4:10']  # column heading for every timetable
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']  # row heading

# total teachers under each subject
teachers = {'ss': ['an', 'prp'], 'aiml': ['sr', 'cm'], 'crypto': ['srh', 'km'], 'ds': ['kr', 'kj'], 'pe1': ['db', 'ps', 'kr'], 'pe2': ['gs', 'dn'],
            'daa': ['dn', 'mkk', 'arm'], 'maths': ['lvr', 'rg', 'yls'], 'mes': ['pk', 'ms', 'sbl'], 'dbms': ['rck', 'ams', 'gls'], 'python': ['aks', 'prp', 'rv', 'sr', 'rsm'],
            'mat': ['nbj', 'lvr'], 'che': ['sha', 'pmk'], 'iot': ['rs', 'vk'], 'egd': ['vp', 'vbr']}

teaching = []  # teachers handling subjects currently

def create():  # to create csv files
    filename = input("Enter file name: ")
    tt = open(filename, 'w', newline='\n')  # to open the file
    wr = csv.writer(tt, delimiter=',')  # writer obj
    wr.writerow(heading)

    for i in days:  # for each day enter the timetable in order
        print("enter ", i, '\'s timetable')
        l = []
        l.append(i)
        l.append(input())
        l.append(input())
        l.append('')
        l.append(input())
        l.append(input())
        l.append('')
        l.append(input())
        l.append(input())
        wr.writerow(l)  # writing into the file in a particular format
    print("file created")
    tt.close()

def display(tt,filename):
    table = Table(title=filename)
    # Add the headings to the table
    for i in heading:
        table.add_column(i, width=15)
    # Add rows to the table from the CSV file
    tt_list=[]
    for i in tt:
        l=[]
        l.append(i)
        for j in tt[i]:
            l.append(str(j))
        
        tt_list.append(l)
    tt_list.pop(0)
    for i in tt_list:
        table.add_row(*i)
    # Create a Console object and print the table
    console = Console()
    console.print(table)

def display_with_clash(tt_rec,day,pos,color):
    table=Table(title=file_name[list_of_files.index(tt_rec)])
    for i in heading:
        table.add_column(i, width=15)   
    tt_list=[]
    for i in tt_rec:
        l=[]
        l.append(i)
        l.extend(tt_rec[i])
        tt_list.append(l)
  
    tt_list.pop(0)
    for i in tt_list:
        if i[0]==day :
           
            i[pos]=Text(i[pos], style=color)
        table.add_row(*i)
    console = Console()
    console.print(table)

def openfile(filename): #to open a file and save it as a dictionary to make the changes in time table
    tt=open(filename,'r')
    rec=csv.reader(tt) 
    _4a={}
    for i in rec: # each day's tt
        day=i[0] # day name
        l=[]
        for j in range(1,len(i)):
                l.append(i[j]) #tt as a list
        _4a[day]=l  # day,list pair
    display(_4a,filename)
    return _4a


def clash_detector(a,b):
    global list_of_files
    day=pos=None
    for i in days:  # days of the week
        for k in range(0,8):  # no of classes in a day
            
            if list_of_files[a][i][k] in ['0',''] or list_of_files[b][i][k] in  ['0','']:  #skip if the class is not scheduled
                continue
            n=list_of_files[a][i][k][1:-1].split(',') # from the list of files find the file, file's day, day's class
            m=list_of_files[b][i][k][1:-1].split(',') # from the list of files find the file, file's day, day's class
            if n[1] not in teaching: teaching.append(n[1]) #adding the teacher to the teching list
            if m[1] not in teaching: teaching.append(m[1]) #[subject, teacher, room no]
            
            if n[1]==m[1]: #checking if the teachers are the same
                #f=False
                print(f'\n{i} {heading[k]}: Teacher clash for {n[1]} ({n[0]} and {m[0]})') #printing the clash msg
                display_with_clash(list_of_files[a],i,k+1,'bold red')
                display_with_clash(list_of_files[b],i,k+1,'bold red')
                #_4a=switch_day(_4a,_6a,i)
                pos=k
                day=i
            
            elif n[2]==m[2]: #checking if the rooms are the same
                #f=False
                print(f'\n{i} {heading[k]}: Room clash in {n[2]} ({n[0]} and {m[0]})') #printing the clash msg
                #_4a=switch_day(_4a,_6a,i)
                display_with_clash(list_of_files[a],i,k+1,'bold red')
                display_with_clash(list_of_files[b],i,k+1,'bold red')
                pos=k
                day=i
    print()
    return day,pos # returnign the clash day and class posititon



def switch_class(i,day,pos): #i= timetable, day= clash day, pos= clash pos
    global list_of_files
    if pos<3: # if the clash in the morning slot exchange the middle and morning classes
        list_of_files[i][day][0],list_of_files[i][day][3]=list_of_files[i][day][3],list_of_files[i][day][0]
        list_of_files[i][day][1],list_of_files[i][day][4]=list_of_files[i][day][4],list_of_files[i][day][1]
    elif pos<6: # if the clash in the middke slot exchange the middle and evening classes
        list_of_files[i][day][3],list_of_files[i][day][6]=list_of_files[i][day][6],list_of_files[i][day][3]
        list_of_files[i][day][4],list_of_files[i][day][7]=list_of_files[i][day][7],list_of_files[i][day][4]
    else: # if the clash in the last slot exchange the last and morning classes
        list_of_files[i][day][0],list_of_files[i][day][6]=list_of_files[i][day][6],list_of_files[i][day][0]
        list_of_files[i][day][1],list_of_files[i][day][7]=list_of_files[i][day][7],list_of_files[i][day][1]
    f=True #shift the flag back to true
    return rec1 #return the flag
    

def switch_day(a,b,day): #a= timetable,b= timetable, day= clash day
    global list_of_files
    for i in days: #in the list of days
        if i != day: # if the day is not equla to tthe clash day
            for k in range(0,8):
                if list_of_files[a][i][k] in ['0',''] or list_of_files[b][day][k] in  ['0','']:
                    continue
                n=list_of_files[a][i][k][1:-1].split(',')
                m=list_of_files[b][day][k][1:-1].split(',')
                if n[1]==m[1] or n[2]==m[2]: #if the clash still exsits continue with the loop
                    continue
                else: #if there is no clash then exhange the 2 day's timetable 
                    list_of_files[a][i],list_of_files[a][day]=list_of_files[a][day],list_of_files[a][i]
                    break
                    
def switch_teacher(a,day,pos):
    global list_of_files,teaching,teachers
    class_=list_of_files[a][day][pos][1:-1].split(',') #extracting the exact class with the clash
    sub=class_[0]
    te=class_[1]
    l=teachers[sub]
    for i in l:
        if i not in teaching:
            new=i
            break
    for i in days:
        for k in range(0,8): 
            if list_of_files[a][i][k] in ['0',''] :#skip if the class is not scheduled
                continue
            class_=list_of_files[a][i][k][1:-1].split(',')# no of classes in a day
            if class_[1]==te:
                class_[1]=new
            list_of_files[a][i][k]=class_

file_name=[] #list of file names for printing
list_of_files = [] #list of file pathnames
n = int(input("Enter number of files: ")) #no of files to check

for i in range(n):
    filename = input("Enter file name: ")
    rec1 = openfile(filename) # open the file and convert it into a dict
    list_of_files.append(rec1) #applend the dict to teh list
    file_name.append(filename.split('/')[-1]) #append the filenaem
for i in range(n): #no of files
    for j in range(i+1, n): # comparing 2 files
        if file_name[i] != file_name[j]:
            print('\n\n',file_name[i], file_name[j], sep="\t") #printing the files names being compared
            day, pos = clash_detector(i, j) #checking clashes

            if day !=None:  # Ensure 'f' is defined somewhere
                print("HOW WOULD YOU LIKE TO FIX THE CLASH\n1. Switch classes within the day\n2. Switch days \n3. Switch teacher\n4. Ignore")
                ch = int(input("Enter a number: ")) #taking a input to call the function
                if ch == 1:
                    switch_class(i,day, pos) #to switch classes
                elif ch == 2:
                    switch_day(i, j, day) #to switch days
                elif ch ==3:
                    switch_teacher(i,day,pos)
                elif ch == 4:
                    continue #to ignore the clash
            else:
                print("\nNO CLASH\n")            

for i in list_of_files: 
    display(i,file_name[list_of_files.index(i)])


#writing back a new editied timetable                
for i in list_of_files:
    n=list_of_files.index(i)
    new_file="/Users/akshayarajagopal/Desktop/time table/new"+file_name[n]
    rec=open(new_file,'w')
    wr=csv.writer(rec , delimiter=',')  #writer obj
    for j in i:
        l=[]
        l.append(j)
        l.extend(i[j])
        wr.writerow(l)
    