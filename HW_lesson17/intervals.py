def sum_of_intervals(intervals):
    sort_intervals = sorted(intervals, key=lambda x: x[0])
    arr_total = []
    cumulative_intersect_arr = list(sort_intervals[0])
    for index in range(1, len(sort_intervals)):
        if cumulative_intersect_arr[1] >= sort_intervals[index][0]:
            if cumulative_intersect_arr[1] < sort_intervals[index][1]:
                cumulative_intersect_arr[1] = sort_intervals[index][1]
        else:
            arr_total.append(cumulative_intersect_arr)
            cumulative_intersect_arr = list(sort_intervals[index])
    arr_total.append(cumulative_intersect_arr)
    return sum(max(i) - min(i) for i in arr_total)





print(sum_of_intervals([(1, 5)]))
print(sum_of_intervals([(1, 5), (6, 10)]))
print(sum_of_intervals([(1, 5), (1, 5)]))
print(sum_of_intervals([[1, 4], [7, 10], [3, 5]]))
print(sum_of_intervals([[1, 5], [10, 20], [1, 6], [16, 19], [5, 11], [21, 22], [22, 23], [40, 41]]))
print(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]))
print(sum_of_intervals([(-1_000_000_000, 1_000_000_000)]))
