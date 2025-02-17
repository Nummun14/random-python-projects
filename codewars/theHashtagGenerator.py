def generate_hashtag(s):
    words = s.split()
    hashtag = "#"
    for word in words:
        upper = word[0].upper() + word[1:].lower()
        hashtag += upper
    if len(hashtag) > 140 or words == []:
        return False
    return hashtag


print(generate_hashtag("Codewars"))

