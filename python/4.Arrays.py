#==========================================ASSIGNMENT-4====================================
def s(arr): return sum(arr)

def a(arr): return sum(arr) / len(arr) if arr else 0

def i(arr, v): return arr.index(v) if v in arr else -1

def h(arr, v): return v in arr

def r(arr, v): return [x for x in arr if x != v]

def c(arr): return arr.copy()

def ins(arr, idx, v):
    arr.insert(idx, v)
    return arr

def mm(arr): return min(arr), max(arr)

def rev(arr): return arr[::-1]

def d(arr): return list(set([x for x in arr if arr.count(x) > 1]))

def com(a1, a2): return list(set(a1) & set(a2))

def rd(arr): return list(set(arr))

def sl(arr):
    u = sorted(set(arr))
    return u[-2] if len(u) > 1 else None

def so(arr):
    u = sorted(set(arr))
    return u[-2] if len(u) > 1 else None

def eo(arr):
    e = len([x for x in arr if x % 2 == 0])
    return e, len(arr) - e

def diff(arr): return max(arr) - min(arr)

def chk(arr): return 12 in arr and 23 in arr

def rd_arr(arr): return list(set(arr))

arr = [10, 20, 30, 40, 20, 10, 50, 60]
arr2 = [20, 50, 70, 80]

print("Sum:", s(arr))
print("Average:", a(arr))
print("Index of 30:", i(arr, 30))
print("Contains 10:", h(arr, 10))
print("After removing 20:", r(arr, 20))
print("Copied Array:", c(arr))
print("After inserting 99 at idx 2:", ins(arr, 2, 99))
print("Min and Max:", mm(arr))
print("Reversed:", rev(arr))
print("Duplicates:", d(arr))
print("Common with arr2:", com(arr, arr2))
print("After removing duplicates:", rd(arr))
print("Second Largest:", sl(arr))
print("Second Largest (Duplicate Method):", so(arr))
print("Even & Odd Count:", eo(arr))
print("Diff between Max & Min:", diff(arr))
print("Contains 12 & 23:", chk(arr))
print("Remove Duplicates & Return New Array:", rd_arr(arr))
