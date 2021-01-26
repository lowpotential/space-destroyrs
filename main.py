def on_a_pressed():
    global dart
    dart = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . 2 . . . . . . . 
                    . . . . 2 2 2 2 4 2 . . . . . . 
                    . . . 2 4 4 2 2 2 4 2 . . . . . 
                    . . 2 2 4 4 6 6 2 2 4 2 2 . . . 
                    . 2 2 2 4 4 2 2 2 4 2 2 . . . . 
                    . . 2 2 2 2 2 2 4 2 2 2 . . . . 
                    . . . 2 2 2 2 2 2 2 . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        spacePlane,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(100)
    music.pew_pew.play()
    otherSprite.destroy(effects.fire, 500)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy(effects.ashes, 500)
    music.wawawawaa.play()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

bogey: Sprite = None
dart: Sprite = None
spacePlane: Sprite = None
spacePlane = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . 8 8 . . . . . . . . 
            . . . . . . . 2 2 . . . . . . . 
            2 2 . . 2 8 8 2 2 2 6 . . . . . 
            4 2 2 f f 8 8 8 2 2 6 6 . . . . 
            4 2 5 2 f 2 8 8 8 2 2 6 6 . . . 
            5 2 2 f f 2 2 8 8 8 2 2 2 2 . . 
            2 2 . . 2 2 2 2 8 8 8 2 2 . . . 
            . . . . . . f . . . f . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
spacePlane.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.set_life(100)
controller.move_sprite(spacePlane, 200, 200)
music.play_melody("C E F F G G F C ", 120)

def on_update_interval():
    global bogey
    bogey = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . 5 5 . . . . . . . . . 5 5 . 
                    . . . . 5 . . . . . . . 5 5 . . 
                    . . . . 5 5 . . . . . . 5 . . . 
                    . . . . . 5 . . . f f 2 . . . . 
                    . . . . . . 6 6 2 f 2 4 . . . . 
                    . . . . . 6 6 . 2 f 2 4 4 . . . 
                    . . . . 2 . . . 2 f 2 2 . . . . 
                    . . . . . 2 2 2 2 f f . . . . . 
                    . . . . . 5 . . . . . 5 . . . . 
                    . . . . 5 . . . . . . . 5 5 . . 
                    . . . 5 5 . . . . . . . . 5 5 . 
                    . . 5 5 . . . . . . . . . . 5 . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    bogey.set_position(160, 0)
    bogey.set_velocity(-100, 0)
    bogey.y = randint(0, scene.screen_height())
    bogey.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(500, on_update_interval)
