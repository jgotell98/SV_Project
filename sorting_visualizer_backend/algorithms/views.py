from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .sorting_algorithms import bubble_sort, insertion_sort, quick_sort, merge_sort

@csrf_exempt
def sort_array(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            array = data.get('array')
            algorithm = data.get('algorithm')

            if not array or not algorithm:
                return JsonResponse({'error': 'Array or algorithm not provided'}, status=400)

            # Sorting logic based on selected algorithm
            if algorithm == 'bubble_sort':
                steps, explanations = bubble_sort(array)
            elif algorithm == 'insertion_sort':
                steps, explanations = insertion_sort(array)
            elif algorithm == 'merge_sort':
                steps, explanations = merge_sort(array)
            elif algorithm == 'quicksort':
                steps, explanations = quick_sort(array)
            else:
                return JsonResponse({'error': 'Invalid sorting algorithm'}, status=400)

            # Return the sorted steps as JSON
            return JsonResponse({"steps": steps, "explanations": explanations})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


