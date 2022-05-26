# How can you make this more scalable and reusable later?
import functools

# Take array of numbers
def find_armstrong_numbers(numbers):
    # Initialize empty lists for later usage
    base_list = []
    answer_list = []
    # Loop over the array of numbers
    for x in numbers:
        # We declare the length of the current element
        length_of_numbers = len(str(x))
        # We check if the element is the size of 0 (1 character within the element)
        if length_of_numbers < 2:
            # Add to the base_list list for later looping
            base_list.append(x)
        # Otherwise we go ahead and do extra math depending on the length of the element
        else:
            # This element has more than 1 character within it so now we multiple by the power of the length of the element
            temp_list = list(map(int, str(x)))
            # We store the power of in a list to evaluate
            list2 = list(map(lambda item : item ** length_of_numbers, temp_list))
            # Merge the broken down element (currently an array) back into a single element/character
            list3 = functools.reduce(lambda agg, item : agg + item, list2)
            # Add this merged value to the base_list list
            base_list.append(list3)
    # After processing the entire length of the given array we compare the results to the target number
    for x in range(0, len(numbers), 1):
        # Is the target number equal to the result number in each list?
        if numbers[x] == base_list[x]:
            # Add to the answer list
            answer_list.append(numbers[x])
    # Return the answer list with all the armstrong numbers, otherwise blank
    return answer_list