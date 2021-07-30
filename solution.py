from typing import List
def twoSum(self, manumber: List[int], lengo: int) -> List[int]:
        dictionary = {}
        answer = []
        
        for i in range(len(manumber)):
            numberTwo = lengo-manumber[i]
            if(numberTwo in dictionary.keys()):
                indexYaPili = manumber.index(numberTwo)
                if(i != indexYaPili):
                    return sorted([i, indexYaPili])
                
            dictionary.update({manumber[i]: i})