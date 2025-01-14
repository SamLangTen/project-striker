import os
import pygame
import random

import lib.globals

# 00-03 背景
# 04-09 右下外转角
# 10-15 左下外转角
# 16-21 左上外转角
# 22-27 右上外转角
# 28-29 右下内转角
# 30-31 左下内转角
# 32-33 左上内转角
# 34-35 右上内转角
# 36-41 上直线
# 42-47 右直线
# 48-53 下直线
# 54-59 左直线
# 60-60 填充
# 61-61 填充
# 62-64 填充
# 65-67 填充
# 68-70 填充
# 71-73 填充
tiles = tuple(pygame.image.load(f'assets/map-{i}.webp').convert() for i in range(74))

backgrounds = []
for x in os.listdir('scriptfiles/map'):
    with open(f'scriptfiles/map/{x}', 'r') as f:
        tileData = f.read()

        blitSequence: list[tuple[pygame.Surface, tuple[float, float]]] = []
        y = 0
        for line in tileData.splitlines():
            line = tuple(int(x) for x in line.split())
            if not line:
                continue
            for x, i in enumerate(line):
                blitSequence.append((random.choice(tiles[i]) if isinstance(tiles[i], tuple) else tiles[i], (x * 32, y * 32)))
            y += 1
        surface = pygame.Surface((384, 448))
        surface.blits(blitSequence)
        backgrounds.append(surface)

def blitBackground(surface: pygame.Surface):
    while lib.globals.backgroundSurfaces and lib.globals.backgroundScrollOffset >= 448:
        lib.globals.backgroundSurfaces.popleft()
        lib.globals.backgroundScrollOffset -= 448

    while len(lib.globals.backgroundSurfaces) < 2:
        lib.globals.backgroundSurfaces.append(random.choice(backgrounds))

    blitSequence: list[tuple[pygame.Surface, tuple[float, float]]] = []
    for i, s in enumerate(lib.globals.backgroundSurfaces):
        blitSequence.append((s, (0, i * -448 + lib.globals.backgroundScrollOffset)))
    surface.blits(blitSequence)
