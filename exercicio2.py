'''
This exercise has as goal develop a simple calculator to verify the BMI of a person
'''

name = 'Greg'
heigh = 1.80
weigh = 95
bmi = weigh / (heigh**2)

print(f'{name} is {heigh:.2f} m tall,')
print(f'He has {weigh} kg and his BMI is: {bmi:.2f}')