# Python3 program to demonstrate
# C-SCAN Disk Scheduling algorithm
from itertools import count


size = 8
disk_size = 200
seek_sequence = []

def CSCAN(arr, head):

	seek_count = 0
	distance = 0
	cur_track = 0
	left = []
	right = []
	seek_sequence.append(head)
    
	# Appending end values
	# which has to be visited
	# before reversing the direction
	left.append(0)
	right.append(disk_size - 1)

	# Tracks on the left of the
	# head will be serviced when
	# once the head comes back
	# to the beggining (left end).
	for i in range(size):
		if (arr[i] < head):
			left.append(arr[i])
		if (arr[i] > head):
			right.append(arr[i])

	# Sorting left and right vectors
	left.sort()
	right.sort()

	# First service the requests
	# on the right side of the
	# head.
	for i in range(len(right)):
		cur_track = right[i]

		# Appending current track
		# to seek sequence
		seek_sequence.append(cur_track)

		# Calculate absolute distance
		distance = abs(cur_track - head)

		# Increase the total count
		seek_count += distance

		# Accessed track is now new head
		head = cur_track

	# Once reached the right end
	# jump to the beggining.
	head = 0

	# adding seek count for head returning from 199 to 0
	seek_count += (disk_size - 1)

	# Now service the requests again
	# which are left.
	for i in range(len(left)):
		cur_track = left[i]

		# Appending current track
		# to seek sequence
		seek_sequence.append(cur_track)

		# Calculate absolute distance
		distance = abs(cur_track - head)

		# Increase the total count
		seek_count += distance

		# Accessed track is now the new head
		head = cur_track

	print("Total number of seek operations =", seek_count, 
    "\nThe average tracks travelled is ", round(seek_count/len(seek_sequence),2))
	print("Seek Sequence is")
	print(*seek_sequence, sep=" => ")

    
# Driver code


# request array
arr = [176, 79, 34, 60,
	92, 11, 41, 114]
head = 50

print("Initial position of head:", head)

CSCAN(arr, head)

for i in range(0,(len(seek_sequence)-1)):
        print(abs(seek_sequence[i]), " to ", abs(seek_sequence[i+1]), "=", abs(seek_sequence[i+1] - abs(seek_sequence[i])))


# This code is contributed by rag2127
