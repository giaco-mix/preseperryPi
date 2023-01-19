# Link utili 
__for more info about *.md* files and tags visit: *https://guides.github.com/features/mastering-markdown/*__

## DIMMER PWM

* http://pcbheaven.com/wikipages/Dimmer_Theory/

una cosa che ho capito é che i modulini che abbiamo "dovrebbero" essere composti da TRIAC che dovrebbero essere tipo dei transistor
e se cerchi pwm triac dimmer esce parecchia roba e sopratutto collegata a quel fatto dello zero crossing detector
nel link qua sopra c'é qualcosa di simile.

un altra cosa che ho capito é che sti TRIAC si attivino quando ricevono un pulse dal segnale pwm e poi stanno ON fin a una presunta 'fine del ciclo' che non 
ho capito esattamente cosa sia, quindi magari il nostro problema potrebbe essere che comunque il TRIAC rimanga ancora acceso per un tot e faccia passare corrente che non vogliamo

_Jack -> la presunta fine del ciclo è il momento in cui l'onda torna a zero. l'interpretazione che dai ai TRIAC è giusta. In pratica, diciamo che vogliamo fornire 1/2 della potenza alla luce. dobbiamo "far passare" solo metà dell'onda alta e metà di quella bassa. Qeusti TRIAC in pratica sono dei diodi per la 220, quindi consentono il passaggio solo da in una direzione della corrente, e hanno un gate. PWM riceve il segnale di Z-C, ipotizzando di avere una AC a 50 HZ, per arrivare a metà dell'onda alta o bassa serve attendere 1/4 di periodo. T = 0.02 sec, PWM attende 0.005 secondi e manda la pulse al gate del TRIAC. Quello consente il passaggio della corrente fino al nuovo Z-C. PWM riceve il segnale di Z-C nuovo, attende di nuovo, manda un altra pulse. TRIAC aperto di nuovo fino al successivo Z-C. Risultato: solo metà di ogni semi-onda porta davvero corrente alla lampada. quindi quella sta a circa metà della potenza. Il ciclo è quindi una semi-onda e poi il TRIAC si chiude, quindi riguardo all'ultima questione, non penso che sia colpa del TRIAC se rimane corrente, ma proprio del dimmer per sua costituzione, che magari non è studiato per i LED ma per l'incandescenza._


## NAMES

* PWM YYAC-3S AC 220V ( https://it.aliexpress.com/item/1005004022779319.html )
* AC Dimmer PWM by RobotDyn

## BOARD PAGES AND DOCS

* https://www.amazon.it/gp/product/B07ZP1WFTS/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
* https://www.amazon.it/gp/product/B07P139CHC/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
* https://it.banggood.com/RobotDyn-AC-Light-Dimmer-Module-For-PWM-Controller-1-Channel-3_3V5V-Logic-AC-50hz-60hz-220V-110V-p-1244351.html?cur_warehouse=CN
* Dimensional drawing: http://myosuploads3.banggood.com/products/20190920/20190920045755DIM-Dimmer-5A-1L.pdf
* Pinout: http://myosuploads3.banggood.com/products/20190920/20190920045759PINOUT-Dimmer-5A-1L.pdf
* Schematic: http://myosuploads3.banggood.com/products/20190920/20190920045803Schematic-Dimmer-5A-1L.pdf
* Datasheet: http://myosuploads3.banggood.com/products/20190920/20190920045926BTA16-600B.pdf


## YouTube

* https://www.youtube.com/watch?v=3hAzLrYsE7A
* https://www.youtube.com/watch?v=zJQf6bNodhE


## RobotDyn

* https://github.com/RobotDynOfficial/Documentation/wiki
* https://github.com/RobotDynOfficial/RBDDimmer

## MPDM v4 DIMMING AC LIGHTBULB WITH R-Pi

* https://www.tindie.com/products/next_evo1/universal-ac-mains-dimmer-mpdmv41/

## ALTERNATIVE GPIO LIBRARY

* http://abyz.me.uk/rpi/pigpio/index.html

## LC FILTER

* https://www.electroyou.it/forum/viewtopic.php?f=1&t=52506

## EXAMPLE PROJECT WITH ARDUINO AND _RBDdimmer.h_

* https://robotdyn.com/Blog/how-to-control-ac-power-with-dimmer.html

