'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # Break the word into an array of letters
    arr = list(word)
    # If the array is empty return zero
    if not arr:
        return 0
    # If the array is greater than one
    elif len(arr) > 1:
        # If the zero index is 't' and the one index is 'h'
        if arr[0] == "t" and arr[1] == "h":
            # Add the occurence of 'th'
            return 1 + count_th("".join(arr[1:]))
        else:
            return 0 + count_th("".join(arr[1:]))
    else:
        return 0
