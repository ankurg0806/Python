# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

def helper(myStr, k):
    if k == 0:
        return 1 
    pos = len(myStr) - k 
    if myStr[pos] == '0':
        return 0
    result = helper (myStr, k-1)
    if k>=2 and int(myStr[pos:pos+2]) <=26:
        result += helper(myStr, k-2)
    return result
def decodingWays(myStr):
    return helper(myStr, len(myStr))
    
print(decodingWays("1111"))