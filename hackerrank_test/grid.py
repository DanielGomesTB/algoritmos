# import string

def gridChallenge(grid):
    # Write your code here
    verification = []
    for strings in grid:
        splited = list(strings)
        splited.sort()
    
    for i in range(len(verification)):
        if verification[i] > verification[i+1]:
            return 'NO'

    return 'YES'
    #     if ''.join(splited) in string.ascii_letters:
    #         verification.append('true')
    #     else:
    #         verification.append('false')

    # is_false = verification.find('false')

print(gridChallenge(['ebacd', 'fghij1', 'olmkn', 'trpqs', 'xywuv']))
