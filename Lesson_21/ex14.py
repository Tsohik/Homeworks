#Write a function that capitalizes the first letter of each word in a sentence.
def capitalize_first_letter(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    result = ' '.join(capitalized_words)
    return result


sentence = "hello world, this is a test."
capitalized_sentence = capitalize_first_letter(sentence)
print(capitalized_sentence)
