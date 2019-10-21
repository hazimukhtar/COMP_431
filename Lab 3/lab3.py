#Hazim Mukhtar
#ONYEN: Hazimukh
from sys import stdin
from sys import stderr
import time

def parseForward(token, string, state):
    if (token == "start"):  #This is the start of the program
        if state == 0:   #Start of a new message
            if fromLine(string):
                if parseForward("response-code", string, state):
                    return state+1
                else:
                    return parseForward("QUIT", string, state)
            else:
                return parseForward("QUIT", string, state)

        elif state == 1 :
            if toLine(string):
                if parseForward("response-code", string, state):
                    return state+1
                else:
                    return parseForward("QUIT", string, state)
            else:
                return parseForward("QUIT", string, state)
        elif state == 2:
            if toLine(string):
                if parseForward("response-code", string, state):
                    return state
            else:
                parseForward("start", string, state+1)
                parseForward("start", string, state+2)
                return state+2
        elif state == 3:
            print "Data"
            parseForward("response-code", string, state)


        elif state == 4:
            if parseForward("Message", string, state):
                return state
            else:
                parseForward("start", string, 0)
                return 1

        else:
            return parseForward("QUIT", string, state)

    elif token == "Message":
        if dataInfo(string):
            return True
        else:
            return False

    elif token == "QUIT":
        return 10

    elif token == "response-code":
        if echoResponse():
            return True
        else:
            return False


def echoResponse():
    response = ""
    response = stdin.readline()
    responseCode = response.split()[0]
    if responseNumber(responseCode):
        stderr.write(response)
        if errors(responseCode):
            return True
    return False


def responseNumber(string):
    if string == '250' or string == '354' or string == '500' or string == '501':
        return True
    return False

def errors(string):
    if string == '500' or string == '501':
        return False
    else:
        return True


def whiteSpace(string):
    index = 0
    for x in string:
        if x != ' ' and x != '\t':
            return string[index:]
        index += 1

def fromLine(string):
    reversePath = string[6:]
    if string[:5] == "From:":
        print "MAIL FROM: " + reversePath.strip()
        return True
    else:
        return False

def toLine(string):
    forwardPath = string[4:]
    if string[:3] == "To:":
        print "RCPT TO: " + forwardPath.strip()
        return True
    else:
        return False

def dataInfo(string):
    if len(string) == 0:
        print"."

    elif string[:5] != "From:":
        print string.strip()
        return True

    else:
        print "."
        echoResponse()





input = " "
fullMessage = ""
tempMessage = ""
state = 0

while input != "":
    if state == 10:
        stderr.write("QUIT")
        break
    else:
        input = stdin.readline()
        state = parseForward("start", input, state)  #Program Starts and Input is put into the parser