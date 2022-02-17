# Creating an empty dictionary

def minTrips(amount):
  single = [2,3]
  dp=[float('inf')]*(amount+1)
  dp[0]=0
  for i in range(1,amount+1):
        for s in single:
            if i-s>=0:
                dp[i]=min(dp[i],1+dp[i-s])
  return -1 if dp[amount]==float('inf') else dp[amount]

def minimumTripstoDeliver():
  freq = {}
  trips = 0
  weights = [3,4,4,1]
  for items in weights:
    freq[items] = weights.count(items)
  for key in freq:
    trips = trips + minTrips(freq[key])
  print(trips)

minimumTripstoDeliver()
