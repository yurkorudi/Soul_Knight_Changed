# Sates: hello, stand, stand_left, stand_right, go_left, go_right, go_up, go_down
import os, os.path
class Character:
    def __init__(self, pygame, path_to_sprite, coords):
        self.STATE = 'stand'
        self.up_list = []
        self.down_list = []
        self.left_list = []
        self.right_list = []
        self.stand_list = []
        print("Character is running")


        for i in range(len(os.listdir(path_to_sprite+'/Up'))):
            image = pygame.image.load(path_to_sprite+'/Up/'+str(i+1)+'.gif').convert()
            image = pygame.transform.scale(image, (200, 200))
            image.set_colorkey((255, 255, 255))
            self.up_list.append(image)
        print('Done with: ', self.up_list)

        for i in range(len(os.listdir(path_to_sprite+'/Down'))):
            image = pygame.image.load(path_to_sprite+'/Down/'+str(i+1)+'.gif').convert()
            image = pygame.transform.scale(image, (200, 200))
            image.set_colorkey((255, 255, 255))
            self.down_list.append(image)
        print('Done with: ', self.down_list)

        for i in range(len(os.listdir(path_to_sprite+'/Left'))):
            image = pygame.image.load(path_to_sprite+'/Left/'+str(i+1)+'.gif').convert()
            image = pygame.transform.scale(image, (200, 200))
            image.set_colorkey((255, 255, 255))
            self.left_list.append(image)
        print('Done with: ', self.left_list)

        for i in range(len(os.listdir(path_to_sprite+'/Right'))):
            image = pygame.image.load(path_to_sprite+'/Right/'+str(i+1)+'.gif').convert()
            image = pygame.transform.scale(image, (200, 200))
            image.set_colorkey((255, 255, 255))
            self.right_list.append(image)
        print('Done with: ', self.right_list)

        for i in range(len(os.listdir(path_to_sprite+'/Stand'))):
            image = pygame.image.load(path_to_sprite+'/Stand/'+str(i+1)+'.gif').convert()
            image = pygame.transform.scale(image, (200, 200))
            image.set_colorkey((255, 255, 255))
            self.stand_list.append(image)
        print('Done with: ', self.stand_list)