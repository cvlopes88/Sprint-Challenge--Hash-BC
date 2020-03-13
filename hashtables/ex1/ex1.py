#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    new_answer = []
    Answer = (new_answer)
    """
    YOUR CODE HERE
    """
    # weights = [12, 10, 11, 6, 9]
    # length = len(weights)
    # limit = 21
    
    # for weight_1 in weights:
    #     for weight_2 in weights:
    #         if weight_1 + weight_2 < limit:
    #             weight_1 = weight_2
    #             weight_2 += 1
                
    #         elif weight_1 + weight_2 == limit:
    #             another_answer = (weight_1, weight_2)
    #             new_answer.append(another_answer)
    #         else: 
    #             print(f"trying")    
    # return Answer
    for index in range(length):
        diference = limit - weights[index]
        if hash_table_retrieve(ht, diference) is not None:
            i = index
            b = hash_table_retrieve(ht, diference)
            if i > b:
                return (i, b)
            else:
                return (b, i)

    return None
    
def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

new_weights = [10, 1, 11, 12, 8]
print(get_indices_of_item_weights(new_weights, 5, 21))

