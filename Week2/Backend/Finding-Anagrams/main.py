# Check if two words are anagrams 
# Example:

def find_anagram(word, anagram):
    if sorted(word) == sorted(anagram):
        return True
    else:
        return False

print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))

