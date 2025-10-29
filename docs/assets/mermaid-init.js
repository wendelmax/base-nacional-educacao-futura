// Initialize Mermaid with larger default font size and responsive scaling
(function () {
  function initMermaid() {
    if (!window.mermaid) return;
    window.mermaid.initialize({
      startOnLoad: false,
      securityLevel: 'loose',
      theme: 'default',
      themeVariables: {
        fontSize: '18px',
        lineColor: '#37474F',
        primaryColor: '#E3F2FD',
        primaryTextColor: '#102027'
      }
    });
    window.mermaid.init(undefined, document.querySelectorAll('.mermaid'));
  }

  // First load
  document.addEventListener('DOMContentLoaded', initMermaid);
  // MkDocs Material hook for SPA navigation
  if (window.document$) {
    window.document$.subscribe(initMermaid);
  }
})();


