## Easy IMU Setup Python Codes
This consist of set of step by step codes to help calibrate, compute necessary covariances, and visualize the filtered readings of the **`Easy IMU Module`** (i.e **`MPU9250 EIMU MODULE`**). 
The application codes requires that you have the **`Easy IMU Module`** connected to your PC.


### Running the Python Codes (Using python virtual environment)

#

#### Prequisite
- This would run on linux (ubuntu), windows, and MAC

> [!NOTE]  
> For Windows and Mac Users, ensure you have the **`CH340 serial converter`** or the **`FTDI`** driver installed. (depending on the module you are using)

- Ensure you have `python3` installed on your PC and also `pip`

- install python virtual environment
  ```shell
    pip3 install virtualenv   //linux or mac
  ```
  ```shell
    pip install virtualenv   //windows
  ```
- Ensure you have the **`Easy IMU Module`** connected to the PC.

#

#### Run App First Time [ linux or mac ]
- Download (by clicking on the green Code button above) or clone the repo into your PC using **`git clone`**
  > you can use this command if you want to clone the repo:
  >
	>  ```git clone https://github.com/samuko-things-company/eimu_setup_py_codes.git```

- change directory into the root **`eimu_setup_py_codes`** folder

- create a python virtual environment named **`.env`** in the root folder 
  ```shell
    python3 -m venv .env
  ```
- activate the virtual environment
  ```shell
    source .env/bin/activate
  ```
- you should see now that you are in the **`.env`** virtual environment

- install all required python modules
  ```shell
    pip3 install -r requirements.txt
  ```
- now you can run the codes step by step

- once you are done, just close and dectivate the environment
  ```shell
    deactivate
  ```

#### Run App [ linux or mac ]
- change directory into the root **`eimu_setup_py_codes`** folder

- activate the virtual environment
  ```shell
    source .env/bin/activate
  ```
- you should see now that you are in the **`.env`** virtual environment

- now you can run the codes step by step

- once you are done, just close and dectivate the environment
  ```shell
    deactivate
  ```

#

#### Run App First Time [ Windows ]
- Download (by clicking on the green Code button above) or clone the repo into your PC using **`git clone`**
  > you can use this command if you want to clone the repo:
  >
	>  ```git clone https://github.com/samuko-things-company/eimu_setup_py_codes.git```

- change directory into the root **`eimu_setup_py_codes`** folder

- create a python virtual environment named **`.env`** in the root folder 
	```shell
    python3 -m venv .env
  ```
- activate the virtual environment
  ```shell
    env/Scripts/activate.bat //In CMD  or
    env/Scripts/Activate.ps1 //In Powershel
  ```
- you should see now that you are in the **`.env`** virtual environment

- install all required python modules
  ```shell
    pip install -r requirements.txt
  ```
- now you can run the codes step by step

- once you are done, just close and dectivate the environment
  ```shell
    deactivate
  ```

#### Run App [ Windows ]
- change directory into the root folder **`eimu_setup_py_codes`**

- activate the virtual environment
  ```shell
    env/Scripts/activate.bat //In CMD   or
    env/Scripts/Activate.ps1 //In Powershel
  ```
- you should see now that you are in the **`.env`** virtual environment

- now you can run the codes step by step

- once you are done using the application, just close and dectivate the environment
  ```shell
    deactivate
  ```