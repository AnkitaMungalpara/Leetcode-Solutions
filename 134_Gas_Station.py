"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Solution:
Time Complexity: O(N)
Space Complexity: O(1)

"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        current, total = 0, 0
        index = 0

        for i in range(len(gas)):
            current += gas[i] - cost[i]
            total += gas[i] - cost[i]

            if current < 0:
                current = 0
                index = i + 1 

        return index if total >= 0 else -1