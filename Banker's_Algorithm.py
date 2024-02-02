'''
A program was implemented to follow the banker algorithm.
To run the program it is necessary to edit the matrices directly on the code.
All of the matrices that need to be edited will be in the first 6 lines of the code.
Additionally when  dealing with a request line 70 will need to be updated to reflect what process will perform the request.
'''
import numpy as np
Allocation = np.array([[0, 0, 1, 2], [1, 0, 0, 0], [1, 3, 5, 4], [0, 6, 3, 2], [0, 0, 1, 4]])
Max = np.array([[0, 0, 1, 2], [1, 7, 5, 0], [2, 3, 5, 6], [0, 6, 5, 2], [0, 6, 5, 6]])
Total_Available = [3, 14, 12, 12]
Request = [1, 0, 0, 1]


def determine_need(allocation, max):
    need = np.subtract(max, allocation)
    return need


def determine_available(allocation, total):
    total_allocated = []
    for i in range(allocation.shape[1]):
        sum = np.sum(allocation[:, i])
        total_allocated.append(sum)
    available = np.subtract(total, total_allocated)
    return available


def safety(allocation, need, available):
    m = allocation.shape[0]
    n = allocation.shape[1]
    work = available
    finish = np.zeros(n, dtype=bool)

    while True:
        x = -1
        for i in range(allocation.shape[1]):
            if finish[i] == 0 and all(need[i, :] <= work):
                x = i
                break
        if x == -1:
            break

        work = work + allocation[x, :]
        finish[x] = 1

    return all(finish)


def resource_request(request, need, available, allocation, process):
    if any(request > need[process, :]):
        print("Error: process has exceeded its maximum claim.")
        return 0
    if any(request > available):
        print("Process must wait since resources are not available")
        return 0
    available = np.subtract(available, request)
    allocation[process, :] = allocation[process, :] + request
    need[process, :] = need[process, :] - request
    if safety(allocation, need, available):
        print("New state is safe, request can be granted")
    else:
        print("Process must wait since new state is unsafe")
    return 0


Need = determine_need(Allocation, Max)
Available = determine_available(Allocation, Total_Available)
if safety(Allocation, Need, Available):
    print("The system is currently in a safe state")
else:
    print("The system is in an unsafe state")

print("Need Matrix: ")
print(str(np.array2string(Need)))
print("Available Matrix: " + str(np.array2string(Available)))
resource_request(Request, Need, Available, Allocation, 2)
