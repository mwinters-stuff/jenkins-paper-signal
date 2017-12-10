# jenkins-paper-signal

Using the arrow paper signal to indicate build status on a jenkins jon. 

# Get started

Build the arrow paper signal from 
https://papersignals.withgoogle.com/

Install the python-jenkins library (pip-install jenkins-python)

Install ServoBlaster from github - https://github.com/srcshelton/servoblaster
*** I configure the first servo to pin 11, as it works better.

Configure the script to point to your jenkins server and job.

Connect the servo, I use a 3 volt battery to power it.

Run the script. The arrow should point upwards when the build is good,
down when the build is bad and to the right when the build is unstable.


