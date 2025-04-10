# Chemical Kinetics
This is a collection of scripts to simulate chemical kinetics given reaction equations (assumed to be elementary) and their rate constants. 

## Notes on input
The reactions are inputted as a string separated by a newline character `\n`. The reactions are formatted as `educts = products`, which is to be understood as `educts -> products`. For equilibrium reactions, the reaction must be given forwards and backwards. Stoichiometric coefficients have to be separated by a single space. The compounds can be named with letters and/or numbers. So `A = 2 B`, `Cl2 = 2 Cl` and `Educt = 2 Product` are all perfectly valid. There is no sanity checking, and inputting something like `A = 2 A` will probably just cause a chrash. 

The rate constants are specified in the order of the given reactions and are taken to be in their usual units.

The initial concentrations are given for the substances in their order of appearance in the reactions, so if the reactions are `"C + B = 2 A\n2 A = B+ C"`, the initial concentrations are also assumed to be in the order `C, B, A`.
