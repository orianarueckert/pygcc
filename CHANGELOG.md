# Changelog

All notable changes to this project are documented here. To ensure that they are using the most up-to-date version of the PyGCC software, users should update PyGCC on their local computers using the following command:

```console
pip install --upgrade pygcc
```

## v1.3.1 (11/11/2024)

#### Added

- we added flexible direct-access modifying option that reads a csv file and makes a new direct-access database. Test = dbaccess_modify(in_filename = 'geotpd_data_block_cr.csv', dbaccess = './speq23.dat')

#### Changed
   
#### Fixed

- we have fixed the calculation error when generating pflotran databased with GWB source database (starting from mar21 format).
  
#### Removed

## v1.3.0 (03/05/2024)

#### Added
 
- we have incorporated the NaCl-H2O phase relationship equations of Driesner and Heinrich (2007) which was utilized in the 
  Syverson, et al. (2023) Geology paper for geothermobarometer calculation.
  

#### Changed
   
#### Fixed

#### Removed

## v1.2.0 (10/09/2023)

#### Added
 
- we have included the thermodynamic databases speq23 and speq23_dimer. To utilize these databases in pygcc, users are now 
  required to specify their selection. For example, users can set "dbaccessdb = speq21_dimer", "dbaccessdb = speq23", "dbaccessdb = speq23_dimer".
  

#### Changed
   
- modified the default speq21 database to reinstate the thermodynamics data for SiO2(aq) to the values presented in Shock et al. (1989)

- modified the database creation to include dimer - Si2O4(aq) - for scenarios where SiO2(aq) from Sverjensky et al. (2014) - speq21_dimer.dat
  is used. Users who intend to utilize speq21_dimer or speq23_dimer databases should verify that the dimer reaction is present in their source database. 
  Note that source databases, including the default 'thermo.com.tdat' and 'thermo_latest.tdat' have been updated to include dimer reactions."

#### Fixed

- In previous versions, errors related to deprecated functionality were encountered when using Python versions greater than 3.9.6.

#### Removed

## v1.1.4 (25/11/2022)

#### Added
 
- Mineral "Graphite" was added to the thermo.2021.dat database. Other modifications were made to the formula 
  of some carboxylic acids in the database
  
- A debug message has been added to the `write_database` class, with a default value of False, to print out
  options included in generating the database. The print option can be turned on by specifying "print_msg = True"

- The source databases included with pygcc downloads can now be specified using the file names rather their 
  full paths, such as "sourcedb = thermo.com", "sourcedb = thermo.2021", "sourcedb = thermo_latest", etc.
  
- Pitzer activity model format for ToughReact is now included

- Created an option to use the GWB source database to generate the EQ36 database, i.e., convert GWB database 
  to EQ36 database.

#### Changed
   
- modified the default output database for ToughReact from "thermo_ToughReact%sbars" to "thermo%sbars"

- modified the creation of output folder to specify subfolders for ToughReact, GWB, EQ36 and PFLOTRAN

- modified the code so that the density extrapolation prompt message is only activated in cases where the
  density is less than 350 g/cm3

#### Fixed

- v1.1.2 and v1.1.3 have errors that are now fixed 

#### Removed

## v1.1.1 (19/09/2022)

#### Added
 
#### Changed
   
- modified the naming of log10_co2_gamma in the `Henry_duan_sun` and `drummondgamma` functions to activity
  coefficients

- corrected dielectric constants units in `water_dielec` class implementation of water dielectric constants 

- modified pressure region for `Helgeson_activity` function to include pressures above 5 kbar
  
#### Fixed

#### Removed

## v1.1.0 (21/06/2022)

#### Added
 
#### Changed
   
- modified `db_reader` function to support jul17 and jan19 gwb legacy formats 
  
#### Fixed

#### Removed

## v1.0.6 (15/05/2022)

#### Added
 
- Added the Holland and Power heat capacity equation using the SUPCRTBL database, tagged as `heatcaphp`.
- A `supcrtaq` function option has been added, allowing users to specify input units for direct-access or
  sequential-access thermodynamic databases. The keyword "InUnit" can take 'cal' or 'KJ' and convert
  to 'cal' which is used in the `supcrtaq` function.
- Added "supcrtbl.dat", a sequential-access thermodynamic database containing Holland and Power datasets  
  documented in SUPCRTBL by Zimmer et al. (2016) SUPCRTBL: A revised and extended thermodynamic dataset 
  and software package of SUPCRT92. Computer and Geosciences 90:97-111.
- Added an option in `calcRxnlogK` to automatically identify species class based on species' last letter/ 
  number. This means that species ending with '(aq)', '+', '-' or last letter/number isdigit are
  classified as aqueous species whereas others are gases or mineral species. This is used in case the user
  does not provide a `specielist`, which has become an optional input into the `calcRxnlogK` class function 
- Added the capability to generate the most recent database version of GWB (mar21) formats.
- Added an option in `solidsolution_thermo` class function "Al_Si" to allow the user to specify how Al and 
  Si will be expressed in the solid solution reactions. The keyword can take 'Arnorsson_Stefansson' which 
  expresses them as 'Al(OH)4-' and 'H4SiO4(aq)' while 'pygcc' expresses them as 'Al3+' and 'SiO2(aq)'

#### Changed
   
- modified `mineral_eos` keyword to `heatcap_method` 
- modified `Mintype` keyword to `ClayMintype` 
- combined functions like `heatcaphp`, `heatcap_Berman` and `heatcapusgscal` into a single class function
  `heatcap`
- updated the online documentation to reflected the functions removed
  
#### Fixed

#### Removed

- The `heatcap`, `heatcap_Berman` and `heatcapusgscal` functions are no longer in use

## v1.0.5 (22/03/2022)

#### Added
 
#### Changed
   
- Issues with polycoeffs logK in GWB database generation have been resolved. 
  The polynomial coefficients were rounded off to shorter significant factors 
  in the previous implementation, which hampered the ability to generate the 
  correct logK values. This update fixed that by extending the significant factors.

#### Fixed
 
## v1.0.4 (10/03/2022)

#### Added
 
- A new option was implemented to automatically specify the structuring layer for `calclogKclays` 
  with the goal of achieving charge balance of 14 for the '7A' group, 22 for the '10A' group and 
  28 for the '14A' group.

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
   
- Modified the `iapws95` class function because the previous implementation had issues
  with using fsolve solver to solve for an array of data to find the roots of any function.

#### Fixed
 
## v1.0.1 (01/02/2022)
  
#### Added
 
- Python tutorial files have been added.

#### Changed
   
#### Fixed

## v1.0.0 (31/01/2022)

- This is the first release of `pygcc`!