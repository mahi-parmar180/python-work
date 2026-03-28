f=open("1.txt","w")
f.write("Hello Students\n")
f.write("Welcome to python file handling.\n")
f.write("Learning is fun!\n")
f.close()

f=open("1.txt","w")
f.write("New Content only.\n")
f.close()

f=open("1.txt","w")
lines=[
    "Python Programming\n",
    "File Handling\n",
    "Error Handling",
    "Expection Handling\n"
]
f.writelines(lines)
f.close()