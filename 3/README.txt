The Assignment consisted of applying smoothing to find the probability of a sentence occurring, given a large corpus. Smoothing includes - 

1. Laplace Smoothing
2. Laplace Smoothing with Interpolation
3. Good Turing Smoothing
4. Good Turing Smoothing with Interpolation

Directory Structure - 

Assignment3_201301109/
|-- English
|   |-- english_smoothing.py
|   `-- token_generator.py
|-- Hindi
|   |-- hindi_smoothing.py
|   `-- token_generator.py
`-- README.txt
`-- Report.pdf

<language>_smoothing.py contains the main code that runs the four smoothing algorthms on the toy data. It imports the relevant unigram, bigram and trigram dictionaries, and their lengths. These dictionaries were generated using my tokenizer implemented on the previous assignment, but can't be added because of memory constraints. The folders also contain token_generator.py which does the job of tokenizing the lines in the test data into unigrams, bigrams and trigrams as required. 

Report.pdf contains a report on the code, pipeline, and the results for the four algorithms on the both the languages.

