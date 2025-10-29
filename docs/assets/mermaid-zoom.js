// Click-to-zoom for Mermaid diagrams
(function () {
  function ensureModal() {
    let modal = document.getElementById('mermaid-zoom-modal');
    if (modal) return modal;
    modal = document.createElement('div');
    modal.id = 'mermaid-zoom-modal';
    modal.innerHTML = '<div class="mz-backdrop"></div><div class="mz-content" role="dialog" aria-modal="true"></div>';
    document.body.appendChild(modal);
    modal.addEventListener('click', () => modal.classList.remove('open'));
    return modal;
  }

  function attach() {
    const diagrams = document.querySelectorAll('.mermaid');
    const modal = ensureModal();
    const content = modal.querySelector('.mz-content');
    diagrams.forEach(d => {
      if (d.dataset.mzAttached) return;
      d.dataset.mzAttached = '1';
      d.style.cursor = 'zoom-in';
      d.setAttribute('tabindex', '0');
      d.setAttribute('role', 'button');
      d.setAttribute('aria-label', 'Ampliar diagrama');
      const open = () => {
        const svg = d.querySelector('svg');
        if (!svg) return;
        content.innerHTML = '';
        const clone = svg.cloneNode(true);
        clone.removeAttribute('height');
        clone.style.width = '100%';
        content.appendChild(clone);
        modal.classList.add('open');
        // focus trap basic
        content.setAttribute('tabindex', '-1');
        content.focus();
      };
      d.addEventListener('click', open);
      d.addEventListener('keydown', (ev) => {
        if (ev.key === 'Enter' || ev.key === ' ') {
          ev.preventDefault();
          open();
        }
      });
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    attach();
    // Re-attach after Material theme client-side nav
    document.addEventListener('DOMContentSwitch', attach);
    // Fallback after small delay for Mermaid async rendering
    setTimeout(attach, 1200);
    // Close on ESC
    document.addEventListener('keydown', (ev) => {
      if (ev.key === 'Escape') {
        const m = document.getElementById('mermaid-zoom-modal');
        if (m) m.classList.remove('open');
      }
    });
  });
})();


