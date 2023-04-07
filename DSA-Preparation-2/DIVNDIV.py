for _ in range( int( input() ) ):
    x, y, z = [int( x ) for x in input().split()]
    
    if y % z == 0:
        print( -1 )
    else:
        k = (x // y) * y + y
        while k % z == 0:
            k += y
        print( k )