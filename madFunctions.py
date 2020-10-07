#Michael Krummenacker
#Madlibs function file
#Purposes: takes in lines from input file and replaces the prompts with new words


#Replaces lines from main with updated words
def replaceLibs(line):
    '''Replaces madlib text files with user input'''

    temp=''
    temp2=line
    line=line.split('<')#splits line
    idx=0
    while idx <= len(line)-1: #loop takes line input and looks for instances of '>'
        l=line[idx]
        if '>' in l:
            i=0
            while i <= l.index('>'):#loop takes instances of '>' and puts the word before it into new temp string
                temp=temp+l[i]
                i=i+1
            
            temp=temp.strip('>')
            new=input("Please type an {}: ".format(temp))#takes user input for replacement of temp
            temp2=temp2.replace(temp,new,1)#replaces first instance of temp with new
            temp=''
        idx=idx+1
    return temp2 #returns edited line


#strip file wasn't good so made an new function to remove all instances of < and > 
def betterStrip(string1):
    string1=string1.replace('<','')#replaces < with ''
    string1=string1.replace('>','')#replaces > with ''
    return string1

        
        

'''def replaceN(line, oldword, newWord):
    line=line.replace(line,newWord)
    return line'''



'''temp=[]
    temp2=''
    for char in line:
        temp.append(char)
    i=temp.index('<')
    while i < temp.index('>')+1:

        temp2=temp2+temp[i]
        i=i+1
    return temp2'''

