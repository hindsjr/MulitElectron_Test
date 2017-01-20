import oscars.sr

import sys

PROCESS = sys.argv[1]

osr = oscars.sr.sr()
osr.set_nthreads_global(8)



# Output file name for spectrum
file_name_spectrum = 'Spectrum_' + PROCESS + '.dat'
print(file_name_spectrum)

spectrum = osr.calculate_spectrum(obs=[0, 0, 30],
                                  energy_range_eV=[100, 450],
                                  npoints=500,
                                  nparticles=2,
                                  ofile=file_name_spectrum)





