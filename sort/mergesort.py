def merge(lst, low, mid, high):

    ##해당 부분 배열 만큼의 빈 배열 준비
    tmp = [0]*(high-low+1)
    i = low
    j = mid+1

    ##머지 배열 인덱스
    k=0
    ##중간을 기준으로 해당 배열을 반으로 나눔
    ##작은 값부터 임시 배열에 저장
    while (i <=mid and j<=high):
        if(lst[i] <lst[j]):
            tmp[k] = lst[i]
            i +=1
            k +=1
        else:
            tmp[k] = lst[j]
            j+=1
            k+=1
     ##남은값 저장
    while i <= mid:
        tmp[k] = lst[i]
        i += 1
        k +=1
    while j <= high:
        tmp[k] = lst[j]
        j += 1
        k +=1
        ##임시배열 대로 원 배열에서 해당 부분 배열을 변경
    for i in range(high-low+1):
        lst[i+low] = tmp[i]

##부분 배열로 쪼개서 삽입정렬
def mergesort(lst,low,high):
    if high - low <1 : return

    mid = int((low+high)/2)
    ##왼쪽으로 쪼개기
    mergesort(lst,low,mid)
    ##오른쪽으로 쪼개기
    mergesort(lst,mid+1,high)
    ##다 쪼갰으면 합쳐 올라가기
    merge(lst, low, mid, high)




##test = [10,6,8,5,60]##,55,4,3,2,1]

##mergesort(test,0,4)

##print(test)

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        ## 해당 반절의 값이 작을때 마다 배열에 값 복사 반절의 인덱스를 증가.

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            ##다음으로 복사될 대상의 원래 배열에서의 위치
            k=k+1
        ##바열의 길이가 인덱스보다 크면, 해당 배열에서의 복사가 완료되지 않았다는 것.
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
