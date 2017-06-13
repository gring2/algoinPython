def shellSort(alist):
    ##갭
    sublistcount = len(alist)//2
    ##갭이 1이되면 전체 삽입정렬을 통해서 정렬을 완료 시킬수 있다
    while sublistcount > 0:

      ##갭보다 작을때 까지 시작 지점을 1씩 올려가면서 sublist를 만들어 삽입정렬
      ##갭보다 커지면 이전 sublist와 중복 됨
      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)
      ##갭을 줄여나가면서 sublist를 만듬
      sublistcount = sublistcount // 2

##삽입정렬 시행부
def gapInsertionSort(alist,start,gap):
    tempArray = []

    for i in range(start, len(alist),gap):
        tempArray.append(alist[i])

    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue
    print("gap is",gap,"sorted sublist is ",tempArray)
alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)

