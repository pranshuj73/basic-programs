from csv import reader
from settings import tile_size
import pygame


def import_csv_layout(path):
    terrain_map = []
    with open(path, 'r') as map:
        level = reader(map, delimiter=',')
        for row in level:
            terrain_map.append(list(row))

        return terrain_map


def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = surface.get_size()[0] // tile_size
    tile_num_y = surface.get_size()[1] // tile_size

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size
            new_surface = pygame.Surface((tile_size, tile_size))
            new_surface.blit(surface, (0, 0), (x, y, tile_size, tile_size))
            cut_tiles.append(new_surface)

    return cut_tiles