mysamples = []
mylinear = []
myquadratic = []
mycubic = []
myexponential = []

for i in range(0, 30):
    mysamples.append(i)
    mylinear.append(i)
    myquadratic.append(i**2)
    mycubic.append(i**3)
    myexponential.append(1.5**i)


plt.figure('lin quad')
plt.clf()
plt.plot(mysamples, mylinear)
plt.plot(mysamples, myquadratic)

plt.figure('cub exp')
plt.clf()
plt.figure('lin quad')
plt.title('L vs Q')
plt.figure('cub exp')
plt.title('C vs E')