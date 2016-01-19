For the English dataset and one of Hindi or Telugu -

1. Compute the co-occurrence matrix using top 250 words from corpus as feature words.
2. Implement K-Means algorithm to cluster the words into 50 groups using embeddings from step 1.
3. Display a list of 25 words per group which are closer to its centroid.

You have to do three experiments -
  1. With removing stop words from 250 feature words
  2. Without removing stop words from 250 feature words
  3. With taking top 50 most occurring unigrams as stop words and not including them as feature words.

The list of hindi and english stop words has been uploaded. List of telugu stop words shall be uploaded shortly.

Deliverables -
  Code for computing Co-occurrence embeddings.
  Code for implementing K-Means clustering.
  Report containing observations on clusters created and difficulties faced along with how they were handled.
  A README file explaining how to run the codes.

Points to note -
  - The data provided has been extracted from the datasets provided in Assignment 1.
    Hence you have to tokenize them first using the tokenizer implemented as a part of assignment 1.
  - Pre - existing libraries for implementing K-Means algorithm are not allowed like sklearn etc.

Deadline - 12 p.m 1st September 
