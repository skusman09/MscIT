import numpy as np
X=np.array([[0,0],[0,1],[1,0],[1,1]])
targets=np.array([0,0,0,1])
learning_rate=0.1
weights=np.random.rand(2)
bias=np.random.rand()
max_epochs=10000
epoch=0
while epoch<max_epochs:
    error_count=0
    for i in range(len(X)):
        weighted_sum = np.dot(X[i], weights) + bias
        prediction = 1 if weighted_sum >=0 else 0
        error = targets[i] - prediction
    if error != 0:
        error_count += 1
        weights += learning_rate * error * X[i]
        bias += learning_rate * error
        print(f"Epoch {epoch + 1}: {error_count} errors")
    if error_count == 0:
        print("Converged. Weights and bias:")
        print("Weights:", weights)
        print("Bias:", bias)
        break
    epoch += 1
if epoch == max_epochs:
    print("Did not converge. Weights and bias:")
    print("Weights:", weights)
    print("Bias:", bias)