#test automation tasks start and end are logged
# what is the max number of test machines needed, at what time

def find_max_tasks(arr, exit):
    arr = sorted(arr)
    exit = sorted(exit)
    tasks_in = 1
    max_tasks = 1
    curr_time = arr[0]
    i = 1
    j = 0
    while i < len(arr) and j < len(exit):
        if arr[i] <= exit[j]:
            tasks_in += 1
            if tasks_in > max_tasks:
                max_tasks = tasks_in
                curr_time = arr[i]
            i += 1
        else:
            tasks_in -= 1
            j += 1

    return max_tasks, curr_time

arr = [1, 3, 5, 7, 9]
# exit = [4, 4, 8, 8, 10]
exit = [4, 5, 12, 9, 12]
print find_max_tasks(arr, exit)