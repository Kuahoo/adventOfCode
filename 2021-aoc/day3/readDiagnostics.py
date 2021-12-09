#!/usr/bin/python3
import sys
import os


class Solution(object):
    def readDiagnostics(inputList):
        """
        :type list: list
        :rtype: int
        """
        totalEntries = Solution.getListSize(inputList)
        
        for binaryNumber in inputList:
            for bit in binaryNumber:
                pass

    def getListSize(inputList):
        return len(inputList)

    def getBinaryNumberSize(binaryNumber):
        return len(binaryNumber)-1

    def initializeNumBitArray(inputList):
        numBitsArray = []
        binaryNumber = inputList[0]
        binarySize = Solution.getBinaryNumberSize(binaryNumber)
        for i in range(0, binarySize):
            numBitsArray.append(0)
        return numBitsArray

    def readFile(inputFile):
        with open(inputFile) as f:
            read_data = f.readlines()
        f.closed
        # print(read_data)
        return read_data

    def readFileFromOS(fileName):
        with open(os.path.join(sys.path[0], fileName), "r") as f:
            read_data = f.readlines()
        f.closed
        return read_data


def main():
    fileContent = Solution.readFileFromOS("input12.txt")

if __name__ == "__main__":
    main()
