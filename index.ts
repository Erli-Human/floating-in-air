async function initWebGPU(): Promise<void> {
    if (!navigator.gpu) {
        console.error("WebGPU not supported. Please use a compatible browser.");
        return;
    }

    const adapter = await navigator.gpu.requestAdapter();
    const device = await adapter.requestDevice();
    const context = document.getElementById('canvas').getContext('webgpu');

    // Set canvas format
    const format = "bgra8unorm"; 
    context.configure({
        device: device,
        format: format,
    });

    // WebGPU logic goes here throughout your render loop
}

async function fetchVoiceOptions() {
    const response = await fetch('http://localhost:5000/api/voice-options');
    const voiceOptions = await response.json();
    populateVoiceOptions(voiceOptions);
}

function populateVoiceOptions(options: Array<{ name: string, language: string, gender: string }>) {
    const select = document.getElementById('voice-select') as HTMLSelectElement;
    options.forEach(option => {
        const opt = document.createElement('option');
        opt.value = option.name;
        opt.textContent = `${option.name} (${option.language}, ${option.gender})`;
        select.appendChild(opt);
    });
}

document.addEventListener('DOMContentLoaded', async () => {
    await initWebGPU();
    await fetchVoiceOptions();
});
