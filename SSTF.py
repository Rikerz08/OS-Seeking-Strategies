tracksTravelled = []

def SSTF(head, sequence):
    totalTracks = 0
    tracksTravelled.append(head)
    for i in range(len(sequence)):
        near_num = sequence[
            min(range(len(sequence)), key=lambda i: abs(sequence[i] - head))
        ]
        if head >= near_num:
            difference = head - near_num
            totalTracks += difference
            head = near_num
        if head <= near_num:
            difference = near_num - head
            totalTracks += difference
            head = near_num
        sequence.remove(near_num)
        tracksTravelled.append(near_num)
    print("Order of tracks travelled : 	", end="")
    for i in tracksTravelled:
        if i == tracksTravelled[len(tracksTravelled) - 1]:
            print(i)
        else:
            print(i, ",", end="")
    return totalTracks


if __name__ == "__main__":
    diskNumber = int(input("Enter the number of disks:	"))
    if diskNumber > 0:
        head = int(input("Enter initial header position : 	"))
        while not head in range(diskNumber + 1):
            head = int(input("Please enter valid initial head position :"))
        sequence = []
        sequence = list(map(int, input("Enter the sequence : 	").split()))
        for i in sequence:
            if i < 0 or i > diskNumber:
                print("Sequence out of range")
                exit(0)

        totalTracks = SSTF(head, sequence)
        print("Total number of tracks is : ", totalTracks)
        print("The average tracks travelled is ", totalTracks/len(tracksTravelled))
        print("Head  Path      Tracks Travelled");
        for i in range(0,(len(tracksTravelled)-1)):
            print(tracksTravelled[i], " to ", tracksTravelled[i+1], "    ", tracksTravelled[i+1] - tracksTravelled[i])