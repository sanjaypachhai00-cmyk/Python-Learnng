#pip :python's package Installer  :allows to install external python libraries



# # ===== PIP =====
# python -m pip install pkg                # install
# python -m pip install pkg==1.2.3         # exact version
# python -m pip install --upgrade pkg      # upgrade
# python -m pip uninstall pkg              # remove
# python -m pip list                       # list installed
# python -m pip show pkg                   # details
# python -m pip freeze > requirements.txt  # save
# python -m pip install -r requirements.txt# restore

# # ===== VENV =====
# python -m venv venv                      # create

# source venv/bin/activate                 # activate (Linux/Mac)
# venv\Scripts\activate                    # activate (Windows cmd)
# venv\Scripts\Activate.ps1                # activate (Windows PowerShell)

# deactivate                               # exit venv

# # ===== VERIFY =====
# which python                             # Linux/Mac
# where python                             # Windows
# python -c "import sys; print(sys.executable)"