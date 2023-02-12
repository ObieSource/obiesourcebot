# Installation instructions

## NOTE
This bot requires python version >3.11

- Go to the [discord developers portal](https://discord.com/developers/applications) and create an application and bot for yourself (for testing).
- Copy the bot secret token for later.
- After cloning the repository, create a virtual environment and install dependencies

```python
python3.11 -m venv venv
venv/bin/pip3 install -r requirements.txt
```

- Start the bot in the following way

```bash
venv/bin/python3 main.py <SECRET TOKEN>
```
