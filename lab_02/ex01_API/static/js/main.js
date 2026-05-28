document.addEventListener('DOMContentLoaded', () => {
  const themeToggle = document.getElementById('themeToggle');
  const copyBtn = document.getElementById('copyBtn');
  const selectBtn = document.getElementById('selectBtn');
  const resultEl = document.getElementById('result');

  // restore theme
  const stored = localStorage.getItem('preferredTheme');
  if (stored === 'dark') document.body.classList.add('dark');

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      document.body.classList.toggle('dark');
      const isDark = document.body.classList.contains('dark');
      localStorage.setItem('preferredTheme', isDark ? 'dark' : 'light');
      themeToggle.textContent = isDark ? '☀️' : '🌙';
    });
  }

  if (copyBtn && resultEl) {
    copyBtn.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(resultEl.innerText);
        copyBtn.textContent = 'Copied ✓';
        setTimeout(() => (copyBtn.textContent = 'Copy'), 1500);
      } catch (e) {
        copyBtn.textContent = 'Failed';
        setTimeout(() => (copyBtn.textContent = 'Copy'), 1500);
      }
    });
  }

  if (selectBtn && resultEl) {
    selectBtn.addEventListener('click', () => {
      const range = document.createRange();
      range.selectNodeContents(resultEl);
      const sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
    });
  }

  // small progressive enhancement: submit form via Ctrl+Enter when focused in textarea
  const textarea = document.getElementById('text');
  if (textarea) {
    textarea.addEventListener('keydown', (ev) => {
      if (ev.ctrlKey && ev.key === 'Enter') {
        ev.preventDefault();
        textarea.form.submit();
      }
    });
  }

  // Testcase autofill buttons
  const testcaseButtons = document.querySelectorAll('.testcase-btn');
  const algoSelect = document.getElementById('algorithm');
  const actionSelect = document.getElementById('action');
  const keyInput = document.getElementById('key');

  // small set of example testcases; extend as needed
  // Use compact/no-space inputs for ciphers that expect continuous letters to avoid backend errors
  const TESTCASES = {
    caesar: { action: 'encrypt', key: '3', text: 'HELLOWORLD' },
    vigenere: { action: 'encrypt', key: 'KEY', text: 'ATTACKATDAWN' },
    railfence: { action: 'encrypt', key: '3', text: 'WEAREDISCOVERED' },
    playfair: { action: 'encrypt', key: 'MONARCHY', text: 'HELLO' },
    transposition: { action: 'encrypt', key: '4', text: 'DEFENDTHEEASTWALL' }
  };

  function clearActiveTestcase() {
    testcaseButtons.forEach(b => b.classList.remove('active'));
  }

  testcaseButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const algo = btn.dataset.algo;
      clearActiveTestcase();
      btn.classList.add('active');
      if (algoSelect) algoSelect.value = algo;
      const t = TESTCASES[algo];
      if (t) {
        if (actionSelect) actionSelect.value = t.action;
        if (keyInput) keyInput.value = t.key;
        if (textarea) {
          // sanitize for ciphers that don't accept spaces or non-letters
          const sanitized = t.text.replace(/[^A-Za-z]/g, '').toUpperCase();
          textarea.value = sanitized;
        }
      } else {
        // defaults
        if (actionSelect) actionSelect.value = 'encrypt';
        if (keyInput) keyInput.value = '';
        if (textarea) textarea.value = '';
      }
    });
  });

  // keep active testcase synced when algorithm select changes
  if (algoSelect) {
    algoSelect.addEventListener('change', () => {
      clearActiveTestcase();
      const v = algoSelect.value;
      const match = Array.from(testcaseButtons).find(b => b.dataset.algo === v);
      if (match) match.classList.add('active');
    });
  }

  // sanitize on submit for known strict ciphers to avoid server-side errors
  const form = document.querySelector('form');
  const STRICT_CIPHERS = new Set(['caesar','vigenere','playfair','railfence','transposition']);
  if (form) {
    form.addEventListener('submit', (ev) => {
      try {
        const algo = algoSelect ? algoSelect.value : null;
        if (algo && STRICT_CIPHERS.has(algo) && textarea) {
          textarea.value = textarea.value.replace(/[^A-Za-z]/g, '').toUpperCase();
        }
      } catch (e) {
        // non-fatal: allow submit to proceed and backend to handle errors
      }
    });
  }
});

// Taskbar and export logic (top-level, runs after DOM load handlers above)
document.addEventListener('DOMContentLoaded', () => {
  const exportBtn = document.getElementById('exportBtn');
  const taskItems = document.querySelectorAll('.task-item');

  taskItems.forEach(t => t.addEventListener('click', () => {
    taskItems.forEach(x => x.classList.remove('active'));
    t.classList.add('active');
    // simple demo: scroll to main page on 'lab02' or highlight areas
    if (t.dataset.action === 'lab02') {
      const main = document.querySelector('main');
      if (main) main.scrollIntoView({behavior:'smooth'});
    }
  }));

  if (exportBtn) {
    exportBtn.addEventListener('click', () => {
      try {
        // gather current form state
        const algo = (document.getElementById('algorithm') || {}).value || '';
        const action = (document.getElementById('action') || {}).value || '';
        const key = (document.getElementById('key') || {}).value || '';
        const text = (document.getElementById('text') || {}).value || '';

        const collection = {
          info: {
            name: 'Lab_02 Cipher Requests',
            schema: 'https://schema.getpostman.com/json/collection/v2.1.0/collection.json'
          },
          item: [
            {
              name: `Cipher ${algo} ${action}`,
              request: {
                method: 'POST',
                header: [{key: 'Content-Type', value: 'application/json'}],
                body: {
                  mode: 'raw',
                  raw: JSON.stringify({ algorithm: algo, action: action, key: key, text: text }, null, 2)
                },
                url: {
                  raw: '{{baseUrl}}/api/cipher',
                  host: ['{{baseUrl}}'],
                  path: ['api','cipher']
                }
              }
            }
          ]
        };

        const blob = new Blob([JSON.stringify(collection, null, 2)], {type: 'application/json'});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'postman_collection_lab02.json';
        document.body.appendChild(a);
        a.click();
        a.remove();
        URL.revokeObjectURL(url);
      } catch (e) {
        alert('Export failed: ' + e.message);
      }
    });
  }
});
