import oscars.sr

osr = oscars.sr.sr()
osr.set_nthreads_global(8)

osr.clear_bfields()
osr.add_bfields_undulator(bfield=[0, 1, 1], period=[0, 0, 0.050], nperiods=71)

osr.set_particle_beam(type='electron',
                      name='beam_0',
                      energy_GeV=3,
                      x0=[0, 0, -2],
                      d0=[0, 0, 1],
                      current=0.500,
                      sigma_energy_GeV=0.001*3,
                      beta=[1.5, 0.8],
                      emittance=[0.9e-9, 0.008e-9],
                      horizontal_direction=[1, 0, 0],
                      lattice_reference=[0, 0, 0])

osr.set_ctstartstop(0, 4)

spectrum = osr.calculate_spectrum(obs=[0, 0, 30],
                                  energy_range_eV=[100, 450],
                                  npoints=500,
                                  nparticles=2,
                                  ofile='del_spec.dat')

power_density = osr.calculate_power_density_rectangle(plane='XY',
                                                      width=[0.05, 0.01],
                                                      npoints=[101, 101],
                                                      translation=[0, 0, 30],
                                                      ofile='del_pd.dat')
