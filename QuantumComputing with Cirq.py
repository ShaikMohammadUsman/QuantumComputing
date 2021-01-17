#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install cirq


# In[2]:


import cirq


# In[3]:


print(cirq.google.Sycamore)


# In[4]:


#Defining the Qubits  using ##NamedQubit## method

a=cirq.NamedQubit('a')
b=cirq.NamedQubit('b')


# In[6]:


##Creating a quantum circuit using #CIRCUIT# method

circuit=cirq.Circuit(   ##Creating a circuit
    cirq.H(a),   
    cirq.CNOT(a,b),
    cirq.measure(a,b))

#Inside the circuit we need to put the gates we want to add to the circuit and passs in which order(queue) we want the gate applied to


# In[7]:


print(circuit)  # to look at how your logic gates are connected in circuit


# In[9]:


#circuit has a conceot of moment where we can see moment #
# we can print the moment of circuit and see what happened in this time moment or time slices

circuit.moments


# In[10]:


# we can also chekck the moments using  repr method

print(repr(circuit))


# In[12]:


##Runiiing our code on a simulator

simulator=cirq.Simulator()

# now to avoid the random noise in quantum computer we need to use repetations(or) run the same circuit numbver of tinmes

result= simulator.run(circuit,repetitions=20)


# In[14]:


print(result)  ## now this gets the output of both a and b as 50% and 50%


# In[ ]:




