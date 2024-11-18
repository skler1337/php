def disemvowel(string):
    vowels = "aeiouAEIOU"
    return "".join(filter(lambda char: char not in vowels, string))

print(disemvowel("This website is for losers LOL!")) 
