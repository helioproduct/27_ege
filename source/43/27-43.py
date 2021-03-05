Fin = open("27-43b.txt")

N = int(Fin.readline())
s1 = s2 = s3 = 0
diff0 = False
diff1 = [ [1e10, -1], [1e10, -1] ]
diff2 = [ [1e10, -1], [1e10, -1] ]
for i in range(N):
  a, b, c = map( int, Fin.readline().split() )
  a, b, c = sorted( [a, b, c] )[::-1]
  #print( a, b, c )
  s1 += a
  s2 += b
  s3 += c
  if (a - b) % 2 == 1:
    diff0 = True
  if (a - c) % 2 == 1:
    if a - c < diff1[0][0]:
      diff1 = [ [a-c, i], diff1[0] ]
    elif a - c < diff1[1][0]:
      diff1[1] = [a-c, i]
  if (b - c) % 2 == 1:
    if b - c < diff2[0][0]:
      diff2 = [ [b-c, i], diff2[0] ]
    elif b - c < diff2[1][0]:
      diff2[1] = [b-c, i]
  #print( s1, s2, s3, diff1, diff2 )

Fin.close()

print( 's1 =', s1, 's2 =', s2 )
print( 's3 =', s3 )
print( 'b <-> a:', diff0 )
print( 'c <-> a:', diff1 )
print( 'c <-> b:', diff2 )

print("Ответ:")
if s1 % 2 == 0  and  s2 % 2 == 0:
  print( s3 )
elif s1 % 2 != 0 and s2 % 2 != 0:
  if diff0:
    print( s3 )
  else:
    d = min( diff1[0][0] + diff2[1][0],
             diff1[1][0] + diff2[0][0],
             diff1[0][0] + diff1[1][0],
             diff2[0][0] + diff2[1][0] )
    if diff1[0][1] != diff2[0][1]:
      d = min( d,  diff1[0][0] + diff2[0][0] )
    print( s3 + d )
elif s1 % 2 != 0:
  print( s3 + diff1[0][0] )
elif s2 % 2 != 0:
  print( s3 + diff2[0][0] )


