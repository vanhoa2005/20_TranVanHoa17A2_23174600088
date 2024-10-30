x,y=100,0
try:
    print('x/y=',x/y)
except ZeroDivisionError as er:
    print('Error:',er)  
finally:
    print('x+y=',x+y) 
    print('x-y=',x-y)
    print('x*y=',x*y)     