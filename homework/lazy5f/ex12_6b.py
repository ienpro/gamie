"""
Recording word construction sequence as well.
"""


# Read words.
with open('words.txt') as fp:
    W = [w.strip().lower() for w in fp]

# Prepare Wn[i] that is list of words of length i.
max_len = max(len(w) for w in W)
Wn = [[] for _ in range(max_len + 1)]
for w in W:
    Wn[len(w)].append(w)

# Dict of {longest word we know currently --> construction sequence}
X0 = dict(i=[''], a=[''])

# Iterate each list of words of length i.
for i in range(2, max_len + 1):
    # Dict longest words we can derive based on X0
    X1 = dict()
    
    # Check each word of length i.
    for w in Wn[i]:
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
