def sort_scores(unsorted_scores, highest_possible_score):         
    # Sort the scores in O(n) time
    if len(unsorted_scores) > 1:
        mid = len(unsorted_scores)//2
        left_arr = unsorted_scores[:mid]
        right_arr = unsorted_scores[mid:]
        
        sort_scores(left_arr, highest_possible_score)
        sort_scores(right_arr, highest_possible_score)
    
        i, j, k = 0, 0, 0
        
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                unsorted_scores[k] = right_arr[j]
                j += 1
            else:
                unsorted_scores[k] = left_arr[i]
                i += 1
            k += 1
            
        while i < len(left_arr):
            unsorted_scores[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            unsorted_scores[k] = right_arr[j]
            j += 1
            k += 1
            
    return unsorted_scores
