##This file contains the mapping of all the coils to the corresponding pins on the Arduino MEGA, G stands for GPIO

##List containing pin mapping fo Laptop charging coils
arduino_laptop = {
    15: "G,34,38",
    26: "G,37,41",
    37: "G,36,40",
    48: "G,37,41"
    #5: "G,40",
    #6: "G,41"
}

##List containing pin mapping fo Phone 1 charging coils
arduino_phone1 = {
    1: "G,22,27",
    2: "G,23,27",
    3: "G,24,27",
    4: "G,25,27",
    5: "G,26,27",
    6: "G,22,28",
    7: "G,23,28",
    8: "G,24,28",
    9: "G,25,28",
    10: "G,26,28",
    11: "G,22,29",
    12: "G,23,29",
    13: "G,24,29",
    14: "G,25,29",
    15: "G,26,29",
    16: "G,22,30",
    17: "G,23,30",
    18: "G,24,30",
    19: "G,25,30",
    20: "G,26,30",
    21: "G,22,31",
    22: "G,23,31",
    23: "G,24,31",
    24: "G,25,31"
}

##List containing pin mapping fo Phone 2 charging coils
arduino_phone2 = {
    1: "G,53,48",
    2: "G,52,47",
    3: "G,51,46",
    4: "G,50,45",
    5: "G,49,44",
    6: "G,53,48",
    7: "G,52,47",
    8: "G,51,46",
    9: "G,50,45",
    10: "G,49,44",
    11: "G,53,48",
    12: "G,52,47",
    13: "G,51,46",
    14: "G,50,45",
    15: "G,49,44",
    16: "G,53,48",
    17: "G,52,47",
    18: "G,51,46",
    19: "G,50,45",
    20: "G,49,44",
    21: "G,53,48",
    22: "G,52,47",
    23: "G,51,46",
    24: "G,50,45"
}

## Mobile 1 location --> coil
## Confirm location coil mapping for Mobile 1 with UFUK
mobile1_location_coil = {
    (4,  7): 13,
    (5,  7): 14,
    (6,  7): 15,
    (4,  8): 16,
    (5,  8): 17,
    (6,  8): 18, 
    (4,  9): 19,
    (5,  9): 20,
    (6,  9): 21
}

## Laptop location --> coil
## Confirm location coil mapping for laptop with UFUK
laptop_location_coil = {
    (35,  36): 15,
    (36,  36): 26, 
    (37,  36): 37,
    (38,  36): 48
}

## Mobile 2 location --> coil
mobile2_location_coil = {
    (15,  12): 1,
    (14,  12): 2,
    (13,  12): 3, 
    (15,  13): 4,
    (14,  13): 5,
    (13,  13): 6,
    (15,  14): 7,
    (14,  14): 8,
    (13,  14): 9, 
    (15,  15): 10,
    (14,  15): 11,
    (13,  15): 12, 
    (15,  16): 13,
    (14,  16): 14,
    (13,  16): 15, 
    (15,  17): 16,
    (14,  17): 17,
    (13,  17): 18, 
    (15,  18): 19,
    (14,  18): 20,
    (13,  18): 21, 
    (15,  19): 22,
    (14,  19): 23,
    (13,  19): 24
}

## Coil --> Region
coil_region = {
    (1, 2, 3): 1,
    (4, 5, 6): 2,
    (7, 8, 9): 3,
    (10, 11, 12): 4,
    (13, 14, 15): 5,
    (16, 17, 18): 6,
    (19, 20, 21): 7,
    (22, 23, 24): 8
}


## Region --> Neighbour coils
region_neighbor_coils = {region: list(coils) for coils, region in coil_region.items()}
        
