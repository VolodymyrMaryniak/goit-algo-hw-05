import random


def binary_search_upper_limit(arr: list[float], target: float) -> tuple[int, float]:
    if not arr:
        return (0, None)

    if target > arr[-1]:
        return (0, None)

    if target <= arr[0]:
        return (0, arr[0])

    # Now we know that target is between arr[0] and arr[-1]
    low = 1
    high = len(arr) - 1

    iteration = 0
    while True:
        iteration += 1
        mid = (high + low) // 2

        if target > arr[mid]:
            low = mid + 1
            continue

        if target <= arr[mid - 1]:
            high = mid - 1
            continue

        # Otherwise target is between arr[mid - 1] and arr[mid]
        return (iteration, arr[mid])


def main():
    arr = sorted([round(random.uniform(0.0, 99.9), 1) for _ in range(25)])
    target = round(random.uniform(0.0, 99.9), 1)

    print("Array: ", arr)
    print("Target: ", target)

    (iteration, upper_limit) = binary_search_upper_limit(arr, target)

    if upper_limit is None:
        print("Upper limit does not exist. Count of iterations: ", iteration)
        return

    print("Upper limit is: ", upper_limit, " Count of iterations: ", iteration)


if __name__ == "__main__":
    main()
