# Counter Strike 2 Web Panel
![Docker Image Size (tag)](https://img.shields.io/docker/image-size/theagent1/cs2webpanel/latest)

**THIS PROJECT IS NEW, EXPECT BUGS**
This project is a Flask based control panel written in Python for a locally hosted Counter Strike 2 container. Updates are ocassional, and depend on Valve releasing game updates, or requests from my local group.



## Local Setup
1. Pull the required files from the repo
2. Use `pip` to install the required packages
```python
pip install -r requirements.txt
```
3. Modify the environment variable defaults, or create a .env to override the defaults
3.5. if you decide to use a .env file, uncomment lines 17 & 18 to make use of the .env
4. Run the file
```python
python app.py
```

## Docker Setup
Image: `theagent1/cs2webpanel:latest`

This image uses multiple environment variables to configure different aspects
|Variable     |Description                                           |Default Value|
|-------------|------------------------------------------------------|-------------|
|CS2_CONTAINER|Local name of the CS2 container to be controlled      | cs2         |
|RCON_HOST    |Private IP address of the CS2 container               |192.168.1.41 |
|RCON_PASSWORD|Remote Console password configured on CS2 container   |None         |
|RCON_PORT    |Port of the Rcon server running from the CS2 container|27015        |
|WEB_PORT     |Port to open to allow users access                    |5000         |

there are also a few users configured under the line `users`, which can be modified as needed. these are exposed as environment variables for simplicity in a `dockercompose.yml`


## License

[MIT](https://choosealicense.com/licenses/mit/)