#! /usr/bin/env python3

class GardenError(Exception):  # A basic error for garden problems
    pass


class PlantError(GardenError):  # For problems with plants
    pass


class WaterError(GardenError):  # For problems with watering
    pass


