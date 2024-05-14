import pygame, sys, random

#Tạo hàm cho trò chơi

#Hàm vẽ sàn của trò chơi
def draw_floor():
    screen.blit(floor,(floor_x_pos,650))
    screen.blit(floor,(floor_x_pos+432,650))

#Hàm tạo ống
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)    
    bottom_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop = (500,random_pipe_pos-650))
    return bottom_pipe, top_pipe

#Hàm di chuyển ống
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

#Hàm vẽ ống lên màn hình
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)

#Hàm kiểm tra va chạm
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            return False
    if bird_rect.top <= -75 or bird_rect.bottom >= 650:
            return False
    return True

#Hàm xoay hình ảnh của chim dựa theo hướng di chuyển của chim
def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1,-bird_movement*3,1)
    return new_bird

#Hàm đổi hình ảnh của chim theo thời gian, tạo hiệu ứng hoạt hình
def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
    return new_bird, new_bird_rect

#Hàm hiển thị điểm số và điểm cao nhất trên màn hình
def score_display(game_state):
    if game_state == 'main game':
        score_surface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center = (216,100))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'score: {int(score)}',True,(255,255,255))
        score_rect = score_surface.get_rect(center = (216,100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High score: {int(high_score)}',True,(255,255,255))
        high_score_rect = high_score_surface.get_rect(center = (216,630))
        screen.blit(high_score_surface, high_score_rect)

#Hàm cập nhật điểm cao nhất
def update_score(score,high_score):
    if score > high_score:
        high_score = score
    return high_score

#Hàm hiển thị giao diện đăng nhập
def login_screen():
    login_font = pygame.font.Font(None, 40)
    login_text = login_font.render("LOGIN", True, (255, 255, 255))

    input_box1 = pygame.Rect(100, 250, 200, 32)  # Ô nhập liệu cho tên người dùng
    input_box2 = pygame.Rect(100, 300, 200, 32)  # Ô nhập liệu cho mật khẩu
    color_inactive = pygame.Color('lightskyblue3') # Định nghĩa màu sắc cho ô nhập khi không được chọn
    color_active = pygame.Color('dodgerblue2')  # Định nghĩa màu sắc cho ô nhập được chọn
    color1 = color_inactive  # Màu sắc cho ô nhập liệu tên người dùng
    color2 = color_inactive  # Màu sắc cho ô nhập liệu mật khẩu
    active1 = False # Biến theo dõi trạng thái ô người dùng
    active2 = False
    text1 = '' #Chuỗi lưu tên người dùng
    text2= ''

    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()

    stored_username = "admin"
    stored_password = "123456"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Kiểm tra xem người dùng nhấp vào ô nhập liệu nào
                if input_box1.collidepoint(event.pos):
                    active1 = not active1
                    active2 = False
                elif input_box2.collidepoint(event.pos):
                    active2 = not active2
                    active1 = False
                else:
                    active1 = False
                    active2 = False
                color1 = color_active if active1 else color_inactive
                color2 = color_active if active2 else color_inactive
                
            if event.type == pygame.KEYDOWN:
                if active1:
                    if event.key == pygame.K_RETURN:
                        if text1 == stored_username and text2 == stored_password:
                            return (text1, text2)
                        else:
                            display_error_message("Tên người dùng hoặc mật khẩu không đúng. Vui lòng thử lại.")
                            text1 = ''  # Xóa thông tin tên người dùng
                            text2 = ''  # Xóa thông tin mật khẩu
                    elif event.key == pygame.K_BACKSPACE:
                        text1 = text1[:-1]
                    else:
                        text1 += event.unicode
                elif active2:
                    if event.key == pygame.K_RETURN:
                        if text1 == stored_username and text2 == stored_password:
                            return (text1, text2)
                        else:
                            display_error_message("Tên người dùng hoặc mật khẩu không đúng. Vui lòng thử lại.")
                            text1 = ''  # Xóa thông tin tên người dùng
                            text2 = ''  # Xóa thông tin mật khẩu
                    elif event.key == pygame.K_BACKSPACE:
                        text2 = text2[:-1]
                    else:
                        text2 += event.unicode

        screen.fill((30, 30, 30))
        
        # Vẽ chữ "Đăng nhập"
        screen.blit(login_text, (150, 200))
        
        pygame.draw.rect(screen, color1, input_box1, 2)
        pygame.draw.rect(screen, color2, input_box2, 2)
        
        text_surface1 = font.render(text1, True, (255, 255, 255))
        screen.blit(text_surface1, (input_box1.x + 5, input_box1.y + 5))
        
        text_surface2 = font.render("*" * len(text2), True, (255, 255, 255))  # Hiển thị dấu * cho mật khẩu
        screen.blit(text_surface2, (input_box2.x + 5, input_box2.y + 5))
        
        input_box1.w = max(200, text_surface1.get_width() + 10)
        input_box2.w = max(200, text_surface2.get_width() + 10)
        
        pygame.display.flip()
        
        clock.tick(30)

def display_error_message(message):
    # Hiển thị thông báo lỗi
    error_font = pygame.font.Font(None, 24)
    error_text = error_font.render(message, True, (255, 0, 0))
    screen.blit(error_text, (100, 300))
    pygame.display.flip()
    pygame.time.delay(2000)  # Hiển thị thông báo trong 2 giây

pygame.mixer.pre_init(frequency=44100, size=-16,channels=2, buffer=512)
pygame.init()
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf',40)

#Tạo màn hình kết thúc
game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (216,384))

#Tạo các biến cho trò chơi
gravity = 0.5   # Kiểm soát tốc độ rơi của chim
bird_movement = 0   # Sự chuyển động của chim khi người chơi di chuyển
game_active = False # Trạng thái trò chơi
score = 0   # Lưu điểm
high_score = 0  # Lưu điểm cao nhất
player_name = '' # Lưu tên người chơi

#Chèn Background
bg = pygame.image.load('assets/background-night.png').convert()
bg = pygame.transform.scale2x(bg)

#Chèn sàn
floor = pygame.image.load('assets/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0

#Tạo chim
bird_down = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-downflap.png').convert_alpha())
bird_mid = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-midflap.png').convert_alpha())
bird_up = pygame.transform.scale2x(pygame.image.load('assets/yellowbird-upflap.png').convert_alpha())
bird_list = [bird_down, bird_mid, bird_up] #0 1 2
bird_index = 0
bird = bird_list[bird_index]
bird_rect = bird.get_rect(center = (100,384))

#Tạo timer cho bird
birdflap = pygame.USEREVENT + 1
pygame.time.set_timer(birdflap,200)

#Tạo ống
pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []

#Tạo timer
spawpipe = pygame.USEREVENT
pygame.time.set_timer(spawpipe, 1200)
pipe_height = [200,300,400]

#Chèn âm thanh
flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
hit_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
score_sound_countdown = 100

player_name = login_screen()

#While Loop của trò chơi
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement = -11
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active==False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100,384)
                bird_movement = 0
                score = 0
        if event.type == spawpipe:
            pipe_list.extend(create_pipe())
        if event.type == birdflap:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index =0
        bird, bird_rect = bird_animation()

    screen.blit(bg,(0,0))

    if game_active:

        #Chim
        bird_movement += gravity
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird,bird_rect)
        game_active = check_collision(pipe_list)

        #Ống
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        score += 0.01
        score_display('main game')
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface,game_over_rect)
        high_score = update_score(score,high_score)
        score_display('game_over')
    
    #Sàn
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(60)
