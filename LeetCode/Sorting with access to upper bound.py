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
    # Sort the scores in O(n) time
    # List with length of hightest Possible Score
    score_counts = [0] * (highest_possible_score+1)
    
    for score in unsorted_scores:
        #store the elements on the index matched with it's value and their total count
        score_counts[score] += 1

    # To store the sorted values
    sorted_scores = []

    # Now go throught each entry of the score_counts list
    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]
        
        # For the number of times the item occurs
        for i in range(count):
            # Add to the sorted list
            sorted_scores.append(score)

    return sorted_scores
    
