# Noodles-Interplay

I believe we are restricted to unix based systems for magenta development, so hopefully everyone has VMware or a mac to use.

Run the automated install for magenta: 
        Say yes to all prompts

        curl https://raw.githubusercontent.com/tensorflow/magenta/main/magenta/tools/magenta-install.sh > /tmp/magenta-install.sh
        bash /tmp/magenta-install.sh

initialize the conda env:

    conda init
    
close the terminal and open a new one

activate the venv:

         source activate magenta
           
  if something goes wrong with the automated install run this:
   
         python3 -m pip install magenta

install remaining packages (django and mido):

        python3 -m pip install -r requirements.txt
    
    
    
    
If you get errors with the magenta install related to gcc try these:

    sudo apt-get install gcc
    sudo apt-get install python3-dev


