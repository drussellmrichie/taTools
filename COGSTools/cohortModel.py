"""
Russell Richie
https://github.com/drussellmrichie
drussellmrichie@gmail.com

A super quick and dirty implementation of the Cohort Model of word recognition, devised
by William Marslen-Wilson. For example:

http://psycholinguistics.wikifoundry.com/page/The+Cohort+Model+of+Word+Recognition

This was written to be readable with minimal Python knowledge. Hence no example is defined
in a `def main()` chunk, nor is there a `if __name__ == "__main__" chunk at the end.

This version uses simpler code to make the behavior of the model more transparent, but the
presence of side effects (print statements) may make it harder to reason about the 
modularity of the implementation.

1) Describe the cohort model in terms of Marr's three levels. One or two sentences per 
level will suffice.

2) What is the Big-O complexity of this model's runtime, in terms of the number of words 
in EnglishWords? In terms of the number of letters in word? You may be able to answer 
these questions by analyzing the code, but you can also run the model with different sized
inputs to get the answer.

3) If the cohort model is an accurate model of human word recognition, then what 
empirical predictions does a Big-O runtime make of human performance? (Example answer: 
People with larger lexicons should take longer to recognize words. In particular, people's
reaction time in a word recognition task should scale at same rate as cohortModel.)

4) Discuss the modularity of this model. What information passes between the model and the
broader program? What information does not? Put another way, what information does model
expose, or not?

5) What about the model seems inaccurate or incomplete with respect to human word 
recognition? How might you modify this model to rectify these issues? You can just discuss
this verbally, but do feel free to try implementing some modifications with Python, if you
are so inclined!

"""

def cohortModel(word, EnglishWords):
    soFar = ''                                # when we start listening to a word, we of course haven't heard anything yet, so we'll represent that as an empty string
    activated = list(EnglishWords)            # we'll start by assuming all the words we know are possible
    for letter in word:                       # then start listening to the word letter by letter
        soFar = soFar + letter                # add the newly heard letter to the portion of the word heard so far
        for word in list(activated):          # now look through the candidate words
            if not word.startswith(soFar):    # if the word seen so far is NOT consistent with a word we know
                activated.remove(word)        # remove the word from the candidates
        print("When we've heard '{}' so far, the activated words are:\n{}".format(soFar,activated))
    print("After hearing everything, the only activated word(s): {}".format(activated))
    return activated

# Test the cohort model with a fragment of English
EnglishWords = ['cathedral', 'cat','dog','catheter']
word = 'cathedral'
cohortModel(word, EnglishWords)
