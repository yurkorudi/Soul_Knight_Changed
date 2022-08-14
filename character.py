# Sates: Hello, Stand, Stand_left, Stand_right, Go_left, Go_right, Go_up, Go_down


class Character:
    def __init__(self, pygame, path_to_sprite, coords, o_s):
        os = o_s
        self.pygame = pygame
        self.STATE = 's=Stand'
        self.up_list = []
        self.down_list = []
        self.left_list = []
        self.right_list = []
        self.stand_list = []
        print("Character is running")

        for i in range(len(os.listdir(path_to_sprite+'/Up'))):
            image = pygame.image.load(path_to_sprite+'/Up/'+str(i)+'.gif').convert()
            #image = pygame.transform.scale(image, (200, 200))
            image.set_colorkey((153, 153, 153))
            self.up_list.append(image)
        print('Done with: ', self.up_list)

        for i in range(len(os.listdir(path_to_sprite+'/Down'))):
            image = pygame.image.load(path_to_sprite+'/Down/'+str(i)+'.gif').convert()
            #image = pygame.transform.scale(image, (200, 200))
            image.set_colorkey((153, 153, 153))
            self.down_list.append(image)
        print('Done with: ', self.down_list) 

        for i in range(len(os.listdir(path_to_sprite+'/Left'))):
            image = pygame.image.load(path_to_sprite+'/Left/'+str(i)+'.gif').convert()
            #image = pygame.transform.scale(image, (200, 200))
            image.set_colorkey((153, 153, 153))
            self.left_list.append(image)
        print('Done with: ', self.left_list)

        for i in range(len(os.listdir(path_to_sprite+'/Right'))):
            image = pygame.image.load(path_to_sprite+'/Right/'+str(i)+'.gif').convert()
            #image = pygame.transform.scale(image, (200, 200))
            image.set_colorkey((153, 153, 153))
            self.right_list.append(image)
        print('Done with: ', self.right_list)

        for i in range(len(os.listdir(path_to_sprite+'/Stand'))):
            image = pygame.image.load(path_to_sprite+'/Stand/'+str(i)+'.png').convert()
            image = pygame.transform.scale(image, (150, 112))
            #image.set_colorkey((153, 153, 153))
            self.stand_list.append(image)
        print('Done with: ', self.stand_list)
        self.image = image

    
    def change_sprite(self):
        if self.STATE == 'go_left':
            try:
                self.image = self.left_list[self.left_right_frame]
                self.left_right_frame +=1
            except:
                self.left_right_frame = 0
                self.image = self.left_list[self.left_right_frame]
                self.left_right_frame += 1
        elif self.STATE == 'go_right':
            try:
                self.image = self.right_list[self.left_right_frame]
                self.left_right_frame +=1
            except:
                self.left_right_frame = 0
                self.image = self.right_list[self.left_right_frame]
                self.left_right_frame += 1
        elif self.STATE == 'go_up':
            try:
                self.image = self.up_list[self.up_down_frame]
                self.up_down_frame +=1
            except:
                self.up_down_frame = 0
                self.image = self.up_list[self.up_down_frame]
                self.up_down_frame += 1
        elif self.STATE == 'go_down':
            try:
                self.image = self.down_list[self.up_down_frame]
                self.up_down_frame +=1
            except:
                self.up_down_frame = 0
                self.image = self.down_list[self.up_down_frame]
                self.up_down_frame += 1
        else:
            self.image = self.stand_list[0]



    def draw(self, where):
        where.blit(self.image, (400, 400))
        print("drowing sprite")
        



