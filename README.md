
# Spaceship Game

This an interesting game where you're the last warrior in the space, don't let you kill, save galaxy!.

# Used Technologies

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![Adobe Photoshop](https://img.shields.io/badge/adobe%20photoshop-%2331A8FF.svg?style=for-the-badge&logo=adobe%20photoshop&logoColor=white)

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## Authors

- [@Carlos Mauricio Ospino](https://github.com/practicaldev-jala)


## Features

- Data Dashboard
- Level Handler (5 Levels)
- Final Level (Boss Enemy)
- Enemy lives Tag
- New Powers (Destruction, Health)
- Bullet Collision
- Player and enemies lives
- Timer
- Added Sound

## Data Dashboard
The data stored in the dashboard is the following:

- Score
- Specific Killed enemies
- Deaths
- Game Durations
- Game history (saved dashboards)

## Level Handler (5 Levels)
This level handler allow to create multiple levels and custom configuration by each one.

### Level 1
This level contains the next configuration:
- GAME SPEED -> 10
- EMENY LIMIT -> 7
- ENEMY_SPAWN_DELAY -> between 1000 and 3000 (ms)
- DEFAULT ENEMIES -> Ship
- POWER LIMIT -> 1
- POWER SPAWN_DELAY -> between 3000 and 7000 ms
- DEFAULT POWERS -> Shield

### Level 2
This level contains the next configuration:
- GAME SPEED -> 11
- EMENY LIMIT -> 10
- ENEMY_SPAWN_DELAY -> between 1000 and 2000 (ms)
- DEFAULT ENEMIES -> Gladiator
- POWER LIMIT -> 3
- POWER SPAWN_DELAY -> between 1000 and 1500 ms
- DEFAULT POWERS -> Shield and Heart

### Level 3
This level contains the next configuration:
- GAME SPEED -> 12
- EMENY LIMIT -> 12
- ENEMY_SPAWN_DELAY -> between 1000 and 1500 (ms)
- DEFAULT ENEMIES -> Striker
- POWER LIMIT -> 5
- POWER SPAWN_DELAY -> between 1000 and 1500 ms
- DEFAULT POWERS -> Shield, Destructor and Heart

### Level 4
This level contains the next configuration:
- GAME SPEED -> 13
- EMENY LIMIT -> 15
- ENEMY_SPAWN_DELAY -> between 500 and 1000 (ms)
- DEFAULT ENEMIES -> Shield, Destructor and Heart
- POWER LIMIT -> 10
- POWER SPAWN_DELAY -> between 1000 and 2000 ms
- DEFAULT POWERS -> Shield, Destructor and Heart

### Level 5
This level contains the next configuration:
- GAME SPEED -> 13
- EMENY LIMIT -> 1
- DEFAULT ENEMIES -> Evil Cat
- POWER LIMIT -> 30
- POWER SPAWN_DELAY -> between 500 and 800 ms
- DEFAULT POWERS -> Shield, Destructor and Heart

## Final Level (Boss Enemy)
This Enemy dies with 30 hits and has a different movement

![Evil Cat](https://github.com/practicaldev-jala/Spaceship-Game-CO-5-2023/blob/main/game/assets/Enemy/enemy_final.png?raw=true)

## Powers (Shield, Destruction, Health)

### Shield
![Shield](https://github.com/practicaldev-jala/Spaceship-Game-CO-5-2023/blob/main/game/assets/Other/shield.png?raw=true)
Makes player inmortal by random seconds

### Destructor

![Destructor](https://github.com/practicaldev-jala/Spaceship-Game-CO-5-2023/blob/main/game/assets/Other/fire.png?raw=true)
Allows player to destroy bullets and enemies just touching them.

### Heart
![Heart](https://github.com/practicaldev-jala/Spaceship-Game-CO-5-2023/blob/main/game/assets/Other/heart.png?raw=true)
Gives player health.

## Bullet Collision
This feature makes a nice collision between player bullets and enemy bullets
