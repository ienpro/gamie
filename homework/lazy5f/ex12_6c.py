from itertools import groupby


# Read words.
with open('words.txt') as fp:
    W = [w.strip().lower() for w in fp]


# Dict of {longest word we know currently --> construction sequence}
X0 = dict(i=[''], a=[''])

# Iterate list of words by length.
for _, Wn in groupby(sorted(W, key=lambda w: len(w)), key=lambda w: len(w)):
    # Dict longest words we can derive based on X0
    X1 = dict()

    # Check each word of length i.
    for w in Wn:
        for i in range(len(w)):
            # Try word made by removing i'th character.
            w1 = w[:i] + w[i + 1:]
            if w1 in X0:
                # Record word and construction sequence!
                X1[w] = [w1] + X0[w1]
                break
    
    # Check if there are no more words that are longer than words in X0.
    if not X1:
        break
    
    # Set a new word list as current.
    X0 = X1

# Print out words we found.
for w, R in X0.items():
    print(len(w), w, ' '.join(R))
