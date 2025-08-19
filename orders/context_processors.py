from .cart import *

def cart (request):
    return{'cart' : Cart(request)}
