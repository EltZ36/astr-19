import numpy as np 

#generate table from text
def sin_table():
    #writes out text 
    x = np.linspace(0, 2* np.pi, 1000)
    sin_x = np.sin(x)
    #transpose and combine the x and sin x into a matrix and format it. Then save the text 
    np.savetxt("sin.txt", np.transpose((x,sin_x)), fmt = '%4.3f %4.3f')
    return 

#print out the text 
def print_table():
    fname = "sin.txt"
    test_data = np.genfromtxt(fname)
    print(test_data)

#main function for it 
def main():
    sin_table()
    print_table() 

if __name__ == "__main__":
    main() 