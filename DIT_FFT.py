import numpy as np
import math

def DIT_FFT(input_signal):

    input_signal[1], input_signal[4] = input_signal[4], input_signal[1]
    input_signal[3], input_signal[6] = input_signal[6], input_signal[3]
    signal = np.array([input_signal])
    input_ = np.hsplit(signal, 4)
    W2 = np.array([[1, 1], [1, -1]])
    for i in range(len(input_)):
        input_[i] = np.dot(input_[i], W2)
    layer1 = []
    for ele in input_:
        layer1.append(ele[0][0])
        layer1.append(ele[0][1])
    W40 = np.array([[1, 1], [1, -1]])
    W41 = np.array([[1, 1], [complex(0, -1), complex(0, 1)]])
    # Swapping for convienience
    layer1[1], layer1[2] = layer1[2], layer1[1]
    layer1[5], layer1[6] = layer1[6], layer1[5]
    layer1 = np.hsplit(np.array([layer1]), 4)
    for i in range(len(layer1)):
        if i % 2 == 0:
            layer1[i] = np.dot(layer1[i], W40)
        else:
            layer1[i] = np.dot(layer1[i], W41)
    layer2 = []
    for ele in layer1:
        layer2.append(ele[0][0])
        layer2.append(ele[0][1])
    layer2[1], layer2[2] = layer2[2], layer2[1]
    layer2[5], layer2[6] = layer2[6], layer2[5]
    
    W80 = np.array([[1, 1], [1, -1]])
    W81 = np.array([[1, 1], [complex(1/math.sqrt(2), -1/math.sqrt(2)), complex(-1/math.sqrt(2), 1/math.sqrt(2))]])
    W82 = np.array([[1, 1], [complex(0, -1), complex(0, 1)]])
    W83 = np.array([[1, 1], [complex(-1/math.sqrt(2), -1/math.sqrt(2)), complex(1/math.sqrt(2), 1/math.sqrt(2))]])
    
    layer2[1], layer2[4] = layer2[4], layer2[1]
    layer2[3], layer2[6] = layer2[6], layer2[3]
    
    
    layer2 = np.hsplit(np.array([layer2]), 4)
    
    layer2[0] = np.dot(layer2[0], W80)
    layer2[1] = np.dot(layer2[1], W82)
    layer2[2] = np.dot(layer2[2], W81)
    layer2[3] = np.dot(layer2[3], W83)
    
    
    output = []
    for ele in layer2:
        output.append(ele[0][0])
        output.append(ele[0][1])

    output[1], output[4] = output[4], output[1]
    output[3], output[6] = output[6], output[3]
    return output

