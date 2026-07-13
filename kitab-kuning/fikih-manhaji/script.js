document.addEventListener('DOMContentLoaded', () => {
    const contentArea = document.getElementById('content-area');
    const pageIndicator = document.getElementById('page-indicator');
    const prevBtn = document.getElementById('prev-page');
    const nextBtn = document.getElementById('next-page');
    const popup = document.getElementById('word-popup');
    const overlay = document.getElementById('overlay');
    const closePopupBtn = document.getElementById('close-popup');
    
    let currentPageIndex = parseInt(localStorage.getItem('fikihCurrentPage')) || 0;
    let activeWordEl = null;
    let isTranslationMode = false;
    let isHarakatVisible = false;

    // Convert to Arabic numerals
    function toArabicNum(num) {
        return num.toString().replace(/\d/g, d => '٠١٢٣٤٥٦٧٨٩'[d]);
    }

    // Strip harakat for logic if needed
    function stripHarakat(text) {
        return text.replace(/[\u064B-\u065F\u0670]/g, '');
    }

    function renderPage(index) {
        contentArea.innerHTML = '';
        
        if (index < 0 || index >= fikihData.length) return;
        const pageData = fikihData[index];
        
        if (isTranslationMode) {
            const transContainer = document.createElement('div');
            transContainer.className = 'translation-container';
            // Simple translation view combining all words
            let fullText = '';
            pageData.lines.forEach(line => {
                let lineText = line.words.map(w => w.translation).filter(t => t && t !== 'Belum ada terjemahan khusus.').join(' ');
                if (lineText) {
                    fullText += '<p>' + lineText + '</p>';
                }
            });
            transContainer.innerHTML = fullText || '<p>Terjemahan belum tersedia.</p>';
            contentArea.appendChild(transContainer);
        } else {
            const linesContainer = document.createElement('div');
            linesContainer.className = 'page-lines-container';
            
            pageData.lines.forEach(line => {
                const lineEl = document.createElement('div');
                lineEl.className = 'line line-' + line.align;
                
                if (line.align === 'title-box') {
                    const box = document.createElement('div');
                    box.className = 'title-inner';
                    line.words.forEach(w => {
                        box.appendChild(createWordEl(w));
                    });
                    lineEl.appendChild(box);
                } else {
                    line.words.forEach(w => {
                        lineEl.appendChild(createWordEl(w));
                    });
                }
                
                linesContainer.appendChild(lineEl);
            });
            
            contentArea.appendChild(linesContainer);
            
            // Add page number at bottom
            const pageNumEl = document.createElement('div');
            pageNumEl.className = 'page-number';
            pageNumEl.textContent = toArabicNum(pageData.pageNumber);
            contentArea.appendChild(pageNumEl);
        }
        
        pageIndicator.textContent = pageData.pageNumber;
        prevBtn.disabled = index === 0;
        nextBtn.disabled = index === fikihData.length - 1;
    }

    function createWordEl(wordData) {
        const wordEl = document.createElement('span');
        wordEl.className = 'word-interactive';
        wordEl.textContent = isHarakatVisible ? wordData.text : stripHarakat(wordData.text);
        
        wordEl.addEventListener('click', (e) => {
            e.stopPropagation();
            if (activeWordEl) activeWordEl.classList.remove('active');
            activeWordEl = wordEl;
            wordEl.classList.add('active');
            showPopup(wordData, wordEl);
        });
        
        return wordEl;
    }

    function showPopup(wordData, targetEl) {
        document.getElementById('popup-word').textContent = wordData.text;
        
        const setField = (id, secId, value) => {
            const el = document.getElementById(id);
            const sec = document.getElementById(secId);
            if (value && value !== '-' && value !== 'Belum ada terjemahan khusus.') {
                el.textContent = value;
                sec.classList.remove('hidden');
            } else if (id === 'popup-translation') {
                el.textContent = 'Belum ada terjemahan khusus.';
                sec.classList.remove('hidden');
            } else {
                sec.classList.add('hidden');
            }
        };

        setField('popup-translation', 'sec-translation', wordData.translation);
        setField('popup-irab-ar', 'sec-irab-ar', wordData.irab_ar);
        setField('popup-ilal-ar', 'sec-ilal-ar', wordData.ilal_ar);
        
        popup.classList.remove('hidden');
        overlay.classList.remove('hidden');
        
        // Wait a frame to get popup dimensions
        setTimeout(() => {
            positionPopup(targetEl);
            popup.classList.add('show');
        }, 10);
    }

    function positionPopup(targetEl) {
        const rect = targetEl.getBoundingClientRect();
        const popupRect = popup.getBoundingClientRect();
        
        let viewportTop = rect.bottom + 10;
        let viewportLeft = rect.left + (rect.width / 2) - (popupRect.width / 2);
        
        if (viewportTop + popupRect.height > window.innerHeight) {
            viewportTop = rect.top - popupRect.height - 10;
        }
        if (viewportTop < 10) viewportTop = 10;
        if (viewportLeft < 10) viewportLeft = 10;
        if (viewportLeft + popupRect.width > window.innerWidth - 10) {
            viewportLeft = window.innerWidth - popupRect.width - 10;
        }
        
        popup.style.top = (viewportTop + window.scrollY) + 'px';
        popup.style.left = (viewportLeft + window.scrollX) + 'px';
    }

    function hidePopup() {
        if (activeWordEl) {
            activeWordEl.classList.remove('active');
            activeWordEl = null;
        }
        popup.classList.remove('show');
        setTimeout(() => {
            if (!popup.classList.contains('show')) {
                popup.classList.add('hidden');
                overlay.classList.add('hidden');
            }
        }, 200);
    }

    closePopupBtn.addEventListener('click', hidePopup);
    overlay.addEventListener('click', hidePopup);
    window.addEventListener('resize', () => {
        if (popup.classList.contains('show') && activeWordEl) {
            positionPopup(activeWordEl);
        }
    });

    // Navigation
    prevBtn.addEventListener('click', () => {
        if (currentPageIndex > 0) {
            currentPageIndex--;
            localStorage.setItem('fikihCurrentPage', currentPageIndex);
            renderPage(currentPageIndex);
            hidePopup();
        }
    });

    nextBtn.addEventListener('click', () => {
        if (currentPageIndex < fikihData.length - 1) {
            currentPageIndex++;
            localStorage.setItem('fikihCurrentPage', currentPageIndex);
            renderPage(currentPageIndex);
            hidePopup();
        }
    });

    // Theme Switcher
    const btnYellow = document.getElementById('theme-yellow');
    const btnWhite = document.getElementById('theme-white');
    const btnTranslate = document.getElementById('toggle-translation');
    const btnFullscreen = document.getElementById('toggle-fullscreen');

    btnTranslate.style.color = '#94a3b8'; // default off state

    btnFullscreen.addEventListener('click', () => {
        if (!document.fullscreenElement) {
            document.documentElement.requestFullscreen().catch(err => {
                console.log(`Error attempting to enable fullscreen: ${err.message}`);
            });
        } else {
            if (document.exitFullscreen) {
                document.exitFullscreen();
            }
        }
    });

    btnTranslate.addEventListener('click', () => {
        isTranslationMode = !isTranslationMode;
        if (isTranslationMode) {
            btnTranslate.classList.add('active');
            btnTranslate.style.color = '#ffffff';
        } else {
            btnTranslate.classList.remove('active');
            btnTranslate.style.color = '#94a3b8';
        }
        renderPage(currentPageIndex);
    });

    const btnHarakat = document.getElementById('toggle-harakat');
    btnHarakat.style.color = '#94a3b8'; // default off state

    btnHarakat.addEventListener('click', () => {
        isHarakatVisible = !isHarakatVisible;
        if (isHarakatVisible) {
            btnHarakat.classList.add('active');
            btnHarakat.style.color = '';
        } else {
            btnHarakat.classList.remove('active');
            btnHarakat.style.color = '#94a3b8'; // grayed out when off
        }
        
        // Re-render only words without fully reconstructing the page if possible
        // But since we just need to update textContent:
        document.querySelectorAll('.word-interactive').forEach(el => {
            if (el.dataset.wordData) {
                const wd = JSON.parse(el.dataset.wordData);
                el.textContent = isHarakatVisible ? wd.text : stripHarakat(wd.text);
            }
        });
        
        // Alternatively, just re-render the page:
        renderPage(currentPageIndex);
    });

    btnYellow.addEventListener('click', () => {
        contentArea.className = 'a4-page theme-yellow';
        btnYellow.classList.add('active');
        btnWhite.classList.remove('active');
        document.getElementById('page-wrapper').style.backgroundColor = 'var(--paper-yellow-bg)';
    });

    btnWhite.addEventListener('click', () => {
        contentArea.className = 'a4-page theme-white';
        btnWhite.classList.add('active');
        btnYellow.classList.remove('active');
        document.getElementById('page-wrapper').style.backgroundColor = 'var(--paper-white-bg)';
    });

    // Initial render
    setTimeout(() => {
        renderPage(currentPageIndex);
    }, 100);
});
