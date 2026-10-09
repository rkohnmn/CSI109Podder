import os
import subprocess

# Paths
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT_DIR = os.path.join(REPO_ROOT, "docs", "screenshots")
SCRATCH_DIR = os.path.join(REPO_ROOT, "docs", "screenshots", ".build")
CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

chrome_bin = next((p for p in CHROME_PATHS if os.path.exists(p)), None)
if not chrome_bin:
    raise FileNotFoundError("Google Chrome or Microsoft Edge executable not found.")

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1200px;
    height: 675px;
    background: radial-gradient(circle at 50% 20%, #172133 0%, #0d121c 65%, #080b11 100%);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    color: #e6edf3;
  }}
  .window {{
    width: 1060px;
    background: #161b22;
    border-radius: 12px;
    border: 1px solid #30363d;
    box-shadow: 0 30px 70px rgba(0, 0, 0, 0.65), 0 0 0 1px rgba(255, 255, 255, 0.05);
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }}
  .titlebar {{
    background: #0d1117;
    height: 42px;
    display: flex;
    align-items: center;
    padding: 0 16px;
    border-bottom: 1px solid #21262d;
    position: relative;
  }}
  .dots {{
    display: flex;
    gap: 8px;
    align-items: center;
  }}
  .dot {{
    width: 12px;
    height: 12px;
    border-radius: 50%;
  }}
  .dot-red {{ background: #ff5f56; border: 1px solid #e0443e; }}
  .dot-yellow {{ background: #ffbd2e; border: 1px solid #dea123; }}
  .dot-green {{ background: #27c93f; border: 1px solid #1aab29; }}
  .title {{
    position: absolute;
    left: 0;
    right: 0;
    text-align: center;
    font-size: 13px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-weight: 500;
    color: #8b949e;
    letter-spacing: 0.2px;
  }}
  .badge {{
    margin-left: auto;
    font-size: 11px;
    font-weight: 600;
    padding: 2px 8px;
    border-radius: 12px;
    background: #21262d;
    color: #58a6ff;
    border: 1px solid rgba(88, 166, 255, 0.2);
    z-index: 2;
  }}
  .terminal-body {{
    padding: 22px 28px;
    font-family: "JetBrains Mono", "Fira Code", "Cascadia Code", "SF Mono", Consolas, monospace;
    font-size: 14px;
    line-height: 1.55;
    color: #c9d1d9;
    min-height: 460px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .content {{
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}
  .cmd-line {{
    display: flex;
    align-items: baseline;
    gap: 8px;
    font-weight: 500;
    font-size: 13.5px;
  }}
  .prompt-arrow {{ color: #3fb950; font-weight: bold; }}
  .prompt-dir {{ color: #58a6ff; font-weight: bold; }}
  .prompt-branch {{ color: #bc8cff; }}
  .prompt-cmd {{ color: #f0f6fc; font-weight: 600; }}
  .output-block {{
    background: rgba(13, 17, 23, 0.6);
    border: 1px solid #21262d;
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 13.5px;
    color: #e6edf3;
  }}
  .highlight {{ color: #79c0ff; font-weight: 600; }}
  .tag-freezing {{
    display: inline-block;
    background: rgba(56, 139, 253, 0.15);
    color: #58a6ff;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 600;
    border: 1px solid rgba(56, 139, 253, 0.3);
  }}
  .tag-hazardous {{
    display: inline-block;
    background: rgba(248, 81, 73, 0.15);
    color: #ff7b72;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 600;
    border: 1px solid rgba(248, 81, 73, 0.3);
  }}
  .tag-accepted {{
    display: inline-block;
    background: rgba(46, 160, 67, 0.15);
    color: #3fb950;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 600;
    border: 1px solid rgba(46, 160, 67, 0.3);
  }}
  .tag-warning {{
    display: inline-block;
    background: rgba(210, 153, 34, 0.15);
    color: #d29922;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 600;
    border: 1px solid rgba(210, 153, 34, 0.3);
  }}
  .tag-ideal {{
    display: inline-block;
    background: rgba(63, 185, 80, 0.15);
    color: #56d364;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 600;
    border: 1px solid rgba(63, 185, 80, 0.3);
  }}
  .tag-purple {{
    display: inline-block;
    background: rgba(188, 140, 255, 0.15);
    color: #d2a8ff;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 600;
    border: 1px solid rgba(188, 140, 255, 0.3);
  }}
  .tag-cyan {{
    display: inline-block;
    background: rgba(57, 197, 207, 0.15);
    color: #56d4dd;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 600;
    border: 1px solid rgba(57, 197, 207, 0.3);
  }}
  .input-text {{ color: #ffa657; font-weight: bold; }}
  .comment {{ color: #8b949e; font-style: italic; }}
  .grid-two {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
  }}
  .footer-status {{
    margin-top: 14px;
    padding-top: 10px;
    border-top: 1px solid #21262d;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 11.5px;
    color: #8b949e;
  }}
  .footer-status span.accent {{
    color: #58a6ff;
    font-weight: 500;
  }}
</style>
</head>
<body>
  <div class="window">
    <div class="titlebar">
      <div class="dots">
        <div class="dot dot-red"></div>
        <div class="dot dot-yellow"></div>
        <div class="dot dot-green"></div>
      </div>
      <div class="title">{title}</div>
      <div class="badge">{badge}</div>
    </div>
    <div class="terminal-body">
      <div class="content">
        {content}
      </div>
      <div class="footer-status">
        <div><span>Repository:</span> <span class="accent">rkohnmn/CSI109Podder</span> · <span>Branch:</span> <span class="accent">main</span></div>
        <div><span>Muhlenberg College</span> · <span>CSI 109: Introduction to Data Science</span></div>
      </div>
    </div>
  </div>
</body>
</html>
"""

screens = [
    {
        "filename": "01-overview.png",
        "title": "zsh — python Lab02/simulate_station.py (Sensor Telemetry Simulation)",
        "badge": "Lab 02 · Telemetry Pipeline",
        "content": """
          <div class="cmd-line">
            <span class="prompt-arrow">➜</span>
            <span class="prompt-dir">CSI109</span>
            <span class="prompt-branch">git:(main)</span>
            <span class="prompt-cmd">python Lab02/simulate_station.py</span>
          </div>
          <div class="output-block">
            <div style="font-weight: bold; color: #58a6ff; margin-bottom: 8px; font-size: 15px;">Simulated reading</div>
            <div style="margin-bottom: 4px;">Temperature: <span class="highlight">-6.0 C</span></div>
            <div style="margin-bottom: 8px;">Wind speed: <span class="highlight">7 km/h</span></div>
            <div style="margin-bottom: 8px;">Climate Classification: <span class="tag-freezing">Freezing</span></div>
            <div style="margin-bottom: 8px;">Operational Advisory: <span class="tag-hazardous">Hazardous conditions.</span></div>
            <div>Physical Range Check: <span class="tag-accepted">Validator: accepted</span></div>
          </div>
          <div class="output-block" style="background: rgba(22, 27, 34, 0.4); border-color: #30363d; font-size: 13px;">
            <div style="color: #8b949e; margin-bottom: 4px;"><span style="color: #79c0ff; font-weight: 600;">[SIMULATION PIPELINE SPECIFICATION]</span></div>
            <div style="color: #8b949e;">• PRNG Reproducibility: Seed fixed at <span style="color: #e6edf3;">67</span> for deterministic validation</div>
            <div style="color: #8b949e;">• Decision Rule: Temperature &lt; 0°C triggers Freezing band and immediate Hazardous status</div>
            <div style="color: #8b949e;">• Physical Bounds: Telemetry validated against empirical sensor thresholds [-90.0°C, 60.0°C]</div>
          </div>
        """
    },
    {
        "filename": "02-main-workflow.png",
        "title": "zsh — python Lab02/advisory.py (Multi-Variable Boolean Safety Logic)",
        "badge": "Lab 02 · Safety Decision System",
        "content": """
          <div class="grid-two">
            <div>
              <div class="cmd-line">
                <span class="prompt-arrow">➜</span>
                <span class="prompt-dir">CSI109</span>
                <span class="prompt-branch">git:(main)</span>
                <span class="prompt-cmd">python Lab02/advisory.py</span>
              </div>
              <div class="output-block" style="margin-top: 8px;">
                <div style="color: #8b949e;">Temperature (C): <span class="input-text">18.5</span></div>
                <div style="color: #8b949e;">Wind speed (km/h): <span class="input-text">6.2</span></div>
                <div style="margin-top: 10px; margin-bottom: 6px;">Band: <span class="highlight">Mild</span></div>
                <div>Status: <span class="tag-ideal">Ideal conditions for field work.</span></div>
              </div>
            </div>
            <div>
              <div class="cmd-line">
                <span class="prompt-arrow">➜</span>
                <span class="prompt-dir">CSI109</span>
                <span class="prompt-branch">git:(main)</span>
                <span class="prompt-cmd">python Lab02/advisory.py</span>
              </div>
              <div class="output-block" style="margin-top: 8px;">
                <div style="color: #8b949e;">Temperature (C): <span class="input-text">24.0</span></div>
                <div style="color: #8b949e;">Wind speed (km/h): <span class="input-text">26.5</span></div>
                <div style="margin-top: 10px; margin-bottom: 6px;">Band: <span class="highlight">Mild</span></div>
                <div>Status: <span class="tag-hazardous">Hazardous conditions.</span></div>
              </div>
            </div>
          </div>
          <div class="output-block" style="background: rgba(22, 27, 34, 0.4); border-color: #30363d; font-size: 13px;">
            <div style="color: #8b949e; margin-bottom: 4px;"><span style="color: #79c0ff; font-weight: 600;">[BOOLEAN EVALUATION CRITERIA]</span></div>
            <div style="color: #8b949e;">• <span style="color: #56d364;">Ideal:</span> (15°C ≤ temp ≤ 25°C) <strong>AND</strong> (wind &lt; 10 km/h) → Optimal conditions for research operations</div>
            <div style="color: #8b949e;">• <span style="color: #ff7b72;">Hazardous:</span> (temp &lt; 0°C) <strong>OR</strong> (wind &gt; 20 km/h) → Immediate field work hazard alert</div>
          </div>
        """
    },
    {
        "filename": "03-results.png",
        "title": "zsh — python Lab02/validator.py (Telemetry Cleaning & Outlier Ingestion)",
        "badge": "Lab 02 · Data Cleaning Pipeline",
        "content": """
          <div class="cmd-line">
            <span class="prompt-arrow">➜</span>
            <span class="prompt-dir">CSI109</span>
            <span class="prompt-branch">git:(main)</span>
            <span class="prompt-cmd">python Lab02/validator.py (Interactive Test Suite)</span>
          </div>
          <div style="display: flex; flex-direction: column; gap: 8px; margin-top: 2px;">
            <div class="output-block" style="padding: 9px 14px;">
              <span class="comment"># Case 1: Null/Missing Value Ingestion</span><br>
              Enter a temperature reading: <span class="input-text">N/A</span><br>
              Result: <span class="tag-warning">Missing value -- skipped.</span>
            </div>
            <div class="output-block" style="padding: 9px 14px;">
              <span class="comment"># Case 2: Sensor Anomaly & Extreme Physical Outlier Filtering</span><br>
              Enter a temperature reading: <span class="input-text">75.4</span><br>
              Result: <span class="tag-hazardous">Implausible reading (75.4) -- flagged.</span>
            </div>
            <div class="output-block" style="padding: 9px 14px;">
              <span class="comment"># Case 3: Verified Physical Telemetry Point Accepted</span><br>
              Enter a temperature reading: <span class="input-text">21.8</span><br>
              Result: <span class="tag-accepted">Accepted: 21.8 C</span>
            </div>
          </div>
          <div style="font-size: 12.5px; color: #8b949e; margin-top: 4px;">
            Adheres to Data Science Lifecycle Step 2: Ingesting raw sensor strings, parsing whitespace, catching missing flags, and verifying bounds [-90.0°C, 60.0°C].
          </div>
        """
    },
    {
        "filename": "04-simulation-analysis.png",
        "title": "zsh — Lab 03: Stochastic Tournament Simulation & Stream Streak Tracking",
        "badge": "Lab 03 · Iterative Simulation",
        "content": """
          <div class="grid-two">
            <div>
              <div class="cmd-line">
                <span class="prompt-arrow">➜</span>
                <span class="prompt-dir">CSI109</span>
                <span class="prompt-branch">git:(main)</span>
                <span class="prompt-cmd">python Lab03/tournamentTracker.py</span>
              </div>
              <div class="output-block" style="margin-top: 8px;">
                <div style="color: #8b949e; font-size: 12.5px;">Processing games for Player #1...</div>
                <div style="color: #8b949e; font-size: 12.5px;">Processing games for Player #2...</div>
                <div style="color: #8b949e; font-size: 12.5px; font-style: italic;">[... 10 players · 5 games each (50 trials) ...]</div>
                <div style="color: #8b949e; font-size: 12.5px;">Processing games for Player #10...</div>
                <div style="margin-top: 10px; border-top: 1px solid #21262d; padding-top: 8px;">
                  Champion: <span class="tag-purple">Player #3</span>
                </div>
                <div style="margin-top: 6px; color: #56d364; font-weight: bold;">
                  High Score: <span class="highlight">999</span> / 1000 pts
                </div>
              </div>
            </div>
            <div>
              <div class="cmd-line">
                <span class="prompt-arrow">➜</span>
                <span class="prompt-dir">CSI109</span>
                <span class="prompt-branch">git:(main)</span>
                <span class="prompt-cmd">python Lab03/longestStreak.py</span>
              </div>
              <div class="output-block" style="margin-top: 8px;">
                <div style="color: #8b949e;">Stream: <span class="input-text">2</span> → <span class="input-text">5</span> → <span class="input-text">8</span> <span class="comment">(run = 3)</span></div>
                <div style="color: #8b949e;">Drop: <span class="input-text">3</span> <span class="comment">(resets run to 1)</span></div>
                <div style="color: #8b949e;">Surge: <span class="input-text">4</span> → <span class="input-text">7</span> → <span class="input-text">9</span> → <span class="input-text">12</span> <span class="comment">(run = 5)</span></div>
                <div style="color: #8b949e;">End sentinel: <span class="input-text">-1</span> <span class="comment">(stream terminates)</span></div>
                <div style="margin-top: 10px; border-top: 1px solid #21262d; padding-top: 8px;">
                  Longest streak: <span class="tag-cyan">5 increasing numbers</span>
                </div>
              </div>
            </div>
          </div>
          <div class="output-block" style="background: rgba(22, 27, 34, 0.4); border-color: #30363d; font-size: 13px;">
            <div style="color: #8b949e; margin-bottom: 4px;"><span style="color: #79c0ff; font-weight: 600;">[ITERATIVE SIMULATION & SINGLE-PASS STREAM PROCESSING]</span></div>
            <div style="color: #8b949e;">• <span style="color: #d2a8ff;">Monte Carlo Simulation:</span> Nested loop tracking 10 players across 5 games (50 trials) updating tournament high-score state.</div>
            <div style="color: #8b949e;">• <span style="color: #56d4dd;">Streaming Streak Analysis:</span> O(N) memory-efficient single-pass algorithm tracking strictly increasing sequences with sentinel termination.</div>
          </div>
        """
    },
    {
        "filename": "05-matrix-data-structures.png",
        "title": "zsh — Practice 04: Multidimensional Matrix Symmetry & Sequence Operations",
        "badge": "Practice 04 · Data Structures",
        "content": """
          <div class="grid-two">
            <div>
              <div class="cmd-line">
                <span class="prompt-arrow">➜</span>
                <span class="prompt-dir">CSI109</span>
                <span class="prompt-branch">git:(main)</span>
                <span class="prompt-cmd">python Practice4/symmetric_matrix.py</span>
              </div>
              <div class="output-block" style="margin-top: 8px;">
                <div style="color: #8b949e; margin-bottom: 4px;">Matrix (3×3 Tensor):</div>
                <div style="font-family: monospace; color: #79c0ff; margin-bottom: 8px; line-height: 1.4;">
                  &nbsp;&nbsp;[[1, 2, 3],<br>
                  &nbsp;&nbsp;&nbsp;[2, 4, 5],<br>
                  &nbsp;&nbsp;&nbsp;[3, 5, 6]]
                </div>
                <div>Condition: <span style="color: #c9d1d9;">M[i][j] == M[j][i] ∀ i, j</span></div>
                <div style="margin-top: 8px;">Status: <span class="tag-accepted">Is symmetric: True</span></div>
              </div>
            </div>
            <div>
              <div class="cmd-line">
                <span class="prompt-arrow">➜</span>
                <span class="prompt-dir">CSI109</span>
                <span class="prompt-branch">git:(main)</span>
                <span class="prompt-cmd">python Practice4/remove_duplicates.py</span>
              </div>
              <div class="output-block" style="margin-top: 8px;">
                <div style="color: #8b949e;">Original list: <span style="color: #ff7b72;">[1, 2, 2, 3, 4, 4, 4, 5]</span></div>
                <div style="margin-top: 4px; margin-bottom: 8px;">Without duplicates: <span class="tag-ideal">[1, 2, 3, 4, 5]</span></div>
                
                <div style="border-top: 1px solid #21262d; padding-top: 8px; margin-top: 6px;">
                  <div class="cmd-line" style="font-size: 12px; margin-bottom: 4px;">
                    <span class="prompt-arrow">➜</span> <span class="prompt-cmd">python Practice4/rotate_list.py (k=2)</span>
                  </div>
                  <div style="color: #8b949e; font-size: 13px;">Original: <span style="color: #c9d1d9;">[1, 2, 3, 4, 5]</span></div>
                  <div style="font-size: 13px;">Rotated: <span class="tag-cyan">[4, 5, 1, 2, 3]</span></div>
                </div>
              </div>
            </div>
          </div>
          <div class="output-block" style="background: rgba(22, 27, 34, 0.4); border-color: #30363d; font-size: 13px;">
            <div style="color: #8b949e; margin-bottom: 4px;"><span style="color: #79c0ff; font-weight: 600;">[MULTIDIMENSIONAL TENSORS & SEQUENCE TRANSFORMATIONS]</span></div>
            <div style="color: #8b949e;">• <span style="color: #56d364;">Matrix Symmetry:</span> Rigorous 2D index traversal validating transpositions (M = Mᵀ) reflecting linear algebra principles.</div>
            <div style="color: #8b949e;">• <span style="color: #58a6ff;">List Operations:</span> First-seen set preservation for deduplication alongside cyclic array rotation via slice operations (<code style="color: #f0f6fc;">[-k:] + [:-k]</code>).</div>
          </div>
        """
    },
    {
        "filename": "06-computational-math.png",
        "title": "zsh — Practice 03: Algorithmic Number Theory & Sentinel Streaming Statistics",
        "badge": "Practice 03 · Computational Math",
        "content": """
          <div class="grid-two">
            <div>
              <div class="cmd-line">
                <span class="prompt-arrow">➜</span>
                <span class="prompt-dir">CSI109</span>
                <span class="prompt-branch">git:(main)</span>
                <span class="prompt-cmd">python Practice3/prime_check.py</span>
              </div>
              <div class="output-block" style="margin-top: 8px;">
                <div style="color: #8b949e;">Enter a number (1-100): <span class="input-text">29</span></div>
                <div style="margin-top: 6px; margin-bottom: 8px;">Result: <span class="tag-accepted">29 is prime.</span></div>
                
                <div style="border-top: 1px solid #21262d; padding-top: 6px; margin-top: 6px;">
                  <div class="cmd-line" style="font-size: 12px; margin-bottom: 4px;">
                    <span class="prompt-arrow">➜</span> <span class="prompt-cmd">python Practice3/fibonacci.py (n=10)</span>
                  </div>
                  <div style="color: #79c0ff; font-size: 13px; font-weight: 500;">
                    0 1 1 2 3 5 8 13 21 34
                  </div>
                </div>
              </div>
            </div>
            <div>
              <div class="cmd-line">
                <span class="prompt-arrow">➜</span>
                <span class="prompt-dir">CSI109</span>
                <span class="prompt-branch">git:(main)</span>
                <span class="prompt-cmd">python Practice3/temp_avg.py</span>
              </div>
              <div class="output-block" style="margin-top: 8px;">
                <div style="color: #8b949e;">Reading 1: <span class="input-text">68.5</span></div>
                <div style="color: #8b949e;">Reading 2: <span class="input-text">72.0</span></div>
                <div style="color: #8b949e;">Reading 3: <span class="input-text">70.5</span></div>
                <div style="color: #8b949e;">Sentinel flag: <span class="input-text">done</span></div>
                <div style="margin-top: 8px; border-top: 1px solid #21262d; padding-top: 6px;">
                  <div>Number of readings: <span class="highlight">3</span></div>
                  <div style="font-weight: bold; margin-top: 2px;">Average temperature: <span class="tag-ideal">70.33</span></div>
                </div>
              </div>
            </div>
          </div>
          <div class="output-block" style="background: rgba(22, 27, 34, 0.4); border-color: #30363d; font-size: 13px;">
            <div style="color: #8b949e; margin-bottom: 4px;"><span style="color: #79c0ff; font-weight: 600;">[NUMBER THEORY & RUNNING STREAM ACCUMULATION]</span></div>
            <div style="color: #8b949e;">• <span style="color: #56d364;">Number Theory:</span> Trial division prime-testing with early exit optimization alongside O(N) Fibonacci recurrence (<code style="color: #f0f6fc;">Fₙ = Fₙ₋₁ + Fₙ₋₂</code>).</div>
            <div style="color: #8b949e;">• <span style="color: #79c0ff;">Sentinel Telemetry Accumulator:</span> Streaming while-loop computing running totals and sample mean (<code style="color: #f0f6fc;">:.2f</code>) without prior knowledge of stream length.</div>
          </div>
        """
    }
]

for s in screens:
    html_content = TEMPLATE.format(
        title=s["title"],
        badge=s["badge"],
        content=s["content"]
    )
    html_file = os.path.join(SCRATCH_DIR, s["filename"].replace(".png", ".html"))
    out_png = os.path.join(OUT_DIR, s["filename"])
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    cmd = [
        chrome_bin,
        "--headless=new",
        "--no-sandbox",
        "--hide-scrollbars",
        "--window-size=1200,675",
        f"--screenshot={out_png}",
        f"file:///{html_file.replace(os.sep, '/')}"
    ]
    print(f"Rendering {s['filename']}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(out_png):
        print(f"Successfully generated {out_png} ({os.path.getsize(out_png)} bytes)")
    else:
        print(f"Failed to generate {out_png}. Stderr: {result.stderr}")

print("Screenshot generation completed.")
