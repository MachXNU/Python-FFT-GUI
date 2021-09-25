# Python-FFT-GUI
Easily get the FFT of a signal sampled in a .csv file

This program allows you to easily get the Fast Fourier Transform (aka. FFT) from a signal that has been sampled and stored in a .csv.
This program also reconstructs the original signal (left of the window) and prints its FFT (on the right).
The expected structure of the .csv is : `<time>,<value>` with no line to skip
This can obviously be changed easily by adapting the Python code !

An example `.csv` is included in the repo as well.

## Troubleshooting
If you can't see properly the FFT spectrum, try adjusting the bounds of the FFT window in the code (at the moment, it's optimised for the `.csv` file provided here

## License
MIT license
