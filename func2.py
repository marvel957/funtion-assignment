def V_argument(*args):
    """This is a function that takes  parameters like n1,n2,n3... 
    and return the result of n * n1 * n2 * n3....."""
    t = 1
    for i in args:
        t*=i
    print("The result is",t)
V_argument(2,3,5)