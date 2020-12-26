'''
#This question is taken from the course Interview cake: 
https://www.interviewcake.com/question/python3/top-scores?course=fc1&section=sorting-searching-logarithms
You created a game that is more popular than Angry Birds.
Each round, players receive a score between 0 and 100, which you use to rank them from highest to lowest. 
So far you're using an algorithm that sorts in O(n\lg{n})O(nlgn) time, but players are complaining that their 
rankings aren't updated fast enough. You need a faster sorting algorithm.
Write a function that takes:
a list of unsorted_scores
the highest_possible_score in the game
and returns a sorted list of scores in less than O(n\lg{n})O(nlgn) time.
For example:
  unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100
# Returns [91, 89, 65, 53, 41, 37]
sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
'''

def sort_scores(unsorted_scores, highest_possible_score):         
    # Sort the scores in O(nlogn) time
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
