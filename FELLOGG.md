# Fellogg

En rad per fel. Skriv medan du minns hur du gjorde.

| Nr | Vad stod i loggen? | Lokalt eller på GitHub? | Hur tog du reda på orsaken? | Hur löste du det? |
|----|--------------------|-------------------------|-----------------------------|-------------------|
| 1  |                    |                         |                             |                   |
| 2  |                    |                         |                             |                   |
| 3  |                    |                         |                             |                   |

Fortsätt tabellen med fler rader vid behov.


1. Att det var fel vid line 11, det stod i github actions, kollade i körningarna, gick in och kollade koden
2. Det stod i actions att uv sync inte fungerade med flaggan, github, kollade i körningarna, tog bort '--freeze' flaggan
3. Att import os fanns med men att den inte användes, github, kollade i körningarna, tog bort 'import os' då den inte användes
4. 'File would be reformatted, lokalt, körde kommndot lokalt, testade med att köra uv run ruff format
5. AssertinError, lokalt, jag läste loggarna, bytte ut siffrorna i test_moving_average_window_two