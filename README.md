# Electronic-coupling
Repository for codes used in the electronic coupling calculations
Rafal Szabla and Mikolaj Gurba are the authors of the code. 

The short description for each script is provided below.

### coupling-7.6.py:

This script is used to calculate the electronic coupling from the results of ADC(2) calculations performed with the TURBOMOLE 7.6 package.
Two approaches are implemented in the program: Generalized Mulliken-Hush (GMH) approach and Boys localization method. The theory behind both approaches and derivation of the equations can be found in DOI: 10.1063/1.3042233.

To use the program, only the output file from the TURBOMOLE 7.6 ADC(2) job is needed. To calculate the electronic coupling between two excited states, this output file must contain the components of the electric dipole moment of the system in those states and the components of the transition dipole moment between them. To ensure the calculation of these properties by the ricc2 program, the following lines must be included in the $excitations section of the control file:

  spectrum  states=all  operators=xdiplen,ydiplen,zdiplen
  exprop  states=all relaxed  operators=xdiplen,ydiplen,zdiplen
  tmexc istates=(a 1) fstates=(a 2-8) operators=diplen,dipvel

The coupling-7.6.py script can be called with this command:

  python coupling-7.6.py -n output_file_name -i initial_state_number -f final_state_number

The initial and final state numbers are the indices of the states between which the electronic coupling has to be calculated. The ground state has index 0, the first excited state has index 1, and so on.

Example: calculate the coupling between the 1st and 5th excited states from the ricc2.out file:

   python coupling-7.6.py -n ricc2.out -i 1 -f 5
  
