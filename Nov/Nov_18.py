print("Nov-18")

def binary(arr,l,r,x):
    if l<=r:
        mid=(l+r)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x :
            return binary(arr,l,mid-1,x)
        else:
            return binary(arr,mid+1,r,x)
    return -1

arr=[1,3,5,7,8,9]
x=8

# print(f"Element is present at {binary(arr,0,len(arr)-1,x)}")
