_IMAGE TAGGING AND RETRIVAL Readme_
-----------------------------------

Basic :
=======

If you have git installed on your machine follow these steps -

*   Create a new folder on your Desktop or anyplace you wish.
*   Now go inside the folder and open terminal/VsCode in this folder.
*   Copy this link - [Link](https://github.com/shubhamByte/Image_Tagging_and_Retrival.git)
*   Now, in the terminal write -

    git clone "and paste the above copied link here"
    

If you don’t have git installed, follow these steps -

*   Visit the link - [Link](https://github.com/shubhamByte/Image_Tagging_and_Retrival.git)
*   Click on “Code ( highlighted in green color) " and in the dropdown menu click on " Download Zip”
*   Extract the Zip file and open terminal/VsCode in this folder.

Installing Prerequisites :
==========================

For our project, you need to have python and pip installed on your machine.

PYTHON INSTALLATION -  
If you dont have python installed,follow the steps -

*   visit the link - [link](https://www.python.org/)
*   Go to downloads and download the latest version and install it.  
    FOR WINDOWS -
*   At the time of installation, check the box " add python to PATH" .  
    FOR MAC -  
    after installing, open the terminal and follow these steps -

    nano ~/.bash_profile
    

at the end of the bash file add -

    alias python=python3
    

now to save the file-

*   press CTRL+X
*   press y
*   press enter

PIP INSTALLATION -

*   In the terminal paste the link - [link](https://bootstrap.pypa.io/get-pip.py)
*   Now write-

    python get-pip.py
    

and wait for the installion to be completed.

Installation and Running the Code :
===================================

Go inside the downloaded folder named "Image Tagging and Retrival " and open terminal/VScode in it.  
\[Make sure you are in the directory named “Image Tagging and Retrival” \]

*   Create a virtual environment called venv in the project directory  
    FOR WINDOWS -

    python -m venv venv
    venv\Scripts\activate
    

FOR MAC -

    python3 -m venv venv
    source venv/bin/activate
    

*   Install Flask and also python-dotenv packages -

    pip install flask python-dotenv
    
*   Runing flask

    flask run
    

Verify the deployment by navigating to your server address in your preferred browser.

    127.0.0.1:5000
    

*   press CTRL and click on the link displayed in the terminal .

Deployed Link (Sample) -  https://nameless-eyrie-29156.herokuapp.com/

#END
