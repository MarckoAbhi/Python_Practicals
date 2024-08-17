import sympy as sp

#define the vriable and the fuction
x, y = sp.symbole("x y")
F = 3*x**2 +2*x +sp.sin(x +y)

#find the partial derivative
F_x = sp.diff(F, x)
F_y = sp.diff(F, y)

#define the differential equation
equation = sp.Eq(F_x + F_y,0)

# check if the equation is exact
is_exact = sp.Eq(F_x, F_y)

#solve the equation
solution= sp.dsolve(equation)

print("Is the equation exact?", is_exact)
print("Solution:", solution)











