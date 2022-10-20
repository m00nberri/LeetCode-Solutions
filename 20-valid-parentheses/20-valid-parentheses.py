class Solution:
    def isValid(self, s: str) -> bool:
        
        storage = []
        
        valid = {'()','{}','[]'}
        
        for c in s:
            if storage == []:
                storage.append(c)
            else:
                checkList = ''.join((storage[-1],c))
                if checkList in valid:
                    storage.pop()
                else:
                    storage.append(c)
        
        if storage == []:
            return True
        else:
            return False