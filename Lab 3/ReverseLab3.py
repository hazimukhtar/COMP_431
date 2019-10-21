#Hazim Mukhtar
#ONYEN: Hazimukh
from sys import stdin
from sys import stderr

def parseForward(token, string, state):
    if (token == "start"):  #This is the start of the program
        if string[:5]== "From:" and state == 0:
            fromLine(string)
            if echoResponse():
                return state
            else:
                return 10
        elif string[:5]== "From:" and state == 4:
            stderr.write('.')
            if echoResponse():
                state = 0
            else:
                return 10
            fromLine(string)
            if echoResponse():
                return state
            else:
                return 10

        elif string[:3] == "To:":
            toLine(string)
            if echoResponse():
                return 2
            else:
                return 10

        elif state == 2:
            stderr.write('Data')
            if echoResponse():
                stderr.write(string.rstrip())
                return 4
            else:
                return 10
        else:
            stderr.write(string.rstrip())
            return state

    else:
        print 'helpMe'






def echoResponse():
    response = stdin.readline()
    print(response)
    if responseNumber(response[:3]):
        if errors(response[:3]):
            return True
        return False
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

def fromLine(string):
    reversePath = string[6:]
    if string[:5] == "From:":
        stderr.write("MAIL FROM: " + reversePath.strip())
        return True
    else:
        return False

def toLine(string):
    forwardPath = string[4:]
    if string[:3] == "To:":
        stderr.write("RCPT TO: " + forwardPath.strip())
        return True
    else:
        return False


input = " "
state = 0

while input != "":
    if state == 10:
        stderr.write("QUIT")
        break
    else:
        input = stdin.readline()
        state = parseForward("start", input, state)  #Program Starts and Input is put into the parser