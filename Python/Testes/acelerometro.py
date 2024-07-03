import pyvjoy
import pygame

def process_events():
    j = pyvjoy.VJoyDevice(1)
    pygame.init()
    clock = pygame.time.Clock()

    try:
        pygame.joystick.init()
        joystick_count = pygame.joystick.get_count()
        if joystick_count < 1:
            print("No joystick detected.")
            return

        joystick = pygame.joystick.Joystick(0)
        joystick.init()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    if event.axis == 0:  # X axis
                        j.data.wAxisX = int((event.value + 1) * 32767.5)
                    elif event.axis == 1:  # Y axis
                        j.data.wAxisY = int((event.value + 1) * 32767.5)
                    j.update()
                elif event.type == pygame.QUIT:
                    return
            clock.tick(60)  # Limit to 60 FPS
    finally:
        j.data.wAxisX = 16384  # Center X axis
        j.data.wAxisY = 16384  # Center Y axis
        j.update()

try:
    process_events()
except KeyboardInterrupt:
    print("Programa encerrado pelo usuário.")
