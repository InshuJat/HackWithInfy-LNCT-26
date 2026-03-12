class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        


        if sum(gas) < sum(cost):
            return -1
        
        total_tank = 0
        current_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            net_gain = gas[i] - cost[i]
            current_tank = current_tank + net_gain
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0
                
        return start_index