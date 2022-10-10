import pygame
from monster import Monster
from player import Player


# classe du jeu
class Game:
    
    def __init__(self):
        # jeu a commence ou non 
        self.is_playing = False
        # joueur 
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        
        
    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        self.player.rect.x = 0
        
    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        
    def update(self, screen):
        # image joueur
        screen.blit(self.player.image, self.player.rect)
        
        # barre de vie du joueur
        self.player.update_health_bar(screen)
        
        # recuperer les projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()
        
        # images projectile
        self.player.all_projectiles.draw(screen)
        
        # recuperer les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
        
        # images monstre
        self.all_monsters.draw(screen)
        
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        
    def spawn_monster(self):
        self.all_monsters.add(Monster(self))
        