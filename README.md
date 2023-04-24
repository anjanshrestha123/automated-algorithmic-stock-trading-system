# Automated Algorithmic Stock Trading System

## How to set up whole application in Azure:

### 1. Setup server:
- Create Azure Virtual Machine
- Open port 5002 from networking (API runs on this port)
- Create DNS name for this machine

### 2. Modify stockTradingBackendUrl in automated-algorithmic-stock-trading-system/frontend/src/environments/environment.test.ts with virtual machine public IP address or DNS name

### 3. Set up repository in server:
- ssh csce5214@20.228.243.128 (replace with new ip address and enter password)
- mkdir develop
- git clone https://github.com/anjanshrestha123/automated-algorithmic-stock-trading-system.git

### 4. Set up backend API:
- sudo apt install python3-pip
- pip install flask
- pip install flask_cors
- pip install nbformat
- pip install --upgrade pip ipython ipykernel
- ipython kernel install --name "python3" --user
- pip install pandas
- pip install numpy
- pip install yfinance
- pip install matplotlib
- pip install sklearn
- pip install scikit-learn
- pip install alpaca
- pip install alpaca-py
- pip install alpaca-trade-api
- pip install tensorflow
- cd automated-algorithmic-stock-trading-system/backend/api/
- python3 run.py
- nohup python3 run.py & (if want to run in background)
- tail -f nohup.out (for checking logs)

### 5. Set frontend application:
- cd automated-algorithmic-stock-trading-system/frontend/
- sudo apt-update
- sudo curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash 
- source ~/.bashrc
- sudo nvm install 14
- sudo npm install -g @angular/cli
- sudo npm cache clean -f
- sudo npm install -g n
- sudo n 14
- sudo npm install
- npm start
- nohup npm start & (if want to run in background)
- tail -f nohup.out (for checking logs)

### 6. Delete today's file for traded stock info from automated-algorithmic-stock-trading-system/backend/trading-system/output/

### 7.  Can be accessed at (replate host name with new host name): http://csce-5214-group-8.eastus.cloudapp.azure.com/#/stock-trading-system
