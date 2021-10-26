# Function to find a pair in an array with a given sum using hashing
def pair_search(arr, sum_value):
    # create an empty dictionary
    dict_store = {}
    # do for each element
    for i, e in enumerate(arr):
        # check if pair (e, sum_value - e) exists
        # if the difference is seen before, print the pair
        if sum_value - e in dict_store:
            x = arr[dict_store.get(sum_value - e)], arr[i]
            print("Pair found", x)
            return
        # store index of the current element in the dictionary
        dict_store[e] = i
    # No pair with the given sum exists in the list
    print("Sorry, no pair found")


if __name__ == '__main__':
    Arr_test = [8, 7, 2, 5, 3, 1]
    sum_value_test = 10

    pair_search(Arr_test, sum_value_test)
