import numpy as np 
from astropy.table import Table 
from astropy.io import ascii 
from astropy.io import fits

#generate table from text using numpy
def np_sin_table():
    #writes out text 
    x = np.linspace(0, 2* np.pi, 1000)
    sin_x = np.sin(x)
    #transpose and combine the x and sin x into a matrix and format it. Then save the text 
    np.savetxt("sin.txt", np.transpose((x,sin_x)), fmt = '%4.3f %4.3f')
    return 

def astro_sin_table():
    x = np.linspace(0, 2* np.pi, 1000)
    sin_x = np.sin(x)
    data = Table([x,sin_x],names=['x','sin(x)'])
    ascii.write(data, 'table.txt', format='commented_header')
    data_in = ascii.read('table.txt')
    print(data_in)
    return 


#main function for it 
def main():
    np_sin_table()
    astro_sin_table()

if __name__ == "__main__":
    main() 