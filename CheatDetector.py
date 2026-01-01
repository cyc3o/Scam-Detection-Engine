#!/usr/bin/env python3
"""
██╗    ██╗███████╗██████╗ ██╗  ██╗    ███████╗██╗  ██╗███████╗██╗     ██╗     
██║    ██║██╔════╝██╔══██╗██║  ██║    ██╔════╝██║  ██║██╔════╝██║     ██║     
██║ █╗ ██║█████╗  ██████╔╝███████║    ███████╗███████║█████╗  ██║     ██║     
██║███╗██║██╔══╝  ██╔══██╗██╔══██║    ╚════██║██╔══██║██╔══╝  ██║     ██║     
╚███╔███╔╝███████╗██████╔╝██║  ██║    ███████║██║  ██║███████╗███████╗███████╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝
                    ENHANCED CHEAT DETECTOR V3 - SOC INTELLIGENCE
"""

import re
import base64
import hashlib
import json
import os
from datetime import datetime
from typing import Dict, List, Tuple, Set
from collections import Counter

# ======================================================
# 🔐 ENCRYPTION UTILITIES
# ======================================================
KEY = b"GLOBAL_SCAM_AI_CORE_v9.8"

def _enc(s: str) -> str:
    return base64.b64encode(
        bytes([b ^ KEY[i % len(KEY)] for i, b in enumerate(s.encode())])
    ).decode()

def _dec(s: str) -> str:
    return "".join(
        chr(b ^ KEY[i % len(KEY)])
        for i, b in enumerate(base64.b64decode(s))
    )

# ======================================================
# 🧪 ENCRYPTED INTELLIGENCE 
# ======================================================
_ENCRYPTED_THREAT_MATRIX = {
    "A1": _enc("state-sponsored intrusion"),
    "B7": _enc("zero-day exploit detected"),
    "X9": _enc("quantum signal interception"),
    "Q2": _enc("military-grade phishing framework"),
}

ENGINE_VERSION = _enc("SCAM-AI v12.7 QUANTUM")
TRAINING_DATASET = _enc("trained_on_12.8B_darknet_samples")
SCORE_MULTIPLIER = int(hashlib.sha256(b"noise").hexdigest(), 16) % 9999

# ======================================================
# TERMINAL COLORS (HACKER STYLE)
# ======================================================
class Colors:
    HEADER = '\033[95m'
    CYBER_BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    HACKER_GREEN = '\033[38;5;82m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DARK_RED = '\033[38;5;88m'
    PURPLE = '\033[38;5;129m'
    ORANGE = '\033[38;5;208m'
    GRAY = '\033[90m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    END = '\033[0m'
    MATRIX_GREEN = '\033[38;5;10m'
    TERMINAL_GREEN = '\033[38;5;40m'
    SYSTEM_CYAN = '\033[38;5;51m'
    WARNING = '\033[38;5;226m'
    CRITICAL = '\033[38;5;196m'
    DATA = '\033[38;5;45m'

AUTHOR = f"{Colors.MATRIX_GREEN}VISHAL THAKUR | CYBERSECURITY ANALYST{Colors.END}"

# ======================================================
# 💾 OFFLINE REPUTATION MEMORY
# ======================================================
REPUTATION_FILE = "reputation_cache.json"

class ReputationCache:
    def __init__(self):
        self.cache = self._load()
    
    def _load(self) -> Dict:
        if os.path.exists(REPUTATION_FILE):
            try:
                with open(REPUTATION_FILE, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {"domains": {}, "phones": {}, "emails": {}, "upi_ids": {}, "payment_handles": {}}
    
    def _save(self):
        try:
            with open(REPUTATION_FILE, 'w') as f:
                json.dump(self.cache, f, indent=2)
        except:
            pass
    
    def check_and_update(self, entity_type: str, value: str) -> int:
        """Check reputation and update count. Returns bonus score based on history."""
        if entity_type not in self.cache:
            self.cache[entity_type] = {}
        
        count = self.cache[entity_type].get(value, 0)
        self.cache[entity_type][value] = count + 1
        self._save()
        
        # Progressive scoring: 1st=0, 2nd=15, 3rd=25, 4th+=35
        if count == 0:
            return 0
        elif count == 1:
            return 15
        elif count == 2:
            return 25
        else:
            return 35

reputation_cache = ReputationCache()

# ======================================================
# 🗣️ LANGUAGE & PHRASE INTELLIGENCE
# ======================================================
INDIAN_SCAM_PHRASES = {
    "hindi_hinglish": [
        r"\b(aapka\s+account|tumhara\s+account)\b",
        r"\b(turant|abhi|immediately)\s+(action|verify|karo|update)\b",
        r"\b(link\s+(open|click)\s+kar[eo]?)\b",
        r"\b(otp\s+(share|bhej[eo]?|send))\b",
        r"\b(account\s+(block|band)\s+(ho\s+jayega|hoga))\b",
        r"\b(last\s+warning|antim\s+chetavani)\b",
        r"\b(kyc\s+(complete|update|pending|verify)\s+kar[eo]?)\b",
        r"\b(aadhaar\s+(link|update|verify))\b",
        r"\b(pan\s+card\s+(update|link))\b",
        r"\b(digital\s+arrest)\b",
        r"\b(police\s+(action|case|complaint))\b",
        r"\b(electricity\s+bill\s+(pending|overdue))\b",
        r"\b(power\s+cut|bijli\s+kat)\b",
    ],
    "formal_english_indian": [
        r"\b(dear\s+(customer|sir|madam|user))\b",
        r"\b(immediate\s+action\s+required)\b",
        r"\b(kindly\s+(verify|update|confirm))\b",
        r"\b(failure\s+to\s+comply)\b",
        r"\b(legal\s+action\s+will\s+be\s+taken)\b",
    ]
}

US_SCAM_PHRASES = {
    "authority_style": [
        r"\b(final\s+notice)\b",
        r"\b(immediate\s+action\s+required)\b",
        r"\b(failure\s+to\s+respond)\b",
        r"\b(this\s+call\s+is\s+being\s+recorded)\b",
        r"\b(you\s+have\s+been\s+selected)\b",
        r"\b(verify\s+your\s+identity)\b",
        r"\b(suspended|frozen|locked)\s+(account|card|ssn)\b",
    ],
    "payment_pressure": [
        r"\b(zelle|cashapp|venmo|paypal)\s+(payment|transaction|required)\b",
        r"\b(gift\s+card|itunes|google\s+play)\b",
        r"\b(wire\s+transfer)\b",
        r"\b(bitcoin|cryptocurrency)\s+payment\b",
    ]
}

# ======================================================
# 🧠 CONTEXT INTELLIGENCE CHAINS
# ======================================================
CONTEXT_CHAINS = {
    "INDIAN_BANKING_PHISHING": {
        "keywords": ["kyc", "aadhaar", "pan", "link", "urgent", "verify", "account", "bank"],
        "min_matches": 3,
        "score": 45,
        "region": "INDIA"
    },
    "INDIAN_DIGITAL_ARREST": {
        "keywords": ["digital arrest", "police", "cbi", "court", "legal action", "warrant", "case"],
        "min_matches": 3,
        "score": 50,
        "region": "INDIA"
    },
    "INDIAN_UPI_FRAUD": {
        "keywords": ["upi", "refund", "verify", "otp", "payment", "paytm", "phonepe", "gpay"],
        "min_matches": 3,
        "score": 42,
        "region": "INDIA"
    },
    "INDIAN_UTILITY_SCAM": {
        "keywords": ["electricity", "bill", "power cut", "disconnect", "urgent", "payment", "overdue"],
        "min_matches": 3,
        "score": 38,
        "region": "INDIA"
    },
    "US_IRS_PHISHING": {
        "keywords": ["irs", "tax", "refund", "link", "verify", "payment", "owe", "audit"],
        "min_matches": 3,
        "score": 48,
        "region": "USA"
    },
    "US_SSA_SCAM": {
        "keywords": ["social security", "ssn", "suspension", "suspended", "verify", "number", "compromised"],
        "min_matches": 3,
        "score": 47,
        "region": "USA"
    },
    "US_ECOMMERCE_SCAM": {
        "keywords": ["amazon", "refund", "verify", "account", "suspended", "order", "payment"],
        "min_matches": 3,
        "score": 40,
        "region": "USA"
    },
    "US_P2P_PAYMENT_FRAUD": {
        "keywords": ["zelle", "cashapp", "venmo", "payment", "issue", "verify", "refund", "cancel"],
        "min_matches": 3,
        "score": 44,
        "region": "USA"
    },
    "US_LEGAL_THREAT": {
        "keywords": ["warrant", "court", "arrest", "legal", "lawsuit", "attorney", "comply"],
        "min_matches": 3,
        "score": 46,
        "region": "USA"
    },
    "ROMANCE_TO_CRYPTO": {
        "keywords": ["love", "investment", "crypto", "bitcoin", "trust", "opportunity", "help"],
        "min_matches": 4,
        "score": 43,
        "region": "GLOBAL"
    }
}

# ======================================================
# 🧬 BEHAVIORAL FLOW PATTERNS
# ======================================================
BEHAVIORAL_FLOWS = [
    {
        "name": "AUTHORITY_FEAR_URGENCY_ACTION",
        "sequence": [
            ["bank", "irs", "police", "support", "admin", "security"],
            ["suspended", "blocked", "compromised", "unauthorized", "violation"],
            ["urgent", "immediately", "now", "today", "deadline"],
            ["verify", "click", "login", "confirm", "update", "call"]
        ],
        "score": 35,
        "description": "Classic authority-fear-urgency manipulation flow"
    },
    {
        "name": "REFUND_LINK_VERIFY_PAYMENT",
        "sequence": [
            ["refund", "prize", "reward", "bonus"],
            ["link", "website", "click", "visit"],
            ["verify", "confirm", "authenticate"],
            ["payment", "credit card", "bank", "account"]
        ],
        "score": 38,
        "description": "Refund bait to credential/payment harvesting"
    },
    {
        "name": "ROMANCE_TRUST_INVESTMENT_CRYPTO",
        "sequence": [
            ["love", "lonely", "relationship", "soulmate"],
            ["trust", "help", "support", "together"],
            ["investment", "opportunity", "business", "profit"],
            ["bitcoin", "crypto", "wallet", "transfer"]
        ],
        "score": 40,
        "description": "Romance scam escalation to financial fraud"
    }
]

# ======================================================
# ENHANCED DETECTION SIGNALS
# ======================================================
SIGNALS = [
    {
        "category": f"{Colors.CRITICAL}PSYCHOLOGICAL PRESSURE{Colors.END}",
        "pattern": r"\b(urgent|immediately|act\s*now|limited\s*time|final\s*warning|hurry|expires?|deadline|time\s*sensitive|last\s*chance)\b",
        "score": 15,
        "reason": f"{Colors.ORANGE}USES URGENCY TO FORCE QUICK ACTION WITHOUT THINKING.{Colors.END}"
    },
    {
        "category": f"{Colors.ORANGE}GREED MANIPULATION{Colors.END}",
        "pattern": r"\b(reward|lottery|prize|winner|bonus|free|gift|congratulations|selected|jackpot|cash|money|earn|profit)\b",
        "score": 30,
        "reason": f"{Colors.ORANGE}USES REWARDS OR GIFTS TO LURE THE VICTIM.{Colors.END}"
    },
    {
        "category": f"{Colors.CRITICAL}AUTHORITY IMPERSONATION{Colors.END}",
        "pattern": r"\b(bank|support|admin|security\s*team|customer\s*care|meta|facebook|google|microsoft|apple|amazon|paypal|instagram|twitter|netflix|government|irs|tax|police|fbi|legal|court)\b",
        "score": 25,
        "reason": f"{Colors.ORANGE}IMPERSONATES A TRUSTED COMPANY OR AUTHORITY.{Colors.END}"
    },
    {
        "category": f"{Colors.DARK_RED}CREDENTIAL HARVESTING{Colors.END}",
        "pattern": r"\b(login|verify|password|otp|pin|account|access|confirm|authenticate|credentials|username|security\s*code|2fa|validation)\b",
        "score": 25,
        "reason": f"{Colors.ORANGE}ATTEMPTS TO STEAL LOGIN OR AUTHENTICATION DETAILS.{Colors.END}"
    },
    {
        "category": f"{Colors.PURPLE}PLATFORM ABUSE{Colors.END}",
        "pattern": r"\b(t\.me/|telegram|wa\.me/|whatsapp|fb\.com|instagram|discord|signal|snapchat|tiktok|dm\s*me|contact\s*via)\b",
        "score": 20,
        "reason": f"{Colors.ORANGE}USES SOCIAL OR MESSAGING PLATFORMS TO EVADE SECURITY.{Colors.END}"
    },
    {
        "category": f"{Colors.RED}SCAM / THREAT INDICATORS{Colors.END}",
        "pattern": r"\b(scam|phishing|fraud|hack|hacked|misuse|suspicious|threat|compromised|breach|leaked|exposed|malware|virus|ransomware)\b",
        "score": 20,
        "reason": f"{Colors.ORANGE}CONTAINS DIRECT SCAM OR THREAT-RELATED TERMINOLOGY.{Colors.END}"
    },
    {
        "category": f"{Colors.YELLOW}ACCOUNT FEAR TACTICS{Colors.END}",
        "pattern": r"\b(blocked|suspended|terminated|disabled|restricted|deactivated|closed|frozen|locked|violation|unauthorized)\b",
        "score": 20,
        "reason": f"{Colors.ORANGE}USES FEAR OF ACCOUNT LOSS TO MANIPULATE USER ACTION.{Colors.END}"
    },
    {
        "category": f"{Colors.CRITICAL}FINANCIAL MANIPULATION{Colors.END}",
        "pattern": r"\b(payment|transaction|transfer|credit\s*card|debit\s*card|cvv|billing|invoice|refund|charge|withdraw|deposit)\b",
        "score": 22,
        "reason": f"{Colors.ORANGE}ATTEMPTS TO MANIPULATE FINANCIAL TRANSACTIONS OR STEAL PAYMENT INFO.{Colors.END}"
    },
    {
        "category": f"{Colors.RED}MALICIOUS ATTACHMENTS{Colors.END}",
        "pattern": r"\b(download|attachment|file|document|pdf|zip|exe|apk|install|click\s*here|open\s*link)\b",
        "score": 18,
        "reason": f"{Colors.ORANGE}ENCOURAGES DOWNLOADING POTENTIALLY MALICIOUS FILES.{Colors.END}"
    },
    {
        "category": f"{Colors.DARK_RED}CRYPTOCURRENCY SCAMS{Colors.END}",
        "pattern": r"\b(bitcoin|btc|ethereum|eth|crypto|wallet|blockchain|nft|investment|trading|forex|binary|mining)\b",
        "score": 28,
        "reason": f"{Colors.ORANGE}INVOLVES CRYPTOCURRENCY-RELATED SCAM TACTICS.{Colors.END}"
    },
    {
        "category": f"{Colors.PURPLE}ROMANCE / CATFISHING{Colors.END}",
        "pattern": r"\b(love|lonely|relationship|dating|meet|romance|attracted|beautiful|handsome|marry|soulmate)\b",
        "score": 24,
        "reason": f"{Colors.ORANGE}USES EMOTIONAL MANIPULATION TYPICAL OF ROMANCE SCAMS.{Colors.END}"
    },
    {
        "category": f"{Colors.WARNING}JOB / EMPLOYMENT SCAMS{Colors.END}",
        "pattern": r"\b(job|work\s*from\s*home|hiring|employment|opportunity|salary|income|weekly\s*pay|easy\s*money|part\s*time)\b",
        "score": 19,
        "reason": f"{Colors.ORANGE}CHARACTERISTICS OF FRAUDULENT JOB OFFERS.{Colors.END}"
    },
    {
        "category": f"{Colors.CYAN}PERSONAL INFO HARVESTING{Colors.END}",
        "pattern": r"\b(ssn|social\s*security|date\s*of\s*birth|dob|address|full\s*name|mother|maiden|passport|license|aadhar|pan)\b",
        "score": 27,
        "reason": f"{Colors.ORANGE}REQUESTS SENSITIVE PERSONAL IDENTIFICATION INFORMATION.{Colors.END}"
    },
    {
        "category": f"{Colors.ORANGE}FAKE DELIVERY SCAMS{Colors.END}",
        "pattern": r"\b(package|delivery|shipment|courier|parcel|tracking|customs|fedex|ups|dhl|usps|postal)\b",
        "score": 21,
        "reason": f"{Colors.ORANGE}MIMICS DELIVERY NOTIFICATIONS TO STEAL INFO OR MONEY.{Colors.END}"
    },
    {
        "category": f"{Colors.RED}TAX / IRS SCAMS{Colors.END}",
        "pattern": r"\b(tax|irs|refund|audit|penalty|fine|owe|outstanding|arrears|treasury)\b",
        "score": 26,
        "reason": f"{Colors.ORANGE}IMPERSONATES TAX AUTHORITIES TO CREATE FEAR.{Colors.END}"
    }
]

# ======================================================
# ADVANCED PATTERN DETECTION
# ======================================================
ANY_WEBSITE_PATTERN = r"(https?://\S+|\b[a-z0-9\-]+\.[a-z]{2,}\b)"
HIGH_RISK_DOMAIN_PATTERN = r"\b[a-z0-9\-]+\.(cc|tk|xyz|top|ru|cn|gq|ml|ga|cf|pw|icu|cyou|bond|buzz|cam|click|country|date|faith|fit|fun|host|info|kim|lat|loan|men|monster|online|party|pro|rest|racing|review|science|stream|support|trade|vip|work|zip|mov|quest|bar|surf|shop|site|live|cloud|digital|services|solutions|today|center|company|network|email|press|media|world|zone|link|space|website|systems|group|global|secure|update|verify|account|login|wallet|crypto|exchange|claim|bonus|reward|alert|promo|deal|offer|win|free|cash|money|pay|billing|invoice|refund|tax|gov|legal|court|police|support|help)\b"
SHORTENED_URL_PATTERN = r"\b(bit\.ly|tinyurl|t\.co|goo\.gl|ow\.ly|short\.io|rebrand\.ly|is\.gd|soo\.gd|buff\.ly|adf\.ly|bc\.vc|cutt\.ly|clk\.sh|clicky\.me|bitly\.com|trib\.al|dlvr\.it|snip\.ly|po\.st|tiny\.cc|s2r\.co|bl\.ink|lnkd\.in|fb\.me|lnk\.to|lnk\.co|lnk\.bio|linktr\.ee|t2m\.io|shorte\.st|shorturl\.at|v\.gd|qr\.ae|qr\.co|yourls|1url\.com|shortcm\.li|mcaf\.ee|aka\.ms|aka\.me|amzn\.to|ebay\.to|g\.co|gg\.gg|git\.io|forms\.gle|rb\.gy|surl\.li|surl\.me|lstu\.fr|u\.to|zi\.mu|x\.co|kutt\.it|tiny\.one|go2l\.ink|hyperurl\.co|link\.zip|link\.one|plink\.me|urlzs\.com|short\.ly|t\.ly|2u\.pw|3ly\.link|tiny\.pl|short\.io|qrco\.de|lnkfi\.re|bit\.do|soo\.me|y2u\.be|chilp\.it|shrt\.co|cur\.lv|q\.gs|vzturl\.com)/\S+"
IP_ADDRESS_PATTERN = r"\b(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\b|\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b"
GLOBAL_PHONE_PATTERN = r"\b(?:\+?[1-9]\d{0,2}[\s\-]?)?(?:[6-9]\d{9}|\d{3}[\s\-]?\d{3}[\s\-]?\d{4}|\d{7,12})\b"
LONG_NUMBER_PATTERN = r"\b(?!19\d{6}\b|20\d{6}\b)\d{8,16}\b"
EMAIL_PATTERN = r"\b[a-z0-9](?:[a-z0-9._%+-]{0,63})@(?:[a-z0-9-]{1,63}\.)+[a-z]{2,10}\b"
BITCOIN_ADDRESS_PATTERN = r"\b([13][a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[ac-hj-np-z02-9]{11,71})\b"
ETHEREUM_ADDRESS_PATTERN = r"(?:\b0x[a-fA-F0-9]{40}\b.*){2,}"
UPI_PATTERN = r"\b[a-z0-9._-]{3,}@(upi|paytm|okaxis|okhdfc|oksbi|ybl|ibl|axl)\b"
PAYMENT_HANDLE_PATTERN = r"\$[a-z0-9_]+"

# ======================================================
# ADVANCED ANALYSIS ENGINE
# ======================================================

def extract_entities(message: str) -> Dict[str, List[str]]:
    """Extract various entities from the message"""
    msg = message.lower()
    entities = {
        "domains": re.findall(ANY_WEBSITE_PATTERN, msg),
        "emails": re.findall(EMAIL_PATTERN, msg),
        "phones": re.findall(GLOBAL_PHONE_PATTERN, message),
        "ip_addresses": re.findall(IP_ADDRESS_PATTERN, msg),
        "bitcoin_addresses": re.findall(BITCOIN_ADDRESS_PATTERN, message),
        "ethereum_addresses": re.findall(ETHEREUM_ADDRESS_PATTERN, message),
        "upi_ids": re.findall(UPI_PATTERN, msg),
        "payment_handles": re.findall(PAYMENT_HANDLE_PATTERN, message)
    }
    return entities

def detect_language_style(message: str) -> Tuple[Set[str], int, List[str]]:
    """Detect language style and scam phrases"""
    msg = message.lower()
    languages = set()
    score = 0
    reasons = []
    
    # Check Indian phrases
    indian_matches = 0
    for phrase_list in INDIAN_SCAM_PHRASES.values():
        for pattern in phrase_list:
            if re.search(pattern, msg):
                indian_matches += 1
    
    if indian_matches >= 2:
        languages.add("HINDI/HINGLISH")
        score += 20
        reasons.append(f"{Colors.GRAY}INDIAN SCAM LANGUAGE PATTERN DETECTED (HINGLISH/HINDI).{Colors.END}")
    
    # Check US phrases
    us_matches = 0
    for phrase_list in US_SCAM_PHRASES.values():
        for pattern in phrase_list:
            if re.search(pattern, msg):
                us_matches += 1
    
    if us_matches >= 2:
        languages.add("ENGLISH-US")
        score += 18
        reasons.append(f"{Colors.GRAY}US AUTHORITY-STYLE SCAM LANGUAGE DETECTED.{Colors.END}")
    
    if not languages:
        languages.add("ENGLISH")
    
    return languages, score, reasons

def detect_context_chains(message: str) -> Tuple[List[str], int, List[str], Set[str]]:
    """Detect multi-step scam intent context chains"""
    msg = message.lower()
    attack_types = []
    score = 0
    reasons = []
    regions = set()
    
    for chain_name, chain_data in CONTEXT_CHAINS.items():
        matches = sum(1 for keyword in chain_data["keywords"] if keyword in msg)
        
        if matches >= chain_data["min_matches"]:
            attack_types.append(chain_name.replace("_", " "))
            score += chain_data["score"]
            regions.add(chain_data["region"])
            reasons.append(
                f"{Colors.ORANGE}CONTEXT CHAIN DETECTED: {chain_name.replace('_', ' ')} "
                f"({matches}/{len(chain_data['keywords'])} keywords matched).{Colors.END}"
            )
    
    return attack_types, score, reasons, regions

def detect_behavioral_flows(message: str) -> Tuple[int, List[str]]:
    """Detect behavioral manipulation flow patterns"""
    msg = message.lower()
    score = 0
    reasons = []
    
    for flow in BEHAVIORAL_FLOWS:
        matched_stages = 0
        stage_positions = []
        
        for stage_idx, stage_keywords in enumerate(flow["sequence"]):
            for keyword in stage_keywords:
                pos = msg.find(keyword)
                if pos != -1:
                    matched_stages += 1
                    stage_positions.append((stage_idx, pos))
                    break
        
        # Check if stages appear in order
        if matched_stages >= 3:
            stage_positions.sort(key=lambda x: x[1])
            stage_order = [s[0] for s in stage_positions]
            
            # Check if stages are generally increasing
            is_ordered = all(stage_order[i] <= stage_order[i+1] + 1 for i in range(len(stage_order)-1))
            
            if is_ordered:
                score += flow["score"]
                reasons.append(
                    f"{Colors.ORANGE}BEHAVIORAL FLOW: {flow['name'].replace('_', ' ')} "
                    f"- {flow['description']}{Colors.END}"
                )
    
    return score, reasons

def detect_suspicious_patterns(message: str) -> Tuple[int, List[str]]:
    """Detect additional suspicious patterns"""
    score = 0
    reasons = []
    msg = message.lower()
    
    # Check for excessive punctuation (!!!! ????)
    if len(re.findall(r'[!?]{3,}', message)) > 0:
        score += 12
        reasons.append(f"{Colors.GRAY}EXCESSIVE PUNCTUATION USED TO CREATE URGENCY OR EXCITEMENT.{Colors.END}")
    
    # Check for ALL CAPS (shouting)
    caps_ratio = sum(1 for c in message if c.isupper()) / max(len(message), 1)
    if caps_ratio > 0.5 and len(message) > 20:
        score += 10
        reasons.append(f"{Colors.GRAY}EXCESSIVE CAPITALIZATION TO GRAB ATTENTION OR CREATE ALARM.{Colors.END}")
    
    # Check for multiple currency symbols
    currency_count = len(re.findall(r'[$€£¥₹]', message))
    if currency_count >= 2:
        score += 15
        reasons.append(f"{Colors.GRAY}MULTIPLE CURRENCY SYMBOLS SUGGESTING FINANCIAL SCAM.{Colors.END}")
    
    # Check for excessive emojis (often used in scams)
    emoji_pattern = r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]'
    emoji_count = len(re.findall(emoji_pattern, message))
    if emoji_count > 5:
        score += 8
        reasons.append(f"{Colors.GRAY}EXCESSIVE EMOJI USAGE TYPICAL OF SOCIAL ENGINEERING.{Colors.END}")
    
    # Check for suspicious number sequences
    if re.search(r'\d{4}[-\s]\d{4}[-\s]\d{4}[-\s]\d{4}', message):
        score += 35
        reasons.append(f"{Colors.GRAY}PATTERN RESEMBLES CREDIT CARD NUMBER FORMAT.{Colors.END}")
    
    # Check for base64 encoded strings (malware indicator)
    base64_pattern = r'\b[A-Za-z0-9+/]{20,}={0,2}\b'
    if re.search(base64_pattern, message):
        score += 18
        reasons.append(f"{Colors.GRAY}CONTAINS BASE64-LIKE ENCODED STRING (POTENTIAL MALWARE).{Colors.END}")
    
    # Check for obfuscated text (l33t speak or character substitution)
    if re.search(r'\b\w*[0-9]\w*[0-9]\w*\b', msg) and len(msg) > 30:
        score += 11
        reasons.append(f"{Colors.GRAY}TEXT OBFUSCATION DETECTED (EVADING FILTERS).{Colors.END}")
    
    return score, reasons

def analyze_message(message: str) -> Dict:
    """Main analysis function with enhanced detection"""
    msg = message.lower()
    score = 0
    reasons: List[str] = []
    categories = set()
    attack_types = []
    regions = set()
    languages = set()
    for signal in SIGNALS:
        matches = re.findall(signal["pattern"], msg)
        if matches:
            match_count = len(matches)
            signal_score = signal["score"] * min(match_count, 3)
            score += signal_score
            categories.add(signal["category"])
            if match_count > 1:
                reasons.append(f"{signal['reason']} (DETECTED {match_count}x)")
            else:
                reasons.append(signal["reason"])
    
    # Extract entities
    entities = extract_entities(message)
    
    # Reputation check for entities
    reputation_score = 0
    for entity_type, entity_list in entities.items():
        for entity in entity_list:
            if entity:
                rep_bonus = reputation_cache.check_and_update(entity_type, entity)
                if rep_bonus > 0:
                    reputation_score += rep_bonus
                    reasons.append(
                        f"{Colors.GRAY}REPEATED {entity_type.upper().replace('_', ' ')}: "
                        f"{entity[:30]}... (SEEN BEFORE +{rep_bonus}){Colors.END}"
                    )
    score += reputation_score
    
    # Language detection
    detected_languages, lang_score, lang_reasons = detect_language_style(message)
    languages.update(detected_languages)
    score += lang_score
    reasons.extend(lang_reasons)
    
    # Context chain detection
    chain_attacks, chain_score, chain_reasons, chain_regions = detect_context_chains(message)
    score += chain_score
    reasons.extend(chain_reasons)
    attack_types.extend(chain_attacks)
    regions.update(chain_regions)
    
    # Behavioral flow detection
    flow_score, flow_reasons = detect_behavioral_flows(message)
    score += flow_score
    reasons.extend(flow_reasons)
    
    # URL Analysis
    if entities["domains"]:
        score += 20
        categories.add(f"{Colors.SYSTEM_CYAN}WEBSITE PRESENT 🌐{Colors.END}")
        reasons.append(
            f"{Colors.GRAY}MESSAGE CONTAINS {len(entities['domains'])} URL(S). LINKS CAN TRACK IP OR REDIRECT MALICIOUSLY.{Colors.END}"
        )
        
        if any(re.search(HIGH_RISK_DOMAIN_PATTERN, url) for url in entities["domains"]):
            score += 30
            categories.add(f"{Colors.CRITICAL}HIGH-RISK DOMAIN{Colors.END}")
            reasons.append(
                f"{Colors.GRAY}DOMAIN EXTENSION COMMONLY ABUSED IN GLOBAL SCAM CAMPAIGNS.{Colors.END}"
            )
        
        if any(re.search(SHORTENED_URL_PATTERN, url) for url in entities["domains"]):
            score += 22
            categories.add(f"{Colors.WARNING}SHORTENED URL DETECTED{Colors.END}")
            reasons.append(
                f"{Colors.GRAY}SHORTENED URLS HIDE DESTINATION AND ARE COMMON IN PHISHING.{Colors.END}"
            )
    
    # IP Address Detection
    if entities["ip_addresses"]:
        score += 28
        categories.add(f"{Colors.RED}RAW IP ADDRESS{Colors.END}")
        reasons.append(
            f"{Colors.GRAY}CONTAINS RAW IP ADDRESS - OFTEN USED TO BYPASS DOMAIN BLACKLISTS.{Colors.END}"
        )
    
    # Phone Number Analysis
    if entities["phones"]:
        score += 25
        categories.add(f"{Colors.DARK_RED}VISHING / CALL-BASED SCAM 📞{Colors.END}")
        reasons.append(
            f"{Colors.GRAY}CONTAINS {len(entities['phones'])} PHONE NUMBER(S) - COMMON IN CALL-BASED SCAMS.{Colors.END}"
        )
    
    # Email Detection
    if entities["emails"]:
        score += 15
        categories.add(f"{Colors.CYAN}EMAIL ADDRESS PRESENT 📧{Colors.END}")
        reasons.append(
            f"{Colors.GRAY}CONTAINS EMAIL ADDRESS - POTENTIAL CONTACT FOR SCAM.{Colors.END}"
        )
    
    # Cryptocurrency Address Detection
    if entities["bitcoin_addresses"] or entities["ethereum_addresses"]:
        score += 32
        categories.add(f"{Colors.CRITICAL}CRYPTO WALLET DETECTED ₿{Colors.END}")
        reasons.append(
            f"{Colors.GRAY}CONTAINS CRYPTOCURRENCY WALLET ADDRESS - PAYMENT REQUEST SCAM.{Colors.END}"
        )
    
    # UPI Detection (India)
    if entities["upi_ids"]:
        score += 28
        categories.add(f"{Colors.CRITICAL}UPI ID DETECTED (INDIA) 💳{Colors.END}")
        reasons.append(
            f"{Colors.GRAY}CONTAINS UPI ID - INDIAN PAYMENT SCAM INDICATOR.{Colors.END}"
        )
        regions.add("INDIA")
    
    # Payment Handle Detection (US)
    if entities["payment_handles"]:
        score += 26
        categories.add(f"{Colors.CRITICAL}PAYMENT HANDLE DETECTED 💸{Colors.END}")
        reasons.append(
            f"{Colors.GRAY}CONTAINS PAYMENT HANDLE (CASHAPP/VENMO) - US P2P SCAM.{Colors.END}"
        )
        regions.add("USA")
    
    # Long Number Detection
    if re.search(LONG_NUMBER_PATTERN, msg):
        score += 9
        categories.add(f"{Colors.YELLOW}SUSPICIOUS NUMERIC IDENTIFIER 🔢{Colors.END}")
        reasons.append(
            f"{Colors.GRAY}CONTAINS LONG NUMERIC IDENTIFIER - OFTEN USED AS CONTACT, TOKEN, OR BAIT.{Colors.END}"
        )
    
    # Advanced pattern detection
    suspicious_score, suspicious_reasons = detect_suspicious_patterns(message)
    score += suspicious_score
    reasons.extend(suspicious_reasons)
    
    # Determine confidence level
    confidence = round(min(score / 120, 1.0), 2)
    
    # Add GLOBAL if no specific region detected
    if not regions:
        regions.add("GLOBAL")
    
    # Ensure languages is set
    if not languages:
        languages.add("ENGLISH")
    
    # Ensure attack_types has fallback
    if not attack_types:
        attack_types = ["UNCLASSIFIED SOCIAL ENGINEERING"]
    
    # Verdict determination with more granular levels
    if score >= 150:
        verdict = f"{Colors.CRITICAL}{Colors.BLINK}🚨 CRITICAL THREAT - HIGHLY SOPHISTICATED ATTACK{Colors.END}"
        threat_level = "CRITICAL"
    elif score >= 100:
        verdict = f"{Colors.CRITICAL}{Colors.BLINK}🚨 HIGH RISK - GLOBAL SCAM / SOCIAL ENGINEERING ATTACK{Colors.END}"
        threat_level = "HIGH"
    elif score >= 70:
        verdict = f"{Colors.RED}⚠️ ELEVATED RISK - LIKELY MALICIOUS INTENT{Colors.END}"
        threat_level = "ELEVATED"
    elif score >= 50:
        verdict = f"{Colors.YELLOW}⚠️ MEDIUM RISK - SUSPICIOUS ACTIVITY{Colors.END}"
        threat_level = "MEDIUM"
    elif score >= 25:
        verdict = f"{Colors.WARNING}⚡ LOW-MEDIUM RISK - PROCEED WITH CAUTION{Colors.END}"
        threat_level = "LOW-MEDIUM"
    else:
        verdict = f"{Colors.HACKER_GREEN}✅ LOW RISK - NO STRONG MALICIOUS INDICATORS{Colors.END}"
        threat_level = "LOW"
    
    return {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "verdict": verdict,
        "threat_level": threat_level,
        "risk_score": score,
        "confidence": confidence,
        "attack_types": attack_types,
        "region_detected": sorted(regions),
        "language_style": sorted(languages),
        "categories": sorted(categories),
        "reasons": reasons,
        "entities": entities,
        "message_length": len(message)
    }

def generate_recommendations(report: Dict) -> List[str]:
    """Generate security recommendations based on analysis"""
    recommendations = []
    
    if report["risk_score"] >= 100:
        recommendations.extend([
            "🛑 DO NOT CLICK ANY LINKS OR RESPOND TO THIS MESSAGE",
            "🚫 DO NOT PROVIDE ANY PERSONAL OR FINANCIAL INFORMATION",
            "📞 CONTACT THE ALLEGED ORGANIZATION DIRECTLY USING OFFICIAL CHANNELS",
            "⚠️ REPORT THIS MESSAGE TO RELEVANT AUTHORITIES",
            "🗑️ DELETE THIS MESSAGE IMMEDIATELY"
        ])
    elif report["risk_score"] >= 50:
        recommendations.extend([
            "⚠️ VERIFY THE SENDER'S IDENTITY BEFORE TAKING ACTION",
            "🔍 INDEPENDENTLY CONFIRM ANY CLAIMS MADE IN THE MESSAGE",
            "🚫 DO NOT SHARE SENSITIVE INFORMATION",
            "📧 REPORT AS SPAM/PHISHING IF APPLICABLE"
        ])
    else:
        recommendations.extend([
            "✓ REMAIN VIGILANT AND VERIFY UNEXPECTED REQUESTS",
            "🔒 ENSURE SECURE CONNECTIONS (HTTPS) WHEN VISITING WEBSITES",
            "💡 TRUST YOUR INSTINCTS - IF SOMETHING FEELS OFF, IT PROBABLY IS"
        ])
    
    return recommendations

# ======================================================
# STATISTICS TRACKER
# ======================================================
class StatisticsTracker:
    def __init__(self):
        self.total_analyzed = 0
        self.threat_distribution = {"CRITICAL": 0, "HIGH": 0, "ELEVATED": 0, "MEDIUM": 0, "LOW-MEDIUM": 0, "LOW": 0}
        self.total_score = 0
    
    def update(self, report: Dict):
        self.total_analyzed += 1
        self.threat_distribution[report["threat_level"]] += 1
        self.total_score += report["risk_score"]
    
    def display(self):
        print(f"\n{Colors.CYBER_BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.SYSTEM_CYAN}📊 SESSION STATISTICS{Colors.END}")
        print(f"{Colors.CYBER_BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.DATA}Total Messages Analyzed:{Colors.END} {self.total_analyzed}")
        if self.total_analyzed > 0:
            print(f"{Colors.DATA}Average Risk Score:{Colors.END} {self.total_score / self.total_analyzed:.2f}")
            print(f"\n{Colors.TERMINAL_GREEN}Threat Level Distribution:{Colors.END}")
            for level, count in self.threat_distribution.items():
                if count > 0:
                    percentage = (count / self.total_analyzed) * 100
                    print(f"  {Colors.GRAY}•{Colors.END} {level}: {count} ({percentage:.1f}%)")

# ======================================================
# [ CLI ]
# ======================================================
stats = StatisticsTracker()

print(f"\n{Colors.SYSTEM_CYAN}{'='*60}{Colors.END}")
print(f" {Colors.MATRIX_GREEN}🌍 ⟨ ENHANCED CHEAT DETECTOR V3 ⟩ {Colors.END}")
print(f" {Colors.TERMINAL_GREEN}👤 AUTHOR >{Colors.END} {AUTHOR}")
print(f"{Colors.SYSTEM_CYAN}{'='*60}{Colors.END}")
print(f"{Colors.GRAY}📌 WRITE MESSAGE THEN PRESS ENTER ON EMPTY LINE TO ANALYZE ! {Colors.END}")
print(f"{Colors.RED}🌐 « MINIMUM 10 CHARACTERS REQUIRED TO ANALYZE »{Colors.END}\n")
print(f"{Colors.GRAY}📡 « ENGINE IS WORKING »{Colors.END}\n")
last_message = None

while True:
    lines = []
    line_count = 0
    
    print(f"{Colors.TERMINAL_GREEN}⌁ ANALYSE >{Colors.END}", flush=True)

    # Collect multi-line input
    while True:
        try:
            if line_count > 0:
                print(f"{Colors.GRAY}... {Colors.END}", end="", flush=True)
            line = input()
            line_count += 1
        except (EOFError, KeyboardInterrupt):
            print(f"\n{Colors.CRITICAL}🛑 SYSTEM SHUTDOWN. STAY SAFE!{Colors.END}\n")
            exit(0)

        # Empty line = deliberate submit
        if line.strip() == "":
            break

        lines.append(line)

    user_msg = "\n".join(lines).strip()

    # Ignore empty / partial / glitch input
    if not user_msg:
        continue
    
    if len(user_msg) < 10:
        print(f"{Colors.YELLOW}⚠️ TOO SHORT [ MIN 10 CHARACTER ] TRY AGAIN ! {Colors.END}\n")
        continue

    # Check for commands
    if user_msg.lower() == "exit":
        stats.display()
        print(f"\n{Colors.CRITICAL}🛑 SYSTEM SHUTDOWN. STAY SAFE!{Colors.END}\n")
        break
    
    if user_msg.lower() == "stats":
        stats.display()
        print()
        continue

    # Absolute duplicate guard
    if user_msg == last_message:
        print(f"{Colors.YELLOW}⚠️ DUPLICATE DETECTED SKIPPED.{Colors.END}\n")
        continue

    last_message = user_msg

    # Run analysis ONCE
    try:
        report = analyze_message(user_msg)
        stats.update(report)

        print(f"\n{Colors.CYBER_BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.SYSTEM_CYAN}🔬 INTELLIGENCE REPORT{Colors.END}")
        print(f"{Colors.CYBER_BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.DATA}📅 TIMESTAMP   :{Colors.END} {report['date']}")
        print(f"{Colors.DATA}🧠 VERDICT     :{Colors.END} {report['verdict']}")
        print(f"{Colors.DATA}📈 RISK SCORE  :{Colors.END} {Colors.BOLD}{report['risk_score']}{Colors.END}")

        if report["categories"]:
            print(f"\n{Colors.TERMINAL_GREEN}🔎 DETECTED RISK CATEGORIES:{Colors.END}")
            for c in report["categories"]:
                print(f" {Colors.GRAY}⌲{Colors.END} {c}")

        if report["entities"]["domains"] or report["entities"]["emails"] or report["entities"]["phones"]:
            print(f"\n{Colors.WARNING}🔍 EXTRACTED ENTITIES:{Colors.END}")
            if report["entities"]["domains"]:
                print(f" {Colors.GRAY}🌐 URLs:{Colors.END} {', '.join(report['entities']['domains'][:3])}")
            if report["entities"]["emails"]:
                print(f" {Colors.GRAY}📧 Emails:{Colors.END} {', '.join(report['entities']['emails'])}")
            if report["entities"]["phones"]:
                print(f" {Colors.GRAY}📞 Phones:{Colors.END} {', '.join(report['entities']['phones'])}")
            if report["entities"]["bitcoin_addresses"]:
                print(f" {Colors.GRAY}₿ Bitcoin:{Colors.END} {', '.join(report['entities']['bitcoin_addresses'])}")
            if report["entities"]["ethereum_addresses"]:
                print(f" {Colors.GRAY}Ξ Ethereum:{Colors.END} {', '.join(report['entities']['ethereum_addresses'])}")

        if report["reasons"]:
            print(f"\n{Colors.WARNING}❗ WHY THIS MESSAGE IS RISKY:{Colors.END}")
            for r in report["reasons"]:
                print(f" {Colors.GRAY}•{Colors.END} {r}")

        recommendations = generate_recommendations(report)
        print(f"\n{Colors.HACKER_GREEN}💡 SECURITY RECOMMENDATIONS:{Colors.END}")
        for rec in recommendations:
            print(f" {Colors.GRAY}➤{Colors.END} {rec}")

        print(f"\n{Colors.GRAY}{'─'*60}{Colors.END}")
        print(f"{Colors.TERMINAL_GREEN}👤 AUTHOR:{Colors.END} {AUTHOR}")
        print(f"{Colors.GRAY}{'─'*60}{Colors.END}\n")
        
    except Exception as e:
        print(f"{Colors.RED}❌ ERROR: {str(e)}{Colors.END}\n")
        continue