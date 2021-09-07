# Noodles-Interplay

I believe we are restricted to unix based systems for magenta development, so hopefully everyone has VMware or a mac to use.

create the venv:

    python3 -m venv venv

activate the venv:

  Unix based systems
  
    Source /bin/activate

install packages:

    python3 -m pip install -r requirements.txt
    
    sudo apt-get install build-essential libasound2-dev libjack-dev portaudio19-dev
    
    
If you get errors with the magenta install related to gcc try these:

    sudo apt-get install gcc
    sudo apt-get install python3-dev


