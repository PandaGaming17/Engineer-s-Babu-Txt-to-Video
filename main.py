3
q¢gþN  ã               @   sP  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z
d dlZd dlZd dlZd dlZd dlmZ d dlZd dlZd dlZd dlZd dlmZ d dlmZmZmZ d dlmZ d dlmZ d dlmZ d dlmZ d d	lm Z m!Z! d d
l"m#Z# d dl$m%Z% d dl&m'Z' d dl(m)Z) d dl"m*Z*m+Z+ e j,ddZ-dj.dZ/e deeedZ0e j1j2ddZe j1j2ddZe j1j2ddZdd Z3dd Z4e+e*dd d!e*d"d d!ge*d#d$d!ggZ5d%d&d'd(d)d*d+d,gZ6ej7e6Z8d-Z9e0j:e!j;d.ge e#d/d0d1Z<e0j:e!j;d2d3d4 Z=e0j:e!j;d5ge e#d6d7d5Z>e0j?  dS )8é    N)Ú	YoutubeDL)Úprogress_bar)ÚAPI_IDÚAPI_HASHÚ	BOT_TOKEN)ÚClientSession)Úlisten)Úgetstatusoutput)ÚYouTube)ÚClientÚfilters)ÚMessage)Ú	FloodWait)ÚStickerEmojiInvalid)Úmessage)ÚInlineKeyboardButtonÚInlineKeyboardMarkupZCOOKIES_FILE_PATHzyoutube_cookies.txtuU   â¦â¢âââ¿ ð°ðððððððð ð­ððð â¿âââ¢â¦é(   Úbot)Zapi_idZapi_hashZ	bot_tokenr   Z21705536r   Z c5bb241f6e3ecf33fe68a444e288de2dr   Ú c               Ã   s   t j I d H  td d S )NzBot is up and running)r   ÚstartÚprint© r   r   ú2./tempdata/79bad739-b7c5-4f7c-a090-33d305b7982a.pyÚ	start_bot5   s    r   c               Ã   s   t j I d H  d S )N)r   Ústopr   r   r   r   Ústop_bot9   s    r   u   ð Contactzhttps://t.me/Engineers_Babu)ÚtextÚurlu   ð ï¸ Helpu   ðª Updates Channelz!https://t.me/Engineersbabuupdatesz%https://i.postimg.cc/t428ZHY7/02.webpz%https://i.postimg.cc/6QkC6yLK/03.webpz%https://i.postimg.cc/fbdNhHf8/04.webpz%https://i.postimg.cc/yxMGnKwB/05.webpz%https://i.postimg.cc/50ddnwvD/06.webpz%https://i.postimg.cc/wT7zxT6f/07.webpz%https://i.postimg.cc/pVk0GfM4/08.webpz%https://i.postimg.cc/1tBLrbKY/09.webpu   **ððð¥ð¥ð¨ ðððð«ð!**

â  **ð ðð¦ ð ððð±ð­ ðð¨ð°ð§ð¥ð¨ðððð« ðð¨ð­ ðððð ðð¢ð­ð¡ â¥ï¸**
â  **Can Extract Videos & PDFs From Your Text File and Upload to Telegram!**
â  **For Guide Use Command /guide ð**
â  **Use /Upload Command to Download From TXT File** ð
â  **ðððð ðð²:** @Engineers_Babur   )r   r   c             Ã   s    | j |jjtttdI d H  d S )N)Úchat_idZphotoÚcaptionZreply_markup)Z
send_photoÚchatÚidÚrandom_image_urlr    Úkeyboard)r   r   r   r   r   Ústart_commandb   s    r%   r   c             Ã   s.   |j ddI d H  tjtjtjftj  d S )Nu$   **ðð­ð¨ð©ð©ðð**ð¦T)Ú
reply_textÚosÚexeclÚsysÚ
executableÚargv)Ú_Úmr   r   r   Úrestart_handlerg   s    r.   Úupload)r   r-   c       8   N   Ã   s°  |j dI d H }| j|jjI d H }|j I d H }|jdI d H  d|jj }yZt|d}|j }W d Q R X |jd}g }x|D ]}	|j	|	jdd qW t
j| W n$   |j dI d H  t
j| d S |jd	t| d
I d H  | j|jjI d H }
|
j}|
jdI d H  |jdI d H  | j|jjI d H }|j}|jdI d H  |jdI d H  | j|jjI d H }|j}|jdI d H  yh|dkrd}nT|dkr¬d}nD|dkr¼d}n4|dkrÌd}n$|dkrÜd}n|dkrìd}nd}W n tk
r   d}Y nX |jdI d H  | j|jjI d H }|j}|jdI d H  d}|dkr\|}n|}|jdI d H  | j|jjI d H  }}|j}|jdI d H  |j I d H  |j}|jdsÊ|jdràtd | d! d"}n|d#k t|dkrüd}nt|}y`xXt|d t|D ]@}	||	 d jd$d%jd&d'jd(d)jd*d)}d| }d+|krèt 4 I d H l}|j|d,d-d.d/d.d0d1d2d3d4d5d6d7d8d9d:4 I d H &}|j I d H }tjd;|jd}W d Q I d H R X W d Q I d H R X d<|kr
d=| d>| d?| d@} d+|krt 4 I d H l}|j|d,d-d.d/d.d0d1d2d3d4d5d6d7d8d9d:4 I d H &}|j I d H }tjd;|jd}W d Q I d H R X W d Q I d H R X n¾dA|krÊtjdB| dCdDdEid:j dF }ndG|ksòdH|ksòdA|ksòdI|kr2dJdEdKdLdMdNdOdPdQ}!dF| ff}"tjdR|!|"dS}#|#j dF }n(dT|krZ|jdUd® }$dW|$ dXt }||	 dY jdZd)jd[d)jdUd)jd\d)jd]d)jd^d)jd_d)jd`d)jdad)jdbd)jdcd)j }%t|jdd de|%d df  }dg|krtjdhdDdiid:j dF }dT|krldj|kr0|jdjdk}t | n|}t dl t!j"|I d H }&t |& |j dm|& dnI d H  dT|krdot# dp| dq} t dr ds|kr²dt}'|jdudY |' }n$dT|krÖ|jdUd¯ }(dv|( dw }||	 dY jdZd)jd[d)jdUd)jd\d)jd]d)jd^d)jd_d)jd`d)jdad)jdbd)jdcd)j }%t|jdd de|%d df  }|dxkr|jdUdy})dz|)d{d°  d}}*td~|* d d}+n~|dkrÞ|jdUdy},d|,dd±  d}}*td~|* d d}+n>|dkr|jdUdy})d|)dd²  d}}*td~|* d d}+d|kr:d| d| d}-nd| d| d}-d|krjd=| d| d@} npd|ks~d'|krd|- d| d| d} nBds¨d|krÂd|- d| d| d} nd|- d| d| d} y:dt|jdd d|% d| d| dt$ d}.d t|jdd d|% d¡| d| d¢t$ d}/d£|k	rÞyLt!j||I d H }0| j%|jj|0|/d¤I d H }1|d7 }t
j|0 t&j'd W nH t(k
	rØ }2 z*|j t|2I d H  t&j'|2j) wW Y d d }2~2X nX n6d¥|k
rybd=| d¦| d@} |  d§}3t
j*|3 | j%|jj| d¥|/d¤I d H }1|d7 }t
j| d¥ W nH t(k

r }2 z*|j t|2I d H  t&j'|2j) wW Y d d }2~2X nX n~d¨| d©| dªt$ d}4|j |4I d H }5t!j+|| |I d H }6|6}7|5jdI d H  t!j,| ||.|7|||5I d H  |d7 }t&j'd W nF tk
r\ }2 z(|j d«| d¬| dnI d H  wW Y d d }2~2X nX qW W n4 tk
r }2 z|j |2I d H  W Y d d }2~2X nX |j d­I d H  d S )³Nus   ðð¨ ðð¨ð°ð§ð¥ð¨ðð ð ðð±ð­ ðð¢ð¥ð ððð§ð ððð«ð ðTz./downloads/ÚrÚ
z://é   uK   **â ðð§ð¯ðð¥ð¢ð ðð¢ð¥ð ð¢ð§ð©ð®ð­.**uW   **â ðð¨ð­ðð¥ ðð¢ð§ð¤ ðð¨ð®ð§ð ðð«ð ð** **u®   **

**ððð§ð ðð«ð¨ð¦ ðð¡ðð«ð ðð¨ð® ððð§ð­ ðð¨ ðð¨ð°ð§ð¥ð¨ðð ðð§ð¢ð­ðð¥ ð¢ð¬** **1**u~   **â ðð¨ð° ðð¥ððð¬ð ððð§ð ðð ðð¨ð®ð« ððð­ðð¡ ððð¦ð**u´   **â ðð§ð­ðð« ððð¬ð¨ð¥ð®ð­ð¢ð¨ð§ ð¬
â144,240,360,480,720,1080
 ðð¥ððð¬ð ðð¡ð¨ð¨ð¬ð ðð®ðð¥ð¢ð­ð²Z144Z256x144Z240Z426x240Z360Z640x360Z480Z854x480Z720Z1280x720Z1080Z	1920x1080ZUNuÂ   ðð¨ð° ðð§ð­ðð« ðð¨ð®ð« ððð¦ð ð­ð¨ ððð ððð©ð­ð¢ð¨ð§ ð¨ð§ ð²ð¨ð®ð« ð®ð©ð¥ð¨ðððð ðð¢ð¥ðu   ï¸ âªâ¬â®â®â®ZRobinuý   ð ðð¨ð° ð¬ðð§ð ð­ð¡ð ðð¡ð®ð¦ð ððð 
 ðð . Â» https://i.postimg.cc/d1JW4kb6/01.jpg 
 ðð« ð¢ð ðð¨ð§'ð­ ð°ðð§ð­ ð­ð¡ð®ð¦ðð§ðð¢ð¥ ð¬ðð§ð = ð§ð¨zhttp://zhttps://zwget 'z' -O 'thumb.jpg'z	thumb.jpgÚnozfile/d/zuc?export=download&id=zwww.youtube-nocookie.com/embedzyoutu.bez?modestbranding=1r   z/view?usp=sharingZ	visioniasztext/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zen-US,en;q=0.9zno-cachez
keep-alivezhttp://www.visionias.in/ZiframeZnavigatez
cross-siteÚ1zuMozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36z("Chromium";v="107", "Not=A?Brand";v="24"z?1z	"Android")ÚAcceptzAccept-LanguagezCache-ControlÚ
ConnectionÚPragmaÚRefererzSec-Fetch-DestzSec-Fetch-ModezSec-Fetch-SitezUpgrade-Insecure-Requestsz
User-Agentz	sec-ch-uazsec-ch-ua-mobilezsec-ch-ua-platform)Úheadersz(https://.*?playlist.m3u8.*?)\"Zacecwplyzyt-dlp -o "z .%(ext)s" -f "bestvideo[height<=zQ]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "ú"zvideos.classplusappzChttps://api.classplusapp.com/cams/uploader/video/jw-signed-url?url=Ú0zx-access-tokenZ\eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9r   ztencdn.classplusappz media-cdn-alisg.classplusapp.comzmedia-cdn.classplusappzapi.classplusapp.comzMobile-Androidz1.4.37.1Z18Z5d0d17ac8b3c9f51z(2848b866799971ca_2848b8667a33216c_SDK-30Úgzip)ÚHostzx-access-tokenz
user-agentzapp-versionzapi-versionz	device-idzdevice-detailszaccept-encodingz>https://api.classplusapp.com/cams/uploader/video/jw-signed-url)r9   Úparamsz/master.mpdú/é   z+https://madxapi-d0cbf6ac738c.herokuapp.com/z/master.m3u8?token=r   ú	ú:ú+ú#ú|ú@Ú*Ú.ÚhttpsÚhttpé   z) é<   zcpvod.testbookzyhttps://mon-key-3612a8154345.herokuapp.com/get_keys?url=https://cpvod.testbook.com/65f02cbd734b790a42d7317f/playlist.m3u8Z]eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9rzhttps://sec1.pw.live/z&https://d1d34p8vz63oiq.cloudfront.net/z	mpd checkzgot keys form api : 
`ú`z3 yt-dlp -k --allow-unplayable-formats -f bestvideo.z --fixup never ú Zcountedzedge.api.brightcove.coma>  bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0egZ	bcov_authz&https://d26g5bnklkwsh4.cloudfront.net/z/master.m3u8Z
vikramjeetz%2Fzhttps://www.toprankers.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fsignedsec.toprankers.com%2Fé'   é   z%2Fmaster.m3u8zcurl "z" -c "cookie.txt"z
cookie.txtZsure60zhttps://onlinetest.sure60.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.sure60.com%2Fé    Ztheoptimistclasseszhttps://live.theoptimistclasses.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.theoptimistclasses.com%2Fé,   Zyoutuz
b[height<=z][ext=mp4]/bv[height<=z!][ext=mp4]+ba[ext=m4a]/b[ext=mp4]z]/bv[height<=z]+ba/b/bv+bazjw-prodz.mp4" "zyoutube.comz)yt-dlp --cookies youtube_cookies.txt -f "z" "z" -o "z".mp4Úm3u8Z
livestreamzyt-dlp -f "z%" --no-keep-video --remux-video mkv "z	.%(ext)s"z.mp4"u!   **ðï¸ ððð_ðð: u   .

ð ðð¢ð­ð¥ð: u4    .mkv
ð ððð­ðð¡ ððð¦ð Â» u;   
ð¥ ðð¨ð°ð§ð¥ð¨ðððð ðð² Â» z**
**z**u   **ð ððð_ðð: u4    .pdf
ð ððð­ðð¡ ððð¦ð Â» z**
<c>Údrive)r   Údocumentr    z.pdfz.pdf" "z -R 25 --fragment-retries 25ud   **ââ± ðð¨ð°ð§ð¥ð¨ððð¢ð§ð  â±â... Â»**

**ð ððð¦ð Â»** `u'   
**â ðð®ðð¥ð¢ð­ð² Â» u&   `
**ðððð Â»** `[Hidden]`

us   â ðð¨ð°ð§ð¥ð¨ððð¢ð§ð  ðð§ð­ðð«ð®ð©ð­ðð

â ððð¦ð Â» u   
â ðð¢ð§ð¤ Â» `uI   **â ðð®ðððð¬ð¬ðð®ð¥ð¥ð² ðð¨ð§ð**éþÿÿÿrV   iòÿÿÿiòÿÿÿiòÿÿÿ)-r&   r   r!   r"   ZdownloadÚdeleteÚopenÚreadÚsplitÚappendr'   ÚremoveÚeditÚlenr   Ú	ExceptionÚ
startswithr	   ÚintÚrangeÚreplacer   ÚgetÚreÚsearchÚgroupÚrequestsÚjsonZ	raw_text4ÚstripÚstrÚzfillr   ÚhelperZget_drm_keysÚqualityÚcentered_textZsend_documentÚtimeÚsleepr   ÚxÚsystemZdownload_videoZsend_vid)8r   r-   ZeditableÚinputrr   ÚpathÚfÚcontentÚlinksÚiZinput0Zraw_textZinput1Z	raw_text0Zinput2Z	raw_text2ÚresZinput3Z	raw_text3ZhighlighterZMPHZinput6r   Z	raw_text6ZthumbÚcountÚVr   ÚsessionÚrespr   ÚnameÚcmdr9   r>   ÚresponseZvid_idZname1ÚkeyZbcovr"   ÚyZroutZcookÚy1ZytfÚccZcc1ÚkaÚcopyÚeZdownload_cmdZShowÚprogZres_fileÚfilenamer   r   r   r/   n   sl   











,
62

64
$(
h 






h 




..




  ")@r'   re   r)   ri   rp   ZaiohttpÚasynciorh   Ú
subprocessÚurllib.parseÚurllibZcloudscraperrS   ÚrandomZyt_dlpr   Z
youtube_dlÚcorerm   Úutilsr   Úvarsr   r   r   r   Zpyromodr   r	   Zpytuber
   Zpyrogramr   r   Zpyrogram.typesr   Zpyrogram.errorsr   Z*pyrogram.errors.exceptions.bad_request_400r   Z!pyrogram.types.messages_and_mediar   r   r   ÚgetenvZcookies_file_pathÚcenterro   r   Úenvironrd   r   r   r$   Z
image_urlsÚchoicer#   r    Z
on_messageÚcommandr%   r.   r/   Úrunr   r   r   r   Ú<module>   s~   


	 }