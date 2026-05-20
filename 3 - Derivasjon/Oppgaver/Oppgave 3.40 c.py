def f(x):
    return (3*x + 1)/(x - 2)

def snittfart(x, delta_x):
    return(f(x + delta_x) - f(x))/delta_x

print(snittfart(1, 1E-8))

# Output:
# d-7,000000046275545