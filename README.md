# Processing & Analysis for Radio Science Experiments (PARSE)

### Functionality:

TODO: This is where I can describe what the app does.

### How to Download the Application:

TODO: Here I can explain how to download the application.

### How to Use the Interface to Process and Analyze Radio Data:

Once the application is launched, you will see a start screen with several buttons in the right-hand column. 

TODO: insert annotated image

Selecting "Tutorial" will provide a simple and user-friendly guide to using the application. 

Alternatively, selecting "Documentation" will provide a scientific and technical description of the program's underlying processes, so the user can better understand how it has been implemented.

### Supported Missions and Data Formats:

This distribution is conveniently bundled with data files from the following missions:
- Rosetta Mission (Target: Comet 67P)
- Dawn Mission (Target: Asteroid Vesta)

Alternatively, the user may upload data files from other missions or experiments. To do so, please see the instructions below.

##### How to upload your own data files:

To upload data files manually, please convert them to the .npy format. This format is common in data science, highly optimized, and platform independent. To convert data files to this format, the user will need a basic familiarity with:
- Python 3
- Numpy (a standard package for scientific computing with Python)

TODO: explain the Numpy formats!

If you run into issues with this process, please contact the developer at paulsirri@gmail.com

 # TODO: REMOVE OLD JUNK
Note: this program only accepts data formatted using NASA's PDS3 standard (see documentation online)

For this program to run correctly, please ensure the following are true of the uploaded files :
- files must use the "detached label" sub-format of the PDS3 data standard (see chapter 5.1 in the PDS3 documentation)
- once accurately stored according to the PDS3 detached label format, verify the following in the label file:
    PDS_VERSION_ID = PDS3
    RECORD_TYPE = FIXED_LENGTH
    INTERCHANGE_FORMAT = BINARY
- within the "TABLE" object, the radio signal data (BSR, or IQ-samples, etc.) must be stored in a "COLUMN" object with:
    NAME = "SAMPLE WORDS"
