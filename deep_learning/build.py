#!/usr/bin/env python3
"""공통 교육용 GitHub Pages HTML 생성기 — 구성: course.json + content/*.md.

실행: python -m pip install mistune && python build.py
생성: dist/index.html, dist/chXX_*_vNN.html (이미지·스타일·스크립트 내장)
"""
import base64
import html
import json
import re
from pathlib import Path
import mistune

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'dist'
CONFIG = json.loads((ROOT/'course.json').read_text(encoding='utf-8'))
CSS = (ROOT/'assets/site.css').read_text(encoding='utf-8')
SCRIPT = (ROOT/'assets/site.js').read_text(encoding='utf-8')
IMAGE = base64.b64encode((ROOT/'assets/hero-bookshelf.jpg').read_bytes()).decode('ascii')
CSS = re.sub(r"url\((['\"])hero-bookshelf\.jpg\1\)", f"url('data:image/jpeg;base64,{IMAGE}')", CSS)
MARKDOWN = mistune.create_markdown(escape=True, plugins=['table'])


def escape(s):
    return html.escape(str(s), quote=True)


def course_chapters():
    chapters=[]
    for raw in CONFIG['chapters']:
        ch=dict(raw)
        ch['file']=f"{ch['slug']}_{ch['version']}.html"
        chapters.append(ch)
    return chapters


CHAPTERS=course_chapters()

def page(title, kicker, desc, chips, body, chapter_id='', footer=''):
    manifest={'title':CONFIG['site_title'], 'short_title':CONFIG.get('course_code',''), 'home_label':'전체 학습 안내서', 'chapters':[
        {'id':x['id'],'number':x['number'],'title':x['title'],'file':x['file']} for x in CHAPTERS]}
    chips_html=''.join(f'<span class="chip">{escape(c)}</span>' for c in chips)
    course_data=json.dumps(manifest,ensure_ascii=False).replace('<','\\u003c')
    return f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{escape(desc)}"><title>{escape(title)} · {escape(CONFIG['site_title'])}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body data-chapter="{escape(chapter_id)}">
<button type="button" class="mobile-menu" id="mobile-menu" aria-controls="course-nav" aria-expanded="false">☰ 장·목차</button><div class="shade" id="shade"></div>
<header class="hero"><div class="hero-inner"><p class="kicker">{escape(kicker)}</p><h1>{escape(title)}</h1><p>{escape(desc)}</p><div class="chips">{chips_html}</div></div></header>
<div class="wrap"><nav class="toc" id="course-nav" aria-label="장과 절 탐색"></nav><main class="content" id="main-content">{body}<div class="chapter-links" id="chapter-links"></div></main></div>
<footer class="footer">{escape(CONFIG['site_title'])} · {escape(CONFIG['version'])} {escape(footer)} · 실습 결과는 실제 환경에서 검증</footer>
<script>window.COURSE={course_data};</script><script>{SCRIPT}</script></body></html>'''


# (추가) 수식: 원고의 ```math 블록과 `$...$` 인라인 수식을 MathML로 바꿔 브라우저가 수식으로 그리게 한다.
# 변환은 빌드할 때 한 번만 하므로 페이지에 JavaScript·외부 수식 라이브러리가 필요 없다.
# 변환에 실패한 수식은 원문 LaTeX를 코드 표기로 남기고, 실패 개수를 빌드 로그에 출력한다.
MATH_FAIL = []


def latex_to_mathml(tex, display):
    from latex2mathml.converter import convert
    tex = html.unescape(tex).strip()
    try:
        return convert(tex, display='block' if display else 'inline')
    except Exception:
        MATH_FAIL.append(tex)
        return None


def render_math(content):
    def block(m):
        mathml = latex_to_mathml(m.group(1), True)
        if mathml is None:
            return m.group(0)
        return f'<div class="math-block" role="math" aria-label="{escape(html.unescape(m.group(1)).strip())}">{mathml}</div>'

    def inline(m):
        mathml = latex_to_mathml(m.group(1), False)
        return m.group(0) if mathml is None else mathml

    content = re.sub(r'<pre><code class="language-math">(.*?)</code></pre>', block, content, flags=re.S)
    return re.sub(r'<code>\$([^<]+?)\$</code>', inline, content)


# (추가) 코드 박스 제목 줄에 파일명·언어·검증 상태를 넣고(공통 코드 규칙 10절),
# 실행 결과는 코드와 구분되는 출력 상자로, ```flow 블록은 단계 흐름도(.flow)로 바꾼다.
def enhance_blocks(content):
    content = render_math(content)
    # (추가) 한글 조사 앞에서 닫히지 않는 굵은 글씨 표시(⟪b⟫)를 <strong>으로 바꾼다
    content = content.replace('⟪b⟫', '<strong>').replace('⟪/b⟫', '</strong>')
    code_re = r'<p>코드 박스: (.*?)</p>\s*<pre><code(?: class="language-([^\"]+)")?>(.*?)</code></pre>'
    content = re.sub(code_re,
        lambda m: '<div class="codeblock"><div class="codebar"><span>' + (m.group(2) or 'text').upper()
            + ' · ' + m.group(1) + '</span></div><pre class="src"><code>' + m.group(3) + '</code></pre></div>',
        content, flags=re.S)
    out_re = r'<p>실행 결과: (.*?)</p>\s*<pre><code(?: class="language-[^\"]+")?>(.*?)</code></pre>'
    content = re.sub(out_re,
        lambda m: '<div class="outputblock"><div class="codebar"><span>OUTPUT · ' + m.group(1)
            + '</span></div><pre>' + m.group(2) + '</pre></div>',
        content, flags=re.S)

    def flow(m):
        steps = [s.strip() for s in m.group(1).strip().split('\n') if s.strip()]
        steps = [re.sub(r'`([^`]+)`', r'<code>\1</code>', s) for s in steps]
        body = '<div class="down" aria-hidden="true">↓</div>'.join(f'<div class="step">{s}</div>' for s in steps)
        return f'<div class="flow" role="list" aria-label="개념 흐름도">{body}</div>'

    return re.sub(r'<pre><code class="language-flow">(.*?)</code></pre>', flow, content, flags=re.S)


# (추가) 과정 INDEX: 기준 디자인(ai-agent-engineering) 첫 화면처럼
# 과정 개요·숫자 요약 → 전체 학습 테크트리 → 학습·실습·배포 안내 → 장별 카드(산출물·세부 목차) → 학습·검증 원칙
def build_index(default_content):
    if 'goal' not in CONFIG:
        return default_content, ['단계별 학습', '실습 중심', 'GitHub Pages']
    by_no = {ch['number']: ch for ch in CHAPTERS}
    toc = {}
    for ch in CHAPTERS:
        md = (ROOT / ch['source']).read_text(encoding='utf-8')
        toc[ch['id']] = re.findall(r'^##\s+(.+?)\s*$', md, flags=re.M)
    n_ch = len(CHAPTERS)
    n_nb = sum(ch.get('notebooks', 0) for ch in CHAPTERS)
    n_sec = sum(len(v) for v in toc.values())
    other = CONFIG.get('other_course')

    stats = ''.join(f'<div class="stat"><b>{v}</b><span>{escape(k)}</span></div>'
                    for v, k in [(n_ch, '전체 학습 장'), (n_nb, '실습 노트북'), (n_sec, '세부 절 합계')])
    intro = (f'<p>{escape(CONFIG["site_description"])}</p><div class="stats">{stats}</div>'
             f'<h3>전체 학습의 최종 목적</h3>{MARKDOWN(CONFIG["goal"])}')

    lanes = []
    for i, lane in enumerate(CONFIG['lanes']):
        items = ' → '.join(f'<a href="{escape(by_no[n]["file"])}">{n:02d} {escape(by_no[n]["title"])}</a>' for n in lane['chapters'])
        if i:
            lanes.append('<div class="down" aria-hidden="true">↓</div>')
        lanes.append(f'<div class="step lane"><span class="lane-label">{escape(lane["label"])}</span>'
                     f'<span class="lane-items">{items}</span><small>{escape(lane["caption"])}</small></div>')
    roadmap = ('<p>다음 구성도는 학습 진행의 중심 경로입니다. 각 장은 앞 장의 개념과 코드를 이어서 사용합니다.</p>'
               '<div class="flow" role="list" aria-label="전체 학습 테크트리">' + ''.join(lanes) + '</div>')

    rows = [('기본 환경', 'Python 3 + PyTorch + Jupyter Notebook(또는 Google Colab)'),
            ('실습 순서', '배경 개념 → 개념 흐름도 → 코드 → 실행 결과 → 풀이 → 검증'),
            ('노트북 위치', '과정 폴더의 <code>notebooks/</code>를 작업 폴더로 열고 장 안 순번(<code>chNN_K</code>)대로 실행'),
            ('실행 결과', '페이지의 결과·그림은 원본 노트북에 저장된 기록이며, 다시 실행하지 않은 항목은 미검증으로 표시'),
            ('공개 자료', '로컬 경로·계정 정보를 점검해 가린 뒤 GitHub Pages로 배포')]
    if other:
        rows.append((other['role'], f'<a href="{escape(other["href"])}">{escape(other["title"])}</a>'))
    table = ('<div class="table-wrap"><table><thead><tr><th>구분</th><th>진행 기준</th></tr></thead><tbody>'
             + ''.join(f'<tr><td>{escape(a)}</td><td>{b}</td></tr>' for a, b in rows) + '</tbody></table></div>')

    cards = []
    for ch in CHAPTERS:
        secs = toc[ch['id']]
        items = ''.join(f'<li><span class="n">{i:02d}</span>{escape(t)}</li>' for i, t in enumerate(secs))
        tags = ' · '.join(escape(t) for t in ch.get('tags', []))
        cards.append(
            f'<article class="course-card"><div class="card-top"><span class="card-no">{ch["number"]:02d}</span>'
            f'<span class="card-meta">CHAPTER {ch["number"]:02d} · {escape(ch.get("level", ""))}</span></div>'
            f'<h3>{escape(ch["title"])}</h3><p>{escape(ch["subtitle"])}</p><p class="tools">{tags}</p>'
            f'<p class="outcome"><b>실습 산출물</b> {escape(ch.get("outcome", ""))}</p>'
            f'<details><summary>세부 목차 펼쳐보기 · 00–{len(secs) - 1:02d}절 · {len(secs)}개 절 · 노트북 {ch.get("notebooks", 0)}개</summary>'
            f'<ol class="subtoc">{items}</ol></details>'
            f'<a class="start" href="{escape(ch["file"])}">제{ch["number"]:02d}장 학습 시작 ↗</a></article>')
    chapters = ('<p>각 장의 학습 목적, 주요 도구, 실습 산출물을 비교할 수 있습니다. 세부 목차는 실제 장 원고(<code>content/chNN.md</code>)의 절 제목과 순서를 그대로 반영합니다.</p>'
                '<div class="card-grid">' + ''.join(cards) + '</div>')

    principle = ('<p>배경 개념 → 개념 흐름도 → 단계별 코드 → 실행 결과 → 풀이 → 검증 순서로 진행합니다. 원본 노트북의 실행 기록과 이번 정리에서 확인한 결과를 구분하고, '
                 '확인하지 않은 항목은 <b>미검증</b>으로 표시합니다. 판정은 통과·실패·미검증·해당 없음으로 나눕니다.</p>')

    sections = [('intro', '과정 개요', intro), ('roadmap', '전체 학습 테크트리', roadmap),
                ('guide', '학습·실습·배포 안내', table), ('chapters', '장별 학습 목차와 산출물', chapters),
                ('practice', '학습·검증 원칙', principle)]
    content = ''.join(f'<section class="section" id="{sid}"><h2><span class="num">{i:02d}</span>{escape(t)}</h2>{body}</section>'
                      for i, (sid, t, body) in enumerate(sections))
    chips = [f'총 {n_ch}장', f'노트북 {n_nb}개', f'세부 절 {n_sec}개', 'PyTorch · Jupyter']
    return content, chips


def render_markdown_sections(md):
    parts=re.split(r'^##\s+(.+?)\s*$',md,flags=re.M)
    if parts[0].strip():
        raise ValueError('장 본문은 ## 절 제목으로 시작해야 합니다.')
    sections=[]
    for n in range(1,len(parts),2):
        title=parts[n].strip()
        content=MARKDOWN(parts[n+1].strip())
        # (추가) 코드 박스 제목 줄·실행 결과 상자·개념 흐름도 처리
        content=enhance_blocks(content)
        # fenced code needs a consistent header and copy button container
        content=re.sub(r'<pre><code(?: class="language-([^\"]+)")?>(.*?)</code></pre>',
            lambda m:'<div class="codeblock"><div class="codebar"><span>'+escape(m.group(1) or 'TEXT')+'</span></div><pre><code>'+m.group(2)+'</code></pre></div>',content,flags=re.S)
        sections.append(f'<section class="section" id="s{n//2:02d}"><h2><span class="num">{n//2:02d}</span>{escape(title)}</h2>{content}</section>')
    return ''.join(sections),len(sections)


def build():
    OUT.mkdir(exist_ok=True)
    expected={'index.html'}
    cards=[]
    for ch in CHAPTERS:
        source=(ROOT/ch['source']).resolve()
        if ROOT not in source.parents or not source.is_file():
            raise ValueError('잘못된 본문 파일 경로: '+ch['source'])
        body,n=render_markdown_sections(source.read_text(encoding='utf-8'))
        if not n: raise ValueError('본문 절이 없습니다: '+ch['source'])
        html_page=page(f"제{ch['number']:02d}장 · {ch['title']}",f"{CONFIG['course_code']} · CHAPTER {ch['number']:02d}",ch['subtitle'],ch.get('tags',[]),body,ch['id'])
        (OUT/ch['file']).write_text(html_page,encoding='utf-8')
        expected.add(ch['file'])
        cards.append(f'<a class="chapter-card" href="{escape(ch["file"])}"><span>CHAPTER {ch["number"]:02d}</span><b>{escape(ch["title"])}</b><span>{escape(ch["subtitle"])}</span></a>')
    roadmap='<div class="flow">'+''.join(('<div class="down">↓</div>' if i else '')+f'<div class="step"><strong>{ch["number"]:02d} · {escape(ch["title"])}</strong> — {escape(ch["subtitle"])}</div>' for i,ch in enumerate(CHAPTERS))+'</div>'
    content=f'''<section class="section" id="intro"><h2><span class="num">00</span>과정 개요</h2><p>{escape(CONFIG['site_description'])}</p></section>
<section class="section" id="roadmap"><h2><span class="num">01</span>전체 학습 테크트리</h2>{roadmap}</section>
<section class="section" id="chapters"><h2><span class="num">02</span>장별 목차</h2><div class="chapter-grid">{''.join(cards)}</div></section>
<section class="section" id="practice"><h2><span class="num">03</span>학습·검증 원칙</h2><p>개념 → 구조도 → 단계별 코드 → 예상 출력 → 검증 → 완료 기준 순서로 진행합니다. 실제 실행 결과와 교육용 예시는 명확히 구분합니다.</p><p>코드와 설정은 공식 문서를 우선하며, 외부 시스템을 수정하는 작업에는 사용자 승인 및 원본 보호를 적용합니다.</p></section>'''
    # (추가) 과정 INDEX 구성 (build_index)
    content, index_chips = build_index(content)
    (OUT/'index.html').write_text(page(CONFIG['site_title'],CONFIG['course_code'],CONFIG['site_description'],index_chips,content),encoding='utf-8')
    # 최신 버전만 남기기: 출력 디렉터리에 있는 이전 장 HTML 제거, 소스/타 저장소에는 영향 없음
    for p in OUT.glob('*.html'):
        if p.name not in expected: p.unlink()
    print('생성 완료:',len(expected),'개 HTML 파일')
    # (추가) 수식 변환 실패 보고
    print('수식 변환 실패:', len(MATH_FAIL), '개', *MATH_FAIL[:10], sep='\n  ' if MATH_FAIL else ' ')
    for name in sorted(expected):print(' ',OUT/name)

if __name__=='__main__':build()
