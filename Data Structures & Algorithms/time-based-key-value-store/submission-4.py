
'''
class TimeMap:


    def __init__(self):
        self.timeMap = {} #key= string, value = list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None: # O(1) approach    
        # 1: ["alice", "happy"],
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value,timestamp])
        
    def get(self, key: str, timestamp: int) -> str: # From O(n) to O(log n) binary approach
        res = ""    
        values = self.timeMap.get(key, []) # the [] is becuz if the key doesn't exist in the hashmap

        #binary search
        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
'''



 

'''
 {
    "alice": [[1, "happy"], [3,"sad"]]
    "bob": [[1,"crazy"], [2,"angry"]]
 }
'''


class TimeMap:
    def __init__(self):
        self.store= defaultdict(list) # "key": {["happy",value]}

    def set(self, key:str, value: str, timestamp: int) ->None:
        self.store[key].append([value, timestamp])
    
    def get(self, key:str, timestamp: int) -> str:
        if not self.store[key]:
            return ""
        else:
            values= self.store[key]
        l, r = 0, len(values)-1
        res=""

        while l <=r:
            mid = (l+r)//2
            if(values[mid][1] <= timestamp):
                res=values[mid][0]
                l=mid+1
            else:
                r=mid-1

        return res


            
    
























































