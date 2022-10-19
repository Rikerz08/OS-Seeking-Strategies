seekSeq = []
def max_num(head, sequence):
    for i in sequence:
        if i > head:
            return i


def min_num(head, sequence):
    for i in range(len(sequence) - 1, -1, -1):
        if sequence[i] < head:
            return sequence[i]

def SCAN(N, head, sequence):
    old_head = head
    seekOps = 0
    seekSeq.append(head)
    nearNum = max_num(head, sequence)
    for i in range(len(sequence)):
        if nearNum > head:
            difference = nearNum - head
            seekOps += difference
            head = nearNum
            seekSeq.append(head)
            nearNum = max_num(head, sequence)
        elif nearNum < head:
            difference = head - nearNum
            seekOps += difference
            head = nearNum
            seekSeq.append(head)
            nearNum = min_num(head, sequence)
            if head == min(sequence):
                break
        if head == max(sequence):
            nearNum = min_num(old_head, sequence)
            difference = (N - 1 - head) + (N - 1 - nearNum)
            seekOps += difference
            head = nearNum
            seekSeq.append(head)
            nearNum = min_num(head, sequence)
    print("Seek Sequence : 	", end=" ")
    for i in seekSeq:
        if i == min(seekSeq):
            print(i)
        elif i == max(sequence):
            print(i, " ==> ", N - 1, " ==> ", end=" ")
        else:
            print(i, " ==> ", end=" ")
    return seekOps


if __name__ == "__main__":
    Number_disk = int(input("Enter the number of disks:	"))
    if Number_disk > 0:
        head = int(input("Enter initial header position : 	"))
        while not head in range(Number_disk + 1):
            head = int(input("Please enter valid initial head position :"))
        sequence = []
        sequence = list(map(int, input("Enter the sequence : 	").split()))
        sequence.sort()
        if min(sequence) < 0 or max(sequence) > Number_disk:
            print("Sequence out of range")
            exit(0)

        seekOps = SCAN(Number_disk, head, sequence)
        print("Total number of seek operations : ", seekOps)
        print("The average tracks travelled is ", seekOps/len(seekSeq))
        print("Head  Path       Tracks Travelled");
        for i in range(0,(len(seekSeq)-1)):
            print(abs(seekSeq[i]), " to ", abs(seekSeq[i+1]), "=", abs(seekSeq[i+1] - abs(seekSeq[i])))

