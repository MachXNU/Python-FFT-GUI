from numpy.fft import fft, ifft
import matplotlib.pyplot as plt

def getPeriod(time):
    n = len(time)
    period = 0
    for i in range(n-1):
        period += time[i+1]-time[i]
    return period/n

time, val = np.loadtxt('test.txt',delimiter=',',unpack=True)

X=fft(val)

# calculate the frequency
N = len(X)
n = np.arange(N)
T = getPeriod(time)
freq = n/T

plt.figure("Python FFT GUI",figsize = (12, 6))

# Get the one-sided specturm
n_oneside = N//2
# get the one side frequency
f_oneside = freq[:n_oneside]

# normalize the amplitude
X_oneside =X[:n_oneside]/n_oneside

plt.subplot(121)
plt.stem(f_oneside, abs(X_oneside), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('Normalized FFT Amplitude |X(freq)|')
plt.xlim(-1e+6, 0.8e+8)

plt.subplot(122)
plt.plot(time, ifft(X))
plt.xlabel('Time')
plt.ylabel('Signal')
plt.tight_layout()

plt.show()

