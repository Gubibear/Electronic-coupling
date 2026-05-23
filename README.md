# Electronic Coupling
Repository of codes used in electronic coupling calculations
The code was authored by Rafał Szabla and Mikołaj Gurba.

A brief description of each script is provided below.

### coupling-7.6.py:

This script calculates electronic coupling based on the results of ADC(2) calculations performed using the TURBOMOLE 7.6 package.
The program implements two approaches: the generalized Mulliken-Hush (GMH) approach and the Boys localization method. The theory of both approaches and the derivation of the equations can be found at DOI: 10.1063/1.3042233.

To use the program, all you need is the output file from the ADC(2) problem in the TURBOMOLE 7.6 package. To calculate electronic coupling between two excited states, the output file must contain the components of the electric dipole moment of the system in these states and the components of the transition dipole moment between them. To ensure that ricc2 calculates these properties, the following lines should be included in the $excitations section of the control file:

  spectrum  states=all  operators=xdiplen,ydiplen,zdiplen
  
  exprop  states=all relaxed  operators=xdiplen,ydiplen,zdiplen
  
  tmexc istates=(a 1) fstates=(a 2-8) operators=diplen,dipvel

The coupling-7.6.py script can be called with this command:

  python coupling-7.6.py -n output_file_name -i initial_state_number -f final_state_number

The initial and final state numbers are the indices of the states between which the electron coupling should be calculated. The ground state has index 0, the first excited state has index 1, and so on.

Example: Calculating the coupling between the first and fifth excited states from the ricc2.out file:

   python coupling-7.6.py -n ricc2.out -i 1 -f 5
  
