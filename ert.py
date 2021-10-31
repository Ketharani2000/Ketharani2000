def printinfo( arg1=10, *vartuple ):
    "This prints a variable passed arguments"
    print ("Output is: ")
    print (arg1)
    for var in vartuple:
        print (var)
    return
printinfo(  )
printinfo( 70, 60, 50, 90, 100 )
