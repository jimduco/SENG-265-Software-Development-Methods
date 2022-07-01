#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 01 08:35:33 2022
@author: rivera

This is a text processor that allows to translate XML-based events to YAML-based events.
CAREFUL: You ARE NOT allowed using (i.e., import) modules/libraries/packages to parse XML or YAML
(e.g., yaml or xml modules). You will need to rely on Python collections to achieve the reading of XML files and the
generation of YAML files.
"""
import sys
import re
import datetime
import operator
from time import strftime

def print_hello_message(message):
    """Prints a welcome message.

    Parameters
    ----------
    message : str, required
        The file path of the file to read.

    Returns
    -------
    void
        This function is not expected to return anything
    """
    print(message)

def extractArgs():
    """Returns a dictionary with the wanted arguments from the system terminal inputs

    Parameters
    ----------
    N/A

    Returns
    -------
    Dictionary
        Dictionary that contains the wanted arguments
    """
    argsDict = {}

    for i in range(1, len(sys.argv)):
        splitArg = sys.argv[i].split('=')
        argsDict[splitArg[0][2:]] = splitArg[1]

    splitStart = argsDict["start"].split('/')
    argsDict["start"] = datetime.datetime(year=(int)(splitStart[0]),
                                          month = (int)(splitStart[1]),
                                          day = (int)(splitStart[2]))
    splitEnd = argsDict["end"].split('/')
    argsDict["end"] = datetime.datetime(year=(int)(splitEnd[0]),
                                          month = (int)(splitEnd[1]),
                                          day = (int)(splitEnd[2]))

    return argsDict

def parseFile(fileType, fileName):
    """Given an xml file, parse it for relevant information and
       return a list of dicionaries of the relevant extracted info.
       Code based off of the parse_xml.py file given

    Parameters
    ----------
    fileType: str, required
        Can be any of the three: events or circuits or broadcasters
    fileName: str, required
        The name of the xml file to read

    Returns
    -------
    List
        List of dictionary that contains relevent extracted information of the circuits/events/broadcasters
    """
    if(fileType == 'events'):
        moduloNum = 9
    if(fileType == 'circuits'):
        moduloNum = 5
    if(fileType == 'broadcasters'):
        moduloNum = 3

    listToReturn = []
    filtered_lines = []

    inputFile = open(fileName)
    with inputFile as file:
        for line in file:
            line = re.findall(r'<(.*?)>(.*?)</\1>', line)
            if len(line) > 0:
                filtered_lines.append(line[0])

    temp_dic = {}

    for i in range(len(filtered_lines)):
        tup = filtered_lines[i]
        temp_dic[tup[0]] = tup[1]
        if (i+1)%(moduloNum) == 0 and i>0:
            listToReturn.append(temp_dic)
            temp_dic = {}

    inputFile.close()
    return listToReturn

def createDateTimeForEvent(eventList):
    """Given an event list that doesn't have datetime dictionary entries,
       create a start and end datetime dictionary entries for each event

    Parameters
    ----------
    eventList: list, required
        List of dictionaries of events

    Returns
    -------
    N/A

    """
    for i in range(len(eventList)):
        splitStart = eventList[i]["start"].split(':')
        splitEnd = eventList[i]["end"].split(':')
        eventList[i]["startDateTime"] = datetime.datetime(year=(int)(eventList[i]["year"]),
                                                       month=(int)(eventList[i]["month"]), 
                                                       day=(int)(eventList[i]["day"]), 
                                                       hour=(int)(splitStart[0]), 
                                                       minute=(int)(splitStart[1]))
        eventList[i]["endDateTime"] = datetime.datetime(year=(int)(eventList[i]["year"]),
                                                       month=(int)(eventList[i]["month"]), 
                                                       day=(int)(eventList[i]["day"]), 
                                                       hour=(int)(splitEnd[0]), 
                                                       minute=(int)(splitEnd[1]))

def findCircuit(circuitID, circuits):
    """Given a circuit ID and a list of circuits, find and return the 
       dictionary with the circuit ID

    Parameters
    ----------
    circuitID: str, required
        circuit ID of the circuit to find
    circuits: list, required
        circuits list to find circuitID in

    Returns
    -------
    Dictionary
        Dictionary of found circuit
    """
    for i in range(len(circuits)):
        if(circuitID == circuits[i]['id']):
            return circuits[i]

def findBroadcaster(broadcasterID, broadcasters):
    """Given a broadcaster ID and a list of broadcasters, find and return the 
       dictionary with the broadcaster ID

    Parameters
    ----------
    broadcasterID: str, required
        broadcaster ID of the broadcaster to find
    broadcasters: list, required
        broadcasters list to find broadcasterID in

    Returns
    -------
    List
        List of dictionaries of found broadcaster(s)
    """
    broadcasterList = []
    broadcasterID = broadcasterID.split(',')
    for i in range(len(broadcasters)):
        for j in range(len(broadcasterID)):
            if(broadcasterID[j] == broadcasters[i]['id']):
                broadcasterList = broadcasterList + [broadcasters[i]]
    
    return broadcasterList

def fillDictWithEvents(inputList, events, circuits, broadcasters, dateRangeStart, dateRangeEnd):
    """Given an input list, fill it up with all the required 
       events, circuits, and broadcasters information based on the
       date range given on the command line input

    Parameters
    ----------
    inputList: list, required
        list to be filled out
    events: list, required
        event list to fill out inputDict with
    circuits: list, required
        circuit info list to fill out inputDict with
    broadcasters: list, required
        broadcasters list to fill out inputDict with

    Returns
    -------
    N/A

    """
    zero = datetime.timedelta()

    for i in range(len(events)):
        if(((events[i]['startDateTime'] - dateRangeStart) >= zero) and ((events[i]['startDateTime'] - dateRangeEnd) <= zero)):
            tempDic = {
            'dateStart' : events[i]['startDateTime'],
            'dateEnd' : events[i]['endDateTime'],
            'id' : events[i]['id'],
            'description' : events[i]['description'],
            'circuit' : findCircuit(events[i]['location'], circuits),
            'broadcaster' : findBroadcaster(events[i]['broadcaster'], broadcasters)
                }
            inputList.append(tempDic)

def printEvent(outFile, eventToPrint):
    """Given an output file and an event, print the event to the output file according to the assignment specification

    Parameters
    ----------
    outFile
        The file to print to
    eventToPrint
        The event to print

    Returns
    -------
    N/A

    """
    broadcasterListString = "\n          - " + eventToPrint['broadcaster'][0]['name']
    for i in range(1, len(eventToPrint['broadcaster'])):
        broadcasterListString = broadcasterListString + "\n          - " + eventToPrint['broadcaster'][i]['name']
    
    outFile.write("\n      - id: " + eventToPrint['id'] +
                  "\n        description: " + eventToPrint['description'] +
                  "\n        circuit: " + eventToPrint['circuit']['name'] + " (" + eventToPrint['circuit']['direction'] + ")" +
                  "\n        location: " + eventToPrint['circuit']['location'] +
                  "\n        when: " + eventToPrint['dateStart'].strftime("%I:%M %p - ") + eventToPrint['dateEnd'].strftime("%I:%M %p %A, %B %d, %Y") + " (" + eventToPrint['circuit']['timezone'] + ")" +
                  "\n        broadcasters:" + broadcasterListString)

def printEventList(outFile, inputList):
    """Given an output file and the event list, print the event list to the output file according to the assignment specifications

    Parameters
    ----------
    outFile
        The file to print to
    inputList
        The event list to print

    Returns
    -------
    N/A
    
    """
    if(not inputList):
        return

    outFile.write("\n   - " + inputList[0]['dateStart'].strftime("%d-%m-%Y") + ":")
    printEvent(outFile, inputList[0])

    currentDate = inputList[0]['dateStart']

    for i in range(1, len(inputList)):
        if(not((inputList[i]['dateStart'].year == currentDate.year) and (inputList[i]['dateStart'].month == currentDate.month) and (inputList[i]['dateStart'].day == currentDate.day))):
            outFile.write("\n   - " + inputList[i]['dateStart'].strftime("%d-%m-%Y") + ":")
            currentDate = inputList[i]['dateStart']
        printEvent(outFile, inputList[i])

def createYaml(inputList):
    """Given an event list, create and print the yaml output according to the assignment specifications

    Parameters
    ----------
    inputList
        The event list to create an output yaml file out of

    Returns
    -------
    N/A
    
    """
    outputFile = open("output.yaml", "w")
    outputFile.write("events:")

    printEventList(outputFile, inputList)

    outputFile.close()

def main():
    """The main entry point for the program.
    """
    # Calling a dummy function to illustrate the process in Python
    #print('Hi! from:', sys.argv[0])
    givenArgs = extractArgs()

    broadcasters = parseFile('broadcasters', givenArgs["broadcasters"])
    circuits = parseFile('circuits', givenArgs["circuits"])
    events = parseFile('events', givenArgs["events"])

    createDateTimeForEvent(events)

    events.sort(key = operator.itemgetter("startDateTime"))

    yamlList = []
    fillDictWithEvents(yamlList, events, circuits, broadcasters, givenArgs['start'], givenArgs['end'])

    createYaml(yamlList)
    

if __name__ == '__main__':
    main()
