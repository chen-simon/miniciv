# MiniCIV

MiniCiv is an 8-bit local-multiplayer browser-game recreation of Sid Meier's Civilization (1991) where players can play a Civ game with a map they can pick as anywhere in the world. Upon starting their game, players can choose their Civilization and their map using a Google Maps interactive map, and are then put into a game where they can found cities, build roads, create warriors to defend themselves, choose the production of their cities, all like an actual miniature Civ game! 🏙

Submission for MLH Hack-cade 2021 ([Devpost](https://devpost.com/software/miniciv))
 
Created by [Simon Chen](https://github.com/SimonChenWasTaken) and  [Zhenia Sigayev](https://github.com/zheniasigayev)

## Installation Instructions

1. Clone the repository to your machine.
1. Open `api_key.py` and assign your Google Cloud API key to the variable `API_KEY`. (Make sure you have Google Maps Static API and Google Maps Javascript API enabled in your Google Cloud console!)
1. Either install all the packages listed in `requirements.txt`, or create a virtual environment using those modules. (Note: The PyCharm IDE automatically detects `requirements.txt` and suggests to create a virtual environment with those as dependencies.)
1. Run `server.py`. (If you made a virtual environment, make sure you are using the correct interpreter!)
1. Open http://localhost:5000/ in the browser 
1. Game on! 🕹️😊
