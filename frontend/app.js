const API_URL = window.location.origin;

let selectedImage = null;

document.getElementById('uploadBtn').addEventListener('click', () => {
    document.getElementById('imageInput').removeAttribute('capture');
    document.getElementById('imageInput').click();
});

document.getElementById('captureBtn').addEventListener('click', () => {
    document.getElementById('imageInput').setAttribute('capture', 'environment');
    document.getElementById('imageInput').click();
});

document.getElementById('imageInput').addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file) {
        selectedImage = file;
        const reader = new FileReader();
        reader.onload = (e) => {
            document.getElementById('previewImage').src = e.target.result;
            document.getElementById('preview').classList.remove('hidden');
            document.getElementById('results').classList.add('hidden');
        };
        reader.readAsDataURL(file);
    }
});

document.getElementById('analyzeBtn').addEventListener('click', async () => {
    if (!selectedImage) return;

    document.getElementById('loading').classList.remove('hidden');
    document.getElementById('results').classList.add('hidden');

    const formData = new FormData();
    formData.append('image', selectedImage);

    try {
        const response = await fetch(`${API_URL}/api/analyze`, {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            displayResults(data);
        } else {
            alert('Error: ' + data.error);
        }
    } catch (error) {
        alert('Failed to analyze image. Please try again.');
        console.error(error);
    } finally {
        document.getElementById('loading').classList.add('hidden');
    }
});

function displayResults(data) {
    const medicineName = data.identified_medicine || data.generic_name || 'Medicine Information';
    document.getElementById('medicineName').textContent = medicineName;
    
    const subtitle = data.generic_name && data.identified_medicine !== data.generic_name 
        ? `Generic: ${data.generic_name}` 
        : 'Detailed Information';
    document.getElementById('medicineSubtitle').textContent = subtitle;

    const resultsContent = document.getElementById('resultsContent');
    resultsContent.innerHTML = '';

    const fieldOrder = [
        { key: 'brand_names', icon: '🏷️', title: 'Brand Names' },
        { key: 'active_ingredients', icon: '🧪', title: 'Active Ingredients' },
        { key: 'uses', icon: '💊', title: 'Medical Uses' },
        { key: 'dosage', icon: '📏', title: 'Dosage Information' },
        { key: 'side_effects', icon: '⚠️', title: 'Side Effects' },
        { key: 'precautions', icon: '🛡️', title: 'Precautions' },
        { key: 'interactions', icon: '🔄', title: 'Drug Interactions' },
        { key: 'storage', icon: '📦', title: 'Storage Instructions' }
    ];

    fieldOrder.forEach(field => {
        if (data[field.key] && data[field.key] !== 'N/A') {
            const card = createInfoCard(field.icon, field.title, data[field.key]);
            resultsContent.appendChild(card);
        }
    });

    for (const [key, value] of Object.entries(data)) {
        if (value && value !== 'N/A' && 
            key !== 'identified_medicine' && 
            key !== 'generic_name' &&
            !fieldOrder.find(f => f.key === key)) {
            const title = key.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
            const card = createInfoCard('ℹ️', title, value);
            resultsContent.appendChild(card);
        }
    }

    document.getElementById('results').classList.remove('hidden');
}

function createInfoCard(icon, title, content) {
    const card = document.createElement('div');
    card.className = 'info-card';
    
    card.innerHTML = `
        <div class="info-card-title">${icon} ${title}</div>
        <div class="info-card-content">${formatValue(content)}</div>
    `;
    
    return card;
}

function formatValue(value) {
    if (Array.isArray(value)) {
        return '<ul>' + value.map(v => `<li>${escapeHtml(v)}</li>`).join('') + '</ul>';
    }
    if (typeof value === 'object') {
        return '<pre>' + JSON.stringify(value, null, 2) + '</pre>';
    }
    return escapeHtml(String(value));
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
