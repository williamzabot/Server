import os, platform
from datetime import datetime
from datetime import date
from PingInfo import PingInfo

file = "customping.txt"

def doPing(url):
    qtdPackages = verifyPlatform(str("3"))
    command = "ping " + qtdPackages + url + " > " + file
    os.system(command)
    return getPingInfo(url)

def verifyPlatform(qtd):
    command = "-n " if platform.system().lower() == "windows" else "-c "
    return command + qtd + " "

def getPingInfo(url):
    arq = open(file)
    lines = arq.readlines()
    firstLine = lines[0].split()
    secondLine = lines[1].split()
    pingInfo = PingInfo()
    pingInfo.url = url
    pingInfo.ip = firstLine[2].replace(":", "").replace("(", "").replace(")", "")
    pingInfo.ttl = getPosition(secondLine, 5)
    pingInfo.time = getPosition(secondLine, 6)
    pingInfo.date = date.today().strftime('%d/%m/%Y')
    pingInfo.currentTime = datetime.now().strftime('%H:%M')
    return pingInfo

def getPosition(splitLine, position):
    target = splitLine[position]
    return target.split("=")[1]