from pyfiglet import Figlet
class fig():
    @staticmethod
    def write(text,*,fontNumber=0,color="white"):
        """fonts defult 0  (from 0 to 424) 
        colors defult white from ('red', 'green', 'yellow', 'blue', 'black', 'magenta', 'cyan', 'white') you can add bright_ befor color for more brightness"""
        f = Figlet()
        fonts=f.getFonts()
        fonts[0]="slant"
        #fontNumber=0
        #color="white"
        




        f = Figlet(font=fonts[fontNumber])

        text= f.renderText(text)
        colors={"black": "\u001b[30m"
                ,"red": "\u001b[31m"
                ,"green": "\u001b[32m"
                ,"yellow": "\u001b[33m"
                ,"blue": "\u001b[34m"
                ,"magenta": "\u001b[35m"
                ,"cyan": "\u001b[36m"
                ,"white": "\u001b[37m"
                ,"bright_black": "\u001b[30;1m"
                ,"bright_red": "\u001b[31;1m"
                ,"bright_green":"\u001b[32;1m"
                ,"bright_yellow": "\u001b[33;1m"
                ,"bright_blue": "\u001b[34;1m"
                ,"bright_magenta": "\u001b[35;1m"
                ,'bright_cyan': "\u001b[36;1m"
                ,"bright_white": "\u001b[37;1m"}
        try:
            return(u""+colors[color]+""+text+ u"\u001b[0m" )
        except :
            return(u""+colors["white"]+""+text+u"\u001b[0m" )



'''
PyInquirer
Clint

fig fonts 
Font: 3-d
 ****     ****                  
/**/**   **/**                  
/**//** ** /**  ******   ****** 
/** //***  /** **////** **////**
/**  //*   /**/**   /**/**   /**
/**   /    /**/**   /**/**   /**
/**        /**//****** //****** 
//         //  //////   //////  



Font: 3x5
            
# #         
### ### ### 
### # # # # 
# # ### ### 
# #         



Font: 5lineoblique
                                    
                                    
    /|    //| |                     
   //|   // | |     ___      ___    
  // |  //  | |   //   ) ) //   ) ) 
 //  | //   | |  //   / / //   / /  
//   |//    | | ((___/ / ((___/ /   



Font: acrobatic
  o          o                            
 <|\        /|>                           
 / \\o    o// \                           
 \o/ v\  /v \o/    o__ __o      o__ __o   
  |   <\/>   |    /v     v\    /v     v\  
 / \        / \  />       <\  />       <\ 
 \o/        \o/  \         /  \         / 
  |          |    o       o    o       o  
 / \        / \   <\__ __/>    <\__ __/>  
                                          
                                          
                                          



Font: alligator
        :::   :::   ::::::::  :::::::: 
      :+:+: :+:+: :+:    :+::+:    :+: 
    +:+ +:+:+ +:++:+    +:++:+    +:+  
   +#+  +:+  +#++#+    +:++#+    +:+   
  +#+       +#++#+    +#++#+    +#+    
 #+#       #+##+#    #+##+#    #+#     
###       ### ########  ########       



Font: alligator2
::::    ::::  ::::::::  ::::::::  
+:+:+: :+:+:+:+:    :+::+:    :+: 
+:+ +:+:+ +:++:+    +:++:+    +:+ 
+#+  +:+  +#++#+    +:++#+    +:+ 
+#+       +#++#+    +#++#+    +#+ 
#+#       #+##+#    #+##+#    #+# 
###       ### ########  ########  



Font: alphabet
M   M         
MM MM         
M M M ooo ooo 
M   M o o o o 
M   M ooo ooo 
              
              



Font: avatar
 _      ____  ____ 
/ \__/|/  _ \/  _ \
| |\/||| / \|| / \|
| |  ||| \_/|| \_/|
\_/  \|\____/\____/
                   



Font: banner
#     #               
##   ##  ####   ####  
# # # # #    # #    # 
#  #  # #    # #    # 
#     # #    # #    # 
#     # #    # #    # 
#     #  ####   ####  
                      



Font: banner3-D
'##::::'##::'#######:::'#######::
 ###::'###:'##.... ##:'##.... ##:
 ####'####: ##:::: ##: ##:::: ##:
 ## ### ##: ##:::: ##: ##:::: ##:
 ##. #: ##: ##:::: ##: ##:::: ##:
 ##:.:: ##: ##:::: ##: ##:::: ##:
 ##:::: ##:. #######::. #######::
..:::::..:::.......::::.......:::



Font: banner3
##     ##  #######   #######  
###   ### ##     ## ##     ## 
#### #### ##     ## ##     ## 
## ### ## ##     ## ##     ## 
##     ## ##     ## ##     ## 
##     ## ##     ## ##     ## 
##     ##  #######   #######  



Font: banner4
.##.....##..#######...#######.
.###...###.##.....##.##.....##
.####.####.##.....##.##.....##
.##.###.##.##.....##.##.....##
.##.....##.##.....##.##.....##
.##.....##.##.....##.##.....##
.##.....##..#######...#######.



Font: barbwire
><<       ><<                    
>< ><<   ><<<                    
><< ><< > ><<   ><<       ><<    
><<  ><<  ><< ><<  ><<  ><<  ><< 
><<   ><  ><<><<    ><<><<    ><<
><<       ><< ><<  ><<  ><<  ><< 
><<       ><<   ><<       ><<    
                                 



Font: basic
.88b  d88.  .d88b.   .d88b.  
88'YbdP`88 .8P  Y8. .8P  Y8. 
88  88  88 88    88 88    88 
88  88  88 88    88 88    88 
88  88  88 `8b  d8' `8b  d8' 
YP  YP  YP  `Y88P'   `Y88P'  
                             
                             



Font: bell
 __   __              
 |    |    __.    __. 
 |\  /|  .'   \ .'   \
 | \/ |  |    | |    |
 /    /   `._.'  `._.'
                      



Font: big
 __  __             
|  \/  |            
| \  / | ___   ___  
| |\/| |/ _ \ / _ \ 
| |  | | (_) | (_) |
|_|  |_|\___/ \___/ 
                    
                    



Font: bigchief
______________________
    _   _             
    /  /|             
---/| /-|----__----__-
  / |/  |  /   ) /   )
_/__/___|_(___/_(___/_
                      
                      



Font: binary
01001101 01101111 01101111 



Font: block
                                
_|      _|                      
_|_|  _|_|    _|_|      _|_|    
_|  _|  _|  _|    _|  _|    _|  
_|      _|  _|    _|  _|    _|  
_|      _|    _|_|      _|_|    
                                
                                



Font: bubble
  _   _   _  
 / \ / \ / \ 
( M | o | o )
 \_/ \_/ \_/ 



Font: bulbhead
 __  __  _____  _____ 
(  \/  )(  _  )(  _  )
 )    (  )(_)(  )(_)( 
(_/\/\_)(_____)(_____)



Font: calgphy2
                                          
     #####   ##    ##                     
  ######  /#### #####                     
 /#   /  /  ##### #####                   
/    /  /   # ##  # ##                    
    /  /    #     #                       
   ## ##    #     #      /###     /###    
   ## ##    #     #     / ###  / / ###  / 
   ## ##    #     #    /   ###/ /   ###/  
   ## ##    #     #   ##    ## ##    ##   
   ## ##    #     ##  ##    ## ##    ##   
   #  ##    #     ##  ##    ## ##    ##   
      /     #      ## ##    ## ##    ##   
  /##/      #      ## ##    ## ##    ##   
 /  #####           ## ######   ######    
/     ##                ####     ####     
#                                         
 ##                                       
                                          
                                          



Font: caligraphy
                                              
     *****   **    **                         
  ******  ***** *****                         
 **   *  *  ***** *****                       
*    *  *   * **  * **                        
    *  *    *     *        ****       ****    
   ** **    *     *       * ***  *   * ***  * 
   ** **    *     *      *   ****   *   ****  
   ** **    *     *     **    **   **    **   
   ** **    *     *     **    **   **    **   
   ** **    *     **    **    **   **    **   
   *  **    *     **    **    **   **    **   
      *     *      **   **    **   **    **   
  ****      *      **    ******     ******    
 *  *****           **    ****       ****     
*     **                                      
*                                             
 **                                           
                                              
                                              
                                              



Font: catwalk
_//       _//                    
_/ _//   _///                    
_// _// _ _//   _//       _//    
_//  _//  _// _//  _//  _//  _// 
_//   _/  _//_//    _//_//    _//
_//       _// _//  _//  _//  _// 
_//       _//   _//       _//    
                                 



Font: chunky
 _______              
|   |   |.-----.-----.
|       ||  _  |  _  |
|__|_|__||_____|_____|
                      



Font: coinstak
O))       O))                    
O) O))   O)))                    
O)) O)) O O))   O))       O))    
O))  O))  O)) O))  O))  O))  O)) 
O))   O)  O))O))    O))O))    O))
O))       O)) O))  O))  O))  O)) 
O))       O))   O))       O))    
                                 



Font: colossal
888b     d888                 
8888b   d8888                 
88888b.d88888                 
888Y88888P888 .d88b.  .d88b.  
888 Y888P 888d88""88bd88""88b 
888  Y8P  888888  888888  888 
888   "   888Y88..88PY88..88P 
888       888 "Y88P"  "Y88P"  
                              
                              
                              



Font: computer
8""8""8             
8  8  8 eeeee eeeee 
8e 8  8 8  88 8  88 
88 8  8 8   8 8   8 
88 8  8 8   8 8   8 
88 8  8 8eee8 8eee8 
                    



Font: contessa
.  .      
|\/| _  _ 
|  |(_)(_)
          



Font: contrast
.%%...%%...%%%%....%%%%..
.%%%.%%%..%%..%%..%%..%%.
.%%.%.%%..%%..%%..%%..%%.
.%%...%%..%%..%%..%%..%%.
.%%...%%...%%%%....%%%%..
.........................



Font: cosmic
.        :       ...         ...     
;;,.    ;;;   .;;;;;;;.   .;;;;;;;.  
[[[[, ,[[[[, ,[[     \[[,,[[     \[[,
$$$$$$$$"$$$ $$$,     $$$$$$,     $$$
888 Y88" 888o"888,_ _,88P"888,_ _,88P
MMM  M'  "MMM  "YMMMMMP"   "YMMMMMP" 



Font: cosmike
.        :       ...         ...     
;;,.    ;;;   .;;;;;;;.   .;;;;;;;.  
[[[[, ,[[[[, ,[[     \[[,,[[     \[[,
$$$$$$$$"$$$ $$$,     $$$$$$,     $$$
888 Y88" 888o"888,_ _,88P"888,_ _,88P
MMM  M'  "MMM  "YMMMMMP"   "YMMMMMP" 



Font: cricket
 ___ ___             
|   Y   .-----.-----.
|.      |  _  |  _  |
|. \_/  |_____|_____|
|:  |   |            
|::.|:. |            
`--- ---'            
                     



Font: cyberlarge
 _______  _____   _____ 
 |  |  | |     | |     |
 |  |  | |_____| |_____|
                        



Font: cybermedium
_  _ ____ ____ 
|\/| |  | |  | 
|  | |__| |__| 
               



Font: cybersmall
 _  _ ____ ____
 |\/| [__] [__]



Font: diamond
/\\       /\\                    
/\ /\\   /\\\                    
/\\ /\\ / /\\   /\\       /\\    
/\\  /\\  /\\ /\\  /\\  /\\  /\\ 
/\\   /\  /\\/\\    /\\/\\    /\\
/\\       /\\ /\\  /\\  /\\  /\\ 
/\\       /\\   /\\       /\\    
                                 



Font: digital
+-+-+-+
|M|o|o|
+-+-+-+



Font: doh
                                                                 
                                                                 
MMMMMMMM               MMMMMMMM                                  
M:::::::M             M:::::::M                                  
M::::::::M           M::::::::M                                  
M:::::::::M         M:::::::::M                                  
M::::::::::M       M::::::::::M   ooooooooooo      ooooooooooo   
M:::::::::::M     M:::::::::::M oo:::::::::::oo  oo:::::::::::oo 
M:::::::M::::M   M::::M:::::::Mo:::::::::::::::oo:::::::::::::::o
M::::::M M::::M M::::M M::::::Mo:::::ooooo:::::oo:::::ooooo:::::o
M::::::M  M::::M::::M  M::::::Mo::::o     o::::oo::::o     o::::o
M::::::M   M:::::::M   M::::::Mo::::o     o::::oo::::o     o::::o
M::::::M    M:::::M    M::::::Mo::::o     o::::oo::::o     o::::o
M::::::M     MMMMM     M::::::Mo::::o     o::::oo::::o     o::::o
M::::::M               M::::::Mo:::::ooooo:::::oo:::::ooooo:::::o
M::::::M               M::::::Mo:::::::::::::::oo:::::::::::::::o
M::::::M               M::::::M oo:::::::::::oo  oo:::::::::::oo 
MMMMMMMM               MMMMMMMM   ooooooooooo      ooooooooooo   
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 



Font: doom
___  ___            
|  \/  |            
| .  . | ___   ___  
| |\/| |/ _ \ / _ \ 
| |  | | (_) | (_) |
\_|  |_/\___/ \___/ 
                    
                    



Font: dotmatrix
 _           _                                  
(_) _     _ (_)                                 
(_)(_)   (_)(_)    _  _  _        _  _  _       
(_) (_)_(_) (_) _ (_)(_)(_) _  _ (_)(_)(_) _    
(_)   (_)   (_)(_)         (_)(_)         (_)   
(_)         (_)(_)         (_)(_)         (_)   
(_)         (_)(_) _  _  _ (_)(_) _  _  _ (_)   
(_)         (_)   (_)(_)(_)      (_)(_)(_)      
                                                
                                                



Font: drpepper
 __ __           
|  \  \ ___  ___ 
|     |/ . \/ . \
|_|_|_|\___/\___/
                 



Font: eftichess
##################
###(:)######(:)###
###|:|######|:|###
###|:|######|:|###
##################



Font: eftifont
 _   _     
| \_/ |_ _ 
| \_/ /oYo\
|_| |_\_|_/
           



Font: eftipiti
 _ _   
//\/\oo
       



Font: eftirobot
 _   _           
( `-' )          
| \_/ | ___  ___ 
( ) ( )( o )( o )
/_\ /_\ \_/  \_/ 
                 



Font: eftitalic
   _   __       
  / \,' / _   _ 
 / \,' /,'o|,'o|
/_/ /_/ |_,'|_,'
                



Font: eftiwall
               #   ___       #   ___      
     )))       #  <_*_>      #  <_*_>     
    (o o)      #  (o o)      #  (o o)     
ooO--(_)--Ooo--8---(_)--Ooo--8---(_)--Ooo-



Font: eftiwater
 _  _         
 )\/,) __  __ 
((`(( ((_)((_)
              



Font: epic
 _______  _______  _______ 
(       )(  ___  )(  ___  )
| () () || (   ) || (   ) |
| || || || |   | || |   | |
| |(_)| || |   | || |   | |
| |   | || |   | || |   | |
| )   ( || (___) || (___) |
|/     \|(_______)(_______)
                           



Font: fender
'||\   /||`               
 ||\\.//||                
 ||     ||  .|''|, .|''|, 
 ||     ||  ||  || ||  || 
.||     ||. `|..|' `|..|' 
                          
                          



Font: fourtops
|\  /|      
| \/ |/~\/~\
|    |\_/\_/
            



Font: fuzzy
.-..-.            
: `' :            
: .. : .--.  .--. 
: :; :' .; :' .; :
:_;:_;`.__.'`.__.'
                  
                  



Font: goofy
          ___     _____     ___
|        |   )   (     )   (   
|  |\/|  |  /     \   /     \  
|  |  |  | (       ) (       ) 
|  |  |  |  \     /   \     /  
|  |__|  |___)   (_____)   (___



Font: gothic
                       
  /\\,/\\,             
 /| || ||              
 || || ||   /'\\  /'\\ 
 ||=|= ||  || || || || 
~|| || ||  || || || || 
 |, \\,\\, \\,/  \\,/  
_-                     
                       



Font: graffiti
   _____                 
  /     \   ____   ____  
 /  \ /  \ /  _ \ /  _ \ 
/    Y    (  <_> |  <_> )
\____|__  /\____/ \____/ 
        \/               



Font: hollywood
           _                      
          ' )     _)              
          //  _/~/'               
        /'/_/~ /' ____     ____   
      /' /~  /' /'    )--/'    )--
    /'     /' /'    /' /'    /'   
(,/'      (_,(___,/'  (___,/'     
                                  
                                  
                                  



Font: invita
   __     __)      
  (, /|  /|        
    / | / |  ______
 ) /  |/  |_(_)(_) 
(_/   '            
                   



Font: isometric1
      ___           ___           ___     
     /\__\         /\  \         /\  \    
    /::|  |       /::\  \       /::\  \   
   /:|:|  |      /:/\:\  \     /:/\:\  \  
  /:/|:|__|__   /:/  \:\  \   /:/  \:\  \ 
 /:/ |::::\__\ /:/__/ \:\__\ /:/__/ \:\__\
 \/__/~~/:/  / \:\  \ /:/  / \:\  \ /:/  /
       /:/  /   \:\  /:/  /   \:\  /:/  / 
      /:/  /     \:\/:/  /     \:\/:/  /  
     /:/  /       \::/  /       \::/  /   
     \/__/         \/__/         \/__/    



Font: isometric2
      ___           ___           ___     
     /\  \         /\  \         /\  \    
    |::\  \       /::\  \       /::\  \   
    |:|:\  \     /:/\:\  \     /:/\:\  \  
  __|:|\:\  \   /:/  \:\  \   /:/  \:\  \ 
 /::::|_\:\__\ /:/__/ \:\__\ /:/__/ \:\__\
 \:\~~\  \/__/ \:\  \ /:/  / \:\  \ /:/  /
  \:\  \        \:\  /:/  /   \:\  /:/  / 
   \:\  \        \:\/:/  /     \:\/:/  /  
    \:\__\        \::/  /       \::/  /   
     \/__/         \/__/         \/__/    



Font: isometric3
      ___           ___           ___     
     /__/\         /  /\         /  /\    
    |  |::\       /  /::\       /  /::\   
    |  |:|:\     /  /:/\:\     /  /:/\:\  
  __|__|:|\:\   /  /:/  \:\   /  /:/  \:\ 
 /__/::::| \:\ /__/:/ \__\:\ /__/:/ \__\:\
 \  \:\~~\__\/ \  \:\ /  /:/ \  \:\ /  /:/
  \  \:\        \  \:\  /:/   \  \:\  /:/ 
   \  \:\        \  \:\/:/     \  \:\/:/  
    \  \:\        \  \::/       \  \::/   
     \__\/         \__\/         \__\/    



Font: isometric4
      ___           ___           ___     
     /  /\         /  /\         /  /\    
    /  /::|       /  /::\       /  /::\   
   /  /:|:|      /  /:/\:\     /  /:/\:\  
  /  /:/|:|__   /  /:/  \:\   /  /:/  \:\ 
 /__/:/_|::::\ /__/:/ \__\:\ /__/:/ \__\:\
 \__\/  /~~/:/ \  \:\ /  /:/ \  \:\ /  /:/
       /  /:/   \  \:\  /:/   \  \:\  /:/ 
      /  /:/     \  \:\/:/     \  \:\/:/  
     /__/:/       \  \::/       \  \::/   
     \__\/         \__\/         \__\/    



Font: italic
          
 /|/|     
/   |()() 
          



Font: ivrit
                                                                        __  __ 
                                                             ___   ___ |  \/  |
                                                            / _ \ / _ \| |\/| |
                                                           | (_) | (_) | |  | |
                                                            \___/ \___/|_|  |_|
                                                                               



Font: jazmine
                      
o     o               
8b   d8               
8`b d'8 .oPYo. .oPYo. 
8 `o' 8 8    8 8    8 
8     8 8    8 8    8 
8     8 `YooP' `YooP' 
..::::..:.....::.....:
::::::::::::::::::::::
::::::::::::::::::::::



Font: jerusalem
                                                                               
                                                      ________ ________ __  __ 
                                                     |.  ___  |.  ___  |  \/  |
                                                      | |   | || |   | | |\/| |
                                                      | |___| || |___| | |  | |
                                                      |_______||_______|_|  |_|
                                                                               



Font: katakana
######## #   # #   # 
       # #   # #   # 
      #  #   # #   # 
    ##   #   # #   # 
  ## #      #     #  
 ##   #    #     #   
#      # ##    ##    
                     



Font: kban
'||    ||'                 
 |||  |||    ...     ...   
 |'|..'||  .|  '|. .|  '|. 
 | '|' ||  ||   || ||   || 
.|. | .||.  '|..|'  '|..|' 
                           
                           



Font: larry3d
                           
 /'\_/`\                   
/\      \    ___     ___   
\ \ \__\ \  / __`\  / __`\ 
 \ \ \_/\ \/\ \L\ \/\ \L\ \
  \ \_\\ \_\ \____/\ \____/
   \/_/ \/_/\/___/  \/___/ 
                           
                           



Font: lcd
                  
|\ /|             
| + |  -     -    
|   | | |   | |   
       -     -    
                  



Font: lean
                                   
    _/      _/                     
   _/_/  _/_/    _/_/      _/_/    
  _/  _/  _/  _/    _/  _/    _/   
 _/      _/  _/    _/  _/    _/    
_/      _/    _/_/      _/_/       
                                   
                                   



Font: letters
MM    MM               
MMM  MMM  oooo   oooo  
MM MM MM oo  oo oo  oo 
MM    MM oo  oo oo  oo 
MM    MM  oooo   oooo  
                       



Font: linux
.-.-.-..----..----.
| | | || || || || |
`-'-'-'`----'`----'
                   



Font: lockergnome
::::::|          
:::"::|,::\ ,::\ 
::| ::|`::/ `::/ 
                 



Font: madrid
/\/\         
|==| /=\ /=\ 
\  / \=/ \=/ 
             



Font: marquee
.::       .::                    
.: .::   .:::                    
.:: .:: . .::   .::       .::    
.::  .::  .:: .::  .::  .::  .:: 
.::   .:  .::.::    .::.::    .::
.::       .:: .::  .::  .::  .:: 
.::       .::   .::       .::    
                                 



Font: maxfour
|\  /|      
| \/ |/~\/~\
|    |\_/\_/
            



Font: mike
          
 ||\  |  |
          



Font: mini
           
|\/| _  _  
|  |(_)(_) 
           



Font: mirror
                                                                        __  __ 
                                                             ___   ___ |  \/  |
                                                            / _ \ / _ \| |\/| |
                                                           | (_) | (_) | |  | |
                                                            \___/ \___/|_|  |_|
                                                                               



Font: mnemonic
Moo



Font: morse
-- --- --- 



Font: moscow
                  
#   #  ###   ###  
## ## #   # #   # 
# # # #   # #   # 
#   # #   # #   # 
#   #  ###   ###  



Font: nancyj-fancy
M"""""`'"""`YM                   
M  mm.  mm.  M                   
M  MMM  MMM  M .d8888b. .d8888b. 
M  MMM  MMM  M 88'  `88 88'  `88 
M  MMM  MMM  M 88.  .88 88.  .88 
M  MMM  MMM  M `88888P' `88888P' 
MMMMMMMMMMMMMM                   
                                 



Font: nancyj-underlined
8888ba.88ba                    
88  `8b  `8b                   
88   88   88 .d8888b. .d8888b. 
88   88   88 88'  `88 88'  `88 
88   88   88 88.  .88 88.  .88 
dP   dP   dP `88888P' `88888P' 
ooooooooooooooooooooooooooooooo
                               



Font: nancyj
8888ba.88ba                    
88  `8b  `8b                   
88   88   88 .d8888b. .d8888b. 
88   88   88 88'  `88 88'  `88 
88   88   88 88.  .88 88.  .88 
dP   dP   dP `88888P' `88888P' 
                               
                               



Font: nipples
{__       {__                    
{_ {__   {___                    
{__ {__ { {__   {__       {__    
{__  {__  {__ {__  {__  {__  {__ 
{__   {_  {__{__    {__{__    {__
{__       {__ {__  {__  {__  {__ 
{__       {__   {__       {__    
                                 



Font: ntgreek
                     
 __   __             
|  \ /  |            
|   v   | ___   ___  
| |\_/| |/ _ \ / _ \ 
| |   | ( (_) | (_) )
|_|   |_|\___/ \___/ 
                     
                     



Font: o8
oooo     oooo                        
 8888o   888   ooooooo     ooooooo   
 88 888o8 88 888     888 888     888 
 88  888  88 888     888 888     888 
o88o  8  o88o  88ooo88     88ooo88   
                                     



Font: ogre
                    
  /\/\   ___   ___  
 /    \ / _ \ / _ \ 
/ /\/\ \ (_) | (_) |
\/    \/\___/ \___/ 
                    



Font: pawp
                         
  __   __                
 (__)_(__)               
(_) (_) (_)  ___    ___  
(_) (_) (_) (___)  (___) 
(_)     (_)(_)_(_)(_)_(_)
(_)     (_) (___)  (___) 
                         
                         



Font: peaks
/^^       /^^                    
/^ /^^   /^^^                    
/^^ /^^ / /^^   /^^       /^^    
/^^  /^^  /^^ /^^  /^^  /^^  /^^ 
/^^   /^  /^^/^^    /^^/^^    /^^
/^^       /^^ /^^  /^^  /^^  /^^ 
/^^       /^^   /^^       /^^    
                                 



Font: pebbles
Oo      oO             
O O    o o             
o  o  O  O             
O   Oo   O             
O        o .oOo. .oOo. 
o        O O   o O   o 
o        O o   O o   O 
O        o `OoO' `OoO' 
                       
                       



Font: pepper
          
 /|,/_  _ 
/  //_//_/
          



Font: poison
                                 
@@@@@@@@@@    @@@@@@    @@@@@@   
@@@@@@@@@@@  @@@@@@@@  @@@@@@@@  
@@! @@! @@!  @@!  @@@  @@!  @@@  
!@! !@! !@!  !@!  @!@  !@!  @!@  
@!! !!@ @!@  @!@  !@!  @!@  !@!  
!@!   ! !@!  !@!  !!!  !@!  !!!  
!!:     !!:  !!:  !!!  !!:  !!!  
:!:     :!:  :!:  !:!  :!:  !:!  
:::     ::   ::::: ::  ::::: ::  
 :      :     : :  :    : :  :   
                                 



Font: puffy
                     
/'\_/`\              
|     |   _      _   
| (_) | /'_`\  /'_`\ 
| | | |( (_) )( (_) )
(_) (_)`\___/'`\___/'
                     
                     



Font: pyramid
  ^    ^    ^  
 /M\  /o\  /o\ 
<___><___><___>



Font: rectangles
               
 _____         
|     |___ ___ 
| | | | . | . |
|_|_|_|___|___|
               



Font: relief
_________________________________
/~~\__/~~\__/~~~~~~\___/~~~~~~\__
/~~~\/~~~\_/~~\__/~~\_/~~\__/~~\_
/~~~~~~~~\_/~~\__/~~\_/~~\__/~~\_
/~~\__/~~\_/~~\__/~~\_/~~\__/~~\_
/~~\__/~~\__/~~~~~~\___/~~~~~~\__
_________________________________



Font: relief2
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
/// \\/// \\/////// \\\/////// \\
//// //// \/// \\/// \/// \\/// \
/// / /// \/// \\/// \/// \\/// \
/// \\/// \/// \\/// \/// \\/// \
/// \\/// \\/////// \\\/////// \\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



Font: rev
=========================
=  =====  ===============
=   ===   ===============
=  =   =  ===============
=  == ==  ===   ====   ==
=  =====  ==     ==     =
=  =====  ==  =  ==  =  =
=  =====  ==  =  ==  =  =
=  =====  ==  =  ==  =  =
=  =====  ===   ====   ==
=========================



Font: roman
ooo        ooooo                     
`88.       .888'                     
 888b     d'888   .ooooo.   .ooooo.  
 8 Y88. .P  888  d88' `88b d88' `88b 
 8  `888'   888  888   888 888   888 
 8    Y     888  888   888 888   888 
o8o        o888o `Y8bod8P' `Y8bod8P' 
                                     
                                     
                                     



Font: rot13
Zbb



Font: rounded
 _______             
(_______)            
 _  _  _  ___   ___  
| ||_|| |/ _ \ / _ \ 
| |   | | |_| | |_| |
|_|   |_|\___/ \___/ 
                     



Font: rowancap
    dMMMMMMMMb  .aMMMb  .aMMMb 
   dMP"dMP"dMP dMP"dMP dMP"dMP 
  dMP dMP dMP dMP dMP dMP dMP  
 dMP dMP dMP dMP.aMP dMP.aMP   
dMP dMP dMP  VMMMP"  VMMMP"    
                               



Font: rozzo
    e   e                         
   d8b d8b     e88 88e   e88 88e  
  e Y8b Y8b   d888 888b d888 888b 
 d8b Y8b Y8b  Y888 888P Y888 888P 
d888b Y8b Y8b  "88 88"   "88 88"  
                                  
                                  



Font: runic
|\  /| 
| \/ | 
| /\ | 
|/  \| 
|    | 
|    | 



Font: runyc
|\  /|       
| \/ |       
| /\ |       
|/  \| /\ /\ 
|    | \/ \/ 
|    | /\ /\ 



Font: sblood
 @@@@@@@@@@   @@@@@@   @@@@@@ 
 @@! @@! @@! @@!  @@@ @@!  @@@
 @!! !!@ @!@ @!@  !@! @!@  !@!
 !!:     !!: !!:  !!! !!:  !!!
  :      :    : :. :   : :. : 
                              



Font: script
 ,__ __             
/|  |  |            
 |  |  |   __   __  
 |  |  |  /  \_/  \_
 |  |  |_/\__/ \__/ 
                    
                    



Font: serifcap
 __  __  __    __  
(  \/  )/  \  /  \ 
 )    (( () )( () )
(_/\/\_)\__/  \__/ 



Font: shadow
  \  |             
 |\/ |  _ \   _ \  
 |   | (   | (   | 
_|  _|\___/ \___/  
                   



Font: short
|\/|    
|  |()()
        



Font: slant
    __  ___          
   /  |/  /___  ____ 
  / /|_/ / __ \/ __ \
 / /  / / /_/ / /_/ /
/_/  /_/\____/\____/ 
                     



Font: slide
##   ||           
### H|| #H|  #H|  
###HH||## H|## H| 
## H ||## H|## H| 
##   || #H|  #H|  
                  



Font: slscript
 _ _ _      
' ) ) )     
 / / / __ __
/ ' (_(_)(_)
            
            



Font: small
 __  __          
|  \/  |___  ___ 
| |\/| / _ \/ _ \
|_|  |_\___/\___/
                 



Font: smisome1
    ___       ___       ___   
   /\__\     /\  \     /\  \  
  /::L_L_   /::\  \   /::\  \ 
 /:/L:\__\ /:/\:\__\ /:/\:\__\
 \/_/:/  / \:\/:/  / \:\/:/  /
   /:/  /   \::/  /   \::/  / 
   \/__/     \/__/     \/__/  



Font: smkeyboard
 ____ ____ ____ 
||M |||o |||o ||
||__|||__|||__||
|/__\|/__\|/__\|



Font: smscript
 ,_ _           
/| | |   _   _  
 | | |  / \_/ \_
 | | |_/\_/ \_/ 
                



Font: smshadow
  \  |           
 |\/ |  _ \  _ \ 
_|  _|\___/\___/ 
                 



Font: smslant
   __  ___        
  /  |/  /__  ___ 
 / /|_/ / _ \/ _ \
/_/  /_/\___/\___/
                  



Font: smtengwar
 _ _  c c 
|_)_) | | 
          



Font: speed
______  ___            
___   |/  /___________ 
__  /|_/ /_  __ \  __ \
_  /  / / / /_/ / /_/ /
/_/  /_/  \____/\____/ 
                       



Font: stampatello
,-,-,-.           
`,| | |   ,-. ,-. 
  | ; | . | | | | 
  '   `-' `-' `-' 
                  
                  



Font: standard
 __  __             
|  \/  | ___   ___  
| |\/| |/ _ \ / _ \ 
| |  | | (_) | (_) |
|_|  |_|\___/ \___/ 
                    



Font: starwars
.___  ___.   ______     ______   
|   \/   |  /  __  \   /  __  \  
|  \  /  | |  |  |  | |  |  |  | 
|  |\/|  | |  |  |  | |  |  |  | 
|  |  |  | |  `--'  | |  `--'  | 
|__|  |__|  \______/   \______/  
                                 



Font: stellar
`..       `..                    
`. `..   `...                    
`.. `.. ` `..   `..       `..    
`..  `..  `.. `..  `..  `..  `.. 
`..   `.  `..`..    `..`..    `..
`..       `.. `..  `..  `..  `.. 
`..       `..   `..       `..    
                                 



Font: stop
 ______              
|  ___ \             
| | _ | | ___   ___  
| || || |/ _ \ / _ \ 
| || || | |_| | |_| |
|_||_||_|\___/ \___/ 
                     



Font: straight
           
|\/| _  _  
|  |(_)(_) 
           



Font: tanja
 M)mm mmm                  
M)  mm  mm                 
M)  mm  mm  o)OOO   o)OOO  
M)  mm  mm o)   OO o)   OO 
M)      mm o)   OO o)   OO 
M)      mm  o)OOO   o)OOO  
                           
                           



Font: tengwar
                  .dP"Yb   .dP"Yb 
                dP'   d' dP'   d' 
                                  
`Yb d88b d88b     'Yb      'Yb    
 88P   88   8b     88       88    
 88    8P   88     88       88    
 88  .dP  .dP     .8P      .8P    
.888888888888b.                   
                                  
                                  



Font: term
Moo



Font: thick
8b   d8             
8YbmdP8 .d8b. .d8b. 
8  "  8 8' .8 8' .8 
8     8 `Y8P' `Y8P' 
                    



Font: thin
               
,-.-.          
| | |,---.,---.
| | ||   ||   |
` ' '`---'`---'
               



Font: threepoint
|\/| _  _ 
|  |(_)(_)
          



Font: ticks
_/\/\______/\/\_________________________
_/\/\/\__/\/\/\____/\/\/\______/\/\/\___
_/\/\/\/\/\/\/\__/\/\__/\/\__/\/\__/\/\_
_/\/\__/\__/\/\__/\/\__/\/\__/\/\__/\/\_
_/\/\______/\/\____/\/\/\______/\/\/\___
________________________________________



Font: ticksslant
     _/\/\______/\/\_________________________
    _/\/\/\__/\/\/\____/\/\/\______/\/\/\___ 
   _/\/\/\/\/\/\/\__/\/\__/\/\__/\/\__/\/\_  
  _/\/\__/\__/\/\__/\/\__/\/\__/\/\__/\/\_   
 _/\/\______/\/\____/\/\/\______/\/\/\___    
________________________________________     



Font: tinker-toy
o   o         
|\ /|         
| O | o-o o-o 
|   | | | | | 
o   o o-o o-o 
              
              



Font: tombstone
 _, _  _,  _,
 |\/| / \ / \
 |  | \ / \ /
 ~  ~  ~   ~ 
             



Font: trek
     dBBBBBBb  dBBBBP dBBBBP
      '   dB' dBP.BP dBP.BP 
   dB'dB'dB' dBP.BP dBP.BP  
  dB'dB'dB' dBP.BP dBP.BP   
 dB'dB'dB' dBBBBP dBBBBP    
                            



Font: tsalagi
  _    ___  _____  __
 / '    |    | |    |
| __    \    | \    |
|'  \    \  /   \  / 
 \__/     \/     \/  



Font: twopoint
|\/| _  _ 
|  |(_)(_)



Font: univers
                                           
88b           d88                          
888b         d888                          
88`8b       d8'88                          
88 `8b     d8' 88  ,adPPYba,   ,adPPYba,   
88  `8b   d8'  88 a8"     "8a a8"     "8a  
88   `8b d8'   88 8b       d8 8b       d8  
88    `888'    88 "8a,   ,a8" "8a,   ,a8"  
88     `8'     88  `"YbbdP"'   `"YbbdP"'   
                                           
                                           



Font: usaflag
 :::=======  :::====  :::==== 
 ::: === === :::  === :::  ===
 === === === ===  === ===  ===
 ===     === ===  === ===  ===
 ===     ===  ======   ====== 
                              



Font: weird
               
 /|/|          
( / | ___  ___ 
|   )|   )|   )
|  / |__/ |__/ 

'''