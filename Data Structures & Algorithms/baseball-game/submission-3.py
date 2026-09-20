class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        score_card = []
        for i in range(len(operations)):
            curr_element = operations[i]
            if curr_element == '+':
                score_card.append(score_card[-1] + score_card[-2])
            elif curr_element == 'D':
                score_card.append(2 * score_card[-1])
            elif curr_element == 'C':
                score_card.pop()
            else:
                score_card.append(int(curr_element))
        
        return sum(score_card)