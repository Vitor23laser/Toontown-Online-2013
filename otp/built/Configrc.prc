#
# constant config settings
#

chan-config-sanity-check #f
window-title Toontown
require-window 0
language english #portuguese #japanese #spanish #german #france
icon-filename toontown.ico

cull-bin shadow 15 fixed
cull-bin ground 14 unsorted
cull-bin gui-popup 60 unsorted

# downloader settings
decompressor-buffer-size 32768
extractor-buffer-size 32768
patcher-buffer-size 512000
downloader-timeout 15
downloader-timeout-retries 4
downloader-disk-write-frequency 4
downloader-byte-rate 125000
downloader-frequency 0.1

# texture settings
textures-power-2 down

# loader settings
load-file-type toontown
dc-file $TOONTOWN$/src/configfiles/toon.dc
dc-file $OTP$/src/configfiles/otp.dc
aux-display pandadx9
aux-display pandadx8
aux-display pandadx7
aux-display pandagl
compress-channels #t
text-encoding utf8
text-never-break-before ,.-:?!;。？！、

ssl-certificates $OTP$/src/configfiles/certificates.txt
ssl-certificates $OTP$/src/configfiles/gameserver.txt
expected-ssl-server /O=Disney Enterprises/OU=WDIG/CN=account.toontown.com
expected-ssl-server /O=Disney Enterprises/OU=WDIG/CN=gameserver.toontown.com
expected-ssl-server /O=Disney Enterprises/OU=WDIG/CN=account.qa.toontown.com
expected-ssl-server /O=Disney Enterprises/OU=WDIG/CN=gameserver.qa.toontown.com
expected-ssl-server /O=Disney Enterprises/OU=WDIG/CN=account.test.toontown.com
expected-ssl-server /O=Disney Enterprises/OU=WDIG/CN=gameserver.test.toontown.com
expected-ssl-server /O=Disney Enterprises/OU=DOS/CN=toontown.go.com
collect-tcp 1
collect-tcp-interval 0.2

# notify settings
notify-level-collide warning
notify-level-chan warning
notify-level-gobj warning
notify-level-loader warning
notify-timestamp #t

# Server version
server-version sv1.0.47.38 #server-version sv1.1.47.37 #server-version sv1.2.47.36 server-version sv1.3.47.35 #server-version sv1.4.47.34 #2011 server-version sv1.4.40.32
required-login playToken
server-failover 80 443
want-fog #t
dx-use-rangebased-fog #t
aspect-ratio 1.333333
on-screen-debug-font phase_3/models/fonts/ImpressBT.ttf
temp-hpr-fix 1
ime-aware 1
ime-hide 1

cursor-filename toonmono.cur

show-frame-rate-meter #t

lod-stress-factor 0.25

load-display pandadx9

fullscreen #f

#
# audio related options
#

# load the loaders
audio-loader mp3
audio-loader midi
audio-loader wav
audio-software-midi #f

audio-sfx-active #t
audio-music-active #t

audio-master-sfx-volume 1
audio-master-music-volume 1

#
# display resolution
#

win-size 640 480

#
# server type
#

server-type prod 
server-type dev
