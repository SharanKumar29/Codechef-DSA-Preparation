n, heights = int( input() ), [int( x ) for x in input().split()]



h, s = heights[0], 1

for hs in heights[1:]:

    if hs > h:

        h = hs

        s += 1

print( s )

