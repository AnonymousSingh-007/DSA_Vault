#brute force appraoch

def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    result = []
    for L, R in queries:
        xor = 0
        for i in range(L, R + 1):
            xor ^= arr[i]
        result.append(xor)
    return result

#chatgpt optimized appraoch
def xorQueries(arr, queries):
    n = len(arr)
    prefix = [0] * (n + 1)  # Extra space for easier calculations

    # Step 1: Compute prefix XOR
    for i in range(n):
        prefix[i + 1] = prefix[i] ^ arr[i]

    # Step 2: Answer queries in O(1)
    result = []
    for L, R in queries:
        result.append(prefix[R + 1] ^ prefix[L])
    
    return result
