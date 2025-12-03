const projects = [
    {
        title: "Cisco",
        description: "Cisco'nun Introduction to Networking kursunu tamamlayıp ve sertifika aldım.",
        tags: ["Networking"],
        files: [
            { path: "cisco.jpg", language: "image" }
        ]
    },
    {
        title: "Microphone Enforcer",
        description: "Windows 10 ve 11'in mikrofon sesini otomatik olarak kısma özelliğini engelleyen bir program geliştirdim.",
        tags: ["Python"],
        files: [
            { path: "MicVolumeEnforcerByAsid.py", language: "python" }
        ]
    },
    {
        title: "Youtube Chat Watcher Bot",
        description: "YouTube canlı yayın sohbetini izleyen ve moderatörler tarafından yasaklanan kullanıcıları resime çevirip görsel haline getirdikten sonra Discord'a gönderen bir bot geliştirdim.",
        tags: ["Python", "Web Scraping", "Görüntü İşleme"],
        files: [
            { path: "dcmodbotmain.py", language: "python" }
        ]
    },
    {
        title: "Google Shopping Scrapper",
        description: "Şirketin veritabanındaki ürünlerin Google Alışveriş'teki fiyatlarını kontrol eden ve fiyat farklarını raporlayan bir web scrapper'a geliştirdim.",
        tags: ["Python", "Web Scraping", "SQL"],
        files: [
        ]
    },
    {
        title: "Pixel Art Sharpener",
        description: "Pixel Art oyunlarda kullanılacak görüntüleri keskinleştiren bir algoritma yazdım.",
        tags: ["Python", "Görüntü İşleme"],
        files: [
            { path: "pixel-art-sharpener.py", language: "python" }
        ]
    },
    {
        title: "Audio Normalizer",
        description: "Ses dosyalarının ses seviyesini normalize eden bir Python programı yazdım.",
        tags: ["Python", "Ses İşleme"],
        files: [
            { path: "audio-normalizer.py", language: "python" }
        ]
    },
    {
        title: "Unity Oyun Projesi",
        description: "Unity kullanarak basit bir 2D oyun geliştirdim. Ses efektleri, müzikler, animasyonlar ve oyun mekaniği gibi özellikler ekledim.",
        tags: ["Unity", "C#"],
        files: [
            { path: "reboot.jpg", language: "image" }
        ]
    },
    {
        title: "Restoran Yönetim Sistemi (Prototip)",
        description: "Bir restoranda müşterilerin siparişlerini QR kod ile verebileceği, restoranın masa, sipariş ve adisyonları yönetebileceği bir uygulama geliştiriyordum ancak proje tamamlanamadı.",
        tags: ["Node.JS", "Express", "Web Development", "SQL"],
        files: [
            { path: "rms.js", language: "javascript" }
        ]
    },
    {
        title: "UPS Kargo Entegrasyon Sistemi",
        description: "Şirketimizin e-ticaret sitesine UPS kargo entegrasyonu yaparak otomatik gönderi oluşturma ve takip sistemi geliştirdim.",
        tags: ["HTML", "JavaScript", "API Integration"],
        files: [
            { path: "ups.png", language: "image" }
        ]
    },
    {
    title: "3D objelerin döndürülürken rotasyon matrislerini gösteren web uygulaması",
    description: "Canlı Demo",
    tags: ["Web", "Three.JS"],
    url: "https://asidistaken.github.io/3D-Rotation-Calculator"
    },
    {
    title: "Don't Starve adlı oyun için yardımcı takvim sitesi",
    description: "Canlı Demo",
    tags: ["Web"],
    url: "https://asidistaken.github.io/Lunar-Calendar-for-Dont-Starve-Together-and-Dont-Starve"
    },
    {
    title: "Don't Starve adlı oyun için yardımcı boss takip sitesi",
    description: "Canlı Demo",
    tags: ["Web"],
    url: "https://asidistaken.github.io/Boss-Tracker-for-Dont-Starve-Together-and-Dont-Starve"
    },
    {
        title: "Ebeveyn-Çocuk Takip Uygulaması",
        description: "Ebeveynlerin çocuklarının telefon konumlarını izleyebileceği bir uygulama geliştirdim.",
        tags: ["HTML", "JavaScript", "Node.JS", "Android", "Kotlin"],
        files: []
    },
    {
        title: "Altyazı Senkronizasyon Aracı",
        description: "Video seçilen, seçilen videodan altyızıyı alan videodakine göre senkronize eden bir araç geliştirdim.",
        tags: ["Python"],
        files: []
    },
];

function loadImage(filePath, container) {
    const img = document.createElement('img');
    img.src = filePath;
    img.style.width = '100%';
    img.style.height = 'auto';
    img.style.borderRadius = '8px';
    img.style.display = 'block';
    img.onerror = () => {
        container.innerHTML = `<pre><code>// Resim yüklenemedi: ${filePath}</code></pre>`;
    };
    container.appendChild(img);
}

async function loadCodeFile(filePath, language, container) {
    try {
        const response = await fetch(filePath);
        const code = await response.text();
        
        const codeBlock = document.createElement('pre');
        const codeElement = document.createElement('code');
        codeElement.className = `language-${language}`;
        codeElement.textContent = code;
        codeBlock.appendChild(codeElement);
        container.appendChild(codeBlock);
        
        hljs.highlightElement(codeElement);
    } catch (error) {
        container.innerHTML = `<pre><code>// Kod dosyası yüklenemedi: ${filePath}\n// Hata: ${error.message}</code></pre>`;
    }
}

function createProjectCard(project) {
    const card = document.createElement('div');
    card.className = 'project-card';
    
    const tagsHTML = project.tags.map(tag => 
        `<span class="tag">${tag}</span>`
    ).join('');
    
    let contentHTML = '';
    
    if (project.url) {
        contentHTML = `
            <div class="code-container">
                <div class="code-header">
                    <div class="code-dot red"></div>
                    <div class="code-dot yellow"></div>
                    <div class="code-dot green"></div>
                    <span style="color: #abb2bf; font-size: 12px; margin-left: 10px;">${project.url}</span>
                </div>
                <div class="iframe-container">
                    <iframe src="${project.url}" frameborder="0"></iframe>
                </div>
            </div>
        `;
    } else {
        contentHTML = project.files.map((file, index) => `
            <div class="code-container">
                <div class="code-header">
                    <div class="code-dot red"></div>
                    <div class="code-dot yellow"></div>
                    <div class="code-dot green"></div>
                    <span style="color: #abb2bf; font-size: 12px; margin-left: 10px;">${file.path}</span>
                </div>
                <div class="code-block" data-file-index="${index}">
                    <pre><code>// Yükleniyor...</code></pre>
                </div>
            </div>
        `).join('');
    }
    
    card.innerHTML = `
        <div class="project-header">
            <h2>${project.title}</h2>
            <p>${project.description}</p>
        </div>
        <div class="project-content">
            <div class="tags">
                ${tagsHTML}
            </div>
            ${contentHTML}
        </div>
    `;
    
    return card;
}

function initPortfolio() {
    const grid = document.getElementById('projectsGrid');
    
    projects.forEach(project => {
        const card = createProjectCard(project);
        grid.appendChild(card);
        
        if (project.files && Array.isArray(project.files)) {
            project.files.forEach((file, index) => {
                const codeBlock = card.querySelector(`[data-file-index="${index}"]`);
                codeBlock.innerHTML = '';
                
                if (file.language === 'image') {
                    loadImage('../res/' + file.path, codeBlock);
                } else {
                    loadCodeFile('../res/' + file.path, file.language, codeBlock);
                }
            });
        }
    });
}

document.addEventListener('DOMContentLoaded', initPortfolio);