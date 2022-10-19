def maxNum(head, sequence):
    for i in sequence:
        if i > head:
            return i


def minNum(head, sequence):
    for i in range(len(sequence) - 1, -1, -1):
        if sequence[i] < head:
            return sequence[i]

seekSequence = []

def CLOOK(N, head, sequence):
    
    stopCondition = minNum(head, sequence)
    seekOperations = 0
    seekSequence.append(head)
    nearNum = maxNum(head, sequence)
    for i in range(len(sequence)):
        if nearNum > head:
            difference = nearNum - head
            seekOperations += difference
            head = nearNum
            seekSequence.append(head)
            nearNum = maxNum(head, sequence)
            if head == stopCondition:
                break
        if head == max(sequence):
            difference = head - min(sequence)
            head = min(sequence)
            nearNum = maxNum(head, sequence)
            seekOperations += difference
            seekSequence.append(head)
    print("Seek Sequence : 	", end=" ")
    for i in seekSequence:
        if i == stopCondition:
            print(i)
        else:
            print(i, " ==> ", end=" ")
    return seekOperations


if __name__ == "__main__":
    numberDisk = int(input("Enter the number of disks:	"))
    if numberDisk > 0:
        head = int(input("Enter initial header position : 	"))
        while not head in range(numberDisk + 1):
            head = int(input("Please enter valid initial head position :"))
        sequence = []
        sequence = list(map(int, input("Enter the sequence : 	").split()))
        sequence.sort()
        if min(sequence) < 0 or max(sequence) > numberDisk:
            print("Sequence out of range")
            exit(0)

        seekOperations = CLOOK(numberDisk, head, sequence)
        print("Total number of seek operations : ", seekOperations)
        
        print("The average tracks travelled is ", round(seekOperations/len(seekSequence),2))
        print("Head  Path       Tracks Travelled");
        for i in range(0,(len(seekSequence)-1)):
            print(abs(seekSequence[i]), " to ", abs(seekSequence[i+1]), "         =", abs(seekSequence[i+1] - abs(seekSequence[i])))

