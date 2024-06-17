def count_range_sum(nums, lower, upper):
    if not nums:
        return 0
    sum_arr = [0] * len(nums)
    sum_arr[0] = nums[0]
    for i in range(1, len(nums)):
        sum_arr[i] = sum_arr[i - 1] + nums[i]
    return process(sum_arr, 0, len(sum_arr) - 1, lower, upper)

def process(sum_arr, L, R, lower, upper):
    if L == R:
        return 1 if lower <= sum_arr[L] <= upper else 0
    M = L + ((R - L) >> 1)
    return process(sum_arr, L, M, lower, upper) + process(sum_arr, M + 1, R, lower, upper) + merge(sum_arr, L, M, R, lower, upper)

def merge(arr, L, M, R, lower, upper):
    ans = 0
    windowL = L
    windowR = L
    for i in range(M + 1, R + 1):
        min_val = arr[i] - upper
        max_val = arr[i] - lower
        while windowR <= M and arr[windowR] <= max_val:
            windowR += 1
        while windowL <= M and arr[windowL] < min_val:
            windowL += 1
        ans += windowR - windowL

    help_arr = [0] * (R - L + 1)
    i = 0
    p1 = L
    p2 = M + 1
    while p1 <= M and p2 <= R:
        if arr[p1] <= arr[p2]:
            help_arr[i] = arr[p1]
            p1 += 1
        else:
            help_arr[i] = arr[p2]
            p2 += 1
        i += 1
    while p1 <= M:
        help_arr[i] = arr[p1]
        i += 1
        p1 += 1
    while p2 <= R:
        help_arr[i] = arr[p2]
        i += 1
        p2 += 1
    for i in range(len(help_arr)):
        arr[L + i] = help_arr[i]
    return ans

# for test
def comparator(arr, lower, upper):
    ans = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if lower <= arr[j] - arr[i] <= upper:
                ans += 1
    return ans

# for test
import random

def generate_random_array(max_size, max_value):
    return [random.randint(-max_value, max_value) for _ in range(random.randint(1, max_size + 1))]

# for test
def copy_array(arr):
    if arr is None:
        return None
    return arr[:]

# for test
def is_equal(arr1, arr2):
    if (arr1 is None and arr2 is not None) or (arr1 is not None and arr2 is None):
        return False
    if arr1 is None and arr2 is None:
        return True
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

# for test
def print_array(arr):
    if arr is None:
        return
    print(" ".join(map(str, arr)))

# for test
def main():
    test_time = 500000
    max_size = 100
    max_value = 100
    print("测试开始")
    for _ in range(test_time):
        arr1 = generate_random_array(max_size, max_value)
        arr2 = copy_array(arr1)
        if count_range_sum(arr1, -50, 50) != comparator(arr2, -50, 50):
            print("Oops!")
            print_array(arr1)
            print_array(arr2)
            break
    print("测试结束")

if __name__ == "__main__":
    main()
