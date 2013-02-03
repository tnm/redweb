Installation
---------------

After you've created your fork you probably want to work in a virtualenv:

     #git clone .... redweb
     pip install virtualenv
     cd redweb
     virtualenv --distribute venv
     source venv/bin/activate

Then use the requirements file to get redweb up and running:

     pip install -r requirements.txt

Fire it up:

     cd redweb/ && python redweb.py


