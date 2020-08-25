import sys

# python FILE input.txt output.txt 

inputFile = sys.argv[1]

outputFile = sys.argv[2]

def main(inputFile:str,outputFile:str):

    wordStorage = countOccurrences(inputFile=inputFile)

    writeOutputFile(outputFile=outputFile,wordStorage=wordStorage)


def writeOutputFile(outputFile:str,wordStorage:dict):

    fileName = open(f"./{outputFile}","w")

    with fileName as f:

        for word,wordCount in wordStorage.items():

            line = f"{word} {wordCount}\n"

            f.write(line)

        f.close()

    return True



def countOccurrences(inputFile:str):

    if ".txt" not in inputFile:
        print("[-] Input file not accepted because of extension")
        exit()

    fileName = open(f"./{inputFile}","r")

    storage = dict()

    with fileName as f:

        line = f.readlines()

        for e in line:

            wordList = e.split(" ")

            for idx, e in enumerate(wordList):

                if "-" in e:
                    del wordList[idx]
                    cleanWord = e.split("-",2)
                    wordList.extend(cleanWord)
                elif "'" in e:
                    del wordList[idx]
                    cleanWord = e.split("'",2)
                    wordList.extend(cleanWord)

            for w in wordList:

                # Case In-Sensitive
                w = w.lower()
                # Sanitizing Text
                w = w.rstrip()
                # Remove Punctuation
                w = w.replace(".","")
                w = w.replace(",","")
                w = w.replace(";","")
                w = w.replace(":","")
                w = w.replace("!","")
                w = w.replace("?","")

                if w in storage:

                    storage[w] += 1

                else:

                    storage[w] = 1

    storage = dict(sorted(storage.items()))

    del storage[""]

    return storage


if __name__ == "__main__":

    main(inputFile,outputFile)
