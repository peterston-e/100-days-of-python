#  Nesting a dictionary in a dictionary

travel_log = {
    "France": {"cities_visited": ["paris", "lille", "Dijon"], "total_burgers": 100},
    "America": {"States_visited": ["florida", "california", "Washington"], "total_burgers": 5000},
}

# Nesting a dictionary in a list

travel_log = [
    {
        "country": "france",
        "cities_visited": ["paris", "lille", "Dijon"],
        "total_burgers": 100,
    },
    {
        "country": "America",
        "States_visited": ["florida", "california", "Washington"],
        "total_burgers": 5000,
    },
]
