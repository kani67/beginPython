import stddraw

stddraw.square(.2, .8, .1)
stddraw.filledSquare(.8, .8, .2)
stddraw.circle(.8, .2, .2)

xd = [.1 , .2, .3, .2] 

yd = [.2 , .3, .2, .1]


stddraw.filledPolygon(xd, yd)

stddraw.text(.2, .5, 'black text')
stddraw.setPenColor(stddraw.WHITE)
stddraw.text(.8, .8, 'white text')
stddraw.show()
