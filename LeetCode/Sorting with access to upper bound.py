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
    
