# Running SUMO simulations on MIT SuperCloud

## Introduction
- This tutorial is for Mac users. It would probably be the same for Linux OS, but I haven't tested it 
- Additionally, this is specifically designed for the Wulab (we assume SUMO is already installed in the proper place, etc...)
- Credit to Jinhee Won and Marcus Bluestone for this Write-Up (please email marcusbl@mit.edu for follow-up questions) 

## Getting Your Key
- In order to connect to the MIT SuperCloud, you need to ssh into it. This allows you to access the SuperCloud computer from your computer. To do this, you need to get your comptuer's public encryption key. 
1. Check if you already have a public key by openning a Terminal and running: `cat ~/.ssh/id_rsa.pub`. 
2. If a long string of numbers and letters is outputted, then this your rsa public key. If no file or directory is found, then you have to generate a public key. To do this, enter `ssh-keygen -t rsa` into the terminal. You will be prompted with messages and just press return for all. You can run step 1 and get the key. 
3. Copy the public key text and add it to your SuperCloud account online. If you're working with someone else's account, send them your public and they will then add your computer to their account. 

## Connect to the SuperCloud
- Write `ssh USERNAME@txe1-login.mit.edu` (e.g. `USERNAME` is `chickert` to ssh into Cameron's account)
- Now, your terminal should begin with green words instead of the usual black. This means your ssh was successful! 

## Copying Files to Cloud
- Now, we want to copy the folder that we have saved locally on our computer to the SuperCloud. To do this, we use the Secure Copy Protocol (SCP) command. 
1. Open a **new** terminal and `cd` to the directory that contains the folder of files you want to upload.
2. Then, run: 
```scp -r folder_name USERNAME@txe1-login.mit.edu:```
- Do not forget the colon at the end of the line. `folder_name` should be replaced by the actual name of the folder that you want to upload to the cloud computer.
3. Go back to the terminal where you are sshed into the SuperCloud account and write `ls`. You should see the files that you just uploaded dispalyed. 
4. cd into the new folder that you uploaded. 

## Setting Up Environment Variables
- This part is the most complex and the most prone to errors. Please follow the following steps carefully
1. Confirm sumo is already installed. Run `which sumo`. You should see `/home/gridsan/tools/groups/wulab/sumo-1.12.0/bin/sumo` displayed. This is the location where sumo is installed on the cloud
2. Next, we modify the bashrc file, which is a configuration file that loads a user's preferences when they log into Linux. This will set up some variables so that SUMO will know where to look for certain files. Run `nano ~/.bashrc` to open the bashrc file in the terminal. (The `~` symbol is a shortcut for your the home directory; it will probably look like `/home/gridsan/USERNAME`; the `.` is added for hidden files which means that it won't show up when you use `ls` to list the files in a folder)
3. Scroll down to the bottom of the file and add the following lines. These lines set the variables so that SUMO and Python know where to look to access the correct files The last section can be used to set new variables for your specific project
```
#Python Path
export PYTHONPATH="/home/gridsan/tools/groups/wulab/sumo-1.12.0/tools:$PYTHONPATH"

# SUMO binaries
export W=/home/gridsan/tools/groups/wulab
export SUMO_HOME=$W/sumo-1.12.0
export LD_LIBRARY_PATH=$W/root_sumo-1.12.0/usr/lib:$W/root_sumo-1.12.0/usr/lib/x86_64-linux-gnu
export PATH=$SUMO_HOME/bin:$PATH

#Add Extra Variables Needed For Your Project
```
4. To save the file, press `CNTRL X` and then `Y` and then `Return`. 
5. Then, run `source ~/.bashrc` to run the bashrc file. 
6. Finally, we are going to need to use a bunch of libraries saved through Anaconda, so run `module load anaconda/2022a` to gain access to all the libraries. If you want to use a different version, run `module unload anaconda/2022a` and then `module load anaconda/VERSION`

## Create Slurm Scripts
Follow this [tutorial](https://www.arch.jhu.edu/short-tutorial-how-to-create-a-slurm-script/) to understand how to create slurm scripts (.sh extensions). This is the file that will actually be run on the cloud. If you wanted to create a script to test things, run `nano test.sh` to open up a new file and then follow the previous link to create the file. To save the file, press `CNTRL X` and then `Y` and then `Return`.
- It is good practice to include output and error files to help you debug and check results


## Overview of Important Supercloud Commands
1. `LLsub file.sh` will run a slrum script named `file.sh` on the cloud. 
2. As soon as this is done, you can run `LLstat` to view all jobs running on this account at this moment. The leftmost column will contain the ID of the running job. It will probably say `PENDING` in the `STATE` columns; this will probably change a few moments later when it begins to run. 
3. If you are creating output or error logs, you will see them appear in your current directory. They will probably be of the form `error_JOB_ID.txt` and `output_JOB_ID`.txt (where JOB ID is the number found using LLstat). They are extremely useful for debugging and checking results. 
4. If needed, `LLkill JOB_ID` will stop the job running with the corresponding ID.  

## Cleanup
Storage Efficiency is extremely important on SuperCloud acccounts, so make sure to delete all unecessary files (like output or errors logs) after you are done. 
1. To remove a directory and all of its contents, run `rm -rf directory_name`
2. To remove a file, run `rm -r file_name`

For instance, a clean up may look like:
```
rm -rf test_results
rm -r error_1238912.txt
rm -r output_1238912.txt
```


