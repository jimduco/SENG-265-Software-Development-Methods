#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define MAX_LINE_LEN 200
#define MAX_EVENTS 1000

/*
    An event struct that will hold the required information in an event.
    These required informations are:
        description, timezone, location
        day, month, year, dweek, start, end
    Inside the event struct is a 'struct tm'
    Event handles: description, timezone, location, start, end
    struct tm date handles: day, month, year, dweek
*/
struct event{
    struct tm date;
    struct tm timeEnd;
    char description[MAX_LINE_LEN];
    char timezone[MAX_LINE_LEN];
    char location[MAX_LINE_LEN];
};

/*
    Function: extractDateFromArgs
    Description: takes a string of a calendar date (intended to be taken from command line input)
                 and converts it to integers present in an struct calendarDate
    Inputs: 
        - stringDate: A string that contains a calendar date made up of char to be converted
        - tangibleDate: a struct calendarDate to be filled out with the corresponding coverted
                        calendar date from stringDate. Modifies the passed in struct calendarDate
    Output: void
*/
void extractDateFromArgs(char stringDate[], struct tm* tangibleDate){

    char cutoff0[2]= "=";
    char cutoff1[2] = "/";
    char* token;

    token = strtok(stringDate, cutoff0);

    token = strtok(NULL, cutoff1);
        tangibleDate->tm_year = atoi(token) - 1900;
    token = strtok(NULL, cutoff1);
        tangibleDate->tm_mon = atoi(token) - 1;
    token = strtok(NULL, cutoff1);
        tangibleDate->tm_mday = atoi(token); 
}

/*
    Function: extractFileNameFromArgs
    Description: takes a string of a calendar date (intended to be taken from command line input)
                 and converts it to integers present in an struct calendarDate
    Inputs: 
        - stringDate: A string that contains a calendar date made up of char to be converted
        - tangibleDate: a struct calendarDate to be filled out with the corresponding coverted
                        calendar date from stringDate. Modifies the passed in struct calendarDate
    Output: void
*/
void extractFileNameFromArgs(char fileNameArg[], char fileNameString[]){

    char cutoff[2]= "="; //need to cutoff at the '=' from the taken command line input
    char* token;

    token = strtok(fileNameArg, cutoff);

    token = strtok(NULL, cutoff);
        strcpy(fileNameString, token);
}

/*
    Function: processDescription
    Description: Fills out an event's description, given a pointer to an event
    Inputs: 
        - eventToFill: a pointer to the event to be modified
        - token: a token to be used for the strtok() function
        - cutoff0: the first token to be used, ">"
        - cutoff1: the second token to be used, "</"
        - inpFile: a FILE* variable to access the given file
    Output: void
*/
void processDescription(struct event* eventToFill, char* token, char cutoff0[], char cutoff1[], FILE* inpFile){

    char buffer[100];

    fgets(buffer, 100, inpFile); //gets to line of description

    token = strtok(buffer, cutoff0);
    token = strtok(NULL, cutoff1);
    strcpy(eventToFill->description, token);
    strcat(eventToFill->description, "\0");
}

/*
    Function: processTimezone
    Description: Fills out an event's timezone, given a pointer to an event
    Inputs: 
        - eventToFill: a pointer to the event to be modified
        - token: a token to be used for the strtok() function
        - cutoff0: the first token to be used, ">"
        - cutoff1: the second token to be used, "</"
        - inpFile: a FILE* variable to access the given file
    Output: void
*/
void processTimezone(struct event* eventToFill, char* token, char cutoff0[], char cutoff1[], FILE* inpFile){

    char buffer[100];

    fgets(buffer, 100, inpFile); //gets to line of timezone

    token = strtok(buffer, cutoff0);
    token = strtok(NULL, cutoff1);
    strcpy(eventToFill->timezone, token);
    strcat(eventToFill->timezone, "\0");
}

/*
    Function: processLocation
    Description: Fills out an event's location, given a pointer to an event
    Inputs: 
        - eventToFill: a pointer to the event to be modified
        - token: a token to be used for the strtok() function
        - cutoff0: the first token to be used, ">"
        - cutoff1: the second token to be used, "</"
        - inpFile: a FILE* variable to access the given file
    Output: void
*/
void processLocation(struct event* eventToFill, char* token, char cutoff0[], char cutoff1[], FILE* inpFile){

    char buffer[100];

    fgets(buffer, 100, inpFile); //gets to line of location

    token = strtok(buffer, cutoff0);
    token = strtok(NULL, cutoff1);
    strcpy(eventToFill->location, token);
    int length = strlen(eventToFill->location);
    eventToFill->location[length] = '\0';
}

/*
    Function: processDay
    Description: Fills out an event's day, given a pointer to an event
    Inputs: 
        - eventToFill: a pointer to the event to be modified
        - token: a token to be used for the strtok() function
        - cutoff0: the first token to be used, ">"
        - cutoff1: the second token to be used, "</"
        - inpFile: a FILE* variable to access the given file
    Output: void
*/
void processDay(struct event* eventToFill, char* token, char cutoff0[], char cutoff1[], FILE* inpFile){

    char buffer[100];

    fgets(buffer, 100, inpFile); //gets to line of day

    token = strtok(buffer, cutoff0);
    token = strtok(NULL, cutoff1);
    eventToFill->date.tm_mday = atoi(token);
}

/*
    Function: processMonth
    Description: Fills out an event's month, given a pointer to an event
    Inputs: 
        - eventToFill: a pointer to the event to be modified
        - token: a token to be used for the strtok() function
        - cutoff0: the first token to be used, ">"
        - cutoff1: the second token to be used, "</"
        - inpFile: a FILE* variable to access the given file
    Output: void
*/
void processMonth(struct event* eventToFill, char* token, char cutoff0[], char cutoff1[], FILE* inpFile){

    char buffer[100];

    fgets(buffer, 100, inpFile); //gets to line of month

    token = strtok(buffer, cutoff0);
    token = strtok(NULL, cutoff1);
    eventToFill->date.tm_mon = atoi(token) - 1;
}

/*
    Function: processYear
    Description: Fills out an event's year, given a pointer to an event
    Inputs: 
        - eventToFill: a pointer to the event to be modified
        - token: a token to be used for the strtok() function
        - cutoff0: the first token to be used, ">"
        - cutoff1: the second token to be used, "</"
        - inpFile: a FILE* variable to access the given file
    Output: void
*/
void processYear(struct event* eventToFill, char* token, char cutoff0[], char cutoff1[], FILE* inpFile){

    char buffer[100];

    fgets(buffer, 100, inpFile); //gets to line of year

    token = strtok(buffer, cutoff0);
    token = strtok(NULL, cutoff1);
    eventToFill->date.tm_year = atoi(token) - 1900;
}

/*
    Function: convertWeekdayStringToInt
    Description: Given a string representation of a week day, return
                 its integer representation. (0-6: Sunday-Saturday)
    Inputs: 
        - weekday: week day string to convert to an int
    Output:
        - int: integer representation of the given weekday
*/
int convertWeekdayStringToInt(char weekday[]){

    char monday[]="Monday";
    char tuesday[]="Tuesday";
    char wednesday[]="Wednesday";
    char thursday[]="Thursday";
    char friday[]="Friday";
    char saturday[]="Saturday";
    char sunday[]="Sunday";

    if(strcmp(weekday, sunday)==0){
        return 0;
    } else if(strcmp(weekday, monday)==0){
        return 1;
    }else if(strcmp(weekday, tuesday)==0){
        return 2;
    }else if(strcmp(weekday, wednesday)==0){
        return 3;
    }else if(strcmp(weekday, thursday)==0){
        return 4;
    }else if(strcmp(weekday, friday)==0){
        return 5;
    }else if(strcmp(weekday, saturday)==0){
        return 6;
    }else{
        return 7;
    }
}

/*
    Function: processWeekday
    Description: Fills out an event's weekday, given a pointer to an event
    Inputs: 
        - eventToFill: a pointer to the event to be modified
        - token: a token to be used for the strtok() function
        - cutoff0: the first token to be used, ">"
        - cutoff1: the second token to be used, "</"
        - inpFile: a FILE* variable to access the given file
    Output: void
*/
void processWeekday(struct event* eventToFill, char* token, char cutoff0[], char cutoff1[], FILE* inpFile){

    char buffer[100];

    fgets(buffer, 100, inpFile); //gets to line of weekday

    token = strtok(buffer, cutoff0);
    token = strtok(NULL, cutoff1);

    char weekday[15];
    strcpy(weekday, token);
    strcat(weekday, "\0");

    int weekdayInt = convertWeekdayStringToInt(weekday);
    eventToFill->date.tm_wday = weekdayInt;
}

/*
    Function: processStartTime
    Description: Fills out an event's start time, given a pointer to an event
    Inputs: 
        - eventToFill: a pointer to the event to be modified
        - token: a token to be used for the strtok() function
        - cutoff0: the first token to be used, ">"
        - cutoff1: the second token to be used, "</"
        - inpFile: a FILE* variable to access the given file
        - cutoff2: the third token to be used, ":"
    Output: void
*/
void processStartTime(struct event* eventToFill, char* token, char cutoff0[], char cutoff1[], FILE* inpFile, char cutoff2[]){

    char buffer[100];

    fgets(buffer, 100, inpFile); //gets to line of time start

    token = strtok(buffer, cutoff0);
    token = strtok(NULL, cutoff2);
    eventToFill->date.tm_hour = atoi(token);
    token = strtok(NULL, cutoff1);
    eventToFill->date.tm_min = atoi(token);
}

/*
    Function: processEndTime
    Description: Fills out an event's start time, given a pointer to an event
    Inputs: 
        - eventToFill: a pointer to the event to be modified
        - token: a token to be used for the strtok() function
        - cutoff0: the first token to be used, ">"
        - cutoff1: the second token to be used, "</"
        - inpFile: a FILE* variable to access the given file
        - cutoff2: the third token to be used, ":"
    Output: void
*/
void processEndTime(struct event* eventToFill, char* token, char cutoff0[], char cutoff1[], FILE* inpFile, char cutoff2[]){

    char buffer[100];

    fgets(buffer, 100, inpFile); //gets to line of time start

    token = strtok(buffer, cutoff0);
    token = strtok(NULL, cutoff2);
    eventToFill->timeEnd.tm_hour = atoi(token);
    token = strtok(NULL, cutoff1);
    eventToFill->timeEnd.tm_min = atoi(token);
}

/*
    Function: processEvent
    Description: reads lines from an event section and extracts the required
                 event data.
    Inputs: 
        - eventToBeFilled: A pointer to an event struct to be filled out by the
         function.
        - inpFile: A pointer to the FILE opened by processFile
    Output: void
*/
void processEvent(struct event* eventToBeFilled, FILE* inpFile){

    char buffer[100];

    char cutoff0[2]= ">";
    char cutoff1[3] = "</";
    char cutoff2[2] = ":";
    char* tokenToUse;

    processDescription(eventToBeFilled, tokenToUse, cutoff0, cutoff1, inpFile);
    processTimezone(eventToBeFilled, tokenToUse, cutoff0, cutoff1, inpFile);
    processLocation(eventToBeFilled, tokenToUse, cutoff0, cutoff1, inpFile);
    processDay(eventToBeFilled, tokenToUse, cutoff0, cutoff1, inpFile);
    processMonth(eventToBeFilled, tokenToUse, cutoff0, cutoff1, inpFile);
    processYear(eventToBeFilled, tokenToUse, cutoff0, cutoff1, inpFile);
    processWeekday(eventToBeFilled, tokenToUse, cutoff0, cutoff1, inpFile);
    processStartTime(eventToBeFilled, tokenToUse, cutoff0, cutoff1, inpFile, cutoff2);
    processEndTime(eventToBeFilled, tokenToUse, cutoff0, cutoff1, inpFile, cutoff2);

    fgets(buffer, 100, inpFile); //takes care of </event>
}

/*
    Function: processFile
    Description: opens and reads an .xml file and decides whether an event
                 should be processed based on whether or not it is in the
                 date range. Passes to processEvent
    Inputs: 
        - eventArray: An array to hold all the events processed
        - fileName: string of the file name
    Output:
        - int: # of events processed
*/
int processFile(struct event eventArray[], char fileName[]){

    FILE* inputFile = fopen(fileName, "r");

    char buffer[100];
    char eventSignifier[]= "    <event>\n";
    char calendarEndSignifier[] = "</calendar>";

    fgets(buffer, 100, inputFile);//takes care of <calendar>

    int eventArrayIndex = 0;
    
    while((strcmp(fgets(buffer, 100, inputFile), eventSignifier)) == 0){
        processEvent(&eventArray[eventArrayIndex], inputFile);
        eventArrayIndex++;
    }

    fclose(inputFile);

    return eventArrayIndex;
}

/*
    Function: comparator
    Description: Comparator function used for qsort(). Compares date and time
                 between two events. Earlier events go first.
    Inputs: 
        - event1: pointer to an event to be compared with event2
        - event2: pointer to an event to be compared with event1
    Output: 
        - integer: <0 if event1 should be before event2
                    0 if they are equivalent
                   >0 if event1 should be after event2
    Comparator function declaration based off: https://www.geeksforgeeks.org/comparator-function-of-qsort-in-c/
*/
int comparator(const void* event1, const void* event2){

    int yearDiff = (((struct event*)event1)->date.tm_year) - (((struct event*)event2)->date.tm_year);

    if(yearDiff == 0){
        int monDiff = (((struct event*)event1)->date.tm_mon) - (((struct event*)event2)->date.tm_mon);

        if(monDiff == 0){
            int dayDiff = (((struct event*)event1)->date.tm_mday) - (((struct event*)event2)->date.tm_mday);

            if(dayDiff == 0){
                int hourDiff = (((struct event*)event1)->date.tm_hour) - (((struct event*)event2)->date.tm_hour);

                    if(hourDiff == 0){
                        int minDiff = (((struct event*)event1)->date.tm_min) - (((struct event*)event2)->date.tm_min);

                        if(minDiff == 0){
                            return 0;
                        }else{
                            return minDiff;
                        }

                    }else{
                        return hourDiff;
                    }

            }else{
                return dayDiff;
            }

        }else{
            return monDiff;
        }

    }else{
        return yearDiff;
    }
}

/*
    Function: dateCompare
    Description: Compare function that Compares struct tms' dates ONLY.
    Inputs: 
        - date1: a date to be compared with date2
        - date2: a date to be compared with date1
    Output: 
        - integer: <0 if date1 should be before date2
                    0 if they are equivalent
                   >0 if date1 should be after date2
*/
int dateCompare(struct tm date1, struct tm date2){
    
    if((date1.tm_year - date2.tm_year) == 0){
        if((date1.tm_mon - date2.tm_mon) == 0){
            if((date1.tm_mday - date2.tm_mday) == 0){
                return 0;
            }else{
                return (date1.tm_mday - date2.tm_mday);
            }
        }else{
            return (date1.tm_mon- date2.tm_mon);
        }
    }else{
        return (date1.tm_year - date2.tm_year);
    }
}

/*
    Function: printEvent
    Description: Takes a pointer to an event and prints it to stdout
    Inputs: 
        - eventToPrint: pointer to an event to print
    Output: void
*/
void printEvent(struct event* eventToPrint){

    char buffer[MAX_LINE_LEN];

    struct tm* ptrToDate = &(eventToPrint->date);
    strftime(buffer, MAX_LINE_LEN,"%I:%M %p", ptrToDate);
    printf("%s to ", buffer);
    struct tm* ptrToTimeEnd = &(eventToPrint->timeEnd);
    strftime(buffer, MAX_LINE_LEN,"%I:%M %p", ptrToTimeEnd);

    printf("%s: %s {{%s}} | %s", buffer, eventToPrint->description, eventToPrint->location, eventToPrint->timezone);
}

/*
    Function: printDate
    Description: Takes a pointer to an event and prints the date to stdout
    Inputs: 
        - eventToPrint: pointer to an event to print its date
    Output: void
*/
void printDate(struct event* eventDateToPrint){

    char buffer[MAX_LINE_LEN];
    struct tm* ptrToDate = &(eventDateToPrint->date);
    strftime(buffer, MAX_LINE_LEN,"%B %d, %Y (%A)", ptrToDate);
    printf("%s\n", buffer);

    int charCount = 0;
    while(buffer[charCount] != '\0'){
        printf("-");
        charCount++;
    }
    printf("\n");
}

/*
    Function: printEventList
    Description: Takes a pointer to an event array and uses other print functions to
                 output it to stdout.
    Inputs: 
        - listToPrint: event array to print
        - listSize: size of the event array
        - dateRangeStart: a struct tm containing the start date taken from the comman line input
        - dateRangeEnd: a struct tm containing the end date taken from the comman line input
    Output: void
*/
void printEventList(struct event listToPrint[], int listSize, struct tm dateRangeStart, struct tm dateRangeEnd){

    int arrayIndexToStartFrom = 0;
    int startChecker = 0;
    while(startChecker == 0){
        if((dateCompare(listToPrint[arrayIndexToStartFrom].date, dateRangeStart)) < 0){
            arrayIndexToStartFrom++;
        }else{
            startChecker = 1;
        }
        if(arrayIndexToStartFrom == listSize){
            startChecker = 2;
        }
    }

    int arrayIndexToEndOn = listSize - 1;
    int endChecker = 0;
    while(endChecker == 0){
        if((dateCompare(listToPrint[arrayIndexToEndOn].date, dateRangeEnd)) > 0){
            arrayIndexToEndOn--;
        }else{
            endChecker = 1;
        }
        if(arrayIndexToEndOn == -1){
            endChecker = 2;
        }
    }

    if(startChecker == 2 || endChecker == 2){
        return;
    }

    printDate(&(listToPrint[arrayIndexToStartFrom]));
    struct event currentDate = listToPrint[arrayIndexToStartFrom];
    printEvent(&(listToPrint[arrayIndexToStartFrom++]));
    if(arrayIndexToStartFrom != arrayIndexToEndOn + 1){
            printf("\n");
        }

    for(arrayIndexToStartFrom; arrayIndexToStartFrom < arrayIndexToEndOn + 1; arrayIndexToStartFrom++){
        if((dateCompare(currentDate.date, listToPrint[arrayIndexToStartFrom].date) == 0)){
            printEvent(&(listToPrint[arrayIndexToStartFrom]));
            if(arrayIndexToStartFrom != arrayIndexToEndOn){
                printf("\n");
            }
        }else{
            printf("\n");
            printDate(&(listToPrint[arrayIndexToStartFrom]));
            currentDate = listToPrint[arrayIndexToStartFrom];
            printEvent(&(listToPrint[arrayIndexToStartFrom]));
            if(arrayIndexToStartFrom != arrayIndexToEndOn){
                printf("\n");
            }
        }
    }
    return;
}

/*
    Function: main
    Description: represents the entry point of the program.
    Inputs: 
        - argc: indicates the number of arguments to be passed to the program.
        - argv: an array of strings containing the arguments passed to the program.
    Output: an integer describing the result of the execution of the program:
        - 0: Successful execution.
        - 1: Erroneous execution.
*/
int main(int argc, char *argv[])
{
    /* Starting calling your own code from this point. */
    // Ideally, please try to decompose your solution into multiple functions that are called from a concise main() function.

    //Command Line Input Checking -- Following code based off of lab-03 code
    if (argc < 4) {
        printf("usage: %s --start=<start date> --end=<end date> --file=<file name>\n", argv[0]);
        exit(1);
    }

    //initialize empty struct calendarDate startDate and endDate. These two calendarDates will signify the range of dates to scan in
    struct tm startDate; //empty start date struct
    struct tm endDate;   //empty end date struct
    extractDateFromArgs(argv[1], &startDate); //startDate filled with the start date info
    extractDateFromArgs(argv[2], &endDate);   //endDate filled with the end date info

    char fileToScan[50];
    extractFileNameFromArgs(argv[3], fileToScan); //extracts file name from command line input

    struct event eventList[MAX_EVENTS];

    int eventCount = processFile(eventList, fileToScan); //processes the file and fills out eventList. Also counts the number of events processed.

    qsort(eventList, eventCount, sizeof(struct event), comparator); //sorts eventList in chronological order

    printEventList(eventList, eventCount, startDate, endDate); //prints the event list

    exit(0);
}