def solution(numbers, k):
    idx = 2 * (k - 1)
    idx = idx % len(numbers)
    return numbers[idx]