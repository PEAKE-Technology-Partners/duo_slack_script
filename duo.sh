cd ~/testDuo
cd duo_client_python
virtualenv .env
source .env/bin/activate
pip install --requirement requirements.txt
pip install --requirement requirements-dev.txt
python setup.py install
cd examples
python3 peake.py
