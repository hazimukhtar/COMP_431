#Hazim Mukhtar
#ONYEN: Hazimukh
from sys import stdin
five = 15

def checkMail(mail):
    if mail == "MAIL" or mail == "mail":
        return True
    else:
        return False

def checkFrom(fromInput):
    if fromInput == "FROM:" or fromInput == "from:":
        return True
    else:
        return False

def specialCharacters(str):
    index= 0
    for x in str:
        if (x == '<' or x == '>' or x=='(' or x == ')' or x =='[' or x == ']' or x == '\\' or x == '.' or x == ',' or x == ';' or x == ':' or x == '@' or x == " " or x == "\t"  ):
            return False
    return True

def letters(domain):
    for x in domain:
        if x.isalpha() == False :
            return False
    return True

def numbers(domain):
    for x in domain:
        if x.isdigit() == False :
            return False
    return True

def checkDomain(domain):
    for characters in domain:
        if characters == " " or characters =="\t":
            return False
    splitElements = domain.split(".")
    for x in splitElements:
        if x == '':
            return False
        if letters(x[0]) == False:
            return False
        else:
            for y in x:
                if letters(y) == False and numbers(y) == False:
                    return False
    return True

def whiteSpace(string):
    tempString = ''
    index = 0
    for x in string:
        if x != ' ' and x != '\t':
            return string[index:]
        index += 1



def mailCommands(token, string):

    if token == "start":
        if checkMail(string[:4]):
            mailCommands("mail", string)
     #   if string[:4] == "RCPT":
     #       mailCommands("RCPT", string)
        else:
            print ("ERROR -- mail-from-cmd")

    elif token == "mail":
        if  checkMail(string.split()[0]):

            mailCommands("from", whiteSpace(string[4:]))
        else:
            print("ERROR -- mail-from-cmd")

    elif token == "RCPT":
        if  string.split()[0] == "RCPT":
            mailCommands("to", whiteSpace(string[4:]))
        else:
            print("ERROR -- mail-from-cmd")

    elif token == "from":
        if string.find("from:") != -1 or string.find("FROM:") != -1:

            mailCommands("reverse-path", whiteSpace(string[5:]))
        else:
            print("ERROR -- mail-from-cmd")
    elif token == "to":
        print "RCPT"
        if string.find("TO:") != -1:

            mailCommands("forward-path", string)
        else:
            print("ERROR -- mail-from-cmd")

    elif token == "whitespace":
        mailCommands("SP", string)

    elif token == "reverse-path":
        mailCommands("path", string)

    elif token == "forward-path":
        mailCommands("path", string)

    elif token == "path":
        if string.find("<") != -1:
            mailCommands("mailbox", string[1:])
        else:
            print ("ERROR -- path")


    elif token == "mailbox":
        mailCommands("local-part", string)


    elif token == "local-part":
        mailCommands("string", string)



    elif token == "string":
        mailCommands("char", string)



    elif token == "char":
        atPos = string.find("@")
        if atPos != -1:
            if specialCharacters(string[:atPos]) == True:
                mailCommands("domain", string[atPos+1:])
            else:
                print("ERROR -- mailbox")
        else:
            print ("ERROR -- mailbox")



    elif token == "domain":
        mailCommands("element", string)



    elif token == "element":
        endPos = string.find(">")
        if endPos != -1:
            if checkDomain(string[:endPos]) == True:
                mailCommands("CRLF", whiteSpace(string[endPos+1:]))
            else:
                print ("ERROR -- domain")
        else:
            print ("ERROR -- path")

    elif token == "CRLF":
        if string == '\n':
            print "Sender ok"
        else:
            print ("ERROR -- mail-from-cmd")
    else:
        print("helpme")


input = " "

while input != "":
    input = stdin.readline()
    if(len(input)==0):
        break
    else:
        test = input.find("\n")
        if test != -1 :
            print (input[:test])
        else:
            print(input.rstrip())
        mailCommands("start", input)