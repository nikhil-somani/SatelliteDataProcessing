class SatelliteData:
    def __init__(self):
        self.queue = []
    
    #stores an element at the front of queue
    #must be implemented in O(1)
    def InsertAtFront(self, e):
        self.queue = [e] + self.queue  
    
    #removes an element fromt the front of queue
    #must be implemented in O(1)
    def RemoveFront(self):
        return self.queue.pop(0)
    
    #store an element at the end of the queue
    #must be implemented in O(1)
    def InsertAtEnd(self, e):
        self.queue.append(e)
    
    #remove an element at the end of the queue
    #must be implemented in O(1)
    def RemoveEnd(self):
        res = self.queue[-1]
        self.queue = self.queue[:-1]
        return res
    
    #get data from ith locatiom
    def Get(self, i):
        return self.queue[i-1]
    
    #sorts the data, O(nlog n)
    def Sort(self):
        self.queue = sorted(self.queue)
    
    #returns the number of element in queue , O(1)
    def Count(self):
        return len(self.queue)
    
    #returns capacity of queue, O(1)
    def Capacity(self):
        return 9999999
    
    #retuns entire data as list
    def GetAll(self):
        return self.queue
 
    
class SatelliteUtility:
    def __init__(self, filename):
        
        self.filename = filename
        #store instance for each satellite
        self.satellites = []
        #store all data from file to this list
        self.allLines = []
        
    #instance must be initialised with a filename
    #filename represents the file containining data
    # to be processed
    
   
    def ReadData(self):
        fp = open(self.filename, 'r')
        lines = fp.readlines()
        for line in lines:
            self.allLines.append(line)
            
    def ProcessData(self):
        self.ReadData()
        for aLine in self.allLines:
            #parse the lines to get data from S A D
            # stores data for respective satellite
            s, a, d = [x for x in aLine.split(" ")]
            # print(s, a, d) 
            flag = 0
            # print(self.satellites)
            for satellite in self.satellites:
                if s == satellite[0]:
                    flag = 1
                    satelliteData = satellite[1]
                    if a == 'I':
                        satelliteData.InsertAtEnd(int(d))
                                          
                    elif a == 'D':
                        if int(d) == 0:
                            rem = satelliteData.RemoveFront()
                        elif int(d) == 1:
                            rem = satelliteData.RemoveEnd()
                break
            if flag == 0:
                t = SatelliteData()
                t.InsertAtFront(int(d))
                self.satellites.append([s, t])  
                # print(t.queue)  
                # print(self.satellites)                
        
    def GetSummary(self):
        # returns a list of  tuples where each tuple shows
        # a satellite with number of data for each entry 
        # for example: [(1,100),(2,200)] shows 2 satellites
        # 1 and 2 pass 100 and 200 data elements, respectively
        result = []
        for satellite in self.satellites:
            
            result.append((int(satellite[0]), satellite[1].Get(0) ))
        return result
    
    
def main():
    print("Welcome to satellite Data Processing Department")
    print("We are processing your data right now ........")
    print("..... ")
    dp = SatelliteUtility('Satellite Processing/test.txt')
    # file name should be paramterised as per the folder and content
    dp.ProcessData()
    print(dp.GetSummary())
    
        
if __name__ == '__main__':
    main()
