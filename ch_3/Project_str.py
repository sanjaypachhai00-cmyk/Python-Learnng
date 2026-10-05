#Small Project

# my_project/
# │
# ├── main.py
# ├── functions.py
# ├── requirements.txt
# └── README.md

#eg.    - calculator.py
def add(a, b):
    return a + b

          #  -main.py
from calculator import add
result = add(10, 20)
print(result)


#MEDIUM PROJECTS
# my_project/
# │
# ├── main.py                                   -starts the aplication
# ├── config.py                                 -configuration/setting
# │
# ├── models/                                   -database structure/database model
# │   ├── user.py
# │   └── product.py
# │
# ├── services/                                 -main business logic
# │   ├── user_service.py
# │   └── product_service.py
# │
# ├── utils/                                    -reusable helper functions
# │   └── helpers.py
# │
# ├── tests/                                   -testing code
# │   └── test_user.py 
# │
# ├── requirements.txt                        -required python packages
# ├── .gitignore                              -files python should ignore
# └── README.md                               -project documentation

#eg.
# ch_3/
# │
# ├── app.py
# ├── db.py
# ├── use_api.py
# ├── users.db
# ├── requirements.txt
# └── .gitignore
