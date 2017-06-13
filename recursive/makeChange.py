def recMC(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins

##라쿠텐 입사시험과 매우 습사
##캐쉬를 이용해서 반복 작업을 줄임
##http://25programerkari.blogspot.jp/2012/03/github.html


# def recDC(coinValueList,change,knownResults):
def recDC(coinValueList, change, knownResults, usedCoin):
   #최소 코인 초기화
   minCoins = change
   #만약 1코인으로 잔돈이 만들어 진다면 1을 반환
   if change in coinValueList:
      usedCoin[change]=change
      knownResults[change] = 1
      return 1
   #그렇지 않은경우1. 캐쉬되어 있는 결과라면 해당 캐쉬 결과를 반환
   elif knownResults[change] > 0:
      return knownResults[change]
   #처음 계산하는 경우 캐쉬되어 있지 않으므로 계산을 시작
   else:
      #해당 잔돈이하 단위의 동전을 준비
       for i in [c for c in coinValueList if c <= change]:
       #가장 작은 단위의 동전부터 떼어 가면서 계산
       #최악의 경우 ex4; 4->3->2->1 결과 numCoins = 4
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults,usedCoin)
       #계산결과가 초기화 한 값보다 작은 경우, 즉 최소 갯수를 도출해 낸 경우 치환
         if numCoins < minCoins:

            minCoins = numCoins
            usedCoin[change] = i
            knownResults[change] = minCoins
   return minCoins


def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
    ##처음에는 1센트로 계산하여 금액 수대로 카운트
      coinCount = cents
    ##사용한 동전 종류
      newCoin = 1
      innerFor =  [c for c in coinValueList if c <= cents]
      for j in innerFor:
            ##동전 종류에 따른 최소 수 결정
            ##현재 금액에서 사용 가능한 금액을 뺐을 경우의 캐쉬 금액에서 하나(해당 동전 종류)
            ##더하여 최소 종류를 정함
            ##사용 가능한 cent종류는 [1,5]
            ##예 5센트를 1cent권으로 계산했을 경우 5 coinCount
            ##1센트로 5센트를 만드는 것은 4센트(1센트 4개)<5-1>에 1센트를 더하는것
            ##5센트를 5센트로 만드는 것은 0센트(0개)<5-5>에 5센트 1개를 더하는 것

            ##그렇게 해서 최소 코인이 coinCount보다 작을 경우 최소 코인을 카운트로 캐쉬
            ##5 => 1 됨
            minCoin=minCoins[cents-j] + 1
            if minCoin < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)
    result = recDC(clist,amnt,coinCount,coinsUsed)
    print(result)
    printCoins(coinsUsed,amnt)
    # print("Making change for",amnt,"requires")
    # print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    # print("They are:")
    # printCoins(coinsUsed,amnt)
    # print("The used list is as follows:")
    # print(coinsUsed)
main()