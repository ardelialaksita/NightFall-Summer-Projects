# values of each variables for implemented in linear function
b = 10
x1 = 1
x2 = 2
y1 = 2
y2 = 5
x = 5

# linear function 
def linear(x1, x2, y1, y2, x):
  m = (y2 - y1) / (x2 - x1)
  y = m * x + b
  return y

# save the linear function on a variables, then print it 
hitung = linear(x1, x2, y1, y2, x)
print(hitung)

# this code was arranged by ara
