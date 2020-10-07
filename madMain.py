#Michael Krummenacker
#MadLibs Main file
#Purpose: Takes in a mad lib text file and user input. Runs it through the function document
#and returns a completed madLib. 




from madFunctions import * #imports madFuctions file

terminate='y'
while terminate=='y':  #while loop allows user to use code multiple times
    filename=input("Enter file name (w/o '.txt'): ")
    banana=False
    while banana==False: #this loop uses try: so incorrect input filenames won't stop function
        try:
            input_file=open(filename+'.txt','r')#opens input text file
            banana=True
        except:
            filename=input("File not found. Try again: ")

    outputname=input("Output file name (w/o '.txt'): ")
    pineapple=False
    while pineapple==False:
        if ' ' not in outputname and '.txt' not in outputname: #This loops makes sure a correct output file is names 
            output_file=open(outputname+'.txt','w') #opens output text file
            pineapple=True
        else:
            outputname=input("Invalid Input. Try again: ")

    print()
    line=input_file.readline()
    line.strip('\n')

    while line !='': #loop uses functions from madFunctions to replace prompts with user input

        if '<' in line:
            mad=replaceLibs(line)#uses function from madFuctions to replace prompts
            output_file.write(mad)#writes edited madlib to output file
        line=input_file.readline()
        line.strip('\n')

    output_file.close()
    output_file=open(outputname+'.txt','r')

    print()
    flag=input("View your MadLib? (y/n): ")
    print()

    if flag.lower() == 'y': #Checks if user wants to see completed madlibs
        oline=output_file.readline()#reads output file
        while oline != '':          #loop prints completed madlib
            oline=oline.strip('\n') 
            oline=betterStrip(oline)
            print(oline)
            oline=output_file.readline()
    
    print()
    terminate=input('Proccess another Madlib? (y/n): ') #checks to see if the user would like to create another madlib
    print()
    
            

#closes files
input_file.close()
output_file.close()

