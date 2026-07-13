document.addEventListener('DOMContentLoaded', () => {
    const contentArea = document.getElementById('content-area');
    const pageIndicator = document.getElementById('page-indicator');
    const prevBtn = document.getElementById('prev-page');
    const nextBtn = document.getElementById('next-page');
    
    // Popup Elements
    const popup = document.getElementById('word-popup');
    const overlay = document.getElementById('overlay');
    const popupWord = document.getElementById('popup-word');
    const popupTranslation = document.getElementById('popup-translation');
    const popupRoot = document.getElementById('popup-root');
    const popupExplanation = document.getElementById('popup-explanation');
    const popupIrab = document.getElementById('popup-irab');
    const popupJoined = document.getElementById('popup-joined');
    const popupPronoun = document.getElementById('popup-pronoun');
    const popupVerb = document.getElementById('popup-verb');
    const popupFail = document.getElementById('popup-fail');
    
    const rootSection = document.getElementById('root-section');
    const explanationSection = document.getElementById('explanation-section');
    const irabSection = document.getElementById('irab-section');
    const joinedSection = document.getElementById('joined-section');
    const pronounSection = document.getElementById('pronoun-section');
    const verbSection = document.getElementById('verb-section');
    const failSection = document.getElementById('fail-section');
    
    const closePopupBtn = document.getElementById('close-popup');

    let currentPageIndex = 0;
    let isTranslationMode = false;
    let isHarakatVisible = true;
    
    // Store paginated data
    let paginatedPages = [];

    // Convert numbers to Arabic numerals
    function toArabicNum(num) {
        return num.toString().replace(/\d/g, d => '٠١٢٣٤٥٦٧٨٩'[d]);
    }

    // Remove harakat from Arabic text
    function removeHarakat(text) {
        return text.replace(/[\u064B-\u065F\u0670]/g, '');
    }

    // Dynamic Pagination Logic
    function calculatePagination() {
        if (!fikihData || fikihData.length === 0) return;
        
        paginatedPages = [];
        contentArea.innerHTML = '';
        
        // Ensure content area has a fixed height for calculation
        const originalHeight = contentArea.style.height;
        contentArea.style.height = contentArea.parentElement.clientHeight + 'px';
        
        let currentPageData = [];
        
        // Container to test rendering
        let testContainer = document.createElement('div');
        contentArea.appendChild(testContainer);
        
        let currentBlockEl = null;

        fikihData.forEach(page => {
            page.blocks.forEach(block => {
                
                // Setup the block element for testing
                let blockEl;
                if (block.type === 'title') {
                    blockEl = document.createElement('div');
                    blockEl.className = 'book-header';
                    let frame = document.createElement('div');
                    frame.className = 'title-frame';
                    let inner = document.createElement('div');
                    inner.className = 'title-inner';
                    frame.appendChild(inner);
                    blockEl.appendChild(frame);
                    testContainer.appendChild(blockEl);
                    currentBlockEl = inner;
                } else if (block.type === 'heading') {
                    blockEl = document.createElement('div');
                    blockEl.className = 'subtitle';
                    testContainer.appendChild(blockEl);
                    currentBlockEl = blockEl;
                } else {
                    blockEl = document.createElement('div');
                    blockEl.className = 'paragraph';
                    testContainer.appendChild(blockEl);
                    currentBlockEl = blockEl;
                }
                
                let blockDataForPage = { type: block.type, id: block.id, words: [] };
                currentPageData.push(blockDataForPage);
                
                block.words.forEach(wordData => {
                    let wordEl = document.createElement('span');
                    wordEl.className = 'word-interactive';
                    wordEl.textContent = wordData.text; // Text content for height testing
                    
                    currentBlockEl.appendChild(wordEl);
                    
                    // Check height
                    if (contentArea.scrollHeight > contentArea.clientHeight) {
                        // Overflow!
                        currentBlockEl.removeChild(wordEl);
                        
                        // If the block is now empty on the old page, remove it
                        if (currentBlockEl.childNodes.length === 0) {
                            let blockParent = currentBlockEl.closest('.book-header, .subtitle, .paragraph');
                            if (blockParent && blockParent.parentNode) {
                                blockParent.parentNode.removeChild(blockParent);
                            }
                        }
                        
                        // Save current page
                        paginatedPages.push(currentPageData);
                        
                        // Reset for new page
                        currentPageData = [];
                        testContainer.innerHTML = '';
                        
                        // Recreate block for new page
                        if (block.type === 'title') {
                            blockEl = document.createElement('div');
                            blockEl.className = 'book-header';
                            let frame = document.createElement('div');
                            frame.className = 'title-frame';
                            let inner = document.createElement('div');
                            inner.className = 'title-inner';
                            frame.appendChild(inner);
                            blockEl.appendChild(frame);
                            testContainer.appendChild(blockEl);
                            currentBlockEl = inner;
                        } else if (block.type === 'heading') {
                            blockEl = document.createElement('div');
                            blockEl.className = 'subtitle';
                            testContainer.appendChild(blockEl);
                            currentBlockEl = blockEl;
                        } else {
                            blockEl = document.createElement('div');
                            blockEl.className = 'paragraph';
                            testContainer.appendChild(blockEl);
                            currentBlockEl = blockEl;
                        }
                        
                        blockDataForPage = { type: block.type, id: block.id, words: [] };
                        currentPageData.push(blockDataForPage);
                        
                        // Append the word that overflowed to the new page
                        currentBlockEl.appendChild(wordEl);
                    }
                    
                    blockDataForPage.words.push(wordData);
                });
            });
        });
        
        if (currentPageData.length > 0) {
            paginatedPages.push(currentPageData);
        }
        
        // Clean up
        contentArea.innerHTML = '';
        contentArea.style.height = originalHeight;
    }

    function renderPage(index) {
        contentArea.innerHTML = '';
        if (paginatedPages.length === 0) return;

        const pageData = paginatedPages[index];

        pageData.forEach(block => {
            if (isTranslationMode) {
                if (block.type === 'title') {
                    const titleEl = document.createElement('div');
                    titleEl.className = 'title-id';
                    titleEl.textContent = block.id;
                    contentArea.appendChild(titleEl);
                } else if (block.type === 'heading') {
                    const headingEl = document.createElement('div');
                    headingEl.className = 'subtitle-id';
                    headingEl.textContent = block.id;
                    contentArea.appendChild(headingEl);
                } else {
                    const paragraphEl = document.createElement('div');
                    paragraphEl.className = 'paragraph-id';
                    paragraphEl.textContent = block.id;
                    contentArea.appendChild(paragraphEl);
                }
            } else {
                if (block.type === 'title') {
                    const header = document.createElement('div');
                    header.className = 'book-header';
                    
                    const frame = document.createElement('div');
                    frame.className = 'title-frame';
                    
                    const inner = document.createElement('div');
                    inner.className = 'title-inner';
                    
                    block.words.forEach(wordData => {
                        inner.appendChild(createWordElement(wordData));
                    });
                    
                    frame.appendChild(inner);
                    header.appendChild(frame);
                    contentArea.appendChild(header);
                } else if (block.type === 'heading') {
                    const heading = document.createElement('div');
                    heading.className = 'subtitle';
                    
                    block.words.forEach(wordData => {
                        heading.appendChild(createWordElement(wordData));
                    });
                    
                    contentArea.appendChild(heading);
                } else {
                    const paragraph = document.createElement('div');
                    paragraph.className = 'paragraph';
                    
                    block.words.forEach(wordData => {
                        paragraph.appendChild(createWordElement(wordData));
                    });
                    
                    contentArea.appendChild(paragraph);
                }
            }
        });

        // Add page number at bottom
        const pageNumEl = document.createElement('div');
        pageNumEl.className = 'page-number';
        // Base the physical page number starting from 1
        pageNumEl.textContent = toArabicNum(index + 1);
        contentArea.appendChild(pageNumEl);

        pageIndicator.textContent = index + 1;

        // Update Nav Buttons
        prevBtn.disabled = index === 0;
        nextBtn.disabled = index === paginatedPages.length - 1;
    }

    let activeWordEl = null;

    function createWordElement(wordData) {
        const span = document.createElement('span');
        span.className = 'word-interactive';
        span.textContent = isHarakatVisible ? wordData.text : removeHarakat(wordData.text);
        
        span.addEventListener('click', (e) => {
            e.stopPropagation();
            
            if (activeWordEl) activeWordEl.classList.remove('active');
            
            span.classList.add('active');
            activeWordEl = span;
            
            const displayText = isHarakatVisible ? wordData.text : removeHarakat(wordData.text);
            popupWord.textContent = displayText.replace(/[﴾﴿.,:;]/g, '');
            popupTranslation.textContent = wordData.translation || 'Belum ada terjemahan khusus.';
            
            if (wordData.root && wordData.root !== '-') {
                rootSection.classList.remove('hidden');
                popupRoot.textContent = wordData.root;
            } else {
                rootSection.classList.add('hidden');
            }

            if (wordData.verb_type && wordData.verb_type !== '-') {
                verbSection.classList.remove('hidden');
                popupVerb.textContent = wordData.verb_type;
            } else {
                verbSection.classList.add('hidden');
            }

            if (wordData.fail_ref && wordData.fail_ref !== '-') {
                failSection.classList.remove('hidden');
                popupFail.textContent = wordData.fail_ref;
            } else {
                failSection.classList.add('hidden');
            }

            if (wordData.irab && wordData.irab !== '-') {
                irabSection.classList.remove('hidden');
                popupIrab.textContent = wordData.irab;
            } else {
                irabSection.classList.add('hidden');
            }

            if (wordData.joined_explanation && wordData.joined_explanation !== '-') {
                joinedSection.classList.remove('hidden');
                popupJoined.textContent = wordData.joined_explanation;
            } else {
                joinedSection.classList.add('hidden');
            }

            if (wordData.pronoun_ref && wordData.pronoun_ref !== '-') {
                pronounSection.classList.remove('hidden');
                popupPronoun.textContent = wordData.pronoun_ref;
            } else {
                pronounSection.classList.add('hidden');
            }

            if (wordData.explanation && wordData.explanation !== '-') {
                explanationSection.classList.remove('hidden');
                popupExplanation.textContent = wordData.explanation;
            } else {
                explanationSection.classList.add('hidden');
            }
            
            overlay.classList.remove('hidden');
            popup.classList.remove('hidden');
            setTimeout(() => {
                popup.classList.add('show');
                positionPopup(span);
            }, 10);
        });
        
        return span;
    }

    function positionPopup(targetEl) {
        const rect = targetEl.getBoundingClientRect();
        const popupRect = popup.getBoundingClientRect();
        
        let top = rect.bottom + 10;
        let left = rect.left + (rect.width / 2) - (popupRect.width / 2);
        let isTop = false;
        
        if (top + popupRect.height > window.innerHeight) {
            top = rect.top - popupRect.height - 10;
            isTop = true;
        }
        
        if (top < 10) {
            top = 10;
            if (isTop) {
                top = rect.bottom + 10;
                isTop = false;
            }
        }
        
        if (left < 10) left = 10;
        if (left + popupRect.width > window.innerWidth - 10) {
            left = window.innerWidth - popupRect.width - 10;
        }
        
        popup.style.top = top + 'px';
        popup.style.left = left + 'px';
        
        if (isTop) {
            popup.classList.remove('arrow-top');
        } else {
            popup.classList.add('arrow-top');
        }
        
        const arrow = popup.querySelector('.popup-arrow');
        let arrowLeft = rect.left + (rect.width / 2) - left - 7;
        arrowLeft = Math.max(10, Math.min(arrowLeft, popupRect.width - 24));
        arrow.style.left = arrowLeft + 'px';
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

    function scalePage() {
        const wrapper = document.getElementById('page-wrapper');
        const page = document.getElementById('content-area');
        if (!wrapper || !page) return;
        
        const targetWidth = 768;
        const targetHeight = 1024;
        
        const wrapperWidth = wrapper.clientWidth - 40; 
        const wrapperHeight = wrapper.clientHeight - 40; 
        
        const scaleX = wrapperWidth / targetWidth;
        const scaleY = wrapperHeight / targetHeight;
        const scale = Math.min(scaleX, scaleY);
        
        page.style.transform = `scale(${scale})`;
    }

    closePopupBtn.addEventListener('click', hidePopup);
    overlay.addEventListener('click', hidePopup);
    window.addEventListener('resize', () => {
        scalePage();
        if (popup.classList.contains('show') && activeWordEl) {
            positionPopup(activeWordEl);
        }
    });
    
    document.getElementById('page-wrapper').addEventListener('scroll', () => {
        if (popup.classList.contains('show') && activeWordEl) {
            positionPopup(activeWordEl);
        }
    });

    // Navigation
    prevBtn.addEventListener('click', () => {
        if (currentPageIndex > 0) {
            currentPageIndex--;
            renderPage(currentPageIndex);
            hidePopup();
        }
    });

    nextBtn.addEventListener('click', () => {
        if (currentPageIndex < paginatedPages.length - 1) {
            currentPageIndex++;
            renderPage(currentPageIndex);
            hidePopup();
        }
    });

    // Theme Switcher
    const btnYellow = document.getElementById('theme-yellow');
    const btnWhite = document.getElementById('theme-white');
    const btnTranslate = document.getElementById('toggle-translation');
    const btnHarakat = document.getElementById('toggle-harakat');
    const btnFullscreen = document.getElementById('toggle-fullscreen');

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

    btnHarakat.addEventListener('click', () => {
        isHarakatVisible = !isHarakatVisible;
        if (isHarakatVisible) {
            btnHarakat.classList.add('active');
            btnHarakat.style.color = '#3b82f6';
        } else {
            btnHarakat.classList.remove('active');
            btnHarakat.style.color = '';
        }
        calculatePagination();
        renderPage(currentPageIndex);
    });

    btnTranslate.addEventListener('click', () => {
        isTranslationMode = !isTranslationMode;
        if (isTranslationMode) {
            btnTranslate.classList.add('active');
            btnTranslate.style.color = '#3b82f6';
        } else {
            btnTranslate.classList.remove('active');
            btnTranslate.style.color = '';
        }
        calculatePagination();
        if (currentPageIndex >= paginatedPages.length) currentPageIndex = Math.max(0, paginatedPages.length - 1);
        renderPage(currentPageIndex);
    });

    btnYellow.addEventListener('click', () => {
        contentArea.classList.add('theme-yellow');
        contentArea.classList.remove('theme-white');
        btnYellow.classList.add('active');
        btnWhite.classList.remove('active');
        document.getElementById('page-wrapper').style.backgroundColor = 'var(--paper-yellow-bg)';
    });

    btnWhite.addEventListener('click', () => {
        contentArea.classList.add('theme-white');
        contentArea.classList.remove('theme-yellow');
        btnWhite.classList.add('active');
        btnYellow.classList.remove('active');
        document.getElementById('page-wrapper').style.backgroundColor = 'var(--paper-white-bg)';
    });

    // Initial render
    setTimeout(() => {
        scalePage();
        calculatePagination();
        renderPage(currentPageIndex);
    }, 100);
});
