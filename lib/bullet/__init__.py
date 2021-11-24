import pygame

from .. import sprite
from .. import globals

import lib.sprite.explosion

r = globals.stgSurface.get_rect()
bulletBoundary = pygame.Rect(-30, -30, r.width + 60, r.height + 60)

class Bullet(sprite.Sprite):
    damage: int = 0
    size: float = 0
    speedRadius: float = 0

    def __init__(self, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)
        self.speed = pygame.Vector2()
        self.boundary = bulletBoundary

    def update(self, *args, **kwargs) -> None:
        self.speed.from_polar((self.speedRadius, -self.angle - 90))

        super().update(*args, **kwargs)

        if self.outOfBoundary:
            self.kill()

    def explode(self) -> None:
        self.kill()
        lib.sprite.explosion.ExplosionBullet(self.position)