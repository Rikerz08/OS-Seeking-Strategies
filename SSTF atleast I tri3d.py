#Getting input for starting track and track numbers
numJobs = int(input("How many jobs are to be processed? "));
startingTrack = int(input("Input head: "));

#Array for jobs
trackArray = [];

#Array for displaying track sequence including the head
trackSeq = [];
trackSeq.append(startingTrack);

#For loop for inputting jobs into array
for i in range(0,numJobs):
    element = int(input("Enter job track #" + str(i+1) + ":"));
    trackArray.append(element);

#Array for differences
diffArray = [];

#Function for calculating difference
def SSTF(jobArray, head):
    #Instantiating vars to be used
    leastDiff = 999999;
    currentDiff = 999999;
    targetNum = None;

    for i in range(0,numJobs):
        #TargetNum for the changing of "head" to be compared with other numbers in trackArray
        if targetNum == None:
            targetNum = head;
        else:
            jobArray.remove(targetNum);
        print("HELLO");
        print(targetNum);
        j = 0;
        while True:
            #Current difference by subtracting next element with the current one
            currentDiff = abs(jobArray[j] - targetNum);

            #Establishing the least diff thru iterative comparison
            if currentDiff < leastDiff:
                leastDiff = currentDiff;
                #Storing the number that will be the track to be compared on
                targetNum = jobArray[j];
            
            j += 1;

            #Add the new track to the track sequence
            if j == (len(jobArray)-1):
                trackSeq.append(targetNum);
                break;


SSTF(trackArray, startingTrack)
print(trackSeq);
print(trackArray);

[27,45,60,29]
[30]