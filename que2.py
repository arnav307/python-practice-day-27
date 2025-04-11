def filename():
    
    try:
        searchfile=input("Enter a file name: ")
        with open(searchfile,'r') as inputfile:
            inputfile=inputfile.read()
            print(inputfile)
    except FileNotFoundError:
        print("Your file does not exist")
         
filename()
