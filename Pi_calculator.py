import math
import random




def est_pi():
    
    n = random.randint(100,10000)
    
    return round(n*math.sin(math.radians(180)/n),7)
    
    

est_pi()