#####################______Method_1______##########################

class McCullochPittsNeuron:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold
    def activate(self, inputs):
        if sum([x * w for x, w in zip(inputs, self.weights)]) >= self.threshold:
            return 1
        else:
            return 0
def ANDNOT(a, b):
    weights = [1, -1]
    threshold = 1
    neuron = McCullochPittsNeuron(weights, threshold)
    return neuron.activate([a, b])

print("ANDNOT(0, 0) =", ANDNOT(0, 0))
print("ANDNOT(0, 1) =", ANDNOT(0, 1))
print("ANDNOT(1, 0) =", ANDNOT(1, 0))
print("ANDNOT(1, 1) =", ANDNOT(1, 1))


######################______Method_2______##########################
def mccullock_pitts_andnot(A,B):
    w1=1
    w2=-1
    threshold=0
    weighted_sum=w1*A+w2*B
    output=1 if weighted_sum>threshold else 0
    return output
input_A=int(input("Enter the value of A (0 or 1): "))
input_B=int(input("Enter the value of B (0 or 1): "))
if input_A in (0,1) and input_B in (0,1):
    result=mccullock_pitts_andnot(input_A,input_B)
    print(f"ANNOT({input_A},{input_B})={result}")
else:
    print("Invalid input.Please enter 0 or 1 for A and B.")