"""
virtual envs are used to protect integrity of projects
 which have similar dependencies

when you update a package some projects may get corrupt so
 you need to setup a specific enviroment for each project

----------------------------------------------------------

pip install virtualenv

mkdir Enviroments

cd Enviroments

virtualenv project1_env # this creates an env named project1_env

source project1_env/bin/activate

# this will activate the env from now on any package you install
  will remain in here

pip install numpy

pip install pytz

pip install psutil

pip list

pip freeze --local # takes only the local packages in the env

deactivate # this closes the env and returns to global env

rm -rf project1_env # this is all you need to do to remove an env


virtualenv -p /usr/bin/python2.6 py26_env

# this lets us specify the python version to use

!!! Do not store your project files within the env folder!!!
"""
