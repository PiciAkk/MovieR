# MovieR

MovieR is a neat program for downloading and playing Hungarian movies from the command line, using your favorite video player 

*Disclaimer: the program is downloading torrent files from [nCORE](ncore.pro), which is a Hungarian-only, invitation-based torrent site*

## Installation guide

1. Clone this GitHub repository

```bash
git clone https://github.com/PiciAkk/movier
```

2. Go to the newly cloned repo's folder

```bash
cd movier
```

3. Install the dependencies

```bash
pip install -r requirements.txt
```

## Usage

1. Make a config file that contains your preferences and nCORE login informations, and save it as `config.json`

Here's an example `config.json` file

```json
{
	"login": {
		"username": "yourUsername",
		"password": "yourPassword"
	},
	"mediaPlayer": "VLC"
}
```

2. Start the app

```bash
python src/main.py
```

3. Enter a search query

4. Done! You should see your favorite movies on the screen!

# The idea for making the program

The idea came from [notflix](https://github.com/Bugswriter/notflix) - thanks, [Bugswriter](https://github.com/Bugswriter/)