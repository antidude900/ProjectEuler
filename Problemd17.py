# Dictionaries that map numbers to their word equivalents
numbers = {0: "", 1: " One", 2: " Two", 3: " Three", 4: " Four", 5: " Five", 6: " Six", 7: " Seven", 8: " Eight", 9: " Nine"}

# Mapping for numbers 10-19 (other 20-29,30-39 and so on follows tens+ones for eg: 25=twenty(tens) five(ones) but 10-19 doesn't. so making seperate dictionary for it)
teens = {10: " Ten", 11: " Eleven", 12: " Twelve", 13: " Thirteen", 14: " Fourteen", 15: " Fifteen", 16: " Sixteen", 17: " Seventeen", 18: " Eighteen", 19: " Nineteen"}

# Mapping for tens multiples (20, 30, ..., 90)
tens = {20: " Twenty", 30: " Thirty", 40: " Forty", 50: " Fifty", 60: " Sixty", 70: " Seventy", 80: " Eighty", 90: " Ninety"}


# Function to convert a number into its word equivalent
def num_to_words(n):
    # If the number is less than 10, it means we are dealing with a single-digit number.
    # So, we directly return its corresponding word from the 'numbers' dictionary.
    if n < 10:
        return numbers[n]
    
    # If the number is between 10 and 19, it means it falls within the "teens" group.
    # Numbers in this range have unique names, so we return the word from the 'teens' dictionary.
    elif n < 20:
        return teens[n]
    
    # If the number is a multiple of 10 and less than 100, it means we are dealing with a round "tens" number.
    # We can directly return its word from the 'tens' dictionary, as there are no ones to handle (e.g., 20, 30).
    elif n < 100 and n % 10 == 0:
        return tens[n]
    
    # If the number is less than 100 but not a multiple of 10, we are dealing with both a "tens" part and a "ones" part.
    # Here, n // 10 gives the tens part, and n % 10 gives the remainder (ones part).
    # For example, if n = 45:
    # - n // 10 = 4 (which corresponds to "Forty"),
    # - n % 10 = 5 (which corresponds to "Five"),
    # Hence, the result is "Forty Five".
    elif n < 100:
        return tens[10 * (n // 10)] + numbers[n % 10]
    
    # If the number is less than 1000, it means we have at least a "hundreds" place.
    # We split the number into the hundreds part using n // 100, and convert the remainder (n % 100) recursively.
    # For example, if n = 345:
    # - n // 100 = 3 (which corresponds to "Three"),
    # - n % 100 = 45 (which is recursively converted to "Forty Five").
    # The final result is "Three Hundred Forty Five".
    elif n < 1000:
        return numbers[n // 100] + " Hundred" + num_to_words(n % 100)
    
    # If the number is less than 1 million, it means we are dealing with thousands.
    # We extract the thousands part using n // 1000, and handle the remainder (n % 1000) recursively.
    # For example, if n = 12,345:
    # - n // 1000 = 12 (which is recursively converted to "Twelve"),
    # - n % 1000 = 345 (which is recursively converted to "Three Hundred Forty Five").
    # The final result is "Twelve Thousand Three Hundred Forty Five".
    elif n < 1000000:
        return num_to_words(n // 1000) + " Thousand" + num_to_words(n % 1000)
    
    # If the number is less than 1 billion, it means we are dealing with millions.
    # We extract the millions part using n // 1000000, and recursively process the remainder (n % 1000000).
    # For example, if n = 23,456,789:
    # - n // 1000000 = 23 (which is recursively converted to "Twenty Three"),
    # - n % 1000000 = 456,789 (which is recursively converted to "Four Hundred Fifty Six Thousand Seven Hundred Eighty Nine").
    # The final result is "Twenty Three Million Four Hundred Fifty Six Thousand Seven Hundred Eighty Nine".
    elif n < 1000000000:
        return num_to_words(n // 1000000) + " Million" + num_to_words(n % 1000000)
    
    # If the number is 1 billion or more, it means we are dealing with billions.
    # We extract the billions part using n // 1000000000, and recursively process the remainder (n % 1000000000).
    # For example, if n = 1,234,567,890:
    # - n // 1000000000 = 1 (which corresponds to "One"),
    # - n % 1000000000 = 234,567,890 (which is recursively converted to "Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety").
    # The final result is "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety".
    else:
        return num_to_words(n // 1000000000) + " Billion" + num_to_words(n % 1000000000)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(num_to_words(n).strip()) #we have spaces ahead of all strings in the dictinoary. so they string which comes at first will also have spaces ahead
									   #and when comparing to the answer, it wont match. so removing the leading and trailing whitespaces

"""
for doing the original question of project euler, 
just iterate through the string we got after conversion and count the number of letters 
"""
