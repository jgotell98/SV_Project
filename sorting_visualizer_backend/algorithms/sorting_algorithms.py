import time

def bubble_sort(arr):
    steps = []
    explanations = []
    n = len(arr)
    array = arr.copy()

    for i in range(n):
        for j in range(0, n-i-1):
            explanation = f"Comparing {array[j]} and {array[j+1]}."
            if array[j] > array[j+1]:
                explanation += f" Swapping {array[j]} and {array[j+1]} because {array[j]} > {array[j+1]}."
                array[j], array[j+1] = array[j+1], array[j]
            else:
                explanation += f" No swap needed because {array[j]} ≤ {array[j+1]}."
            
            steps.append(array.copy())
            explanations.append(explanation)

    return steps, explanations


def insertion_sort(arr):
    steps = []
    explanations = []
    array = arr.copy()

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        explanation = f"Inserting {key}. Comparing with elements on its left."

        while j >= 0 and key < array[j]:
            explanation += f" Moving {array[j]} to the right because {key} < {array[j]}."
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key
        explanation += f" Inserting {key} at position {j + 1}."
        steps.append(array.copy())
        explanations.append(explanation)

    return steps, explanations


def quick_sort(arr):
    steps = []
    explanations = []

    def partition(array, low, high):
        pivot = array[high]
        explanation = f"Choosing pivot {pivot}."
        i = low - 1

        for j in range(low, high):
            explanation += f" Comparing {array[j]} with pivot {pivot}."
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                explanation += f" Swapping {array[i]} and {array[j]} because {array[j]} < pivot."
        
        array[i + 1], array[high] = array[high], array[i + 1]
        explanation += f" Swapping {array[i + 1]} and pivot {pivot} to finalize partition."

        steps.append(array.copy())
        explanations.append(explanation)
        return i + 1

    def quick_sort_recursive(array, low, high):
        if low < high:
            pi = partition(array, low, high)
            quick_sort_recursive(array, low, pi - 1)
            quick_sort_recursive(array, pi + 1, high)

    quick_sort_recursive(arr.copy(), 0, len(arr) - 1)
    return steps, explanations


def merge_sort(arr):
    steps = []
    explanations = []

    def merge(left, right):
        merged = []
        explanation = f"Merging {left} and {right}. "
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                explanation += f"Adding {left[i]} because it's smaller than {right[j]}. "
                i += 1
            else:
                merged.append(right[j])
                explanation += f"Adding {right[j]} because it's smaller than {left[i]}. "
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, explanation

    def merge_sort_recursive(array):
        if len(array) <= 1:
            return array, ""

        mid = len(array) // 2
        left, left_exp = merge_sort_recursive(array[:mid])
        right, right_exp = merge_sort_recursive(array[mid:])

        merged, merge_exp = merge(left, right)
        steps.append(merged.copy())
        explanations.append(f"{left_exp} {right_exp} {merge_exp}")

        return merged, merge_exp

    sorted_array, _ = merge_sort_recursive(arr.copy())
    return steps, explanations

