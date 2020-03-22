# ⚔️ Project Katana - Production ML
> Katana project is a pre-built bioler plate code for production level model deployement. 

## Features 💫
1. Flask Restx at your rescue
2. Swagger UI and gunicorn integration
3. Docker ready configuration
4. Integrated GitHub actions
5. Almost ready deployement code 🚀

![Katana](screenshots/swagger.png)

## Set-up Instructions 🕺
For develoment and testing purposes we recommend using flask serving with debug turned on. However, the code supports `gunicorn` grade serving functionality as well. 

Katana demo API is like at - https://katana-demo.herokuapp.com/

We included following setup instructions;

1. Local development 
2. Docker supported deployement


### Local Development 👨🏻‍💻
1. Clone this repo with `git@github.com:shaz13/katana.git`
2. Set up environment using `python3 -m venv .env`
3. Activate envrionment using 
```
# Linux / Mac / Unix
$ source activate .env/bin/activate

# Windows
.\env\Scripts\activate
```
4. Install requirements using `pip install -r requirements.txt`
5. For debugging run from root - `python main.py`
6. Deploy using `Procfile` or `bash scripts/start.sh`
7. Your API is being served at `localhost:9000`

### Docker Setup ⛴
1. Clone this repo with `git@github.com:shaz13/katana.git`
2. Install docker in your system
3. Run `docker-compose up`
4. Your local port is mapped and being served at `localhost:9000`



## Contributors
1. Aditya Soni - @AdityaSoni19031997

## License
TDB