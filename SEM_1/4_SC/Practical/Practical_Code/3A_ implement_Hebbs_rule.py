import numpy as np
X=np.array([[1,1,1],[1,-1,-1],[-1,-1,1]])
w=np.zeros(X.shape[1])
for pattern in X:
    w+=pattern
for pattern in X:
    activation=np.dot(w,pattern)
    print(f"Input Pattern:{pattern},Synaptic weights:{w},Activation:{activation:.2f}")
    