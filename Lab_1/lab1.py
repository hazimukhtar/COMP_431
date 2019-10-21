# Hazim Mukhtar
# ONYEN: Hazimukh
from sys import stdin


def specialCharacters(str):
    for x in str:
        if (x == '<' or x == '>' or x=='(' or x == ')' or x =='[' or x == ']' or x == '\\' or x == '.' or x == ',' or x == ';' or x == ':' or x == '@' or x == " " or x == "\t"  ):
            return -1
    return 1

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

def mailCommands(input):
    if checkMail(input[:4]) == True:
        if input.find("FROM") != -1 or input.find("from") != -1:
            if checkFrom(spaceString[1][:5]) == True :
                colonPos = input.index(':') +1
                if input.find("<") != -1:
                    if(input[colonPos : colonPos+1] == '<' or spaceString[2][:1] == '<'):
                        leftPos = input.index("<")+1
                        if input.find("@") != -1:
                            atPos = input.index("@")
                            if(specialCharacters(input[leftPos:atPos]) == 1 and input.find("@", atPos+1)== -1 ):
                                if input.find(">") != -1:
                                    rightPos = input.index(">")
                                    if input[rightPos-1: rightPos] != " " and input[rightPos-1: rightPos] != "\t":

                                        domain = input[atPos+1 : rightPos]

                                        if checkDomain(domain) == True:
                                            if input[rightPos-1] != " " or input[rightPos-1] != "\n":
                                                after = input.find("\n") +1
                                                if input.find("\n") != -1 and len(input) == after:
                                                    print("Sender ok")

                                                else:
                                                    print("ERROR CRLF")
                                            else:
                                                print("ERROR -- element")
                                        else:
                                            print("ERROR -- domain")
                                    else:
                                        print("ERROR --path")
                                else:
                                    print("ERROR -- domain")
                            else:
                                print("ERROR -- mailbox")
                        else:
                            print("ERROR -- mailbox")
                    else:
                        print("ERROR -- path")
                else:
                    print("ERROR -- path")
            else:
                print("ERROR -- mail-from-cmd")
        else:
            print("ERROR -- mail-from-cmd")
    else:
        print("ERROR -- mail-from-cmd")

input = " "
while input != "":
    input = stdin.readline()
    if(len(input)==0):
        break
    else:
        print(input.rstrip())
        spaceString = input.split()
        mailCommands(input)