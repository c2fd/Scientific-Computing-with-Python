# complex numbers: note the use of `j` to specify the imaginary part
x = 1.0 - 1.0j #jia
print(type(x))
print('imaginary part: ', x.imag, '; real part:', x.real)
print(f"imaginary part: {x.imag}; real part: {x.real}")
print('imaginary part: %f; real part: %f' %(x.imag, x.real))
z = 1 + 1j
print(z + 2) # 3 + 1j
print(z.conjugate()) #

print(type(z))