controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    dart = sprites.createProjectileFromSprite(img`
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
        `, spacePlane, 200, 0)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    info.changeScoreBy(100)
    music.pewPew.play()
    otherSprite.destroy(effects.fire, 500)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap2(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy(effects.ashes, 500)
    music.wawawawaa.play()
    info.changeLifeBy(-1)
})
let bogey : Sprite = null
let dart : Sprite = null
let spacePlane : Sprite = null
spacePlane = sprites.create(img`
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
    `, SpriteKind.Player)
spacePlane.setFlag(SpriteFlag.StayInScreen, true)
info.setLife(100)
controller.moveSprite(spacePlane, 200, 200)
music.playMelody("C E F F G G F C ", 120)
game.onUpdateInterval(500, function on_update_interval() {
    
    bogey = sprites.create(img`
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
        `, SpriteKind.Enemy)
    bogey.setPosition(160, 0)
    bogey.setVelocity(-100, 0)
    bogey.y = randint(0, scene.screenHeight())
    bogey.setFlag(SpriteFlag.AutoDestroy, true)
})
