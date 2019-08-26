# FFT-in-Python

Implementation of FFT in Python only using the Numpy module...

# Modelling 

The Transform from the Time to the Frequency domain was represented by Matrix Multiplication of Wk and the respective Layers...

The Wk values are represented as Matrices. For example take W2 then the Matrix is represented by:
                                  
                                                      [[1,  1]
                                                W2  =     
                                                       [1, -1]]
                                            
Now this is multiplied with it's respective layer... Suppose our input signal is 
                                        
                                     input_signal = [2, 3, -1, -1, 4, -3, -2, 1]

For the first layer of operation to be performed we need to split the above signal into sets of two, and perform each element's multiplication with W2. Similarily for second layer and third layer also we need to split the layers into sets of two with one difference.


For second layer we need to associated the calculation with X[i] with X[i + 2] hence in the model designed above it's easier to swap those values and then split them as required and perform the Calculation, after each calculation of layer swap the elements back.

Calculation (In case of the first layer):-
    
                                      layer[i] = np.dot(layer[i], W2)
                                      # if i = 0 then the above transforms to 
                                      # layer[0] = np.dot([[2, 4]], [[1, 1], [1, -1]])

This process is repeated for all layers till the Output layer until we get our result lying in the Complex Domain / Frequency Domain. This is the DIT_FFT Algorithm.

The below diagram depicts the DIT FFT transformation technique:-

![img1592](https://user-images.githubusercontent.com/44934630/63707028-9091f680-c84e-11e9-8647-3619c4d0a780.png)


# Author
Valluri Pavan Preetham (@ppvalluri09)
