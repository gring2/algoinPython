def quicksort(lst, low, high):
    if high-low <1 : return

    ##다음에 조건이 맞을 경우 스왑할 대상의 인덱스
    nextSwap = low
    pivotIndex = low

    ## 기준값 보다 비교값이 작을 경우에만 nextSwap을 이동시키기 때문에 비교값과 교체되는 nextSwap의 값은
    ## 기준값보다 크거나 비교값 그 자신이 된다. 이것으로 인해 정렬의 정합성이 확보.
    ##반복문이 끝나면 nextSwap의 오른쪽은 pivotValue보다 큰 값 왼쪽은 작은값이 위치하게됨.


    for i in range(low+1, high+1):
        if lst[i] < lst[pivotIndex]:
            nextSwap += 1
            lst[i], lst[nextSwap] = lst[nextSwap], lst[i]

    ##반복문 끝나면 해당 스왑 위치로 기준값을 이동
    ##그렇기 때문에 nextSwap과 pivotValue를 스왑하게되면 pivotValue를 기준으로 값이 정렬된다.
    lst[nextSwap], lst[pivotIndex] = lst[pivotIndex], lst[nextSwap]

    ## nextSwap은 기준값의 자기 위치를 가리킨다.
    ##기준값 왼쪽
    quicksort(lst, low, nextSwap-1)
    #기준값 오른쪽
    quicksort(lst, nextSwap+1, high)

test = [6,9,4,10,1]

    ##,2,7,3,5,8]

##quicksort(test,0,9)
##print(test)

import random
def quick_second(lst,start,end):
    if end-start <= 0:return
    pivot = random.randrange(start, end)

    ##기준 기준값의 인덱스는 스타트 지점으로
    lst[start], lst[pivot]= lst[pivot], lst[start]
    pivotIndex = start

    ##기준값보다 낮으면 왼쪽으로 패스
    ##아니면 그자리 그대로

    for i in range(start+1, end+1):
        if lst[i] < lst[pivotIndex]:
            lst.insert(pivotIndex,lst[i])
            del lst[i+1]
            pivotIndex +=1
    ##기준값 왼쪽
    quick_second(lst, start, pivotIndex-1)
    #기준값 오른쪽
    quick_second(lst, pivotIndex+1, end)

quick_second(test,0,4)
print(test)




def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


##반복문 구현은 좀 구린것 같다
def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       ##왼쪽부터 중심값보다 값이 작고 오른쪽 인덱스보다 인덱스가 작을때까지 이동
       ## 값이 기준값보다 크다면 해당 값을 이동 시켜야하는 페어가 오른쪽에 존재
       ##인덱스가 초과하면 중심값의 위치(오른쪽 인덱스의 위치)를 찾은 것
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       ##위와 같은 조건
       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       ##값 이동
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   ##기준값 위치  찾기
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
