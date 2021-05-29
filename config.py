""" The game's constants/configuration """

BOARD_WIDTH = 40
BOARD_HEIGHT = 16

# Terrain Tiles

GRASS_TILE = [['#5cb528', '#569e2c', '#54b048'],
              ['#58b34d', '#40b334', '#54b048'],
              ['#5cb528', '#5cb528', '#569e2c']]

WATER_TILE = [['#0044ff', '#2d79eb', '#0044ff'],
              ['#2d79eb', '#0044ff', '#081cfc'],
              ['#081cfc', '#0044ff', '#2d79eb']]

# main: #0044ff
# darker: #081cfc
# lighter: #2d79eb

# Structure Tiles

ROAD_TILE = [[None, '#4a2912', None],
             ['#4a2912', '#6b3c1c', '#874f29'],
             [None, '#874f29', None]]

CITY_TILE = [[None, '#595858', None],
             ['#595858', '#595858', '#595858'],
             ['#595858', '#595858', '#595858']]

# main: #6b3c1c
# darker: #4a2912
# lighter: #874f29


# Unit Tiles

SETTLER_UNIT = [[None, '#528c35', None],
                [None, '#dadbd7', None],
                [None, None, None]]
# USE THIS HEX IF IT BLENDS INTO THE GRASS: e8e117

WARRIOR_UNIT = [[None, '#eb441e', None],
                [None, '#dadbd7', None],
                [None, None, None]]

WORKER_UNIT = [[None, '#eda915', None],
               [None, '#dadbd7', None],
               [None, None, None]]

CLOUD_TILE = [['#010502', '#010502', '#010003'],
              ['#010101', '#010002', '#000302'],
              ['#010005', '#030002', '#010503']]

# 7x7 selection outline
OUTLINE_COLOURS = {
    'America': '#9999FF',
    'Spain': '#FFFF99',
    'Russia': '#FF9999',
    'Australia': '#',
    'China': '#',
    'Britain': '#',
    'Germany': '#'
}


# Default city names
DEFAULT_CITY_NAMES = {
    'Spain': ['Madrid', 'Barcelona', 'Valencia', 'Seville', 'Zaragoza', 'Palma', 'Bilbao', 'Alicante', 'Cordova'],
    'America': ['Washington', 'New York', 'Philadelphia', 'Boston', 'Baltimore', 'Charleston',
                'New Orleans', 'Cincinnati', 'Los Angeles'],
    'Russia': ['Moscow', 'St.-Petersburg', 'Sverdlovsk', 'Nizhny', 'Samara', 'Omsk', 'Tatarstan', 'Rostov', 'Chelyabinsk'],
    'Australia': ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide', 'Gold Coast', 'Canberra', 'Newcastle', 'Geelong'],
    'China': ['Shanghai', 'Beijing', 'Tianjin', 'Guangzhou', 'Shenzhen', 'Dongguan', 'Chongqing', 'Nanjing', 'Nanchong'],
    'Britain': ['London', 'Birmingham', 'Liverpool', 'Sheffield', 'Bristol', 'Glasgow', 'Leicester', 'Edinburgh', 'Leeds'],
    'Germany': ['Berlin', 'Hamburg', 'Munich', 'Cologne', 'Essen', 'Stuttgart', 'Dortmund', 'Bremen', 'Leipzig'],
}

# Infobox rendering
VIEW_TEXTS = {
    'city': 'CITY VIEW',
    'unit': 'UNIT VIEW',
    'production': 'PRODUCTION VIEW'
}

# Map generation
WATER_COLOUR = (0, 0, 255)
DIFF_THRESHOLD = 230
