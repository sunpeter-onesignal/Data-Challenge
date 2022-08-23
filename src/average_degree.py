import sys
            

def main(inputFile, outputFile):
    """
        This program will run through each tweet in the
        inputFile and calculate the average degree of
        hashtag. 
        
        What you have to do is figure out how to read the tweets from the input files,
        calculate the average degree of each hashtag and write the output to the outputFile.
    """

    print('Input file is: ', inputFile)
    print('Output file is: ', outputFile)
    """
    What you'd need to do:
    - Write logic to pull tweets from input file
    - Write logic to process tweets and calculate the average degree of hashtags
    - Write results to outPutFile
    """
    

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])