/* Jeremiah Cargill · AI Chat Agent
 *
 * A floating chat widget that calls the OpenAI chat completions API.
 * The OpenAI API key is stored per-browser in localStorage — never committed
 * to the repo.  On first use the widget prompts for the key.
 *
 * Conversation history is kept in sessionStorage so it persists across
 * page navigations within the same tab.
 *
 * Configuration:
 *   window.AGENT_ENDPOINT  (optional) — override the API endpoint, e.g. a
 *                           serverless proxy.  Defaults to the OpenAI API.
 *   window.AGENT_MODEL     (optional) — model name.  Defaults to gpt-4o-mini.
 */

(function () {
  'use strict';

  // ── Config ────────────────────────────────────────────────────────────────
  const ENDPOINT =
    (typeof window.AGENT_ENDPOINT !== 'undefined' && window.AGENT_ENDPOINT) ||
    'https://api.openai.com/v1/chat/completions';
  const MODEL =
    (typeof window.AGENT_MODEL !== 'undefined' && window.AGENT_MODEL) ||
    'gpt-4o-mini';
  const LS_KEY = 'agent_api_key';
  const SS_HISTORY = 'agent_history';
  const MAX_HISTORY = 30; // keep last N turns in context

  // ── System prompt ─────────────────────────────────────────────────────────
  const SYSTEM_PROMPT = `You are the AI assistant for Jeremiah Cargill's professional portfolio site (jeremiah9980.github.io/jeremiah9980.2). Your job is to help visitors understand Jeremiah's background, services, and projects — and route interested buyers to the right place.

ABOUT JEREMIAH
• Enterprise architect and independent consultant based in Austin, TX.
• 20+ years in infrastructure, identity, cloud, and platform engineering.
• Deep expertise: Okta (IAM/SSO/MFA), VMware (vSphere/Horizon/NSX), Cisco UCS, NetApp, Red Hat OpenShift, AWS/Azure, DMARC/email-auth, DevOps toolchains.
• Holds multiple certifications across VMware, Okta, Microsoft, and networking disciplines.

TWO PRACTICES
1. Cargill Consulting (enterprise)
   – Serves Fortune 500 and mid-market orgs.
   – Service lines: Identity & Access Management, Infrastructure & Virtualisation, Cloud Migration, Platform Engineering / DevOps, Security Architecture.
   – Packaged engagements: IAM Diagnostic, OpenShift Readiness, Cloud Migration Blueprint, DevSecOps Baseline, VMware Modernisation Assessment, Executive Architecture Briefing.
   – Buyers: IT directors, CISOs, enterprise architects, VP Engineering.
   – Link: /professional/cargill-consulting/

2. Next-Gen-IT (small business)
   – Serves firms of 5–200 employees (title companies, realtors, professional services).
   – Packaged offerings: Full IT Audit, Domain & Email Health Audit, Security Hardening, Managed Operations.
   – Flagship deliverable: the written audit report (see Starsky Owen and Shonna King examples on the site).
   – Buyers: small business owners, office managers, anyone who got a phishing/wire-fraud scare.
   – Link: /professional/next-gen-it/

PROJECTS (the lab)
• Conflict Collection — flagship SaaS product. A multi-model, neutral AI platform for co-parenting conflict documentation. Live in production.
• Infrastructure work — VMware, UCS, NetApp, OpenShift case studies.
• GPS / Flywheel / GameChanger — independent tooling projects.
• Client case studies: Teleotitle (wire-fraud hardening), Abode Labs (DNS/email auth), Starsky Owen (realty data), CosmicGen (scoping).
• Link: /projects/

HOW TO DIRECT LEADS
• Enterprise buyer → /professional/cargill-consulting/ or https://www.linkedin.com/in/jeremiahcargill/
• Small business owner → /professional/next-gen-it/
• Curious about the lab → /projects/
• Want to connect directly → LinkedIn: https://www.linkedin.com/in/jeremiahcargill/

TONE
Be direct, concise, and professional — no filler, no hype. Match the voice of the site. If you don't know something specific, say so clearly and offer to route the visitor to Jeremiah via LinkedIn. Do not invent pricing, timelines, or credentials you don't have in context.

DATE CONTEXT
Today's date is injected at runtime. Do not make assumptions about future events or time-sensitive details not provided in your context.`;

  // Append current date so the model has temporal grounding
  const SYSTEM_PROMPT_WITH_DATE =
    SYSTEM_PROMPT + `\n\nToday's date: ${new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}.`;

  // ── State ─────────────────────────────────────────────────────────────────
  let isOpen = false;
  let isStreaming = false;
  let history = loadHistory();

  function loadHistory() {
    try {
      return JSON.parse(sessionStorage.getItem(SS_HISTORY) || '[]');
    } catch (_) {
      return [];
    }
  }

  function saveHistory() {
    try {
      // Keep only the last MAX_HISTORY messages to avoid bloat
      const trimmed = history.slice(-MAX_HISTORY);
      sessionStorage.setItem(SS_HISTORY, JSON.stringify(trimmed));
    } catch (_) { /* quota exceeded — ignore */ }
  }

  // ── DOM helpers ───────────────────────────────────────────────────────────
  function el(tag, attrs, children) {
    const node = document.createElement(tag);
    if (attrs) Object.assign(node, attrs);
    if (children) {
      children.forEach(c => {
        if (typeof c === 'string') node.insertAdjacentHTML('beforeend', c);
        else node.appendChild(c);
      });
    }
    return node;
  }

  // ── Build widget HTML ─────────────────────────────────────────────────────
  function buildWidget() {
    // Toggle button
    const toggle = el('button', {
      id: 'agent-toggle',
      title: 'Chat with the site assistant',
      'aria-label': 'Open chat assistant',
      'aria-expanded': 'false',
      'aria-controls': 'agent-panel',
    });
    toggle.innerHTML = `
      <svg class="icon-chat" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
      </svg>
      <svg class="icon-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" aria-hidden="true">
        <line x1="18" y1="6" x2="6" y2="18"/>
        <line x1="6" y1="6" x2="18" y2="18"/>
      </svg>`;

    // Panel
    const panel = el('div', { id: 'agent-panel' });
    panel.setAttribute('hidden', '');
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', 'Chat assistant');

    // Header
    panel.innerHTML = `
      <div id="agent-header">
        <div class="agent-avatar" aria-hidden="true">J</div>
        <div class="agent-title">
          <strong>Cargill&amp;Co Assistant</strong>
          <span>Ask about services, projects, or getting in touch</span>
        </div>
        <div class="agent-status-dot" id="agent-status-dot" title="Online"></div>
      </div>`;

    // Key screen (shown when no API key is set)
    const keyScreen = el('div', { id: 'agent-key-screen' });
    keyScreen.innerHTML = `
      <div aria-hidden="true" style="font-size:2rem;">🔑</div>
      <div>
        <strong>OpenAI API key required</strong>
        <p>This assistant calls the OpenAI API directly from your browser. Enter your API key below — it is stored only in this browser and never sent anywhere except OpenAI.</p>
      </div>
      <form class="agent-key-form" id="agent-key-form" novalidate>
        <input class="agent-key-input" id="agent-key-input" type="password"
               placeholder="sk-..." autocomplete="off" spellcheck="false" />
        <button type="submit" class="agent-btn agent-btn-primary">Save &amp; start chatting</button>
      </form>
      <p class="agent-key-note">Your key is stored in localStorage and never leaves your browser except in direct requests to api.openai.com.</p>`;

    // Message thread
    const messages = el('div', { id: 'agent-messages', role: 'log', 'aria-live': 'polite', 'aria-atomic': 'false' });

    // Footer
    panel.appendChild(keyScreen);
    panel.appendChild(messages);
    panel.insertAdjacentHTML('beforeend', `
      <div id="agent-footer">
        <textarea id="agent-input" rows="1" placeholder="Ask me anything…"
                  aria-label="Message" maxlength="2000"></textarea>
        <button id="agent-send" title="Send" aria-label="Send message" disabled>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <line x1="22" y1="2" x2="11" y2="13"/>
            <polygon points="22 2 15 22 11 13 2 9 22 2"/>
          </svg>
        </button>
      </div>
      <div class="agent-footer-meta">
        <button id="agent-clear-key" title="Remove saved API key">Change API key</button>
        <span>Powered by OpenAI</span>
      </div>`);

    document.body.appendChild(toggle);
    document.body.appendChild(panel);

    return { toggle, panel, keyScreen, messages };
  }

  // ── Message rendering ─────────────────────────────────────────────────────
  function appendMessage(role, text, temporary) {
    const messages = document.getElementById('agent-messages');
    if (!messages) return null;
    const div = el('div', { className: `agent-msg ${role}` });
    div.textContent = text;
    if (temporary) div.dataset.temporary = 'true';
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
    return div;
  }

  function appendTypingIndicator() {
    const messages = document.getElementById('agent-messages');
    if (!messages) return null;
    const div = el('div', { className: 'agent-typing', id: 'agent-typing' });
    div.setAttribute('aria-label', 'Assistant is typing');
    div.innerHTML = '<span></span><span></span><span></span>';
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
    return div;
  }

  function removeTypingIndicator() {
    const t = document.getElementById('agent-typing');
    if (t) t.remove();
  }

  function appendError(msg) {
    const messages = document.getElementById('agent-messages');
    if (!messages) return;
    const div = el('div', { className: 'agent-msg error' });
    div.textContent = msg;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
  }

  function renderHistory() {
    const messages = document.getElementById('agent-messages');
    if (!messages) return;
    messages.innerHTML = '';
    history.forEach(m => appendMessage(m.role, m.content));
  }

  // ── Auto-resize textarea ──────────────────────────────────────────────────
  function autoResize(textarea) {
    textarea.style.height = 'auto';
    textarea.style.height = Math.min(textarea.scrollHeight, 112) + 'px';
  }

  // ── Show / hide key screen ─────────────────────────────────────────────────
  function hasApiKey() {
    const key = localStorage.getItem(LS_KEY);
    return key && key.startsWith('sk-');
  }

  function showKeyScreen(show) {
    const keyScreen = document.getElementById('agent-key-screen');
    const messages = document.getElementById('agent-messages');
    const footer = document.getElementById('agent-footer');
    const footerMeta = document.querySelector('.agent-footer-meta');
    if (!keyScreen || !messages || !footer) return;

    if (show) {
      keyScreen.style.display = 'flex';
      messages.style.display = 'none';
      footer.style.display = 'none';
      if (footerMeta) footerMeta.style.display = 'none';
    } else {
      keyScreen.style.display = 'none';
      messages.style.display = 'flex';
      footer.style.display = 'flex';
      if (footerMeta) footerMeta.style.display = 'flex';
      renderHistory();
      if (history.length === 0) {
        appendMessage('assistant',
          'Hi! I\'m the Cargill&Co site assistant. Ask me about the practices, projects, or how to get in touch with Jeremiah.');
      }
    }
  }

  // ── Status dot helper ─────────────────────────────────────────────────────
  function setThinking(on) {
    const dot = document.getElementById('agent-status-dot');
    if (!dot) return;
    if (on) dot.classList.add('thinking');
    else dot.classList.remove('thinking');
  }

  // ── Open / close panel ────────────────────────────────────────────────────
  function openPanel() {
    const panel = document.getElementById('agent-panel');
    const toggle = document.getElementById('agent-toggle');
    if (!panel || !toggle) return;

    isOpen = true;
    panel.classList.add('entering');
    panel.removeAttribute('hidden');
    toggle.classList.add('open');
    toggle.setAttribute('aria-expanded', 'true');

    // Trigger transition after paint
    requestAnimationFrame(() => {
      requestAnimationFrame(() => panel.classList.remove('entering'));
    });

    showKeyScreen(!hasApiKey());

    const input = document.getElementById('agent-input');
    if (input && hasApiKey()) setTimeout(() => input.focus(), 220);
  }

  function closePanel() {
    const panel = document.getElementById('agent-panel');
    const toggle = document.getElementById('agent-toggle');
    if (!panel || !toggle) return;

    isOpen = false;
    panel.setAttribute('hidden', '');
    toggle.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
  }

  // ── Send a message ────────────────────────────────────────────────────────
  async function sendMessage(text) {
    if (isStreaming || !text.trim()) return;

    const apiKey = localStorage.getItem(LS_KEY);
    if (!apiKey) {
      showKeyScreen(true);
      return;
    }

    const input = document.getElementById('agent-input');
    const sendBtn = document.getElementById('agent-send');

    isStreaming = true;
    if (input) { input.value = ''; input.style.height = 'auto'; input.disabled = true; }
    if (sendBtn) sendBtn.disabled = true;
    setThinking(true);

    history.push({ role: 'user', content: text });
    saveHistory();
    appendMessage('user', text);
    appendTypingIndicator();

    const messages = document.getElementById('agent-messages');

    try {
      const payload = {
        model: MODEL,
        stream: true,
        messages: [
          { role: 'system', content: SYSTEM_PROMPT_WITH_DATE },
          ...history.slice(-MAX_HISTORY),
        ],
      };

      const headers = { 'Content-Type': 'application/json' };
      // Only set Authorization when calling OpenAI directly (not a proxy that handles auth).
      // Use URL hostname comparison to avoid substring-match false positives.
      try {
        const endpointHost = new URL(ENDPOINT).hostname;
        if (endpointHost === 'api.openai.com') {
          headers['Authorization'] = `Bearer ${apiKey}`;
        }
      } catch (_) {
        // Relative or malformed URL — assume it's a local proxy; omit auth header.
      }

      const res = await fetch(ENDPOINT, {
        method: 'POST',
        headers,
        body: JSON.stringify(payload),
      });

      if (!res.ok) {
        const errBody = await res.text().catch(() => '');
        let msg = `API error ${res.status}`;
        try {
          const j = JSON.parse(errBody);
          if (j.error && j.error.message) msg = j.error.message;
        } catch (_) { /* ignore */ }
        throw new Error(msg);
      }

      removeTypingIndicator();

      const assistantDiv = el('div', { className: 'agent-msg assistant' });
      assistantDiv.textContent = '';
      if (messages) {
        messages.appendChild(assistantDiv);
        messages.scrollTop = messages.scrollHeight;
      }

      let assistantText = '';
      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });

        const lines = buffer.split('\n');
        buffer = lines.pop(); // keep incomplete line in buffer

        for (const line of lines) {
          const trimmed = line.trim();
          if (!trimmed || trimmed === 'data: [DONE]') continue;
          if (!trimmed.startsWith('data: ')) continue;
          try {
            const json = JSON.parse(trimmed.slice(6));
            const delta = json.choices?.[0]?.delta?.content;
            if (delta) {
              assistantText += delta;
              assistantDiv.textContent = assistantText;
              if (messages) messages.scrollTop = messages.scrollHeight;
            }
          } catch (_) { /* malformed chunk — skip */ }
        }
      }

      // Handle any remaining buffer
      if (buffer.trim() && buffer.startsWith('data: ') && buffer.trim() !== 'data: [DONE]') {
        try {
          const json = JSON.parse(buffer.slice(6));
          const delta = json.choices?.[0]?.delta?.content;
          if (delta) {
            assistantText += delta;
            assistantDiv.textContent = assistantText;
          }
        } catch (_) { /* ignore */ }
      }

      if (assistantText) {
        history.push({ role: 'assistant', content: assistantText });
        saveHistory();
      }
    } catch (err) {
      removeTypingIndicator();
      // Remove the last user message from history on failure so it can be retried
      if (history.length > 0 && history[history.length - 1].role === 'user') {
        history.pop();
        saveHistory();
      }
      let userMsg = 'Something went wrong. Please try again.';
      if (err.message && err.message.includes('401')) {
        userMsg = 'Invalid API key. Please update your key using the link below.';
      } else if (err.message && err.message.includes('429')) {
        userMsg = 'Rate limit reached. Wait a moment and try again.';
      } else if (err.message && err.message.includes('Failed to fetch')) {
        userMsg = 'Network error — check your connection and try again.';
      } else if (err.message) {
        userMsg = err.message;
      }
      appendError(userMsg);
    } finally {
      isStreaming = false;
      if (input) input.disabled = false;
      if (sendBtn) sendBtn.disabled = false;
      setThinking(false);
      if (input && isOpen) input.focus();
    }
  }

  // ── Wire events ───────────────────────────────────────────────────────────
  function wireEvents() {
    const toggle = document.getElementById('agent-toggle');
    const input = document.getElementById('agent-input');
    const sendBtn = document.getElementById('agent-send');
    const keyForm = document.getElementById('agent-key-form');
    const keyInput = document.getElementById('agent-key-input');
    const clearKeyBtn = document.getElementById('agent-clear-key');

    // Toggle open/close
    toggle && toggle.addEventListener('click', () => {
      if (isOpen) closePanel(); else openPanel();
    });

    // Close on Escape
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && isOpen) closePanel();
    });

    // Input: enable send button when there is content
    if (input) {
      input.addEventListener('input', () => {
        autoResize(input);
        if (sendBtn) sendBtn.disabled = !input.value.trim() || isStreaming;
      });

      // Send on Enter (not Shift+Enter)
      input.addEventListener('keydown', e => {
        if (e.key === 'Enter' && !e.shiftKey && !e.ctrlKey) {
          e.preventDefault();
          const text = input.value.trim();
          if (text && !isStreaming) sendMessage(text);
        }
      });
    }

    // Send button
    sendBtn && sendBtn.addEventListener('click', () => {
      if (!input) return;
      const text = input.value.trim();
      if (text && !isStreaming) sendMessage(text);
    });

    // API key form
    keyForm && keyForm.addEventListener('submit', e => {
      e.preventDefault();
      const key = (keyInput ? keyInput.value : '').trim();
      if (!key) return;
      localStorage.setItem(LS_KEY, key);
      keyInput.value = '';
      showKeyScreen(false);
      const inp = document.getElementById('agent-input');
      if (inp) setTimeout(() => inp.focus(), 50);
    });

    // Clear key
    clearKeyBtn && clearKeyBtn.addEventListener('click', () => {
      localStorage.removeItem(LS_KEY);
      history = [];
      saveHistory();
      showKeyScreen(true);
      const ki = document.getElementById('agent-key-input');
      if (ki) setTimeout(() => ki.focus(), 50);
    });
  }

  // ── Init ──────────────────────────────────────────────────────────────────
  function init() {
    buildWidget();
    wireEvents();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
