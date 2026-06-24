document.addEventListener('DOMContentLoaded', () => {
    const contentArea = document.getElementById('content-area');
    const f4Page = document.getElementById('f4-page');
    const pageWrapper = document.getElementById('page-wrapper');
    const viewport = document.getElementById('viewport');
    const pageIndicator = document.getElementById('page-indicator');
    const pageNumDisplay = document.getElementById('page-num-display');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const zoomInBtn = document.getElementById('zoom-in');
    const zoomOutBtn = document.getElementById('zoom-out');
    const zoomFitBtn = document.getElementById('zoom-fit');
    const zoomLevel = document.getElementById('zoom-level');
    const themeToggle = document.getElementById('theme-toggle');
    const themeIconLight = document.getElementById('theme-icon-light');
    const themeIconDark = document.getElementById('theme-icon-dark');

    // Convert number to Arabic-Indic numerals
    function toArabicNum(n) {
        const digits = ['٠','١','٢','٣','٤','٥','٦','٧','٨','٩'];
        return String(n).split('').map(d => digits[+d] || d).join('');
    }

    // State
    let currentPage = 144;
    let zoom = 1;
    const ZOOM_STEP = 0.1;
    const ZOOM_MIN = 0.4;
    const ZOOM_MAX = 2.5;

    // Get sorted page keys
    function getPageKeys() {
        return Object.keys(pagesData).map(Number).sort((a, b) => a - b);
    }

    // Update navigation buttons
    function updateNav() {
        const keys = getPageKeys();
        const idx = keys.indexOf(currentPage);
        prevBtn.disabled = (idx <= 0);
        nextBtn.disabled = (idx >= keys.length - 1);
        pageIndicator.textContent = 'صفحة ' + toArabicNum(currentPage);
        pageNumDisplay.textContent = toArabicNum(currentPage);
    }

    // Zoom functions
    function applyZoom() {
        pageWrapper.style.transform = `scale(${zoom})`;
        zoomLevel.textContent = Math.round(zoom * 100) + '%';
    }

    function fitToScreen() {
        const vpHeight = viewport.clientHeight - 60;
        const vpWidth = viewport.clientWidth - 40;
        // F4 in px at 96dpi: 215mm ≈ 812.6px, 330mm ≈ 1247.2px
        const pageW = 812.6;
        const pageH = 1247.2;
        zoom = Math.min(vpWidth / pageW, vpHeight / pageH);
        zoom = Math.max(ZOOM_MIN, Math.min(ZOOM_MAX, zoom));
        applyZoom();
    }

    zoomInBtn.addEventListener('click', () => {
        zoom = Math.min(ZOOM_MAX, zoom + ZOOM_STEP);
        applyZoom();
    });
    zoomOutBtn.addEventListener('click', () => {
        zoom = Math.max(ZOOM_MIN, zoom - ZOOM_STEP);
        applyZoom();
    });
    zoomFitBtn.addEventListener('click', fitToScreen);

    // Ctrl+scroll zoom
    viewport.addEventListener('wheel', (e) => {
        if (e.ctrlKey) {
            e.preventDefault();
            if (e.deltaY < 0) {
                zoom = Math.min(ZOOM_MAX, zoom + ZOOM_STEP);
            } else {
                zoom = Math.max(ZOOM_MIN, zoom - ZOOM_STEP);
            }
            applyZoom();
        }
    }, { passive: false });

    // Theme toggle
    themeToggle.addEventListener('click', () => {
        const isDark = document.body.getAttribute('data-theme') === 'dark';
        if (isDark) {
            document.body.removeAttribute('data-theme');
            themeIconLight.style.display = '';
            themeIconDark.style.display = 'none';
        } else {
            document.body.setAttribute('data-theme', 'dark');
            themeIconLight.style.display = 'none';
            themeIconDark.style.display = '';
        }
    });

    // Render page content
    function renderPage(pageNum, direction) {
        const pageData = pagesData[pageNum];

        if (!pageData) {
            contentArea.innerHTML = '<p style="text-align:center; font-family: Inter, sans-serif; color: #888; padding-top: 40mm;">بيانات هذه الصفحة غير متوفرة</p>';
            return;
        }

        buildContent(pageData, pageNum);
        viewport.scrollTop = 0;
    }

    function buildContent(pageData, pageNum) {
        contentArea.innerHTML = '';
        
        // Push content down specifically for page 144
        if (pageNum === 144) {
            contentArea.style.paddingTop = '65mm';
        } else {
            contentArea.style.paddingTop = '0';
        }

        pageData.forEach(block => {
            const blockEl = document.createElement('div');

            if (block.type === 'heading') {
                blockEl.className = 'heading-group';
            } else if (block.type === 'subheading') {
                blockEl.className = 'subheading-group';
            } else {
                blockEl.className = 'paragraph-container';
            }

            if (block.lines) {
                block.lines.forEach((lineWords, lineIndex) => {
                    const lineEl = document.createElement('div');
                    lineEl.className = 'line';

                    if (block.type === 'paragraph' && lineIndex === block.lines.length - 1) {
                        lineEl.classList.add('last-line');
                    }

                    lineWords.forEach(word => {
                        const wordGroup = document.createElement('div');
                        wordGroup.className = 'word-group';

                        const arabicEl = document.createElement('span');
                        arabicEl.className = 'arabic-word';
                        arabicEl.textContent = word.ar;

                        const maknaEl = document.createElement('span');
                        maknaEl.className = 'makna';
                        maknaEl.textContent = word.id;

                        wordGroup.appendChild(arabicEl);
                        wordGroup.appendChild(maknaEl);

                        lineEl.appendChild(wordGroup);
                    });

                    blockEl.appendChild(lineEl);
                });
            }

            contentArea.appendChild(blockEl);
        });
    }

    // Page navigation
    prevBtn.addEventListener('click', () => {
        const keys = getPageKeys();
        const idx = keys.indexOf(currentPage);
        if (idx > 0) {
            currentPage = keys[idx - 1];
            updateNav();
            renderPage(currentPage, 'prev');
        }
    });

    nextBtn.addEventListener('click', () => {
        const keys = getPageKeys();
        const idx = keys.indexOf(currentPage);
        if (idx < keys.length - 1) {
            currentPage = keys[idx + 1];
            updateNav();
            renderPage(currentPage, 'next');
        }
    });

    // Keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') nextBtn.click();   // Next page (RTL)
        if (e.key === 'ArrowRight') prevBtn.click();  // Prev page (RTL)
        if (e.key === '+' || e.key === '=') { e.preventDefault(); zoomInBtn.click(); }
        if (e.key === '-') { e.preventDefault(); zoomOutBtn.click(); }
    });

    // Initial render
    if (typeof pagesData !== 'undefined') {
        updateNav();
        zoom = 1;
        applyZoom();
        renderPage(currentPage);
    }
});
