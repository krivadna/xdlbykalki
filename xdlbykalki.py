#!/usr/bin/env python3
import os,sys,argparse,re
from urllib.parse import urlparse,unquote
import base64
import zlib

# Obfuscated strings
_0x7291 = lambda x: base64.b64decode(x).decode('utf-8')
_0x8372 = lambda x: ''.join([chr(ord(c)^7) for c in x])
_0x9183 = lambda x: ''.join(reversed(x))
_0x6254 = lambda x: zlib.decompress(base64.b64decode(x)).decode('utf-8')

# Obfuscated constants
_0x1234 = _0x7291("L2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL2hvbWUvc3RvcmFnZS9kb3dubG9hZHMvVHdpdHRlci9NYWlu")
_0x2345 = [_0x8372("}#p}}ly5jvt"), _0x8372("5jvt"), _0x8372("~~~5}#p}}ly5jvt"), _0x8372("~~~55jvt")]
_0x3456 = [_0x9183("moc.rettiwt"), _0x9183("moc.x"), _0x9183("moc.rettiwt.www"), _0x9183("moc.x.www")]


def display_banner():
    banner = """
\033[1;36m
██╗  ██╗██████╗ ██╗
╚██╗██╔╝██╔══██╗██║
 ╚███╔╝ ██║  ██║██║
 ██╔██╗ ██║  ██║██║
██╔╝ ██╗██████╔╝███████╗
╚═╝  ╚═╝╚═════╝ ╚══════╝

    \033[1;32m[ Twitter Termux X Downloader ]\033[0m
    \033[1;33m[ Created by Cyber Kalki ]\033[0m
    \033[1;34m[\x1b]8;;https://kalkikrivadna.com\x1b\\https://kalkikrivadna.com\x1b]8;;\x1b\\]\033[0m
    \033[1;35m[\x1b]8;;https://github.com/krivadna\x1b\\https://github.com/krivadna\x1b]8;;\x1b\\]\033[0m
    """
    print(banner)
    try:
        import time
        time.sleep(1)
    except ImportError:
        pass


# Fixed help text
_0x9876 = """
USAGE:
  python3 xdlbykalki.py [options] <Twitter/X URL>

OPTIONS:
  -o, --output  <path>    Output directory (default: Termux downloads folder)
  -h, --help              Show this help message and exit

EXAMPLES:
  python3 xdlbykalki.py https://twitter.com/username/status/1234567890
  python3 xdlbykalki.py -o /path/to/directory https://x.com/username/status/1234567890

DESCRIPTION:
  This tool downloads videos from Twitter/X posts using multiple methods:
  1. yt-dlp (recommended, requires installation)
  2. twdown.net (web service fallback)
  3. savetweetvid.com (alternative web service)

  The tool will try each method in sequence until one succeeds.
"""

_0x7890 = display_banner

# Simple animation counter
animation_counter = 0

def _0xA831():
    _0x7890()
    try:
        import time as _t
        _t.sleep(1)
    except:
        pass

def _0xB942():
    print(_0x9876)

def _0xC053(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
            print(f"Created directory: {dir}")
        return True
    except Exception as e:
        print(f"Error creating directory {dir}: {e}")
        return False

def _0xD164(url):
    p = urlparse(unquote(url))
    if p.netloc in _0x2345 + _0x3456:
        clean_path = re.sub(r'\?.*$', '', p.path)
        scheme = p.scheme or 'https'
        return f"{scheme}://{p.netloc}{clean_path}"
    return url

def _0xE275(url):
    p = urlparse(url)
    if p.netloc in _0x2345 + _0x3456:
        path = p.path
        match = re.search(r'/status/(\d+)', path)
        if match:
            return match.group(1)
    return None

def show_animated_progress(percent, downloaded_mb, total_mb):
    """Display a progress bar with simple animation that works reliably in Termux"""
    global animation_counter
    animation_counter = (animation_counter + 1) % 4
    
    # Simple animation characters
    animation = ['-', '\\', '|', '/'][animation_counter]
    
    bar_width = 30
    filled_length = int(bar_width * percent / 100)
    bar = '█' * filled_length + '▒' * (bar_width - filled_length)
    
    sys.stdout.write(f"\r\033[1;36m[{animation}] [{bar}] {percent}% ({downloaded_mb:.1f}MB / {total_mb:.1f}MB)\033[0m")
    sys.stdout.flush()

def _0xF386(url, output_dir=_0x1234):
    try:
        try:
            import yt_dlp
        except ImportError:
            print("\033[1;33myt-dlp is not installed. Installing it now...\033[0m")
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
            import yt_dlp
            print("\033[1;32myt-dlp successfully installed.\033[0m")
        
        clean_tweet_url = _0xD164(url)
        tweet_id = _0xE275(clean_tweet_url)
        
        if not tweet_id:
            print("\033[1;31mInvalid Twitter/X URL\033[0m")
            return False
            
        print(f"\033[1;34mProcessing tweet with ID: {tweet_id}\033[0m")
        
        if not _0xC053(output_dir):
            return False
            
        output_filename = f"twitter_video_{tweet_id}.mp4"
        output_path = os.path.join(output_dir, output_filename)
            
        ydl_opts = {
            'format': 'best',
            'outtmpl': output_path,
            'quiet': False,
            'no_warnings': False,
            'progress': True,
            'verbose': False,
        }
        
        print(f"\033[1;32mDownloading video to {output_path}...\033[0m")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([clean_tweet_url])
            
        if os.path.exists(output_path):
            print(f"\n\033[1;32mVideo successfully downloaded to {output_path}\033[0m")
            return True
        else:
            print(f"\n\033[1;31mDownload seemed to succeed, but file not found at {output_path}\033[0m")
            return False
            
    except Exception as e:
        print(f"\033[1;31mError with yt-dlp download method: {e}\033[0m")
        return False

def _0x1A97(url, output_dir=_0x1234):
    try:
        import requests
    except ImportError:
        print("\033[1;33mrequests is not installed. Installing it now...\033[0m")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        import requests
        print("\033[1;32mrequests successfully installed.\033[0m")
    
    clean_tweet_url = _0xD164(url)
    tweet_id = _0xE275(clean_tweet_url)
    
    if not tweet_id:
        print("\033[1;31mInvalid Twitter/X URL\033[0m")
        return False
        
    print(f"\033[1;34mProcessing tweet with ID: {tweet_id} using twdown.net...\033[0m")
    
    if not _0xC053(output_dir):
        return False
        
    output_filename = f"twitter_video_{tweet_id}.mp4"
    output_path = os.path.join(output_dir, output_filename)
    
    api_url = _0x7291("aHR0cHM6Ly90d2Rvd24ubmV0L2Rvd25sb2FkLnBocA==")
    headers = {
        'User-Agent': _0x8372("Tvgpssh6;5+!^Dpukv~z!U[!8+5+B!^pu<=!?<=*!HwwslCliiP}6;:?5:<!!RO[TS3!sprl!!Nljrv*!Joyvtl6A85+5==?:58:=!Zhmhyp6;:?5:<"),
        'Content-Type': _0x8372("hwwspjh}pvu65.~~~.mvyt.|yslukvklk"),
        'Accept': _0x8372("}l}6o}ts3hwwspjh}pvu65o}ts2ts3hwwspjh}pvu65ts+x)+5A3pthnl6~liwHwwspjh}pvu65h}vt2ts3h}vt2ts3h}vt2ts+x)+5>"),
        'Origin': _0x7291("aHR0cHM6Ly90d2Rvd24ubmV0"),
        'Referer': _0x7291("aHR0cHM6Ly90d2Rvd24ubmV0Lw==")
    }
    
    data = {
        'URL': clean_tweet_url
    }
    
    try:
        response = requests.post(api_url, headers=headers, data=data)
        
        if response.status_code == 200:
            video_url_match = re.search(r'<a href="([^"]*)" class="btn btn-default btn-file" target="_blank">Download Video</a>', response.text)
            
            if video_url_match:
                video_url = video_url_match.group(1)
                
                print(f"\033[1;32mDownloading video to {output_path}...\033[0m")
                video_response = requests.get(video_url, stream=True)
                total_size = int(video_response.headers.get('content-length', 0))
                
                with open(output_path, 'wb') as f:
                    downloaded = 0
                    chunk_count = 0
                    for chunk in video_response.iter_content(chunk_size=1024*1024):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            chunk_count += 1
                            if total_size > 0:
                                percent = int(100 * downloaded / total_size)
                                # Update animation every chunk
                                show_animated_progress(percent, downloaded/(1024*1024), total_size/(1024*1024))
                
                print(f"\n\033[1;32mVideo successfully downloaded to {output_path}\033[0m")
                return True
            else:
                print("\033[1;31mNo video download links found on twdown.net.\033[0m")
                return False
        else:
            print(f"\033[1;31mtwdown.net service returned status code: {response.status_code}\033[0m")
            return False
            
    except Exception as e:
        print(f"\033[1;31mError with twdown.net download method: {e}\033[0m")
        return False

def _0x2BA8(url, output_dir=_0x1234):
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        print("\033[1;33mRequired libraries not installed. Installing them now...\033[0m")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests beautifulsoup4"])
        import requests
        from bs4 import BeautifulSoup
        print("\033[1;32mRequired libraries successfully installed.\033[0m")
    
    clean_tweet_url = _0xD164(url)
    tweet_id = _0xE275(clean_tweet_url)
    
    if not tweet_id:
        print("\033[1;31mInvalid Twitter/X URL\033[0m")
        return False
        
    print(f"\033[1;34mProcessing tweet with ID: {tweet_id} using savetweetvid.com...\033[0m")
    
    if not _0xC053(output_dir):
        return False
        
    output_filename = f"twitter_video_{tweet_id}.mp4"
    output_path = os.path.join(output_dir, output_filename)
    
    api_url = _0x7291("aHR0cHM6Ly93d3cuc2F2ZXR3ZWV0dmlkLmNvbS9kb3dubG9hZGVy")
    headers = {
        'User-Agent': _0x8372("Tvgpssh6;5+!^Dpukv~z!U[!8+5+B!^pu<=!?<=*!HwwslCliiP}6;:?5:<!!RO[TS3!sprl!!Nljrv*!Joyvtl6A85+5==?:58:=!Zhmhyp6;:?5:<"),
        'Content-Type': _0x8372("hwwspjh}pvu65.~~~.mvyt.|yslukvklk"),
        'Accept': _0x8372("}l}6o}ts3hwwspjh}pvu65o}ts2ts3hwwspjh}pvu65ts+x)+5A3pthnl6~liwHwwspjh}pvu65h}vt2ts3h}vt2ts3h}vt2ts+x)+5>"),
        'Origin': _0x7291("aHR0cHM6Ly93d3cuc2F2ZXR3ZWV0dmlkLmNvbQ=="),
        'Referer': _0x7291("aHR0cHM6Ly93d3cuc2F2ZXR3ZWV0dmlkLmNvbS8=")
    }
    
    data = {
        'url': clean_tweet_url
    }
    
    try:
        response = requests.post(api_url, headers=headers, data=data)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            download_links = soup.select('a[href*=".mp4"]')
            
            if download_links:
                video_url = download_links[0]['href']
                
                print(f"\033[1;32mDownloading video to {output_path}...\033[0m")
                video_response = requests.get(video_url, stream=True)
                total_size = int(video_response.headers.get('content-length', 0))
                
                with open(output_path, 'wb') as f:
                    downloaded = 0
                    chunk_count = 0
                    for chunk in video_response.iter_content(chunk_size=1024*1024):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            chunk_count += 1
                            if total_size > 0:
                                percent = int(100 * downloaded / total_size)
                                # Update animation every chunk
                                show_animated_progress(percent, downloaded/(1024*1024), total_size/(1024*1024))
                
                print(f"\n\033[1;32mVideo successfully downloaded to {output_path}\033[0m")
                return True
            else:
                print("\033[1;31mNo video download links found on savetweetvid.com.\033[0m")
                return False
        else:
            print(f"\033[1;31msavetweetvid.com service returned status code: {response.status_code}\033[0m")
            return False
            
    except Exception as e:
        print(f"\033[1;31mError with savetweetvid.com download method: {e}\033[0m")
        return False

def _0x3CB9():
    _0xA831()
    
    parser = argparse.ArgumentParser(description=_0x7291("RG93bmxvYWQgdmlkZW9zIGZyb20gVHdpdHRlci9YLg=="), add_help=False)
    parser.add_argument('url', nargs='?', type=str, help=_0x8372("[~p}}ly6_!}~ll}!]YS!jvu}hpupun!}pklv"))
    parser.add_argument('-o', '--output', type=str, help=f'Output directory (default: {_0x1234})', default=_0x1234)
    parser.add_argument('-h', '--help', action='store_true', help=_0x7291("U2hvdyB0aGlzIGhlbHAgbWVzc2FnZSBhbmQgZXhpdA=="))
    
    args = parser.parse_args()
    
    if args.help or not args.url:
        _0xB942()
        return
    
    print("\033[1;33m[+] Attempting download with yt-dlp (Method 1)...\033[0m")
    if _0xF386(args.url, args.output):
        return
    
    print("\n\033[1;33m[+] Method 1 failed. Trying with twdown.net (Method 2)...\033[0m")
    if _0x1A97(args.url, args.output):
        return
    
    print("\n\033[1;33m[+] Method 2 failed. Trying with savetweetvid.com (Method 3)...\033[0m")
    if _0x2BA8(args.url, args.output):
        return
        
    print("\n\033[1;31m[!] All download methods failed. The tweet might not contain a video or might be protected.\033[0m")

if __name__ == "__main__":
    try:
        _0x3CB9()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Download canceled by user\033[0m")
    except Exception as e:
        print(f"\n\033[1;31m[!] An unexpected error occurred: {e}\033[0m")
