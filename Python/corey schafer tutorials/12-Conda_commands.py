"""
conda -- help

conda list

conda search

conda install

conda update anaconda

conda update all # NOT RECOMMENDED

-----conda env----

# create an env named my_app with some starter packages

conda create --name my_app flask numpy matplotlib

activate my_app # windows

source activate my_app # linux

deactivate # windows

source deactivate # linux

# custom python version env
conda create --name my_app27 python=2.7 flask numpy matplotlib

activate my_app27

which python

deactivate

conda env list # lists out all available envs

conda remove --name my_app --all # deletes the entire env

conda remove --name my_app27 --all

"""
