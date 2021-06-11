import numpy as np

if __name__ == '__main__':
    #numpy exercises
    print(np.zeros(10))
    print(np.ones(10))
    print(np.full((10), 5))
    print(np.arange(10,51))
    print(np.arange(10,51,2))
    print(np.linspace(0,1,20))
    print(np.random.randn(25))
    print(np.arange(start=0.01, stop=1.01, step=0.01).reshape(10,10))

    #numpy indexing and selection
    mat = np.arange(1,26).reshape(5,5)
    print(mat)
    print(mat[2:,1:])
    print(mat[3,4])
    print(mat[:3,1:2])
    print(mat[-1:])
    print(mat[3:5,:])
    print(mat.sum())
    print(mat.std())
    print(mat.sum(axis=0))

