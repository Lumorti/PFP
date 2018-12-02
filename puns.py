#! /usr/bin/env python3

import os
import sys

phraseList = []
wordList = {}

wordFolder = "./dicts/"
phraseFolder = "./phrases/"

verbose = 0

# Load a list of phrases by filename, turning each into phonemes
def loadPhrases(filename):

    filename = filename.replace("//", "/")

    with open(filename, "r") as phraseFile:

        currentOrigin = ""

        for line in phraseFile:

            if len(line.strip()) <= 1: continue

            if line[0] == "#":
                currentOrigin = line[1:].strip()
                continue

            fixedLine = line.strip()
            fixedLine = fixedLine.replace(",", " , ")
            fixedLine = fixedLine.replace(".", " . ")
            fixedLine = fixedLine.replace("?", " ? ")
            fixedLine = fixedLine.replace("!", " ! ")
            fixedLine = fixedLine.replace(":", " : ")

            phraseList.append({"origin": currentOrigin, "file": filename, "original": line.strip(), "words": fixedLine.split(), "phonemes": determinePronunciation(fixedLine)})

# Load a phonetic dictionary by filename
def loadWords(filename):

    filename = filename.replace("//", "/")

    with open(filename, "r", errors='replace') as wordFile:

        for line in wordFile:

            if line[0:3] == ";;;" or line.strip() == "": continue

            split = line.upper().split()
            wordList[split[0]] = split[1:]

# Return an array of phonemes, converting using the word list
def determinePronunciation(phrase):

    phonemes = []

    splitPhrase = phrase.upper().split()

    for word in splitPhrase:

        if word in wordList.keys():

            phonemes.append(wordList[word])

        elif word not in [".", "!", "?", ",", ":"]:

            print("unknown word: " + word)
            phonemes.append([])

        else:

            phonemes.append([])

    return phonemes

# Determine the similiarity between two sets of phonemes (0 is none, 1 is partial,  2 is rhyme, 3 is same)
def similiarity(phonemes1, phonemes2):

    shorterLength = min(len(phonemes1), len(phonemes2))

    # Check for same
    if "".join(phonemes1) == "".join(phonemes2):
        return 3

    # Check for rhyme
    i = 1
    same = 0
    while i < shorterLength:

        if phonemes2[len(phonemes2)-i] == phonemes1[len(phonemes1)-i]: same += 1
        else: break
        i += 1

    if (same >= 2) or (same >= 1 and shorterLength <= 2 and len(phonemes1) == len(phonemes2)):
        return 2

    # Check for partial
    if " ".join("phonemes2") in " ".join("phonemes1"):
        return 1

    # Otherwise no similiarity
    return 0

# The main function, generate a list of puns for a word
def generatePuns(word):

    wordPhonemes = determinePronunciation(word)[0]
    punList = []

    for phrase in phraseList:

        j = 0
        while j < len(phrase["phonemes"]):

            phrasePhonemes = phrase["phonemes"][j]
            sim = similiarity(phrasePhonemes, wordPhonemes)
            if (verbose >= 1 and sim >= 1) or verbose >= 2:

                print("comparing " + str(phrase["words"][j]) + " " + str(phrasePhonemes) + " and " + str(word) + " " + str(wordPhonemes) + " returns " + str(sim))

            if sim >= 1:

                punText = phrase["original"].replace(phrase["words"][j], word)
                punText = punText[0].capitalize() + punText[1:]
                pun = {"pun": punText, "similiarity": sim, "origin": phrase["origin"], "file": phrase["file"]}
                punList.append(pun)
                break

            j += 1

    return punList

# Process the arguments passed to the program, returning boolean of whether to continue or not
def processArgs(argsList):

    global verbose

    i = 0
    while i < len(argsList):

        if argsList[i] in ["-h", "--help", "-help", "--h"]:

            print("[word]            generates a list of puns using this word")
            print("-h                print this message")
            print("-d [directory]    specify the dictionary directory")
            print("-p [directory]    specify the phrase directory")
            print("-v                verbose output")
            print("-v2               extra verbose output")
            return False

        elif argsList[i] in ["-w"]:

            if os.path.isdir(argsList[i+1]):

                global wordFolder
                wordFolder = argsList[i+1]

                i += 1

            else: print("ERROR - not a valid directory: " + argsList[i+1])

        elif argsList[i] in ["-p"]:

            if os.path.isdir(argsList[i+1]):

                global phraseFolder
                phraseFolder = argsList[i+1]

                i += 1

            else: print("ERROR - not a valid directory: " + argsList[i+1])

        elif argsList[i] in ["-v"]:

            verbose = 1

        elif argsList[i] in ["-v2"]:

            verbose = 2

        elif "-" in argsList[i]:

            print("ERROR - not a valid argument: " + argsList[i])
            return False

        i += 1

    return True

if __name__ == "__main__":

    # Ensure a word is given
    if len(sys.argv) <= 1:

        print("ERROR - invalid command, use -h for help")
        exit()

    # Process any other arguments
    if not processArgs(sys.argv[1:len(sys.argv)]): exit()

    # Get the word to make puns from
    wordToUse = "".join(sys.argv[len(sys.argv)-1:])
    if len(wordToUse.strip()) <= 1:

        print("ERROR - please specify a word to generate puns from")
        exit()

    # Load the dictionaries
    wordFiles = os.listdir(wordFolder)
    for file in wordFiles: loadWords(wordFolder + "/" + file)

    # Load the phrase lists
    phraseFile = os.listdir(phraseFolder)
    for file in phraseFile: loadPhrases(phraseFolder + "/" + file)

    # Output if verbose mode is specified
    if verbose >= 1:
        print("Loaded " + str(len(wordList)) + " words")
        print("Loaded " + str(len(phraseList)) + " phrases")
        print("Generating puns for: " + wordToUse)

    # Generate puns and output
    puns = generatePuns(wordToUse)
    for pun in puns:
        print(str(pun))
