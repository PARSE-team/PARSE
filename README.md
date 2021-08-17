## PARSE: Processing & Analysis for Radio Science Experiments
##### Elizabeth M. Palmer, Paul Sirri, Essam Heggy
###### University of Southern California, Department of Electrical and Computer Engineering
###### Developer Contact: paulsirri@gmail.com
First Release: (under review with [*Planetary Science Journal*](https://journals.aas.org/planetary-science-journal/) by American Astronomical Society)

![PARSE Logo](https://github.com/PARSE-team/PARSE/blob/main/src/main/resources/base/PARSE_USC_logo_bw_red_4x5.png?raw=true)

PARSE is a user-friendly GUI tool to assist planetary scientists in analyzing Deep Space Network (DSN) radio science datasets without requiring expertise in signal processing. PARSE can be used on bistatic radar (BSR) surface-scatter experiments, which use the radio communications antenna aboard a spacecraft to transmit X- or S-band radiowaves that scatter from the planetary object's surface and are then received by the DSN. BSR surface echoes can be used to quantify surface roughness at the cm-dm scale, for example, which can be used to constrain thermophysical models of planetary regoliths, support detailed geomorphological mapping, and reduce risk associated with site selection for landing and sampling missions. An example of such an experiment is given by [Palmer, Heggy & Kofman (2017)](https://doi.org/10.1038/s41467-017-00434-6).

An illustrative demonstration of PARSE is available via the [PARSE Tutorial Video](https://youtu.be/JcRaaFpzjIg).

###### Workflow Summary:
![PARSE flowchart](https://github.com/PARSE-team/PARSE/blob/main/src/main/resources/base/softwareX_fig_flowchart_v6_4x4.png?raw=true)

After choosing the data file and supplying basic target body information and spacecraft orbital parameters, users are then shown recommended processing parameters and given the ability to conveniently adjust them. Once the parameters are entered, the user can run the plotting animation to iterate over the time series, displaying a sequence of power spectral density plots, which show the frequency distribution of the signal power received by the DSN. This animation can be paused at any time to better view a single power spectral density. Once the animation is paused, the user can select the signal analysis tab to extract key features from the plot or export it as an image file.

### Installation & Getting Started

#### Users:
1. In the column on the right-hand side of the repository homepage, click "Releases".
2. Select a release, then click on "Source code (zip)" to download the project repository.
   Note: The download is large (6-7 GB) since it includes raw data files, so it will take time to download depending on your connection speeds.
3. After unzipping the file, look inside the "PARSE" directory to find the installer file for your system and run it. Due to the size of the bundled data files, please expect 1-2 minute delays when opening the application or its installer for the first time.
  - For Mac OS X: navigate to "PARSE-1.0 / build / mac / PARSE.dmg"
  - For Microsoft Windows: navigate to "PARSE-1.0 / build / windows / PARSESetup.exe"
    - Note: If using Microsoft Windows, the installer may display a warning message. If so, click "More Info" and "Run Anyway" to begin the installation. 
4. Once the installation is completed, PARSE will be available in your applications folder. Due to the size of the bundled data files, please expect 1-2 minute delays when opening the application or its installer for the first time.
5. After opening the application, use the following menu options to learn about how PARSE works. Some of these resources have been linked here for your convenience.
  - [Tutorial Video](https://youtu.be/JcRaaFpzjIg): a brief illustrative demonstration of PARSE for new users
  - [User's Guide](https://github.com/PARSE-team/PARSE/blob/main/UsersGuide_v1.pdf): the official documentation for PARSE
  - Relevant Publications: publications that discuss PARSE's underlying pipeline

#### Developers:
To begin working with source code directly, install Git LFS on your device before cloning this repository.

### Error Reporting:
If you run into issues with this process, please contact the developer at paulsirri@gmail.com
