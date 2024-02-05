from collections import defaultdict


def solution(a, k):
    count = 0
    dict_track_remain = defaultdict(int)
      
    for i in a:
        remainder = i % k
        to_find = (k - remainder) % k
        
        count += dict_track_remain[to_find]
        dict_track_remain[remainder] += 1  # increment the count of remainder, not to_find
    
    return count