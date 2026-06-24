"""

NEXUS AI – Serverless Intelligent Platform

Powered by OpenRouter via AWS Lambda

"""



import json

import os

import urllib.request

import urllib.error



OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")

# تم التعديل هنا: استخدام نموذج متاح من قائمتك وهو gemma-3-4b-it

MODEL_NAME = os.environ.get("MODEL_NAME", "gemma-3-4b-it")

ALLOWED_ORIGIN = os.environ.get("ALLOWED_ORIGIN", "*")

OPENROUTER_URL = "https://genai.ghaymah.systems/v1/chat/completions"





def call_openrouter(user_text: str) -> str:

    payload = {

        "model": MODEL_NAME,

        "messages": [

            {

                "role": "system",

                "content": (

                    "أنت NEXUS، مساعد ذكاء اصطناعي متقدم ومتخصص. "

                    "أجب بشكل واضح ومفصل ومنظم. "

                    "إذا كان السؤال بالعربية، أجب بالعربية. إذا كان بالإنجليزية، أجب بالإنجليزية. "

                    "استخدم التنسيق المناسب لجعل إجابتك سهلة القراءة."

                )

            },

            {

                "role": "user",

                "content": user_text

            }

        ],

        "max_tokens": 2048,

        "temperature": 0.7

    }



    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(

        OPENROUTER_URL, data=data,

        headers={

            "Content-Type": "application/json",

            "Authorization": f"Bearer {OPENROUTER_API_KEY}",

            "HTTP-Referer": "https://nexus-ai.app",

            "X-Title": "NEXUS AI"

        },

        method="POST"

    )

    with urllib.request.urlopen(req, timeout=30) as resp:

        result = json.loads(resp.read())

        return result["choices"][0]["message"]["content"]





def build_html(ai_response: str = "", error_msg: str = "") -> str:

    response_block = ""

    if error_msg:

        response_block = f'<div id="resultArea"><div class="result-panel error-panel"><div class="panel-header"><div class="panel-dot"></div><div class="panel-tag">ERROR</div></div><p class="result-text">{error_msg}</p></div></div>'

    elif ai_response:

        safe = ai_response.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

        response_block = f'<div id="resultArea"><div class="result-panel"><div class="panel-header"><div class="panel-dot"></div><div class="panel-tag">✦ QUEEN RESPONSE</div></div><p class="result-text">{safe}</p></div></div>'

    else:

        response_block = '<div id="resultArea"></div>'



    return """<!DOCTYPE html>

<html lang="ar" dir="rtl">

<head>

<meta charset="UTF-8"/>

<meta name="viewport" content="width=device-width,initial-scale=1.0"/>

<title>NEXUS — Queen of the Cloud</title>

<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;600&display=swap');

*{box-sizing:border-box;margin:0;padding:0}

body{font-family:'Inter',sans-serif;background:#050510;min-height:100vh;color:#fff;overflow-x:hidden;padding:0}

.bg{position:fixed;inset:0;background:radial-gradient(ellipse 70% 50% at 15% 0%,rgba(180,100,255,0.18) 0%,transparent 60%),radial-gradient(ellipse 50% 40% at 85% 100%,rgba(255,100,180,0.15) 0%,transparent 60%),radial-gradient(ellipse 60% 60% at 50% 50%,rgba(80,150,255,0.06) 0%,transparent 70%);z-index:0;pointer-events:none}

.stars{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}

.star{position:absolute;background:#fff;border-radius:50%;animation:twinkle var(--d,3s) ease-in-out infinite var(--delay,0s)}

@keyframes twinkle{0%,100%{opacity:0.1;transform:scale(0.8)}50%{opacity:1;transform:scale(1.2)}}

.grid-bg{position:fixed;inset:0;z-index:0;pointer-events:none;background-image:linear-gradient(rgba(150,100,255,0.04) 1px,transparent 1px),linear-gradient(90deg,rgba(150,100,255,0.04) 1px,transparent 1px);background-size:50px 50px}

.page{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;padding:40px 20px 80px;max-width:740px;margin:0 auto}

.topbar{width:100%;display:flex;align-items:center;justify-content:space-between;margin-bottom:50px}

.logo{display:flex;align-items:center;gap:10px}

.logo-gem{width:38px;height:38px;background:linear-gradient(135deg,#a855f7,#ec4899);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:18px;box-shadow:0 0 20px rgba(168,85,247,0.6),0 0 40px rgba(168,85,247,0.2);animation:gemPulse 3s ease-in-out infinite}

@keyframes gemPulse{0%,100%{box-shadow:0 0 20px rgba(168,85,247,0.6),0 0 40px rgba(168,85,247,0.2)}50%{box-shadow:0 0 30px rgba(168,85,247,0.9),0 0 60px rgba(236,72,153,0.4),0 0 80px rgba(168,85,247,0.1)}}

.logo-name{font-family:'JetBrains Mono',monospace;font-size:1rem;font-weight:600;letter-spacing:4px;color:#fff}

.live-pill{display:flex;align-items:center;gap:7px;background:rgba(52,211,153,0.08);border:1px solid rgba(52,211,153,0.25);padding:5px 14px;border-radius:100px;font-family:'JetBrains Mono',monospace;font-size:0.7rem;font-weight:600;color:#34d399;letter-spacing:1.5px}

.live-dot{width:7px;height:7px;background:#34d399;border-radius:50%;box-shadow:0 0 8px #34d399;animation:blink 2s ease-in-out infinite}

@keyframes blink{0%,100%{opacity:1}50%{opacity:0.3}}

.hero{text-align:center;margin-bottom:52px;width:100%;position:relative}

.crown-wrap{display:inline-block;margin-bottom:16px;animation:crownFloat 4s ease-in-out infinite;position:relative}

@keyframes crownFloat{0%,100%{transform:translateY(0) rotate(-2deg)}50%{transform:translateY(-12px) rotate(2deg)}}

.crown-svg{width:80px;height:80px}

.sparkles{position:absolute;inset:-20px;pointer-events:none}

.sp{position:absolute;width:6px;height:6px;background:#f59e0b;border-radius:50%;animation:sparkle var(--sd,2s) ease-in-out infinite var(--ss,0s);box-shadow:0 0 6px #f59e0b,0 0 12px #f59e0b}

@keyframes sparkle{0%,100%{opacity:0;transform:scale(0)}50%{opacity:1;transform:scale(1)}}

.hero-tag{font-family:'JetBrains Mono',monospace;font-size:0.68rem;letter-spacing:5px;color:#a855f7;font-weight:600;margin-bottom:18px;opacity:0.9}

.hero-title{font-size:clamp(2.4rem,7vw,4rem);font-weight:900;line-height:1.05;letter-spacing:-2.5px;margin-bottom:8px;background:linear-gradient(135deg,#fff 20%,#e879f9 60%,#818cf8 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}

.hero-title-line2{font-size:clamp(2.4rem,7vw,4rem);font-weight:900;line-height:1.05;letter-spacing:-2.5px;margin-bottom:22px;background:linear-gradient(135deg,#f59e0b 0%,#ec4899 50%,#a855f7 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:shimmer 4s linear infinite;background-size:200% auto}

@keyframes shimmer{0%{background-position:0% center}100%{background-position:200% center}}

.hero-sub{font-size:1rem;color:rgba(255,255,255,0.45);line-height:1.7;max-width:460px;margin:0 auto}

.gems-row{display:flex;gap:8px;justify-content:center;margin-top:24px;flex-wrap:wrap}

.gem-chip{display:flex;align-items:center;gap:6px;padding:5px 14px;border-radius:100px;font-size:0.7rem;font-weight:600;letter-spacing:0.5px;border:1px solid;font-family:'JetBrains Mono',monospace}

.gem-chip.purple{background:rgba(168,85,247,0.1);border-color:rgba(168,85,247,0.3);color:#c084fc}

.gem-chip.pink{background:rgba(236,72,153,0.1);border-color:rgba(236,72,153,0.3);color:#f472b6}

.gem-chip.blue{background:rgba(99,102,241,0.1);border-color:rgba(99,102,241,0.3);color:#818cf8}

.gem-chip.amber{background:rgba(245,158,11,0.1);border-color:rgba(245,158,11,0.3);color:#fbbf24}

.divider{width:100%;height:1px;margin:0 0 36px;background:linear-gradient(90deg,transparent,rgba(168,85,247,0.5),rgba(236,72,153,0.5),transparent);position:relative}

.divider::before{content:'✦';position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font-size:12px;color:#a855f7;background:#050510;padding:0 8px;animation:rotateStar 8s linear infinite}

@keyframes rotateStar{0%{transform:translate(-50%,-50%) rotate(0deg)}100%{transform:translate(-50%,-50%) rotate(360deg)}}

.input-card{width:100%;background:rgba(15,10,35,0.7);border:1px solid rgba(168,85,247,0.2);border-radius:20px;padding:28px;position:relative;backdrop-filter:blur(20px);transition:border-color 0.4s,box-shadow 0.4s}

.input-card:focus-within{border-color:rgba(168,85,247,0.5);box-shadow:0 0 60px rgba(168,85,247,0.1),0 0 120px rgba(236,72,153,0.05),inset 0 0 40px rgba(168,85,247,0.02)}

.corner{position:absolute;width:16px;height:16px;border-color:rgba(168,85,247,0.6);border-style:solid}

.corner.tl{top:12px;left:12px;border-width:2px 0 0 2px;border-radius:4px 0 0 0}

.corner.tr{top:12px;right:12px;border-width:2px 2px 0 0;border-radius:0 4px 0 0}

.corner.bl{bottom:12px;left:12px;border-width:0 0 2px 2px;border-radius:0 0 0 4px}

.corner.br{bottom:12px;right:12px;border-width:0 2px 2px 0;border-radius:0 0 4px 0}

.input-label{font-family:'JetBrains Mono',monospace;font-size:0.68rem;font-weight:600;letter-spacing:2.5px;color:rgba(168,85,247,0.7);margin-bottom:14px;display:block}

textarea{width:100%;min-height:110px;background:rgba(0,0,0,0.3);border:1px solid rgba(255,255,255,0.06);border-radius:12px;color:#e2e8f0;font-size:0.97rem;font-family:'Inter',sans-serif;padding:16px;resize:vertical;direction:rtl;line-height:1.75;transition:border-color 0.2s,box-shadow 0.2s}

textarea::placeholder{color:rgba(255,255,255,0.2)}

textarea:focus{outline:none;border-color:rgba(168,85,247,0.4);box-shadow:0 0 0 3px rgba(168,85,247,0.08)}

.input-footer{display:flex;justify-content:space-between;align-items:center;margin:10px 0 18px}

#char-count{font-family:'JetBrains Mono',monospace;font-size:0.68rem;color:rgba(255,255,255,0.25)}

.hint{font-size:0.7rem;color:rgba(255,255,255,0.2);font-family:'JetBrains Mono',monospace}

kbd{background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.12);border-radius:4px;padding:1px 6px;font-family:'JetBrains Mono',monospace;font-size:0.65rem}

.btn{width:100%;display:flex;align-items:center;justify-content:center;gap:10px;background:linear-gradient(135deg,#7c3aed 0%,#a855f7 40%,#ec4899 100%);border:none;color:#fff;font-size:0.95rem;font-weight:700;font-family:'Inter',sans-serif;letter-spacing:0.5px;padding:16px 24px;border-radius:12px;cursor:pointer;position:relative;overflow:hidden;transition:transform 0.15s,box-shadow 0.15s;box-shadow:0 4px 30px rgba(168,85,247,0.4),0 0 60px rgba(236,72,153,0.1)}

.btn::before{content:'';position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.15),transparent);transition:left 0.6s}

.btn:hover::before{left:100%}

.btn:hover{transform:translateY(-2px);box-shadow:0 8px 40px rgba(168,85,247,0.6),0 0 80px rgba(236,72,153,0.2)}

.btn:active{transform:translateY(0)}

.btn:disabled{opacity:0.5;cursor:not-allowed;transform:none;box-shadow:none}

.spinner{width:16px;height:16px;border:2px solid rgba(255,255,255,0.3);border-top-color:#fff;border-radius:50%;animation:spin 0.7s linear infinite;display:none;flex-shrink:0}

@keyframes spin{to{transform:rotate(360deg)}}

.result-panel{width:100%;margin-top:20px;background:rgba(10,5,30,0.8);border:1px solid rgba(168,85,247,0.25);border-radius:16px;padding:24px;animation:panelIn 0.5s cubic-bezier(0.16,1,0.3,1);position:relative;overflow:hidden;backdrop-filter:blur(20px)}

.result-panel::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,#a855f7,#ec4899,#818cf8,transparent);animation:scanLine 3s linear infinite}

@keyframes scanLine{0%{opacity:0.4}50%{opacity:1}100%{opacity:0.4}}

.error-panel{border-color:rgba(248,113,113,0.3)}

.error-panel::before{background:linear-gradient(90deg,transparent,#f87171,transparent)}

@keyframes panelIn{from{opacity:0;transform:translateY(20px) scale(0.98)}to{opacity:1;transform:translateY(0) scale(1)}}

.panel-header{display:flex;align-items:center;gap:8px;margin-bottom:16px;padding-bottom:14px;border-bottom:1px solid rgba(168,85,247,0.12)}

.panel-dot{width:8px;height:8px;background:#a855f7;border-radius:50%;box-shadow:0 0 8px #a855f7;animation:blink 1.5s ease-in-out infinite}

.panel-tag{font-family:'JetBrains Mono',monospace;font-size:0.65rem;font-weight:600;letter-spacing:3px;color:#a855f7}

.error-panel .panel-dot{background:#f87171;box-shadow:0 0 8px #f87171}

.error-panel .panel-tag{color:#f87171}

.result-text{font-size:0.96rem;line-height:1.85;color:rgba(226,232,240,0.85);white-space:pre-wrap;word-break:break-word;direction:auto}

.footer{margin-top:44px;text-align:center}

.footer-gems{display:flex;gap:8px;justify-content:center;flex-wrap:wrap}

.fchip{background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.06);border-radius:100px;padding:4px 12px;font-size:0.65rem;color:rgba(255,255,255,0.25);font-family:'JetBrains Mono',monospace;letter-spacing:0.5px}

::-webkit-scrollbar{width:4px}

::-webkit-scrollbar-track{background:transparent}

::-webkit-scrollbar-thumb{background:rgba(168,85,247,0.4);border-radius:4px}

</style>

</head>

<body>

<div class="bg"></div>

<div class="grid-bg"></div>

<div class="stars" id="stars"></div>

<div class="page">

  <div class="topbar">

    <div class="logo">

      <div class="logo-gem">✦</div>

      <span class="logo-name">NEXUS</span>

    </div>

    <div class="live-pill"><span class="live-dot"></span>ONLINE</div>

  </div>

  <div class="hero">

    <div class="crown-wrap">

      <div class="sparkles">

        <div class="sp" style="top:10px;left:5px;--sd:2.1s;--ss:0s"></div>

        <div class="sp" style="top:0px;left:50%;--sd:1.8s;--ss:0.3s"></div>

        <div class="sp" style="top:15px;right:5px;--sd:2.4s;--ss:0.6s"></div>

        <div class="sp" style="bottom:10px;left:10px;--sd:2.0s;--ss:0.9s;background:#ec4899;box-shadow:0 0 6px #ec4899,0 0 12px #ec4899"></div>

        <div class="sp" style="bottom:5px;right:10px;--sd:1.9s;--ss:1.2s;background:#818cf8;box-shadow:0 0 6px #818cf8,0 0 12px #818cf8"></div>

      </div>

      <svg class="crown-svg" viewBox="0 0 80 80" fill="none" xmlns="http://www.w3.org/2000/svg">

        <defs>

          <linearGradient id="cg" x1="0" y1="0" x2="80" y2="80" gradientUnits="userSpaceOnUse">

            <stop offset="0%" stop-color="#f59e0b"/>

            <stop offset="40%" stop-color="#fbbf24"/>

            <stop offset="100%" stop-color="#f97316"/>

          </linearGradient>

          <filter id="glow"><feGaussianBlur stdDeviation="2" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>

        </defs>

        <path d="M10 55 L15 25 L30 40 L40 10 L50 40 L65 25 L70 55 Z" fill="url(#cg)" filter="url(#glow)" stroke="#fbbf24" stroke-width="1" stroke-linejoin="round"/>

        <rect x="9" y="55" width="62" height="10" rx="4" fill="url(#cg)" stroke="#fbbf24" stroke-width="0.5"/>

        <circle cx="40" cy="10" r="4" fill="#ec4899" filter="url(#glow)"/>

        <circle cx="15" cy="25" r="3" fill="#818cf8" filter="url(#glow)"/>

        <circle cx="65" cy="25" r="3" fill="#34d399" filter="url(#glow)"/>

        <circle cx="22" cy="57" r="3" fill="#f87171"/>

        <circle cx="40" cy="57" r="3" fill="#fbbf24"/>

        <circle cx="58" cy="57" r="3" fill="#a855f7"/>

      </svg>

    </div>

    <p class="hero-tag">✦ INTELLIGENT AI PLATFORM ✦</p>

    <div class="hero-title">Queen of the Cloud</div>

    <div class="hero-title-line2">منصتك الملكية</div>

    <p class="hero-sub">منصة ذكاء اصطناعي فاخرة — اسألي أي سؤال واحصلي على إجابة فورية ومذهلة</p>

    <div class="gems-row">

      <div class="gem-chip purple">💜 AWS Lambda</div>

      <div class="gem-chip pink">💗 OpenRouter AI</div>

      <div class="gem-chip blue">💙 Serverless</div>

      <div class="gem-chip amber">💛 Free Tier</div>

    </div>

  </div>

  <div class="divider"></div>

  <div class="input-card" id="inputCard">

    <div class="corner tl"></div><div class="corner tr"></div>

    <div class="corner bl"></div><div class="corner br"></div>

    <label class="input-label" for="userText">✦ اكتبي سؤالك أو نصك هنا</label>

    <textarea id="userText" maxlength="4000" placeholder="مثال: ما هي أفضل تقنيات الذكاء الاصطناعي لعام 2025؟"></textarea>

    <div class="input-footer">

      <span id="char-count">0 / 4000</span>

      <span class="hint"><kbd>Ctrl</kbd> + <kbd>↵</kbd></span>

    </div>

    <button class="btn" id="submitBtn" onclick="sendRequest()">

      <span id="btnText">✦ تشغيل الاستعلام الملكي</span>

      <span class="spinner" id="spinner"></span>

    </button>

    <div id="resultArea"></div>

  </div>

  <div class="footer">

    <div class="footer-gems">

      <span class="fchip">AWS Lambda</span>

      <span class="fchip">OpenRouter AI</span>

      <span class="fchip">Serverless</span>

      <span class="fchip">us-east-1</span>

      <span class="fchip">Free Tier</span>

    </div>

  </div>

</div>

<script>

const starsEl=document.getElementById('stars');

for(let i=0;i<80;i++){

  const s=document.createElement('div');

  s.className='star';

  const size=Math.random()*2.5+0.5;

  s.style.cssText='left:'+Math.random()*100+'%;top:'+Math.random()*100+'%;width:'+size+'px;height:'+size+'px;--d:'+(2+Math.random()*4)+'s;--delay:'+Math.random()*4+'s;opacity:'+Math.random()*0.5;

  starsEl.appendChild(s);

}

const textarea=document.getElementById('userText');

const counter=document.getElementById('char-count');

textarea.addEventListener('input',()=>{

  const n=textarea.value.length;

  counter.textContent=n+' / 4000';

  counter.style.color=n>3600?'#f87171':'';

});

async function sendRequest(){

  const text=textarea.value.trim();

  if(!text){showResult('يرجى كتابة سؤال أو نص أولاً ✦',true);return;}

  const btn=document.getElementById('submitBtn');

  const btnText=document.getElementById('btnText');

  const spinner=document.getElementById('spinner');

  btn.disabled=true;

  btnText.textContent='✦ جاري المعالجة...';

  spinner.style.display='block';

  document.getElementById('resultArea').innerHTML='';

  try{

    const res=await fetch(window.location.href,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text})});

    const data=await res.json();

    if(data.error)showResult(data.error,true);

    else showResult(data.response,false);

  }catch(err){

    showResult('خطأ في الاتصال — يرجى المحاولة مرة أخرى',true);

  }finally{

    btn.disabled=false;

    btnText.textContent='✦ تشغيل الاستعلام الملكي';

    spinner.style.display='none';

  }

}

function showResult(text,isError){

  const area=document.getElementById('resultArea');

  area.innerHTML='';

  const div=document.createElement('div');

  div.className='result-panel'+(isError?' error-panel':'');

  const header=document.createElement('div');

  header.className='panel-header';

  header.innerHTML='<div class="panel-dot"></div><div class="panel-tag">'+(isError?'ERROR':'✦ QUEEN RESPONSE')+'</div>';

  const p=document.createElement('p');

  p.className='result-text';

  div.appendChild(header);div.appendChild(p);

  area.appendChild(div);

  div.scrollIntoView({behavior:'smooth',block:'nearest'});

  if(!isError){

    let i=0;

    function type(){if(i<=text.length){p.textContent=text.slice(0,i);i++;setTimeout(type,6);}}

    type();

  }else{p.textContent=text;}

}

textarea.addEventListener('keydown',e=>{if((e.ctrlKey||e.metaKey)&&e.key==='Enter')sendRequest();});

</script>

</body>

</html>"""





def lambda_handler(event, context):

    method = event.get("requestContext", {}).get("http", {}).get("method", "GET").upper()

    cors_headers = {

        "Access-Control-Allow-Origin": ALLOWED_ORIGIN,

        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",

        "Access-Control-Allow-Headers": "Content-Type",

    }



    if method == "OPTIONS":

        return {"statusCode": 204, "headers": cors_headers, "body": ""}



    if method == "GET":

        return {

            "statusCode": 200,

            "headers": {**cors_headers, "Content-Type": "text/html; charset=utf-8", "Cache-Control": "no-store"},

            "body": build_html()

        }



    if method == "POST":

        json_headers = {**cors_headers, "Content-Type": "application/json; charset=utf-8"}

        try:

            body = json.loads(event.get("body") or "{}")

            user_text = (body.get("text") or "").strip()



            if not user_text:

                return {"statusCode": 400, "headers": json_headers,

                        "body": json.dumps({"error": "الحقل 'text' مطلوب ولا يجوز أن يكون فارغاً."}, ensure_ascii=False)}



            if len(user_text) > 4000:

                return {"statusCode": 400, "headers": json_headers,

                        "body": json.dumps({"error": "النص أطول من 4000 حرف. يرجى تقليصه."}, ensure_ascii=False)}



            ai_text = call_openrouter(user_text)

            return {"statusCode": 200, "headers": json_headers,

                    "body": json.dumps({"response": ai_text}, ensure_ascii=False)}



        except urllib.error.HTTPError as e:

            err_body = e.read().decode()

            try:

                err_json = json.loads(err_body)

                err_msg = err_json.get("error", {}).get("message", err_body)

            except Exception:

                err_msg = err_body

            return {"statusCode": 502, "headers": json_headers,

                    "body": json.dumps({"error": f"OpenRouter API Error: {err_msg}"}, ensure_ascii=False)}



        except urllib.error.URLError as e:

            return {"statusCode": 503, "headers": json_headers,

                    "body": json.dumps({"error": "تعذّر الاتصال بخدمة الذكاء الاصطناعي. حاول مرة أخرى."}, ensure_ascii=False)}



        except json.JSONDecodeError:

            return {"statusCode": 400, "headers": json_headers,

                    "body": json.dumps({"error": "صيغة JSON غير صحيحة في جسم الطلب."}, ensure_ascii=False)}



        except Exception as e:

            return {"statusCode": 500, "headers": json_headers,

                    "body": json.dumps({"error": f"خطأ داخلي: {str(e)}"}, ensure_ascii=False)}



    return {"statusCode": 405, "headers": cors_headers,

            "body": json.dumps({"error": "Method Not Allowed"})}
