#!/usr/bin/python3
import sys
import os


class Solution(object):
    def countDepth(inputList):
        """
        :type list: list
        :rtype: int
        """
        print(len(inputList))
        retCount = 0
        if len(inputList) == 1:
            return retCount
        elif len(inputList) >= 2:
            for x in range(0, len(inputList)-1):
                curr = inputList[x]
                next = inputList[x+1]
                if int(curr) < int(next):
                    retCount += 1
            return retCount

    def depthWindowSum(inputList, currIndex):
        sumOfDepths = 0
        depth1 = int(inputList[currIndex])
        depth2 = int(inputList[currIndex+1])
        depth3 = int(inputList[currIndex+2])
        sumOfDepths = depth1 + depth2 + depth3
        return sumOfDepths

    def countDepthWindow(inputList):
        """
        :type list: list
        :rtype: int
        """
        retCount = 0
        if len(inputList) <= 3:
            return retCount
        elif len(inputList) > 3:
            for x in range(0, len(inputList)-3):
                sumOfDepths1 = Solution.depthWindowSum(inputList, x)
                sumOfDepths2 = Solution.depthWindowSum(inputList, x+1)
                if sumOfDepths1 < sumOfDepths2:
                    retCount += 1
            return retCount

    def readFile(inputFile):
        with open(inputFile) as f:
            read_data = f.readlines()
            # print((read_data))
        f.closed
        print(read_data)
        return read_data

    def readFileFromOS(fileName):
        with open(os.path.join(sys.path[0], fileName), "r") as f:
            read_data = f.readlines()
        f.closed
        return read_data

    def readFileRando(fileName):
        with open(fileName) as input:
            read_data = [int(line.strip()) for line in input]
        input.closed
        print(read_data)
        return read_data


def main():
    # inputFile = sys.argv[1]
    fileContent = Solution.readFile("input2000.txt")
    print(Solution.countDepth(fileContent))
    print(Solution.countDepthWindow(fileContent))


if __name__ == "__main__":
    main()
