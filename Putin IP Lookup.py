from pystyle import Anime, Colors, Colorate
from pystyle import Add
import urllib
from urllib import request
import requests
import re
from urllib.request import Request, urlopen
import keyboard
import os 
from requests import get
import sys
import time





os.system('color d')
banner = '''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#(*********,,,,,*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@#////***////*****,,..,.,/@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@*@&(((////((((((((//*****,,.*@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@#@@((((((((((((((((((((/,..,....(@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@(#(((((##((((#((((((((((/,.,.*,.,,/@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@((//((#######%##(((((((((//.,...,,*.@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@%((((((########(##((((((((/*,.,,.,,.@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@&((((#((######(##((/((((((/**,,,,.//@@@@@##@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@/,,**/((/(((####((((///(///**,,/,,/*(/&@,/*//&@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@(,,. ./(/,. ,.  ,.,**///(//*******/,.*//,***(((@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@(/////*((///////(((#((/////***(*#((****//***/(/*@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@///(//(((/(((((###((/////*****,*/(#@#,/,*/,*/(/,@@@@@@@@@@@                         
@@@@@@@@@@@@@@@@@@@@(*//*(##((/**////((((///*****,**.(@@@@,/,/*(((//@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@/**/*//,.*(((/////********,,..,,%    .*,,((((/*@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@(*,//**/((////////*******,..,,*,***  ,,((((((*@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@*,,*,,,,,*************,,...**&**/////*/(((#(**@@@@@@@@@@
@@@@@@@@@@@@@@@@@/,.  ..,*,,.,,**///***,*,.....,,*@%%&,*///*//((#       %@@@@@@
@@@@@@@@@@/,..         ,  **//*////*,,.,......,@@&&%%,***///@               @@@
@@@@/  .             ..   /(*#*,......,,,,,@@@@@@&%#   ,**                    .
@@@,                ,   .(#(%####(/....@@@@@@@@&&%                              
@@@                .   .###&%&@@(   ..*@@@@@@@&&&                               
@@@               .  ,*%%%&@&&&,      ( @@@@@@@                                 
@@/                 *,%&&&&@&#(%  #   ,(%#@@@@                                  
'''

text1 ='''



 _______               __      __           
/       \             /  |    /  |          
$$$$$$$  | __    __  _$$ |_   $$/  _______  
$$ |__$$ |/  |  /  |/ $$   |  /  |/       \ 
$$    $$/ $$ |  $$ |$$$$$$/   $$ |$$$$$$$  |
$$$$$$$/  $$ |  $$ |  $$ | __ $$ |$$ |  $$ |
$$ |      $$ \__$$ |  $$ |/  |$$ |$$ |  $$ |
$$ |      $$    $$/   $$  $$/ $$ |$$ |  $$ |
$$/        $$$$$$/     $$$$/  $$/ $$/   $$/ 
                                            
Putin is a tool to look-up an IP by ReallyFighter!                                                                              
'''

print(Add.Add(banner, text1))
time.sleep(2)
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.08)
  value = input()  
  return value

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)

qip = typingInput('''What is the IP ?
''')

#getting information from ip api
continent = get(f'http://ip-api.com/line/'+qip+"?fields=continent").text
pays = get(f'http://ip-api.com/line/'+qip+"?fields=country").text
region = get(f'http://ip-api.com/line/'+qip+"?fields=regionName").text
city = get(f'http://ipapi.co/'+qip+"/city").text
continent = get(f'http://ip-api.com/line/'+qip+"?fields=continent").text
Pos = get(f'http://ip-api.com/line/'+qip+"?fields=lat").text
Pos2 = get(f'http://ip-api.com/line/'+qip+"?fields=lon").text
timezone = get(f'http://ip-api.com/line/'+qip+"?fields=timezone").text

#printing results
print('''
''')
typingPrint('Continent:'+continent)
time.sleep(0.5)
typingPrint('Country:'+pays)
time.sleep(0.5)
typingPrint('Region:'+region)
time.sleep(0.5)
typingPrint('city:'+city)
time.sleep(0.5)
print('''''')
typingPrint('continent:'+continent)
time.sleep(0.5)
typingPrint('''Position(Note:this can be 100% exact):   
'''+Pos+Pos2)
time.sleep(0.5)
typingPrint('Timezone:'+timezone)
time.sleep(0.5)

print('''
''')
print('finished! Press R to quit!')
print('                                                                                             Check out my github for more tool like that!')
print('                                                                                             https://github.com/ReallyFighter')
while True:
    if keyboard.read_key() == "r":
        break


    






    

    



    
