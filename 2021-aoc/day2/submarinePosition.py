#!/usr/bin/python3
import sys
import os


class Solution(object):
    def readInstructions(inputList):
        """
        :type list: list
        :rtype: int
        """
        horizontal = 0
        depth = 0
        for entry in inputList:
            direction, distance = entry.split()
            if direction == "forward":
                horizontal += int(distance)
            if direction == "down":
                depth += int(distance)
            if direction == "up":
                depth -= int(distance)
        finalPosition = horizontal*depth
        return finalPosition

    def readFile(inputFile):
        with open(inputFile) as f:
            read_data = f.readlines()
            # print((read_data))
        f.closed
        # print(read_data)
        return read_data

    def readFileFromOS(fileName):
        with open(os.path.join(sys.path[0], fileName), "r") as f:
            read_data = f.readlines()
        f.closed
        return read_data


def main():
    fileContent = Solution.readFile("input1000.txt")
    print(Solution.readInstructions(fileContent))

if __name__ == "__main__":
    main()
