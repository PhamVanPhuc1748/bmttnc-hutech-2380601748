function gundamAnimateSubmit(form) {
    const button = form.querySelector('button[type="submit"]');
    if (!button || button.dataset.processing === '1') {
        return true;
    }

    const originalText = button.innerHTML;
    button.dataset.processing = '1';
    button.innerHTML = 'SYNCING... <span class="cursor" style="display:inline-block;width:8px;height:1em;background:currentColor;animation:blink 1s infinite;"></span>';
    button.style.pointerEvents = 'none';

    window.setTimeout(() => {
        button.innerHTML = originalText;
        button.style.pointerEvents = 'auto';
        button.dataset.processing = '0';
    }, 1400);

    return true;
}

function gundamUppercaseAlpha(input) {
    const value = String(input.value || '').toUpperCase();
    input.value = value.replace(/[^A-Z]/g, '').replace(/J/g, 'I');
}

function gundamUppercaseText(input) {
    input.value = String(input.value || '').toUpperCase();
}

function gundamNormalizeNumber(input, minValue, maxValue) {
    const numericValue = Number.parseInt(input.value, 10);
    if (Number.isNaN(numericValue)) {
        return;
    }

    const bounded = Math.min(Math.max(numericValue, minValue), maxValue);
    input.value = String(bounded);
}
