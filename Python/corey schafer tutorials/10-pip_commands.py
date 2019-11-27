"""
pip search packagename

pip install packagename

pip uninstall packagename

pip list ---> shows all installed packages

pip list -o ---> shows outdated packages

pip install -U packagename ---> updates the package

--------- Env Sharing --------
pip freeze ---> outputs all packages in current env in requirements format

pip freeze > requirements.txt ---> outputs as a file(requirements.txt)

pip install -r requirements.txt ---> installs all the required
 packages with the exact versions as listed in the file

------------------------------

pip doesn't have a way to update all outdated packages

pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U

"""
