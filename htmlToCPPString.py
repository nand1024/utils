import sys
import os.path

hint = "\"*.html\" \"*.cpp\" \"name of String variable\""

if  not (len(sys.argv) == 4) or sys.argv[1] == "help" or sys.argv[1] == "Help" or sys.argv[1] == "?":
    print(hint)
    exit()
    
fileHtml = sys.argv[1]
fileRes = sys.argv[2]
strName = sys.argv[3]

if not os.path.exists(fileHtml):
    print("file: " + fileHtml + " is not exist")
    print(hint)
    exit()

if not os.path.exists(fileRes):
    print("file: " + fileRes + " is not exist")
    print(hint)
    exit()

fHtml = open(fileHtml, "rt")
txtHtml = fHtml.read()
fHtml.close()

txtHtml = txtHtml.replace("\n", "\\n\\\n")
txtHtml = txtHtml.replace('"', '\\"')
txtHtml = "String "+strName+" = \"\\\n" + txtHtml +"\\\n\""

fRes = open(fileRes, "w+t")
fRes.write(txtHtml)
fRes.close()
