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

#Function for calculating tracks
def FCFS(jobArray, head):

    totalTracks = 0;
    currentTrack = 0;
    distance = 0;

    for i in range(0,numJobs):
        currentTrack = jobArray[i];

        #calculating for distance between head and current track
        distance = abs(currentTrack - head);

        #total tracks is a collection of added distances
        totalTracks += distance;

        #change head into current track
        head = currentTrack;

    #display total tracks
    print ("The total tracks travelled is " + str(totalTracks) + ".");

    #display track sequence including head
    for i in range(0,numJobs):
        trackSeq.append(jobArray[i]);

    print("Order of execution: " + str(trackSeq));
        

FCFS(trackArray, startingTrack);