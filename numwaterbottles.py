class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        count = 0
        
        empty_bottles = 0
        while numBottles + empty_bottles >= numExchange:
            count += numBottles 
            empty_bottles += numBottles
            numBottles = empty_bottles // numExchange
            empty_bottles = empty_bottles % numExchange
            
        
        count += numBottles 
               
        return count
         #### numWaterBottles


         class Solution(object):
        def minSteps(self,s1, s2):
     
            count = 0
 
    
            char_count = [0] * 26
     
            for i in range(26):
              char_count[i] = 0
 
    
            for i in range(len( s1)):
               char_count[ord(s1[i]) -
                   ord('a')] += 1
 
    
            for i in range(len(s2)):
                char_count[ord(s2[i]) - ord('a')] -= 1
         
            for i in range(26):
                if char_count[i] != 0:
                    count += abs(char_count[i])
            return count / 2
