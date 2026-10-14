class TimeMap:

    def __init__(self):
        self.value_dict = collections.defaultdict(list)
        self.time_dict = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.value_dict[key].append(value)
        self.time_dict[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.time_dict.get(key,[])) -1

        while l <= r:
            m = (l+r)//2
            if self.time_dict[key][m] == timestamp:
                return self.value_dict[key][m]

            elif self.time_dict[key][m] > timestamp:
                r = m-1
            else: 
                l = m+1

        return self.value_dict[key][r] if r>=0 else ""



            


        
