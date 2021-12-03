#!/usr/bin/python3
import sys
import os


class Solution(object):
    def countDepth(inputList):
        """
        :type list: list
        :rtype: int
        """

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
    fileContent = Solution.readFile("input6.txt")


if __name__ == "__main__":
    main()
