"""

Use anaconda and conda for ev handling

mkdir my_projet

cd my_project

conda create python=3.6 --name my_project_env flask numpy

source activate my_project_env

pip list

conda env export > enviroment.yaml # Enviroment backup

cat enviroment.yaml

# env recovery
# conda env create -f enviroment.yaml

------------- Env Vars Manegement --------------

Env vars helps to access sensitive data without including them within code

conda env list

cd /env/my_project_env

mkdir -p etc/conda/activate.d

mkdir -p etc/conda/deactivate.d

touch etc/conda/activate.d/env_vars.sh

touch etc/conda/deactivate.d/env_vars.sh

--------------------- activate.d/env_vars.sh

#!/bin/sh
export DATABASE_URI="postgresql://user:pass@db_server:5432/test_db"

# DATABASE_URI is a makeshift variable with login info

--------------------- deactivate.d/env_vars.sh

#!/bin/sh
unset DATABASE_URI

---------------------

source deactivate

source activate

echo $DATABASE_URI # this will return the variable

source deactivate

echo $DATABASE_URI
# this will NOT return the variable
# beacuse env is not active

# this way you can have env_vars for each project

------------------Example Project------------------------------

cd ~/Projects/web_project

cat enviroment.yaml

conda env list

cd ~/anaconda/envs/web_project_env

ls # to see if tihs env has avtivate and deactivate scripts

source activate web_project_env

echo $DATABASE_URI

python # to check for python version

>>>exit()

---------------------------------------------------------------

"""
