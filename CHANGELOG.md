# Changelog

All notable changes to this project are documented here.

## v1.1.0 (21/06/2022)

#### Added
 
#### Changed
   
- modified `db_reader` function to support jul17 and jan19 gwb legacy formats 
  
#### Fixed

#### Removed

## v1.0.6 (15/05/2022)

#### Added
 
- Added Holland and Power heat capacity equation using SUPCRTBL database, tagged as `heatcaphp`.
- Added an option in `supcrtaq` function to allow users specify input units for direct-access or
  sequential-access thermodynamic database. The keyword "InUnit" can take 'cal' or 'KJ' and converts
  to 'cal' which is used in `supcrtaq` function.
- Added a sequential-access thermodynamic database "supcrtbl.dat" containing Holland and Power datasets  
  as documented in SUPCRTBL by Zimmer et al. (2016) SUPCRTBL: A revised and extended thermodynamic dataset 
  and software package of SUPCRT92. Computer and Geosciences 90:97-111.
- Added an option in `calcRxnlogK` to automatically identify species class based on last letter/number
  of the species. This means species ending with '(aq)', '+', '-' or last letter/number isdigit are
  classified as aqueous species and others are gases or mineral species. This is used incase the user
  do not provide a specielist, which has become an optional input into `calcRxnlogK` class function 
- Added capability to generate GWB latest database version (mar21) formats.
- Added an option in `solidsolution_thermo` class function "Al_Si" to allow user specifies how Al and Si
  will be expressed in the solid solution reactions. The keyword can take 'Arnorsson_Stefansson' which 
  expresses them as 'Al(OH)4-' and 'H4SiO4(aq)' while 'pygcc' expresses them as 'Al3+' and 'SiO2(aq)'

#### Changed
   
- modified `mineral_eos` keyword to `heatcap_method` 
- modified `Mintype` keyword to `ClayMintype` 
- integrated functions like `heatcaphp`, `heatcap_Berman` and `heatcapusgscal` into one class function
  `heatcap`
- updated the online documentation to reflected the functions removed
  
#### Fixed

#### Removed

- `heatcap`, `heatcap_Berman` and `heatcapusgscal` functions are no longer in use

## v1.0.5 (22/03/2022)

#### Added
 
#### Changed
   
- Resolved issues relating to polycoeffs logK in GWB database generation. 
  The earlier implementation had the polynomial coefficients rounded off to a 
  shorter significant factors which impacted the ability to generate the correct logK values.
  This update fixed that by extending the significant factors.

#### Fixed
 
## v1.0.4 (10/03/2022)

#### Added
 
- An option was added to automate specification of the structuring layer for `calclogKclays` 
  to ensure charge balance equals 14 for '7A' group, 22 for '10A' group and 28 for  '14A' group.

#### Changed
   
#### Fixed
 
## v1.0.3 (17/02/2022)

#### Added
 
- Added the importlib_metadata dependencies.

#### Changed
   
#### Fixed
 
## v1.0.2 (02/02/2022)

#### Added
 
#### Changed
   
- made changes to the `iapws95` class function, as the previous implementation had issues
  with using fsolve solver to solve for array of data to find the roots of any function.

#### Fixed
 
## v1.0.1 (01/02/2022)
  
#### Added
 
- Added Tutorial python files.

#### Changed
   
#### Fixed

## v1.0.0 (31/01/2022)

- First release of `pygcc`!