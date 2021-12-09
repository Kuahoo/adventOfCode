#!/usr/bin/python3
import sys
import os

FILENAME = 'input1000.txt'


class Solution(object):
    def readBinaryDiagnostics(inputList):
        """
        :type list: list
        :rtype: int
        """
        countOnesArray = Solution.countBits(inputList)

        gammaBinary = Solution.calcGammaBinary(countOnesArray)
        epsilonBinary = Solution.calcEpsilonRate(countOnesArray)

        gammaRate = Solution.binaryToDecimal(gammaBinary)
        epsilonRate = Solution.binaryToDecimal(epsilonBinary)

        powerConsumption = gammaRate * epsilonRate
        return powerConsumption

    def countBits(inputList):
        retArray = Solution.initializeNumBitArray(inputList)
        for binaryNumber in inputList:
            for idx in range(0, Solution.getBinaryNumberSize(binaryNumber)):
                if binaryNumber[idx] == '1':
                    retArray[idx] += 1
        return retArray

    def initializeNumBitArray(inputList):
        numBitsArray = []
        binaryNumber = inputList[0]
        binarySize = Solution.getBinaryNumberSize(binaryNumber)
        for idx in range(0, binarySize):
            numBitsArray.append(0)
        return numBitsArray

    def calcGammaBinary(inputArray):
        totalEntries = Solution.getListSize(Solution.readFileFromOS(FILENAME))
        retString = []
        for idx in range(0, len(inputArray)):
            numZeros = totalEntries-inputArray[idx]
            numOnes = inputArray[idx]
            if numOnes >= numZeros:
                retString.append('1')
            else:
                retString.append('0')
        return ''.join(retString)

    def calcEpsilonRate(inputArray):
        retString = []
        gammaBinary = Solution.calcGammaBinary(inputArray)
        for bit in gammaBinary:
            if bit == '1':
                retString.append('0')
            else:
                retString.append('1')
        return ''.join(retString)

    def getListSize(inputList):
        return len(inputList)

    def getBinaryNumberSize(binaryNumber):
        return len(binaryNumber)-1

    def binaryToDecimal(binaryNumber):
        return int(binaryNumber, 2)

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
    fileContent = Solution.readFileFromOS(FILENAME)
    print(Solution.readBinaryDiagnostics(fileContent))


if __name__ == "__main__":
    main()
