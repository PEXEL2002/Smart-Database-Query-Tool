def CreateTable(date,orTheHeader=False):
    """
    :param date: data for creating table
    :param orTheHeader: variable checks if the user has provided the header row
    :return: prints tables from the given array
    """
    Elementlength = []
    for a in date[0]: # loop creates arrays of zeros with the length of data to display
        Elementlength.append(0)
    for i in range(len(date)):  # loop finds longest string in given column
        x = 0
        for a in date[i]:
            helpStr = "| "+str(a)+" "
            if len(helpStr) > Elementlength[x]:
                Elementlength[x] = len(helpStr)
            x += 1
    lenSum =  sum(Elementlength)+1
    if orTheHeader: # If the user has specified a header row, it is separated from the others
        print("-"*lenSum)
        x = 0
        for a in date[0]: # listing of headers
            helpStr = "| " + str(a) + " "
            print(helpStr + " " * (Elementlength[x] - len(helpStr)), end="")
            x += 1
        print("|")
        print("-" * lenSum)
    else:
        print("-" * lenSum)
    for i in range(len(date)-1): # output
        x = 0
        for a in date[i+1]:
            helpStr = "| "+str(a)+" "
            print(helpStr+" "*(Elementlength[x]-len(helpStr)),end="")
            x += 1
        print("|")
    print("-" * lenSum)